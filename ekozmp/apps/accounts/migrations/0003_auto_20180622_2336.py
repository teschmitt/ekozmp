# Generated by Django 2.0.6 on 2018-06-22 21:36

from django.db import migrations
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180621_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='timezone',
            field=timezone_field.fields.TimeZoneField(default='Europe/Berlin'),
        ),
    ]
