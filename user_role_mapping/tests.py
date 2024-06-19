# test.py

from django.contrib.auth.models import User
from role.models import Role
from user.models import UserProfile
from user_role_mapping.models import UserRoleMapping

def create_user_profile(username, first_name, last_name, email, phone_number, aadhar, address, postal_code):
    user = User.objects.create(username=username, email=email)
    profile = UserProfile.objects.create(
        username=user,
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone_number=phone_number,
        aadhar=aadhar,
        address=address,
        postal_code=postal_code
    )
    return profile

def create_role(role_name, description):
    role = Role.objects.create(name=role_name, description=description)
    return role

def create_user_role_mapping(user_profile, role):
    user_role_mapping = UserRoleMapping.objects.create(
        user_id=user_profile,
        role_id=role,
        # Add other fields for UserRoleMapping if needed
    )
    return user_role_mapping

# Example usage:
if __name__ == '__main__':
    # Create a UserProfile
    profile = create_user_profile(
        username='john_doe',
        first_name='John',
        last_name='Doe',
        email='john@example.com',
        phone_number='1234567890',
        aadhar='1234567890123456',
        address='123 Main St',
        postal_code='12345'
    )

    # Create a Role
    role = create_role(
        role_name='Admin',
        description='Administrator role'
    )

    # Create UserRoleMapping
    user_role_mapping = create_user_role_mapping(profile, role)
    print(f"User Role Mapping created: {user_role_mapping}")
