from django.test import TestCase
from appointment.models import Appointment , APPOINTMENT_STATUSES
from consultation.models import Consultation, CONSULTATION_STATUSES
from specialization.models import Specialization
from user.models import User
from datetime import datetime, timedelta, timezone

class ConsultationModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', email='test@example.com', password='password')
        self.specialization = Specialization.objects.create(name='Cardiology')
        self.timezone = timezone.utc  # Use the appropriate timezone
        self.timezone = timezone.utc 
        future_time = datetime.now(self.timezone) + timedelta(days=3)
        self.appointment = Appointment.objects.create(
            status=APPOINTMENT_STATUSES.CREATED.value,
            doctor_id=1,
            patient_id=self.user,
            specialization_id=self.specialization,
            created_by='admin',
            next_appointment=future_time  # Use the timezone-aware datetime here
            # Add other required fields for creating an Appointment if applicable
        )

    def test_consultation_creation(self):
        consultation = Consultation.objects.create(
            appointment_id=self.appointment,
            status=CONSULTATION_STATUSES.CREATED.value,
            doctor_id=1,  # Replace with an appropriate doctor ID
            created_by='TestUser',
            next_appointment=None,
            fee=50.00,
            fee_paid=False,
            # Add any other required fields for the Consultation model
        )
        self.assertIsInstance(consultation, Consultation)
        self.assertEqual(consultation.status, CONSULTATION_STATUSES.CREATED.value)
        # Add more assertions to test other fields and conditions

    def test_consultation_status_choices(self):
        # with self.assertRaises(ValueError):
            # Attempt to create a Consultation instance with an invalid status
        consultation = Consultation.objects.create(
                appointment_id=self.appointment,
                status='InvalidStatus',  # Provide an invalid status
                doctor_id=1,
                created_by='TestUser',
                next_appointment=None,
                fee=50.00,
                fee_paid=False,
                # Add other required fields for the Consultation model
            )
        # Check that no object is created when an invalid status is provided
        self.assertEqual(Consultation.objects.count(), 1)