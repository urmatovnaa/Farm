from farm_app.models import Contacts
from rest_framework import serializers


class ContactsSerializer(serializers.Serializer):
    class Meta:
        model = Contacts
        fields = '__all__'
