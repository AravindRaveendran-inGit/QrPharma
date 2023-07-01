from django.urls import path
from .views import *

urlpatterns = [
    path('', qr_codeView, name='Qr_view'),
    ]