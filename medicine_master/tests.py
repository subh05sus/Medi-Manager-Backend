from django.test import TestCase
from .models import MedicineMaster

class MedicineMasterTestCase(TestCase):
    def test_medicine_creation(self):
        medicine = MedicineMaster.objects.create(
            medicine_name='Medicine 1',
            medicine_dosage='10mg'
        )

        self.assertIsNotNone(medicine)
        self.assertEqual(medicine.medicine_name, 'Medicine 1')
        self.assertEqual(medicine.medicine_dosage, '10mg')

    def test_medicine_update(self):
        medicine = MedicineMaster.objects.create(
            medicine_name='Medicine 2',
            medicine_dosage='5mg'
        )

        updated_medicine_dosage = '20mg'
        medicine.medicine_dosage = updated_medicine_dosage
        medicine.save()

        updated_medicine = MedicineMaster.objects.get(id=medicine.id)
        self.assertEqual(updated_medicine.medicine_dosage, updated_medicine_dosage)

    def test_medicine_deletion(self):
        medicine = MedicineMaster.objects.create(
            medicine_name='Medicine 3',
            medicine_dosage='15mg'
        )

        medicine_id = medicine.id
        medicine.delete()

        with self.assertRaises(MedicineMaster.DoesNotExist):
            MedicineMaster.objects.get(id=medicine_id)
