import csv
from django.core.management.base import BaseCommand
from vital_master.models import VitalMaster


class Command(BaseCommand):
    help = 'Import Sample Vitals from CSV file'

    def handle(self, *args, **options):
        file_path = 'sample_csv_files/sample_vitals - Sheet1.csv'  
        with open(file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                x = row['vital_name']
                vital, _ = VitalMaster.objects.get_or_create(
                    vital_name = row['vital_name'],
                    vital_unit = row['vital_unit'],)
                if _:
                    self.stdout.write(self.style.SUCCESS(f'Successfully Added {x}'))
                else:
                    self.stdout.write(self.style.WARNING(f'{vital} already exists'))
