from django.urls import path
from farm_app.views import ContactViewSet


urlpatterns = [
    path('', ContactViewSet.as_view({'get': 'list'}), name='contact-list')
]
