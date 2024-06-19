from rest_framework import serializers
from .models import TestReport

# Define the serializer

class  TestReportSerializer(serializers.ModelSerializer):
    class Meta:
        model   = TestReport
        fields  = (
                'id', 
                "user_id",
                "appointment_id",

                "document_label",
                "document_path",
                )
    


