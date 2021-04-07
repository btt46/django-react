from django.urls import path
from .views import *

urlpatterns = [
    path('', create_customer, name="create_customer"),
]
