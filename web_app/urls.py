from django.urls import path
from web_app.views import CompanyView

urlpatterns = [
    path('', CompanyView.as_view({'get': 'list'}), name='company_list'),
    path('<int:pk>', CompanyView.as_view(
        {'get': 'retrieve'})),
]
