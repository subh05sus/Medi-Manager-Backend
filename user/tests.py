from django.contrib.auth.models import User
from user.models import UserProfile  # Replace 'yourapp' with your Django app name

def create_user_profile(username, first_name, last_name, email, phone_number, aadhar, address, postal_code):
    # Create a User instance
    user = User.objects.create(username=username, email=email)

    profile = UserProfile.objects.create(
        user_id=user,
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone_number=phone_number,
        aadhar=aadhar,
        address=address,
        postal_code=postal_code
    )
    return profile

# Example usage:
if __name__ == '__main__':
    # Replace the arguments with the desired values
    profile = create_user_profile(
        user_id='john_doe',
        first_name='John',
        last_name='Doe',
        email='john@example.com',
        phone_number='1234567890',
        aadhar='404312383055',
        address='123 Main St',
        postal_code='12345'
    )
    print(f"User Profile created: {profile}")


from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import UserProfile , User

class UserAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='test_user', 
        email='test@example.com', 
        password='testpassword',
           first_name='Test',
            last_name='User',)
        existing_user = User.objects.get(username='test_user')
        self.user_profile = UserProfile.objects.create(
            user_id= existing_user , #self.user.username,
            first_name='Test',
            last_name='User',
            email='test@example.com',
            phone_number='1234567890',
            address='Test Address',
            postal_code='12345'
        )

    def test_user_list(self):
        response = self.client.get('/api/v1/user/')  # Replace with your actual user endpoint
        print(response.json())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), User.objects.count())

    def test_user_profile_detail(self):
        response = self.client.get(f'/api/v1/user/user-profile/{self.user_profile.profile_id}/')  # Replace with your actual user profile endpoint
        self.assertEqual(response.status_code, 200)
        print(response.json())
        self.assertEqual(response.data['user_id'], self.user.id)
        self.assertEqual(response.data['first_name'], self.user.first_name)
        # Add more assertions as per your UserProfile fields

    # Add more test cases for other CRUD operations (create, update, delete) as needed

