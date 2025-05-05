from rest_framework import serializers
from .models import Reservation
from django.core.mail import send_mail
from django.conf import settings
from .email import send_reservation_email

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'  # Serialize all fields

    

    def create(self, validated_data):
        reservation = super().create(validated_data)

        # Send confirmation email
        # send_mail(
        #     subject='Childcare Reservation Confirmation',
        #     message=(
        #         f"Hi {reservation.parent_name},\n\n"
        #         f"Your reservation for {reservation.rehearsal_date} has been received.\n\n"
        #         f"Children: {reservation.num_children}\n"
        #         f"Ages: {reservation.child_ages}\n\n"
        #         "Thank you!\nChildcare Team"
        #     ),
        #     from_email=settings.DEFAULT_FROM_EMAIL,
        #     recipient_list=[reservation.email],  # Make sure your model has an email field!
        #     fail_silently=False,
        # )
        send_reservation_email(reservation)

        return reservation
    
    
