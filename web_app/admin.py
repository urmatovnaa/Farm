from django.contrib import admin

from web_app.models import ProductPhoto, ProductName, Company


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'company')


class PersonAdmin2(admin.ModelAdmin):
    list_display = ('company', 'photo')


class PersonAdmin3(admin.ModelAdmin):
    list_display = ('name', 'web_site')


admin.site.register(ProductName, PersonAdmin)
admin.site.register(ProductPhoto, PersonAdmin2)
admin.site.register(Company, PersonAdmin3)
