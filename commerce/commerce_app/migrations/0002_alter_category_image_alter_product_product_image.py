# Generated by Django 5.0.7 on 2024-08-05 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
