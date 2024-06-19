# Generated by Django 4.2.7 on 2024-04-09 06:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fee_structure", "0004_userfeestructure_cost_type"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userfeestructure",
            name="cost_type",
        ),
        migrations.AddField(
            model_name="feetype",
            name="cost_type",
            field=models.CharField(
                choices=[("DF", "DOCTOR_FEE"), ("SC", "SEVICE_CHARGE")],
                default="DF",
                max_length=2,
            ),
        ),
    ]