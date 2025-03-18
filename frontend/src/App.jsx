import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import ParentPage from "./pages/ParentPage";
import AdminDashboard from "./components/AdminDashboard2.jsx";
import ConfirmationPage from "./pages/ConfirmationPage.jsx";

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<ParentPage />} />
        <Route path="/confirmation" element={<ConfirmationPage />} />
        <Route path="/admin" element={<AdminDashboard />} />
      </Routes>
    </Router>
  );
};

export default App;
