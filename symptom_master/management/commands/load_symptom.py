import csv
from django.core.management.base import BaseCommand
from symptom_master.models import SymptomMaster


class Command(BaseCommand):
    help = 'Import Symptoms from CSV file'

    def handle(self, *args, **options):
        file_path = 'sample_csv_files/symptoms - Sheet1.csv'  # Path to your CSV file
        with open(file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                x = row['Symptom']
                symptom, created = SymptomMaster.objects.get_or_create(
                    symptom_name=row['Symptom']
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Successfully added {x}'))
                else:
                    self.stdout.write(self.style.WARNING(f'{x} already exists in symptom DB'))
