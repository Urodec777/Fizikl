from django.urls import path
from .views import index, ajax

urlpatterns = [
    path('', index, name='index'),
    path('ajax/', ajax, name='definedate')
]