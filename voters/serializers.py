from rest_framework import serializers
from .models import Voter

class VoterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voter  # Specify the model to serialize
        fields = '__all__'  # Include all fields from the model
