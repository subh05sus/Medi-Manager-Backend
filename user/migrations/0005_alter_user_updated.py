# Generated by Django 4.2.7 on 2024-03-02 11:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0004_alter_user_email_alter_user_phone_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="updated",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]