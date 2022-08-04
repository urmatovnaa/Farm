from rest_framework import serializers

from web_app.models import ProductPhoto, Company, ProductName


class ProductPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPhoto
        fields = '__all__'


class ProductNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductName
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('id', 'name', 'logo')


class CompanyDetailSerializer(serializers.ModelSerializer):
    products_photos = ProductPhotoSerializer(many=True)
    products_name = ProductNameSerializer(many=True)

    class Meta:
        model = Company
        fields = ('id', 'name', 'logo', 'information', 'web_site', 'products_name', 'products_photos')

