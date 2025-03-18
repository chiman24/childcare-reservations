import React from "react";
import { Container, Paper } from "@mui/material";
import ReservationForm from "../components/ReservationForm.jsx";

const ParentPage = () => {
  return (
    <Container maxWidth="sm">
      <div
        style={{
          display: "grid",
          placeItems: "center",
          height: "100vh",
          padding: "1rem", // Add padding for small screens
          alignItems: "center",
          // width: "100vw",
          // overflowX: "hidden"
        }}
      >
        <Paper
          elevation={3}
          style={{
            padding: "2rem",
            width: "100%",
            maxWidth: "500px"
          }}
        >
          <ReservationForm />
        </Paper>
      </div>
    </Container>
  );
};

export default ParentPage;
