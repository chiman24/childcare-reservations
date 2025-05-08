import React, { useState } from "react";
import { TextField, Button, MenuItem, Container, Typography, Box } from "@mui/material";
import { submitReservation } from "../api/api.jsx";
import { useNavigate } from "react-router-dom";
import dayjs from "dayjs";
import { DatePicker, LocalizationProvider} from "@mui/x-date-pickers";
import { AdapterDayjs } from "@mui/x-date-pickers/AdapterDayjs";

const ReservationForm = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    parent_name: "",
    email: "",
    phone_number: "",
    // rehearsal_date: dayjs().day() <= 1 ? dayjs().day(5).format("YYYY-MM-DD") : dayjs().add(1, "week").day(5).format("YYYY-MM-DD"),
    rehearsal_date: dayjs().day() <= 1 ? dayjs().day(5) : dayjs().add(1, "week").day(5),
    num_children: "",
    child_ages: [],
    special_notes: "",
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleNumChildrenChange = (e) => {
    const numChildren = parseInt(e.target.value, 10) || "";
    setFormData({
      ...formData,
      num_children: numChildren,
      child_ages: new Array(numChildren).fill(0)
    })
  }

  const handleAgeChange = (index, value) => {
    const updatedAges = [...formData.child_ages];
    updatedAges[index] = value;
    setFormData({ ...formData, child_ages: updatedAges });
  }

  const handleDateChange = (e) => {
    setFormData({
      ...formData,
      rehearsal_date: e
    })

  }

  //Convert rehearsal_date to string
  const convertDateToString = (date) => {
    return date.format("YYYY-MM-DD");
  }
  
  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // Convert rehearsal_date to string
      const formattedRehearsalDate = convertDateToString(formData.rehearsal_date);
      const updatedFormData = { ...formData, rehearsal_date: formattedRehearsalDate };
      await submitReservation(updatedFormData);
      navigate("/confirmation")
    } catch (error) {
      console.error("Error submitting reservation", error);
    }
  };

  return (
    <Container maxWidth="sm">
      <Box my={4}>
        <Typography variant="h5">JCCI Choir Childcare Reservation</Typography>
        <form onSubmit={handleSubmit}>
          <TextField label="Parent Name" name="parent_name" value={formData.parent_name} onChange={handleChange} fullWidth required margin="normal" />
          <TextField label="Email" name="email" type="email" value={formData.email} onChange={handleChange} fullWidth required margin="normal" />
          <TextField label="Phone Number" name="phone_number" value={formData.phone_number} onChange={handleChange} fullWidth margin="normal" />

          {/* <TextField label="Rehearsal Date" name="rehearsal_date" type="date" value={formData.rehearsal_date} onChange={handleChange} fullWidth required margin="normal" /> */}

          
          {/* Rehearsal Date */}
          <LocalizationProvider dateAdapter={AdapterDayjs}>
            <DatePicker sx={{width: "100%"}}
              label="Rehearsal Date" 
              name="rehearsal_date" 
              value={formData.rehearsal_date}
              
              // Only allow selection of future Fridays or Saturdays.  
              // In a particular week, Monday is the last day that you're allowed to reserve the Friday or Saturday of that week.
              shouldDisableDate={(date) => {
                const today = dayjs();
                const daysUntilFriday = date.diff(today, "day")
                return ![5, 6].includes(date.day()) || date.isBefore(dayjs()) || daysUntilFriday < 4 }
              } 
              onChange={handleDateChange}
            />
          </LocalizationProvider>
          {/* End Rehearsal Date */}

          <TextField label="Number of Children" name="num_children" type="number" value={formData.num_children} onChange={handleNumChildrenChange} fullWidth required margin="normal" />

          {/* Dynamically generated child age dropdowns */}
          {formData.child_ages.map((age, index) => (
            <TextField
              key={index}
              select
              label={`Child ${index + 1} Age`}
              value={age}
              onChange={(e) => handleAgeChange(index, e.target.value)}
              fullWidth
              margin="normal"
            >
              {[...Array(10).keys()].map((ageOption) => (
                <MenuItem key={ageOption} value={ageOption}>
                  {ageOption}
                </MenuItem>
              ))}
            </TextField>
          ))}

          <TextField label="Special Notes" name="special_notes" multiline rows={3} value={formData.special_notes} onChange={handleChange} fullWidth margin="normal" />
          <Button type="submit" variant="contained" color="primary" fullWidth>
            Submit Reservation
          </Button>
        </form>
      </Box>
    </Container>
  );
};

export default ReservationForm;
