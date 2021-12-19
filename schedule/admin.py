from django.contrib import admin
from .models import Event, Client, Packages

admin.site.register(Event)
admin.site.register(Client)
admin.site.register(Packages)

# Register your models here.
