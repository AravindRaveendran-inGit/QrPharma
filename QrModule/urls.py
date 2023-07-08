from django.urls import path
from .views import *

urlpatterns = [
    path('', QrView, name='Qr_view'),
    path('w-indent/', WithIndentView, name='With_Indent_view'),

    ]