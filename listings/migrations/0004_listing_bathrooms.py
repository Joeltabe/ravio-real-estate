# Generated by Django 5.0.6 on 2024-06-06 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_remove_listing_bathrooms'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='bathrooms',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]