from django.shortcuts import render
from rest_framework import viewsets
from farm_app.models import Contacts
from farm_app.serializers import ContactsSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
