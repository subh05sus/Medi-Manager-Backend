import csv
from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password  # Import make_password to hash passwords
from user.models import User


class Command(BaseCommand):
    help = 'Import dummy users from CSV file'

    def handle(self, *args, **options):
        file_path = 'sample_csv_files/sample_users - Sheet1.csv'  # Path to your CSV file
        with open(file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Create a user
                user, created = User.objects.get_or_create(
                    email=row['email'],
                    first_name=row['first_name'],
                    last_name=row['last_name'],
                    phone_number=row['phone_number'],
                    address=row['address'],
                    postal_code=row['postal_code'],
                )

                # Set password and save user if created
                if created:
                    password = make_password(row['password'])  # Hash the password
                    user.password = password
                    user.save()
                    self.stdout.write(self.style.SUCCESS(f'Successfully created {user}'))
                else:
                    self.stdout.write(self.style.WARNING(f'{user} already exists'))
