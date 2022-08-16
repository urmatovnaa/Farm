from django.db import models


class Contact(models.Model):
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=14)
    location = models.URLField()
    email = models.EmailField()
    whatsapp = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'{self.address}'
