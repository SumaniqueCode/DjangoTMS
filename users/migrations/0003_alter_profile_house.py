# Generated by Django 5.0.3 on 2024-04-03 16:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0001_initial'),
        ('users', '0002_profile_house'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='house',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='members', to='house.house'),
        ),
    ]
