# Generated by Django 5.0.3 on 2024-04-12 17:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_coursediary_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursediary',
            name='batch',
            field=models.IntegerField(choices=[(1, 'Batch 1'), (2, 'Batch 2')], null=True),
        ),
        migrations.AddField(
            model_name='coursediary',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.subject'),
        ),
    ]
