# Generated by Django 4.2.7 on 2024-04-09 07:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        (
            "booking_slot",
            "0003_alter_daygroup_unique_together_bookingslot_doctor_id_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="daygroup",
            name="doctor_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="day_groups",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="daygroup",
            name="name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name="bookingslot",
            unique_together={("day_group",)},
        ),
        migrations.AlterUniqueTogether(
            name="daygroup",
            unique_together={("doctor_id", "name")},
        ),
        migrations.RemoveField(
            model_name="bookingslot",
            name="doctor_id",
        ),
    ]
