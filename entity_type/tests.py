from django.test import TestCase
from rest_framework.test import APIClient
from .models import EntityType

class EntityTypeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        EntityType.objects.create(name='Hospital')  # Create an EntityType instance for testing

    def test_entity_type_creation(self):
        entity_type = EntityType.objects.first()
        self.assertIsNotNone(entity_type)
        self.assertEqual(entity_type.name, 'Hospital')  # Test the name of the entity type
        # Add other assertions based on your model's fields and logic



class EntityTypeAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_entity_type(self):
        entity_type_data = {
            'name': 'Clinic'  # Example entity type name - modify as needed
            # Add other required fields for creating an EntityType if applicable
        }

        response = self.client.post('/api/v1/entity-type/', entity_type_data)
        self.assertEqual(response.status_code, 201)  # Check if EntityType creation was successful
        self.assertTrue(EntityType.objects.filter(name='Clinic').exists())  # Check if EntityType was created in the database

    def test_retrieve_entity_type(self):
        entity_type = EntityType.objects.create(name='Hospital')  # Create a sample entity type for retrieval

        response = self.client.get(f'/api/v1/entity-type/{entity_type.id}/')
        self.assertEqual(response.status_code, 200)  # Check if EntityType retrieval was successful
        self.assertEqual(response.data['name'], 'Hospital')  # Check if retrieved EntityType matches the created one
        # Add other assertions based on your API response

    # Add test methods for update, delete, and other API endpoints related to EntityType
    # Use proper URL endpoints and payload data as per your API design

