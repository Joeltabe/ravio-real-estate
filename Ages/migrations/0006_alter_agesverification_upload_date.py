# Generated by Django 5.0.6 on 2024-06-06 22:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ages', '0005_alter_agesverification_upload_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agesverification',
            name='upload_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 6, 6, 22, 39, 44, 972277)),
        ),
    ]
