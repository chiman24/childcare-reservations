from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models_mongo import Reservation
from .serializers import ReservationSerializer
from django.http import JsonResponse
import datetime

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
    
    def get_reservations_by_date(request, date):
        try:
            # Validate and parse the date
            parsed_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()

            # MongoEngine filter (assuming the field is named 'date')
            reservations = Reservation.objects(rehearsal_date=parsed_date)

            # Convert to list of dicts (MongoEngine uses .to_mongo().to_dict())
            data = [res.to_mongo().to_dict() for res in reservations]

            # Optionally remove MongoDB-specific `_id` or convert to string
            # for item in data:
            #     item["_id"] = str(item["_id"])

            return JsonResponse(data, safe=False)

        except ValueError:
            return JsonResponse({"error": "Invalid date format. Use YYYY-MM-DD."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
