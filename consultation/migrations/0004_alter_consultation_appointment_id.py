# Generated by Django 4.2.7 on 2024-02-23 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("appointment", "0005_alter_appointment_doctor_id_and_more"),
        ("consultation", "0003_alter_consultation_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="consultation",
            name="appointment_id",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.PROTECT,
                to="appointment.appointment",
            ),
        ),
    ]