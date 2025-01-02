# Generated by Django 3.2.25 on 2025-01-01 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artworks', '0003_alter_artwork_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artwork',
            name='alt_text',
        ),
        migrations.AlterField(
            model_name='artwork',
            name='artist_name',
            field=models.CharField(blank=True, default='Unknown artist', max_length=250),
        ),
    ]