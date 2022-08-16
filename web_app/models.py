from django.db import models


class ProductPhoto(models.Model):
	photo = models.ImageField(upload_to='product_photo')
	company = models.ManyToManyField('web_app.Company', related_name='products_photos')

	def __str__(self):
		return f'{self.photo}'


class Company(models.Model):
	LANGUAGE_CHOICES = [
		('ENGLISH', 'English'),
		('RUSSIAN', 'Русский')
	]
	name = models.CharField(max_length=255)
	logo = models.ImageField(upload_to='logo')
	photo = models.ImageField(upload_to='company_photo')
	information = models.TextField()
	key_words = models.CharField(max_length=255, null=True)
	web_site = models.URLField()
	language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES)

	class Meta:
		verbose_name_plural = 'companies'

	def clean(self):
		self.name = self.name.capitalize()

	def __str__(self):
		return f'{self.name}'

