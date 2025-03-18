from django.shortcuts import render
from rest_framework import generics
from .models import Reservation
from .serializers import ReservationSerializer
from django.http import JsonResponse
import datetime

# Create your views here.
# API: List & Create Reservations (For Parents)
class ReservationListCreateView(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

# API: Retrieve, Update, Delete (For Admins)
class ReservationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

def get_reservations_by_date(request, date):
    try:
        # Validate date format
        datetime.datetime.strptime(date, "%Y-%m-%d")

        reservations = Reservation.objects.filter(rehearsal_date=date).values()
        return JsonResponse(list(reservations), safe=False)
    except ValueError:
        return JsonResponse({"error": "Invalid date format. Use YYYY-MM-DD."}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)