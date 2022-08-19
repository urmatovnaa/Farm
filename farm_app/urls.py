from django.urls import path
from farm_app.views import ContactViewSet, AboutUsViewSet, MainViewSet


urlpatterns = [
    path('contacts/', ContactViewSet.as_view({'get': 'list'}), name='contact-list'),
    path('about_us/', AboutUsViewSet.as_view({'get': 'list'}), name='aboutus-list'),
    path('', MainViewSet.as_view({'get': 'list'}), name='main-list')
]
