# Generated by Django 5.0.6 on 2024-06-01 07:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("awsstations", "0003_remove_trainstation_id_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="awsstation",
            name="curr_windspeed",
            field=models.FloatField(default=0),
        ),
    ]