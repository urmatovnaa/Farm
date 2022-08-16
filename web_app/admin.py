from django.contrib import admin

from web_app.models import ProductPhoto, Company


class PersonAdmin3(admin.ModelAdmin):
    list_display = ('name', 'web_site')


admin.site.register(ProductPhoto)
admin.site.register(Company, PersonAdmin3)

