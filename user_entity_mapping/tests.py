# test.py

from django.contrib.auth.models import User
from user.models import User  # Update 'user.models' import path as needed
from entity.models import Entity  # Update 'entity.models' import path as needed
from user_entity_mapping.models import UserEntityMapping  # Update 'yourapp.models' import path as needed

def create_user(username, email):
    user = User.objects.create(username=username, email=email)
    return user

def create_entity(name):
    entity = Entity.objects.create(name=name)
    return entity

def create_user_entity_mapping(user, entity):
    user_entity_mapping = UserEntityMapping.objects.create(
        user_id=user,
        entity_id=entity,
        # Additional fields for UserEntityMapping if needed
    )
    return user_entity_mapping

# Example usage:
if __name__ == '__main__':
    # Create a User
    user = create_user(username='john_doe', email='john@example.com')

    # Create an Entity
    entity = create_entity(name='Entity 1')

    # Create UserEntityMapping
    user_entity_mapping = create_user_entity_mapping(user, entity)
    print(f"User Entity Mapping created: {user_entity_mapping}")
