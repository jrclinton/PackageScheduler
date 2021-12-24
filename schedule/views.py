from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Client, Event, Packages

# Create your views here.


class CalendarView(generic.DetailView):
    template_name = 'schedule/calendar.html'
    context_object_name = 'latest_events_list'

    def get_queryset(self):
        return Event.objects.order_by('start_time')


class ClientClanedarView(generic.DetailView):
    template_name = 'schedule/calendar_client.html'
    context_object_name = 'latest_events_list'

    def get_queryset(self):
        return Event.objects.order_by('start_time')

class ClientsView(generic.ListView):
    model = Client, Packages
    template_name = 'schedule/all_clients.html'
    context_object_name = 'client_list_desc'

    def get_queryset(self):
        return Client.objects.order_by('last_name')

class ClientView(generic.DetailView):
    template_name = 'schedule/single_client.html'
    context_object_name = 'latest_events_list'

    def get_queryset(self):
        return Event.objects.order_by('start_time')