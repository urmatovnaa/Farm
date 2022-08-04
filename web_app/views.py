from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from web_app.models import Company
from web_app.serializers import CompanySerializer, CompanyDetailSerializer


class CompanyView(ModelViewSet):
    queryset = Company.objects.all().order_by('-id')
    serializer_class = CompanySerializer
    serializer_classes = {
        'retrieve': CompanyDetailSerializer,
    }
    filter_backends = [SearchFilter]
    search_fields = ['name', 'products_name__name']

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)
