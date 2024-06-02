# Generated by Django 5.0.6 on 2024-06-01 06:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("awsstations", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="trainstation",
            name="neareststation",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="awsstations.awsstation",
            ),
        ),
    ]
