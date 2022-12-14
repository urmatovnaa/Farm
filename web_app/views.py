from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from web_app.models import Company
from web_app.serializers import CompanySerializer, CompanyDetailSerializer


class CompanyView(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    serializer_classes = {
        'retrieve': CompanyDetailSerializer,
    }
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name', 'key_words']

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)
