import csv
from django.core.management.base import BaseCommand
from investigation_master.models import InvestigationMaster


class Command(BaseCommand):
    help = 'Import Investigations from CSV file'

    def handle(self, *args, **options):
        file_path = 'sample_csv_files/sample_investigations - Sheet1.csv'  # Path to your CSV file
        with open(file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                x = row['Investigation']
                symptom, created = InvestigationMaster.objects.get_or_create(
                    name=row['Investigation']
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Successfully added {x}'))
                else:
                    self.stdout.write(self.style.WARNING(f'{x} already exists in Investigation DB'))
