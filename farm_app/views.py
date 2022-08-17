from rest_framework import viewsets
from farm_app.models import Contact, AboutUs, Main
from farm_app.serializers import ContactSerializer, AboutUsSerializer, MainSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class AboutUsViewSet(viewsets.ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


class MainViewSet(viewsets.ModelViewSet):
    queryset = Main.objects.all()
    serializer_class = MainSerializer
