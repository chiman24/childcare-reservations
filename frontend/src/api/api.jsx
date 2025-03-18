import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000/api";

// Submit a reservation
export const submitReservation = async (reservationData) => {
  return axios.post(`${BASE_URL}/reservations/`, reservationData);
};

// Fetch all reservations (Admin only)
export const fetchReservations = async () => {
  return axios.get(`${BASE_URL}/reservations/`);
};

export const fetchReservationsByDate = async (date) => {
  return axios.get(`${BASE_URL}/reservations/${date}`);
};
