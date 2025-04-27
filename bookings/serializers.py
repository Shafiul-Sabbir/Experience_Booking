from rest_framework import serializers
from.models import Booking
from experiences.models import AvailabilitySlot
from django.db import transaction

# This serializer is used to handle the booking of experiences
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ['customer', 'status']

    # This method is called when validating the data before creating a new booking
    def validate(self, data):
        slot = data['slot']
        if slot.booked_count > slot.capacity:
            raise serializers.validationError("This slot is fully booked.")
        return data

    # This method is called when creating a new booking
    def create(self, validated_data):
        slot = validated_data['slot']
        if slot.booked_count >= slot.capacity:
            raise serializers.ValidationError("This slot is fully booked.")
        slot.booked_count += 1
        slot.save()
        return Booking.objects.create(**validated_data)
