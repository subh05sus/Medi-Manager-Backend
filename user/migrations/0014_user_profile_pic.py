# Generated by Django 4.2.7 on 2024-04-02 08:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0013_rename_qualifications_user_qualification"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="profile_pic",
            field=models.ImageField(blank=True, null=True, upload_to="profile_pics/"),
        ),
    ]