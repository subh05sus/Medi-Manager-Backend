# Generated by Django 4.2.7 on 2024-02-08 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_alter_appointment_next_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='previous_appointment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_appointments', to='appointment.appointment'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='next_appointment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='previous_appointments', to='appointment.appointment'),
        ),
    ]