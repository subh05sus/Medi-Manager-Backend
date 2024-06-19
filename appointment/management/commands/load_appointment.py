import csv
from django.core.management.base import BaseCommand
from user.models import User
from appointment.models import Appointment
from specialization.models import Specialization


class Command(BaseCommand):
    help = 'Import dummy appointments from CSV file'

    def handle(self, *args, **options):
        file_path = 'sample_csv_files/sample_appointments - Sheet1.csv' 
        with open(file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Retrieve patient instance using provided ID
                patient_id  = int(row['patient_id'])
                patient     = User.objects.get(pk=patient_id)

                doctor_id   = int(row['doctor_id'])
                doctor      = User.objects.get(pk=doctor_id)

                specialization_id       = int(row['specialization_id'])
                specialization_instance = Specialization.objects.get(pk=specialization_id)

                # Create appointment instance
                appointment, created = Appointment.objects.get_or_create(
                    appointment_datetime= row['appointment_datetime'],
                    status      =           row['status'],
                    doctor_id   =           doctor,
                    patient_id          = patient,  # Assign patient instance
                    specialization_id   = specialization_instance,
                    created_by          = row['created_by'],
                    updated_by          = row['updated_by'],
                    type = row['appointment_type']
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Successfully created appointment: {appointment}'))
                else:
                    self.stdout.write(self.style.WARNING(f'Appointment {appointment} already exists'))
