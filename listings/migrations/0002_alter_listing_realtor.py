# Generated by Django 5.0.6 on 2024-06-06 22:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='realtor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.realtor'),
        ),
    ]