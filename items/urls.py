from django.urls import path
from . import views

app_name = 'items'

urlpatterns = [
    path('new/', views.new, name='new'),
]