# Generated by Django 4.0.6 on 2022-08-19 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('name_en', models.CharField(max_length=255, null=True)),
                ('name_ru', models.CharField(max_length=255, null=True)),
                ('logo', models.ImageField(upload_to='logo')),
                ('photo', models.ImageField(upload_to='company_photo')),
                ('information', models.TextField()),
                ('information_en', models.TextField(null=True)),
                ('information_ru', models.TextField(null=True)),
                ('key_words', models.CharField(max_length=255, null=True)),
                ('web_site', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'companies',
            },
        ),
        migrations.CreateModel(
            name='ProductPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='product_photo')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_photos', to='web_app.company')),
            ],
        ),
    ]