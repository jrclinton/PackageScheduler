from django.db import models

# Create your models here.

import datetime

from django.db.models import Sum
from django.utils import timezone

class Client(models.Model):
    user_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        full_name = self.last_name + self.first_name
        return  str(full_name)

    def sessions_remaining(self):
        return self.packages_set.aggregate(Sum('session_count'))['session_count__sum']

class Event(models.Model):
    title = models.CharField(max_length=200)
    start_time = models.DateTimeField(default=datetime.datetime.now)
    duration_in_minutes = models.IntegerField(default=30)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Packages(models.Model):
    title = models.CharField(max_length=200)
    purchase_date = models.DateField(default=datetime.date.today)
    sessions_at_purchase = models.IntegerField(default=4)
    session_count = models.IntegerField(default=4)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.title