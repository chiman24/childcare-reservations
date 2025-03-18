from django.urls import path
from .views import ReservationListCreateView, ReservationDetailView, get_reservations_by_date

urlpatterns = [
    path('reservations/', ReservationListCreateView.as_view(), name='reservation-list-create'),
    path('reservations/<int:pk>/', ReservationDetailView.as_view(), name='reservation-detail'),
    path("reservations/<str:date>/", get_reservations_by_date, name="reservations-by-date"),
]
