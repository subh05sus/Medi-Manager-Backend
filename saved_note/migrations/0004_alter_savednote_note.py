# Generated by Django 4.2.7 on 2024-03-23 11:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("saved_note", "0003_alter_savednote_note_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="savednote",
            name="note",
            field=models.TextField(blank=True, max_length=350, null=True),
        ),
    ]
