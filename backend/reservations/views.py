from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models_mongo import Reservation
from .serializers import ReservationSerializer

class ReservationListCreateView(APIView):
    def get(self, request):
        reservations = Reservation.objects.order_by('-date')
        data = [ReservationSerializer(r).data for r in reservations]
        return Response(data)

    def post(self, request):
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            reservation = serializer.save()
            return Response(ReservationSerializer(reservation).data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
