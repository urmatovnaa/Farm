from django.db import models


class ProductName(models.Model):
	name = models.CharField(max_length=255)
	company = models.ForeignKey('web_app.Company', on_delete=models.CASCADE, related_name='products_name')

	def __str__(self):
		return f'{self.name}'


class ProductPhoto(models.Model):
	photo = models.ImageField(upload_to='product_photo')
	company = models.ForeignKey('web_app.Company', on_delete=models.CASCADE, related_name='products_photos')

	def __str__(self):
		return f'{self.photo}'


class Company(models.Model):
	name = models.CharField(max_length=255)
	logo = models.ImageField(upload_to='logo')
	information = models.TextField()
	web_site = models.URLField()

	class Meta:
		verbose_name_plural = 'companies'

	def clean(self):
		self.name = self.name.capitalize()

	def __str__(self):
		return f'{self.name}'
