import React, { useEffect, useState } from "react";
import { fetchReservations } from "../api/api";
import { Container, Typography, Paper } from "@mui/material";

const AdminDashboard = () => {
  const [reservations, setReservations] = useState([]);

  useEffect(() => {
    const getReservations = async () => {
      try {
        const response = await fetchReservations();
        setReservations(response.data);
      } catch (error) {
        console.error("Error fetching reservations", error);
      }
    };
    getReservations();
  }, []);

  return (
    <Container>
      <Typography variant="h4" gutterBottom>
        Admin Dashboard
      </Typography>
      {reservations.length > 0 ? (
        reservations.map((res) => (
          <Paper key={res.id} style={{ padding: "10px", marginBottom: "10px" }}>
            <Typography>{res.parent_name} - {res.rehearsal_date}</Typography>
          </Paper>
        ))
      ) : (
        <Typography>No reservations found.</Typography>
      )}
    </Container>
  );
};

export default AdminDashboard;
