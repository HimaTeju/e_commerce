from django.urls import path
from . import views

app_name = 'items'

urlpatterns = [
    path('new/', views.new, name='new'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('view_cart/', views.show_cart_items, name='view_cart'),
    path('confirm_order/', views.confirm_order, name='confirm_order'),
]