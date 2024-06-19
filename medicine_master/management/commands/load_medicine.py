import csv
from django.core.management.base import BaseCommand
from medicine_master.models import MedicineMaster


class Command(BaseCommand):
    help = 'Import Sample Medicines from CSV file'

    def handle(self, *args, **options):
        file_path = 'sample_csv_files/sample_medicine - Sheet1.csv'  # Path to your CSV file
        with open(file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                x = row['medicine_name']
                medicine, created = MedicineMaster.objects.get_or_create(
                    medicine_name=row['medicine_name'],
                    medicine_dosage = row['medicine_dosage'],

                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Successfully Added {x}'))
                else:
                    self.stdout.write(self.style.WARNING(f'{medicine} already exists'))
