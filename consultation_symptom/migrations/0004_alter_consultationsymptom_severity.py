# Generated by Django 4.2.7 on 2024-04-17 13:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("consultation_symptom", "0003_consultationsymptom_duration_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="consultationsymptom",
            name="severity",
            field=models.CharField(max_length=20),
        ),
    ]