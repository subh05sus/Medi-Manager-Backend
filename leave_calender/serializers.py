from rest_framework import serializers
from .models import AppliedLeave

class AppliedLeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model   = AppliedLeave
        fields  = ( 'id', 
                    'purpose',  
                    'user_id'  ,
                    'startDate',
                    'endDate',
                     )