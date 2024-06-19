from django.test import TestCase
from .models import Workflow

class WorkflowModelTest(TestCase):
    def setUp(self):
        # Create a sample Workflow instance for testing
        self.workflow = Workflow.objects.create(name='Test Workflow')

    def test_workflow_creation(self):
        # Test whether the workflow is created properly
        workflow_count = Workflow.objects.count()
        self.assertEqual(workflow_count, 1)  

    def test_workflow_attributes(self):
        # Test the attributes of the created workflow
        workflow = Workflow.objects.get(name='Test Workflow')

        self.assertEqual(workflow.name, 'Test Workflow')  # Check the name of the workflow

    def test_workflow_blank_name(self):
        # Test the behavior of a blank (empty) name in the workflow
        blank_workflow = Workflow.objects.create()  # Creating a Workflow instance without a name
        self.assertEqual(blank_workflow.name, '')  

    def test_workflow_deletion(self):
        # Test the deletion of a workflow
        self.workflow.delete()
        remaining_workflows = Workflow.objects.count()
        self.assertEqual(remaining_workflows, 0)  
        # Check if no workflows remain after deletion
