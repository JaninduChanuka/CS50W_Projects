# Generated by Django 4.1.3 on 2022-12-01 17:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_rename_date_created_listing_datecreated_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='dateCreated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
