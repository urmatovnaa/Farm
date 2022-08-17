from farm_app.models import Contact, AboutUs, Main
from rest_framework import serializers


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'


class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Main
        fields = '__all__'
