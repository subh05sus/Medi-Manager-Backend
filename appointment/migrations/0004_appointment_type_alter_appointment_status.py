# Generated by Django 4.2.7 on 2024-02-08 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0003_appointment_previous_appointment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='type',
            field=models.CharField(choices=[('IA', 'INITIAL'), ('FA', 'FOLLOWUP'), ('CA', 'CLOSED')], default='IA', max_length=2),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('CR', 'CREATED'), ('IP', 'IN_PROGRESS'), ('CN', 'CANCELLED'), ('PP', 'POSTPONED'), ('CL', 'CLOSED'), ('RC', 'RESCHEDULED')], default='CR', max_length=2),
        ),
    ]