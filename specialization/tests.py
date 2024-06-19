from django.test import TestCase
from rest_framework.test import APIClient
from .models import Specialization

class SpecializationModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        Specialization.objects.create(name='Cardiology')

    def test_specialization_name(self):
        specialization = Specialization.objects.get(name='Cardiology')
        self.assertEqual(specialization.name, 'Cardiology')

    def test_specialization_id(self):
        specialization = Specialization.objects.get(name='Cardiology')
        self.assertIsNotNone(specialization.id)




class SpecializationAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_specialization(self):
        specialization_data = {
            'name': 'Cardiology'  
        }

        response = self.client.post('/api/v1/specialization/', specialization_data)
        self.assertEqual(response.status_code, 201)  # Check if Specialization creation was successful
        self.assertTrue(Specialization.objects.filter(name='Cardiology').exists())  # Check if Specialization was created in the database

    def test_retrieve_specialization(self):
        specialization = Specialization.objects.create(name='Dermatology')  # Create a sample specialization for retrieval

        response = self.client.get(f'/api/v1/specialization/{specialization.id}/')
        self.assertEqual(response.status_code, 200)  # Check if Specialization retrieval was successful
        self.assertEqual(response.data['name'], 'Dermatology')  # Check if retrieved Specialization matches the created one
        # Add other assertions based on your API response

