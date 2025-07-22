from django.urls import path
from .views import record_health, delete_record, health_database, edit_record
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('record_health/')),
    path('record_health/', record_health, name='record_health'),
    path('delete/<int:record_id>/', delete_record, name='delete_record'),
    path('edit/', edit_record, name='edit_record'),
    path('database/', health_database, name='health_database')
]