from django.core.management.base import BaseCommand
from tracking.models import People, LocationRecord
from django.utils import timezone
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Veritabanını rastgele 1000 kayıt ile doldurur'

    def handle(self, *args, **kwargs):
        fake = Faker()
        try:
            self.stdout.write(self.style.NOTICE('Mevcut kayıtlar siliniyor...'))
            People.objects.all().delete()
            LocationRecord.objects.all().delete()

            self.stdout.write(self.style.NOTICE('Yeni rastgele kayıtlar oluşturuluyor...'))
            
            people_list = []
            for _ in range(1000):
                person = People(
                    first_name=fake.first_name(),
                    last_name=fake.last_name()
                )
                person.save()
                people_list.append(person)

            for person in people_list:
                for _ in range(random.randint(1, 5)): 
                    LocationRecord.objects.create(
                        people=person,
                        latitude=fake.latitude(),
                        longitude=fake.longitude(),
                        datetime=timezone.now() - timezone.timedelta(hours=random.randint(0, 12))  
                    )
            
            self.stdout.write(self.style.SUCCESS('Veritabanı başarıyla rastgele verilerle dolduruldu.'))
        
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Hata oluştu: {e}'))
