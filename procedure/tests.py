from django.test import TestCase
from .models import Procedure

class ProcedureTestCase(TestCase):
    def setUp(self):
        # Create a Procedure instance for testing
        self.procedure = Procedure.objects.create(
            name='Test Procedure',
            growth_required=True,
            vital_required=False
        )

    def test_procedure_creation(self):
        # Retrieve the Procedure instance from the database
        procedure = Procedure.objects.get(name='Test Procedure')

        # Ensure the Procedure is created with the correct attributes
        self.assertEqual(procedure.name, 'Test Procedure')
        self.assertTrue(procedure.growth_required)
        self.assertFalse(procedure.vital_required)

    # Add more test cases as needed to cover specific functionalities or edge cases
