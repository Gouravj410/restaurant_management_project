from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def validate_status(self, value):
        """Prevent invalid status jumps."""
        instance = self.instance  # existing order

        if instance:  # only on update
            valid_transitions = {
                'Pending': ['Preparing'],
                'Preparing': ['Ready'],
                'Ready': ['Served'],
                'Served': [],
            }
            if value not in valid_transitions[instance.status]:
                raise serializers.ValidationError(
                    f"Invalid status change: {instance.status} → {value}"
                )
        return value
