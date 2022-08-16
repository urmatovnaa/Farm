from rest_framework import viewsets
from farm_app.models import Contact
from farm_app.serializers import ContactSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
