import axios from "axios";

// const BASE_URL = "https://jv.tools.childcare-reservations.big-heart-ventures.com:8000/api";
// const BASE_URL = "http://localhost:8000";

// Submit a reservation
export const submitReservation = async (reservationData) => {
  return axios.post(`/api/reservations/`, reservationData);
};

// Fetch all reservations (Admin only)
export const fetchReservations = async () => {
  return axios.get(`/api/reservations/`);
};

export const fetchReservationsByDate = async (date) => {
  return axios.get(`/api/reservations/${date}`);
};
