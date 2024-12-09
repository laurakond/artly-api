# Generated by Django 3.2.25 on 2024-12-09 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artworks', '0001_initial'),
        ('bids', '0002_alter_bid_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='artwork',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='artworks.artwork'),
        ),
    ]
