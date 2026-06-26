from django.urls import path
from . import views

app_name = 'main_Page'

urlpatterns = [
    path('', views.home, name='home'),
]