import csv
from django.core.management.base import BaseCommand
from specialization.models import Specialization


class Command(BaseCommand):
    help = 'Import specializations from CSV file'

    def handle(self, *args, **options):
        file_path = 'sample_csv_files/sample_specializations - Sheet1.csv'  # Path to your CSV file
        with open(file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                specialization, created = Specialization.objects.get_or_create(
                    name=row['Specialization']
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Successfully added {specialization}'))
                else:
                    self.stdout.write(self.style.WARNING(f'{specialization} already exists'))
