# Generated by Django 3.2.25 on 2024-12-03 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bids', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]