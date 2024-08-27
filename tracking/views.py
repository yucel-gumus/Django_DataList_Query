from django.shortcuts import render
from django.utils import timezone
from django.core.cache import cache
from django.core.paginator import Paginator
from django.db.models import Max
from tracking.models import LocationRecord

CACHE_TIMEOUT = 3600  

def get_last_locations(time_range_hours=12, query=None, page_number=1, items_per_page=10):
    """
    Belirtilen saat aralığındaki son konumları döndürür.
    Arama sorgusuna göre filtreleme yapar ve sayfalamayı uygular.
    """
    time_range = timezone.now() - timezone.timedelta(hours=time_range_hours)
    cache_key = f'last_locations_{time_range_hours}_{query}_{page_number}'

    last_locations = cache.get(cache_key)
    if last_locations is not None:
        return last_locations

    location_query = LocationRecord.objects.filter(datetime__gte=time_range).select_related('people')
    
    if query:
        location_query = location_query.filter(
            people__first_name__icontains=query) | location_query.filter(
            people__last_name__icontains=query)

    last_locations = (
        location_query
        .values(
            'id',
            'latitude',
            'longitude',
            'people__first_name',
            'people__last_name',
            'datetime'
        )
        .annotate(max_datetime=Max('datetime'))
        .order_by('people', '-datetime')
    )

    paginator = Paginator(last_locations, items_per_page)
    page_obj = paginator.get_page(page_number)

    result = {
        "locations": [
            {
                "id": loc['id'],
                "latitude": loc['latitude'],
                "longitude": loc['longitude'],
                "people_fullname": f"{loc['people__first_name']} {loc['people__last_name']}",
                "datetime": loc['datetime'].strftime('%Y-%m-%d %H:%M:%S')
            }
            for loc in page_obj
        ],
        "page_obj": page_obj
    }

    cache.set(cache_key, result, timeout=CACHE_TIMEOUT)
    return result

def last_locations(request):
    """
    Son konumların görüntülendiği sayfa.
    """
    query = request.GET.get('q')  
    page_number = request.GET.get('page', 1) 

    data = get_last_locations(query=query, page_number=page_number)
    context = {
        'last_locations_data': data['locations'],
        'page_obj': data['page_obj'],
        'query': query
    }
    return render(request, 'index.html', context)
