from django.urls import path
from .views import index, DateView

urlpatterns = [
    path('', index, name='index'),
    path('ajax/', DateView.as_view(), name='definedate')
]