import React from "react";
import { Link } from "react-router-dom";
import { Container, Typography, Button, Box } from "@mui/material";

const ConfirmationPage = () => {
  return (
    <Container maxWidth="sm">
      <Box textAlign="center" my={5}>
        <Typography variant="h4" gutterBottom>
          🎉 Reservation Submitted!
        </Typography>
        <Typography variant="body1" paragraph>
          Thank you for submitting your childcare reservation. You will receive a confirmation email shortly.
        </Typography>
        <Button component={Link} to="/" variant="contained" color="primary">
          Submit Another Reservation
        </Button>
      </Box>
    </Container>
  );
};

export default ConfirmationPage;
