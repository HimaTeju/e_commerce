from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm

app_name = "core"

urlpatterns = [
    path("index/", views.index, name="index"),
    path("contact/", views.contact, name="contact"),
    path("add_retailer/", views.add_retailer, name="add_retailer"),
    path("", auth_views.LoginView.as_view(
        template_name='core/login.html',
        authentication_form=LoginForm), name="login"),
]
