from rest_framework import serializers
from .models import Experience, AvailabilitySlot
from .tasks import generate_slots

# Experience serializer for handling experience creation.
class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'
        read_only_fields = ['provider']

    # This method is called when creating a new experience
    def create(self, validated_data):
        experience = Experience.objects.create(**validated_data)
        generate_slots.delay(experience.id)
        return experience

# slot serializer for handling availability slots
class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailabilitySlot
        fields = '__all__'
