# Generated by Django 4.2.7 on 2024-04-16 11:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("template_master", "0005_alter_investigationset_collection_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="medicineset",
            name="medicine_modality",
            field=models.CharField(
                choices=[
                    ("AF", "AFTER_FOOD"),
                    ("BF", "BEFORE_FOOD"),
                    ("WF", "WITH_FOOD"),
                ],
                default="AF",
                max_length=2,
            ),
        ),
    ]
