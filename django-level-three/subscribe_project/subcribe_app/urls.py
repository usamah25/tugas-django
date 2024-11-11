from django.urls import path
from subcribe_app import views

urlpatterns = [
    path('', views.customers, name='customers'),
]