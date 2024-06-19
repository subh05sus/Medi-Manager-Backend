# test.py

from entity_type.models import EntityType  # Update import path as needed
from entity.models import Entity  # Update import path as needed

def create_entity_type(name):
    entity_type = EntityType.objects.create(name=name)
    return entity_type

def create_entity(name, entity_type, email, website, phone_number1, phone_number2, address, country, state, postal_code):
    entity = Entity.objects.create(
        name=name,
        type=entity_type,
        email=email,
        website=website,
        phone_number1=phone_number1,
        phone_number2=phone_number2,
        address=address,
        country=country,
        state=state,
        postal_code=postal_code
    )
    return entity

# Example usage:
if __name__ == '__main__':
    # Create an EntityType
    entity_type = create_entity_type(name='Type 1')

    # Create an Entity
    entity = create_entity(
        name='Entity 1',
        entity_type=entity_type,
        email='entity@example.com',
        website='https://example.com',
        phone_number1='1234567890',
        phone_number2='0987654321',
        address='123 Main St',
        country='Saudi Arabia',
        state='Some State',
        postal_code='12345'
    )
    print(f"Entity created: {entity}")

from django.test import TestCase
from rest_framework.test import APIClient
from .models import Entity, EntityType

class EntityAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_entity(self):
        # Create an EntityType to associate with the Entity
        entity_type = EntityType.objects.create(name='Clinic')

        entity_data = {
            'name': 'Sample Entity',
            'type': entity_type.id,
            'email': 'sample@example.com',
            'website': 'http://sample.com',
            'phone_number1': '1234567890',
            'phone_number2': '9876543210',
            'address': '123 Street',
            'country': 'Country',
            'state': 'State',
            'postal_code': '12345'
            # Add other required fields for creating an Entity
        }

        response = self.client.post('/api/v1/entity/', entity_data)
        self.assertEqual(response.status_code, 201)  # Check if Entity creation was successful
        self.assertTrue(Entity.objects.filter(name='Sample Entity').exists())  # Check if Entity was created in the database

    def test_retrieve_entity(self):
        entity_type = EntityType.objects.create(name='Hospital')
        entity = Entity.objects.create(
            name='Test Hospital',
            type=entity_type,
            email='hospital@example.com',
            website='http://hospital.com',
            phone_number1='1234567890',
            address='456 Avenue',
            country='Country',
            state='State',
            postal_code='54321'
            # Add other required fields for creating an Entity
        )

        response = self.client.get(f'/api/v1/entity/{entity.id}/')
        self.assertEqual(response.status_code, 200)  # Check if Entity retrieval was successful
        self.assertEqual(response.data['name'], 'Test Hospital')  # Check if retrieved Entity matches the created one
        # Add other assertions based on your API response

    # Add test methods for update, delete, and other API endpoints related to Entity
    # Use proper URL endpoints and payload data as per your API design

