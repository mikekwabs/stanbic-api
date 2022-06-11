# Generated by Django 3.2.13 on 2022-06-11 06:58

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerinfo',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(limit_value=datetime.date.today)]),
        ),
    ]
