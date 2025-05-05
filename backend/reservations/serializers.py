from rest_framework import serializers
# from .models import Reservation
from .models_mongo import Reservation
from django.core.mail import send_mail
from django.conf import settings
from .email import send_reservation_email

# class ReservationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Reservation
#         fields = '__all__'  # Serialize all fields

    

#     def create(self, validated_data):
#         reservation = super().create(validated_data)

#         # Send email notification
#         send_reservation_email(reservation)

#         return reservation
    
    
class ReservationSerializer(serializers.Serializer):
    parent_name = serializers.CharField(max_length=100)
    rehearsal_date = serializers.DateField()
    num_children = serializers.IntegerField()
    child_ages = serializers.ListField(child=serializers.IntegerField())
    email = serializers.EmailField()
    phone_number = serializers.CharField(max_length=15, required=False)
    # special_notes = serializers.CharField(max_length=500, required=False)
    # timestamp = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        reservation = Reservation(**validated_data).save()
        # Send email notification
        send_reservation_email(reservation)
        return reservation

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance