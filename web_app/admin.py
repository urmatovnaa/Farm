from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from web_app.models import ProductPhoto, Company


@admin.register(Company)
class PersonAdmin3(TranslationAdmin):
    list_display = ('name', 'web_site')


@admin.register(ProductPhoto)
class Admin(admin.ModelAdmin):
    pass

