# Generated by Django 4.2.7 on 2024-02-08 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('symptom_master', '0003_alter_symptommaster_symptom_name'),
        ('consultation', '0001_initial'),
        ('consultation_symptom', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='consultationsymptom',
            unique_together={('consultation_id', 'symptom_id')},
        ),
    ]
