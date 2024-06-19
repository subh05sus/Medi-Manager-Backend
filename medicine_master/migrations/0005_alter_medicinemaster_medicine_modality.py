# Generated by Django 4.2.7 on 2024-02-16 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine_master', '0004_alter_medicinemaster_medicine_modality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicinemaster',
            name='medicine_modality',
            field=models.CharField(choices=[('AF', 'AFTER_FOOD'), ('BF', 'BEFORE_FOOD'), ('WF', 'WITH_FOOD'), ('ES', 'EMPTY_STOMACH')], default='AF', max_length=2),
        ),
    ]