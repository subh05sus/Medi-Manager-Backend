from django.test import TestCase
from rest_framework.test import APIClient
from .models import Role

class RoleModelTest(TestCase):
    def setUp(self):
        self.role = Role.objects.create(name='Admin')  # Create a Role instance for testing
    
    def test_role_name(self):
        role = Role.objects.get(name='Admin')
        self.assertEqual(role.name, 'Admin')  # Check if the name of the role matches

    def test_role_id(self):
        role = Role.objects.get(name='Admin')
        self.assertIsNotNone(role.id)  # Check if the ID is assigned (not None)




class RoleAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_role(self):
        role_data = {
            'name': 'Doctor'  # Example role name - change it according to your requirements
            # Add other required fields for creating a Role if applicable
        }

        response = self.client.post('/api/v1/role/', role_data)
        self.assertEqual(response.status_code, 201)  # Check if Role creation was successful
        self.assertTrue(Role.objects.filter(name='Doctor').exists())  # Check if Role was created in the database

    def test_retrieve_role(self):
        role = Role.objects.create(name='Patient')  # Create a sample role for retrieval

        response = self.client.get(f'/api/v1/role/{role.id}/')
        self.assertEqual(response.status_code, 200)  # Check if Role retrieval was successful
        self.assertEqual(response.data['name'], 'Patient')  # Check if retrieved Role matches the created one
        # Add other assertions based on your API response

    # Add test methods for update, delete, and other API endpoints related to Role
    # Use proper URL endpoints and payload data as per your API design


