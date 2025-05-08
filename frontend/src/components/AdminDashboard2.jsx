import React, { useState, useEffect } from "react";
import { Container, Box, Typography, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper, CircularProgress, Collapse } from "@mui/material";
import { DateCalendar } from "@mui/x-date-pickers"
import TextField from "@mui/material/TextField";
import dayjs from "dayjs";
import { fetchReservationsByDate } from "../api/api";
import { LocalizationProvider } from "@mui/x-date-pickers";
import { AdapterDayjs } from "@mui/x-date-pickers/AdapterDayjs";

const AdminDashboard = () => {
  const [selectedDate, setSelectedDate] = useState(dayjs());  // Default to today
  const [reservations, setReservations] = useState([]);
  const [loading, setLoading] = useState(false);
  const [expandedRow, setExpandedRow] = useState(null);


  // Fetch reservations for the selected date
  const fetchReservations = async (date) => {
    setLoading(true);
    try {
      const formattedDate = date.format("YYYY-MM-DD");
      const response = await fetchReservationsByDate(formattedDate)
      setReservations(response.data);
    } catch (error) {
      console.error("Error fetching reservations:", error);
    }
    setLoading(false);
  };

  // Fetch reservations when date changes
  useEffect(() => {
    fetchReservations(selectedDate);
  }, [selectedDate]);

  return (
    <Container maxWidth="md">
      <Box my={4} textAlign="center">
        <Typography variant="h5" fontWeight="bold">
          Childcare Reservations
        </Typography>
        
        {/* Responsive DatePicker */}
        <Box mt={3} sx={{ display: "flex", justifyContent: "center", flexWrap: "wrap" }}>
         <LocalizationProvider dateAdapter={AdapterDayjs}>
          <DateCalendar
            value={selectedDate}
            onChange={(newDate) => setSelectedDate(newDate)}
            // renderInput={(params) => <TextField {...params} fullWidth />}
            // sx={{ width: { xs: "100%", sm: "50%", md: "40%"} }}
          />
         </LocalizationProvider>
        </Box>
      </Box>

      {/* Loading Spinner */}
      {loading ? (
        <Box display="flex" justifyContent="center" mt={3}>
          <CircularProgress />
        </Box>
      ) : reservations.length > 0 ? (
        <TableContainer component={Paper} sx={{ mt: 3, overflowX: "auto" }}>
          <Table sx={{ minWidth: 330 }}>
            <TableHead>
              <TableRow sx={{ bgcolor: "primary.light" }}>
                <TableCell sx={{ fontWeight: "bold" }}>Parent Name</TableCell>
                <TableCell sx={{ fontWeight: "bold" }}># of Children</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {reservations.map((res) => {
                const isOpen = expandedRow === res._id;

                return (
                  <React.Fragment key={res._id}>
                    <TableRow
                      hover
                      onClick={() => setExpandedRow(isOpen ? null : res._id)}
                      sx={{ cursor: "pointer" }}
                    >
                      <TableCell>{res.parent_name}</TableCell>
                      <TableCell>
                        {res.num_children} {res.child_ages.length > 1 ? `(Ages: ${res.child_ages.join(", ")})` : `(Age: ${res.child_ages[0]})`}
                      </TableCell>
                    </TableRow>

                    {/* Expandable Row for Notes */}
                    <TableRow>
                      <TableCell colSpan={2} sx={{ py: 0, borderBottom: 0 }}>
                        <Collapse in={isOpen} timeout="auto" unmountOnExit>
                          <Box p={2}>
                            <Typography variant="body2" fontStyle="italic">
                              {res.special_notes ? `Notes: ${res.special_notes}` : "No special notes."}
                            </Typography>
                          </Box>
                        </Collapse>
                      </TableCell>
                    </TableRow>
                  </React.Fragment>
                );
              })}
            </TableBody>

          </Table>
        </TableContainer>
      ) : (
        <Typography mt={3} textAlign="center">No reservations found for this date.</Typography>
      )}
    </Container>
  );
};

export default AdminDashboard;
