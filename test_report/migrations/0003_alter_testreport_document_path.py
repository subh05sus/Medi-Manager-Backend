# Generated by Django 4.2.7 on 2024-05-03 09:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("test_report", "0002_testreport_document_label_testreport_document_path"),
    ]

    operations = [
        migrations.AlterField(
            model_name="testreport",
            name="document_path",
            field=models.FileField(blank=True, upload_to="test_reports"),
        ),
    ]
