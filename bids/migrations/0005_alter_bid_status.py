# Generated by Django 3.2.25 on 2024-12-19 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bids', '0004_remove_bid_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Sold', 'Sold')], default='Pending', max_length=50),
        ),
    ]
