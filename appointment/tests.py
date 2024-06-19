from django.test import TestCase
from rest_framework.test import APIClient
from django.test import TestCase
from datetime import datetime, timedelta, timezone
from .models import Appointment, APPOINTMENT_STATUSES
from user.models import User
from specialization.models import Specialization


class AppointmentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', email='test@example.com', password='password')
        self.specialization = Specialization.objects.create(name='Cardiology')
        self.timezone = timezone.utc  # Use the appropriate timezone

    def test_create_appointment(self):
        # Create a timezone-aware datetime for next_appointment
        future_time = datetime.now(self.timezone) + timedelta(days=3)

        # Create an Appointment object with the timezone-aware datetime
        appointment = Appointment.objects.create(
            status=APPOINTMENT_STATUSES.CREATED.value,
            doctor_id=1,
            patient_id=self.user,
            specialization_id=self.specialization,
            created_by='admin',
            next_appointment=future_time  # Use the timezone-aware datetime here
            # Add other required fields for creating an Appointment if applicable
        )

        # Check if the Appointment object was created successfully
        self.assertEqual(appointment.status, APPOINTMENT_STATUSES.CREATED.value)
        self.assertEqual(appointment.doctor_id, 1)
        self.assertEqual(appointment.patient_id, self.user)
        self.assertEqual(appointment.specialization_id, self.specialization)
        self.assertEqual(appointment.created_by, 'admin')
        self.assertEqual(appointment.next_appointment, future_time)  # Verify the next_appointment field

        # Verify created and updated fields are set correctly
        self.assertIsNotNone(appointment.created)
        # self.assertIsNotNone(appointment.updated) # This will nto work because of minute delay in
        # self.assertEqual(appointment.created, appointment.updated)  # Created and updated should be the same after creation


    def test_next_appointment(self):
        # Create an Appointment object with a future next appointment time
        future_time =  datetime.now(self.timezone) + timedelta(days=3)
        appointment = Appointment.objects.create(
            status=APPOINTMENT_STATUSES.CREATED.value,
            doctor_id=1,
            patient_id=self.user,
            specialization_id=self.specialization,
            created_by='admin',
            next_appointment=future_time
            # Add other required fields for creating an Appointment if applicable
        )

        # Check if the next_appointment field holds the correct value
        self.assertEqual(appointment.next_appointment, future_time)


class AppointmentAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username='testuser', email='test@example.com', password='password')
        self.specialization = Specialization.objects.create(name='Cardiology')
        self.timezone = timezone.utc  # Use the appropriate timezone

    def test_create_appointment(self):
        # Create an Appointment via API
        future_time = datetime.now(self.timezone) + timedelta(days=3)
        appointment_data = {
            'status': APPOINTMENT_STATUSES.CREATED.value,
            'doctor_id': 1,
            'patient_id': self.user.id,
            'specialization_id': self.specialization.id,
            'created_by': 'admin',
              'next_appointment' : future_time
           
            # Add other required fields for creating an Appointment if applicable
        }

        response = self.client.post('/api/v1/appointment/', appointment_data)
        self.assertEqual(response.status_code, 201)  # Check if Appointment creation was successful
        self.assertTrue(Appointment.objects.filter(status=APPOINTMENT_STATUSES.CREATED.value).exists())  

    def test_retrieve_appointment(self):
        # Create an Appointment
        future_time =  datetime.now(self.timezone) + timedelta(days=3)
        appointment = Appointment.objects.create(
            status=APPOINTMENT_STATUSES.IN_PROGRESS.value,
            doctor_id=2,
            patient_id=self.user,
            specialization_id=self.specialization,
            created_by='admin',
            # Add other required fields for creating an Appointment if applicable
             next_appointment =  future_time,
        )

        response = self.client.get(f'/api/v1/appointment/{appointment.id}/')
        self.assertEqual(response.status_code, 200)  
        self.assertEqual(response.data['status'], APPOINTMENT_STATUSES.IN_PROGRESS.value)  
        # Add other assertions based on your API response

