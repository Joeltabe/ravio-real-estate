# Generated by Django 5.0.6 on 2024-06-06 22:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_alter_contact_contact_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 6, 6, 22, 7, 45, 628416)),
        ),
    ]