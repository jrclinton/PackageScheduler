from django.urls import path
from . import views

urlpatterns = [
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    path('calendar/<str:user_name>', views.ClientClanedarView.as_view(), name='client_calendar'),
    path('clients/', views.ClientsView.as_view(), name='clients'),
    path('clients/<str:user_name>', views.ClientView.as_view(), name='client'),
]