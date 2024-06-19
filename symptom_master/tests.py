from django.test import TestCase
from .models import SymptomMaster

class SymptomMasterModelTest(TestCase):
    def setUp(self):
        # Create a sample SymptomMaster instance for testing
        self.symptom = SymptomMaster.objects.create(symptom_name='Vomitting')

    def test_symptom_creation(self):
        # Test whether the symptom is created properly
        symptom_count = SymptomMaster.objects.count()
        self.assertEqual(symptom_count, 1)  # Check if one symptom is created

    def test_symptom_attributes(self):
        # Test the attributes of the created symptom
        symptom = SymptomMaster.objects.get(symptom_name='Vomitting')

        self.assertEqual(symptom.symptom_name, 'Vomitting')  # Check the symptom name

    def test_symptom_deletion(self):
        # Test the deletion of a symptom
        self.symptom.delete()
        remaining_symptoms = SymptomMaster.objects.count()
        self.assertEqual(remaining_symptoms, 0)  # Check if no symptoms remain after deletion
