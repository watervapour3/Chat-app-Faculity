# Generated by Django 5.0.3 on 2024-04-12 17:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_coursediary'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursediary',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.student'),
        ),
    ]
