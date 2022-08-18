from django.urls import path
from farm_app.views import ContactViewSet, AboutUsViewSet, MainViewSet


urlpatterns = [
    path('contacts/', ContactViewSet.as_view({'get': 'list'}), name='contact-list'),
    path('aboutus-list/', AboutUsViewSet.AboutUsList, name='aboutus-list'),
    path('aboutus-update/<int:id>', AboutUsViewSet.AboutUsCreate, name='aboutus-update'),
    path('aboutus-delete/<int:id>', AboutUsViewSet.AnoutUSDelete, name='aboutus-delete'),
    path('', MainViewSet.as_view({'get': 'list'}), name='main-list')
]
