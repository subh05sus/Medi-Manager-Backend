# Generated by Django 4.2.7 on 2024-04-01 13:20

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0012_user_qualifications"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="qualifications",
            new_name="qualification",
        ),
    ]
