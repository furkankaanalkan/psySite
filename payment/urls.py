from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('', views.pay_view, name='pay'),
]