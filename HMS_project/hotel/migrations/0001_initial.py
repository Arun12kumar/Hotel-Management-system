# Generated by Django 5.0.1 on 2024-02-08 10:50

import django.db.models.deletion
import shortuuid.django_fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('address', models.CharField(max_length=256)),
                ('image', models.FileField(upload_to='hotel_gallery')),
                ('mobile', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('Disable', 'Disable'), ('Rejected', 'Rejected'), ('In Review', 'Draft'), ('Live', 'Live')], default='Live', max_length=20)),
                ('tags', models.CharField(help_text='seperate tags with comma', max_length=200)),
                ('views', models.ImageField(default=0, upload_to='')),
                ('featured', models.BooleanField(default=False)),
                ('hid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvwxyz', length=10, max_length=20, prefix='', unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]