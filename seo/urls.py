from django.urls import path
from .views import *

urlpatterns = [
    path("", seohome, name='seohome'),
]
