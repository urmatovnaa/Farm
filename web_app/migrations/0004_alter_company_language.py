# Generated by Django 4.0.6 on 2022-08-17 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0003_company_key_words_delete_productname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='language',
            field=models.CharField(choices=[('english', 'English'), ('russian', 'Русский')], max_length=20),
        ),
    ]