# Generated by Django 4.2.7 on 2024-02-29 11:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("consultation", "0006_remove_consultation_medicine_fingerprint_and_more"),
        ("saved_note", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="savednote",
            name="consultation_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="consultation.consultation",
            ),
        ),
        migrations.AlterField(
            model_name="savednote",
            name="user_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
