from django.db import models

class People(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        indexes = [
            models.Index(fields=['first_name']),
            models.Index(fields=['last_name']),
        ]

class LocationRecord(models.Model):
    people = models.ForeignKey(People, on_delete=models.CASCADE, db_index=True)
    datetime = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        indexes = [
            models.Index(fields=['datetime']),
            models.Index(fields=['people']),
            models.Index(fields=['latitude', 'longitude']),
        ]
