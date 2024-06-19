# Generated by Django 4.2.7 on 2024-03-21 06:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("test_report", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="testreport",
            name="document_label",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="testreport",
            name="document_path",
            field=models.FilePathField(blank=True, path="test_reports"),
        ),
    ]
