from django.test import TestCase
from .models import Component

class ComponentModelTest(TestCase):
    def setUp(self):
        self.component1 = Component.objects.create(name='Component 1')
        self.component2 = Component.objects.create(name='Component 2')

    def test_component_creation(self):
        component_count = Component.objects.count()
        self.assertEqual(component_count, 2)  # Check if two components are created

    def test_component_attributes(self):
        component_1 = Component.objects.get(name='Component 1')
        component_2 = Component.objects.get(name='Component 2')

        self.assertEqual(component_1.name, 'Component 1')  # Check the name of component 1
        self.assertEqual(component_2.name, 'Component 2')  

    def test_component_deletion(self):
        self.component1.delete()
        remaining_components = Component.objects.count()
        self.assertEqual(remaining_components, 1)  # Check if only one component remains after deletion
