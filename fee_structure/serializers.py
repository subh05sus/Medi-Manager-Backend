from rest_framework import serializers
from .models import UserFeeStructure, FeeType

# Define the serializer

class UserFeeStructureSerializer(serializers.ModelSerializer):
    fee_type_name = serializers.SerializerMethodField()
    cost_type = serializers.SerializerMethodField()  # This is the new SerializerMethodField for cost_type

    class Meta:
        model = UserFeeStructure
        fields = ('id', 'user_id', 'fee_type', 'fee_amount', 'fee_type_name', 'cost_type')

    def get_fee_type_name(self, obj):
        # Return the name of the fee_type, or None if not available
        return obj.fee_type.name if obj.fee_type else None

    def get_cost_type(self, obj):
        # Return the cost_type of the fee_type, or None if not available
        return obj.fee_type.cost_type if obj.fee_type else None

    # def create(self, validated_data):
    #     fee_structure_data = validated_data
    #     print(fee_structure_data)
    #     fee_str_instance, _          = UserFeeStructure.objects.get_or_create(fee_type=fee_structure_data['fee_type'])
    #     if fee_structure_data.get('fee_amount'):
    #         fee_str_instance.fee_amount  = fee_structure_data['fee_amount']
     
    #     fee_str_instance.save()

    #     return fee_str_instance
    


class FeeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model   = FeeType
        fields  = ('id', 
                   'name',  
                    'cost_type'  ,
                     )