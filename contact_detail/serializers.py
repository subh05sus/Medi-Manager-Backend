from rest_framework import serializers
from .models import VisitorContact

# Define the serializer

class VisitorContactSerializer(serializers.ModelSerializer):
    class Meta:
        model   = VisitorContact
        fields  = ('id', 
                #    'user_id',
                   'visitor_name',
                   'email',
                   'phone_number',
                   'country',
                   'state',
                )

    


