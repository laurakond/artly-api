# Generated by Django 3.2.25 on 2024-11-30 12:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artwork_title', models.CharField(max_length=150)),
                ('artist_name', models.CharField(blank=True, default='Unknown', max_length=250)),
                ('description', models.TextField()),
                ('style', models.CharField(choices=[('Modern', 'Modern'), ('Contemporary', 'Contemporary'), ('Digital art', 'Digital art'), ('Old Masters', 'Old Masters'), ('Classical', 'Classical'), ('Other', 'Other')], default='Other', max_length=150)),
                ('type', models.CharField(choices=[('Collage', 'Collage'), ('Drawing', 'Drawing'), ('Needlework', 'Needlework'), ('Etching', 'Etching'), ('Painting', 'Painting'), ('Photography', 'Photography'), ('Pottery', 'Pottery'), ('Scultpure', 'Scultpure'), ('Watercolour', 'Watercolour'), ('Other', 'Other')], default='Other', max_length=100)),
                ('payment_method', models.CharField(choices=[('Paypal', 'Paypal'), ('Cash', 'Cash')], default='Cash', max_length=100)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('image', models.ImageField(blank=True, default='../default_post_urnaqw', upload_to='images/')),
                ('alt_text', models.CharField(blank=True, default='Artwork image', max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('sold', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
            },
        ),
    ]
