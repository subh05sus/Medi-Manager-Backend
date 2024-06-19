# Generated by Django 4.2.7 on 2024-04-27 14:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "prescription_setting",
            "0003_alter_prescriptionsetting_doctor_info_alignment_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="prescriptionsetting",
            name="doctor_signature_alignment",
            field=models.CharField(
                choices=[("LT", "LEFT"), ("RT", "RIGHT"), ("MD", "MIDDLE")],
                default="LT",
                max_length=2,
            ),
        ),
    ]
