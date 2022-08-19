from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from farm_app.models import Main, AboutUs, Contact


@admin.register(Contact)
class PersonAdmin3(admin.ModelAdmin):
    pass


@admin.register(AboutUs)
class Admin2(TranslationAdmin):
    pass


@admin.register(Main)
class Admin4(TranslationAdmin):
    pass
