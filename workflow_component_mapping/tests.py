from django.test import TestCase
from .models import WorkflowComponentMapping
from component.models import Component
from workflow.models import Workflow

class WorkflowComponentMappingModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create sample Workflow and Component instances for testing
        cls.workflow = Workflow.objects.create(name='Test Workflow')
        cls.component = Component.objects.create(name='Test Component')

    def setUp(self):
        # Create a sample WorkflowComponentMapping instance for testing
        self.mapping = WorkflowComponentMapping.objects.create(
            workflow_id=self.workflow,
            component_id=self.component
        )

    def test_workflow_component_mapping_creation(self):
        # Test whether the mapping is created properly
        mapping_count = WorkflowComponentMapping.objects.count()
        self.assertEqual(mapping_count, 1)  # Check if one mapping is created

    def test_workflow_component_mapping_attributes(self):
        # Test the attributes of the created mapping
        mapping = WorkflowComponentMapping.objects.get(workflow_id=self.workflow)

        self.assertEqual(mapping.workflow_id, self.workflow)    # Check the workflow ID in mapping
        self.assertEqual(mapping.component_id, self.component)  # Check the component ID in mapping

    def test_workflow_component_mapping_deletion(self):
        # Test the deletion of a mapping
        self.mapping.delete()
        remaining_mappings = WorkflowComponentMapping.objects.count()
        self.assertEqual(remaining_mappings, 0)  # Check if no mappings remain after deletion
