from django.urls import path
from .views import Index, DateView

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('ajax/', DateView.as_view(), name='definedate')
]
