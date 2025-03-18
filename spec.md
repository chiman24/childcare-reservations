# Choir Childcare Reservation System - Developer Specification

## **1. Overview**
The Choir Childcare Reservation System is a web application designed to allow choir members to indicate if they plan to bring their children to choir rehearsal so that provisions for childcare can be made. The system will include **two separate interfaces**:
1. **Parent Reservation Page** – A private page where parents submit reservations.
2. **Admin Portal** – A secure portal where admins can manage reservations.

## **2. Key Requirements**

### **2.1 User Roles**
- **Parent**: Can submit childcare reservations.
- **Admin**: Can log in to manage reservations.

### **2.2 Parent Reservation Page**
- **Accessible via a private static link** (not listed publicly).
- Parents enter:
  - Their **name** (required)
  - **Email address** (required)
  - **Phone number** (optional)
  - **Rehearsal date** (only Fridays, with availability rules)
  - **Number of children** (required)
  - **Ages of children** (dropdown: 0-9 years old, required)
  - **Special notes** (optional)
- **Form validation:** Ensure required fields are filled correctly.
- **Submission confirmation email** sent via Amazon SES.

### **2.3 Reservation Rules**
- **Only Fridays** are available for reservations.
- A **Friday in the current week is available only if today is Sunday or Monday**.
- Otherwise, the next available reservation is for the **Friday of the following week**.

### **2.4 Admin Portal (Protected by Login)**
- **Admin authentication via username & password.**
- **Admin account management:**
  - **Only an existing admin** can create new admin accounts.
  - Admins can **reset passwords via email or security questions**.
- **Admin dashboard features:**
  - **Calendar view** of reservations (clicking a date shows details).
  - **Search & filter reservations** by date, parent name, or child count.
  - **Edit reservations** (correct details if needed).
  - **Delete reservations** (remove incorrect entries).
  - **Export reservations**:
    - **Download all reservations as CSV**.
    - **Download individual reservations as PDF**.
- **Admin notifications** when a new reservation is submitted.

---

## **3. Tech Stack & Architecture**

### **3.1 Frontend**
- **Framework**: React + Material UI
- **UI Design**: Mobile-first, responsive

### **3.2 Backend**
- **Framework**: Django (Python)
- **Database**: PostgreSQL (hosted on AWS RDS)
- **Authentication**: Django authentication system for admin accounts
- **Email Notifications**: Amazon SES
- **Hosting**: Deployed on AWS EC2
- **Security**:
  - **Automatic SSL (via Let’s Encrypt)** to enforce HTTPS
  - **Form validation & data sanitization** to prevent invalid inputs

### **3.3 API Endpoints**
#### **Parent API**
- `POST /api/reservations/`
  - Submits a new reservation.
  - Returns success message and triggers a confirmation email.

#### **Admin API**
- `POST /api/admin/login/`
  - Logs in an admin.
- `POST /api/admin/logout/`
  - Logs out an admin.
- `GET /api/admin/reservations/`
  - Retrieves all reservations with filtering options.
- `GET /api/admin/reservations/{id}/`
  - Retrieves details of a specific reservation.
- `PUT /api/admin/reservations/{id}/`
  - Updates a reservation.
- `DELETE /api/admin/reservations/{id}/`
  - Deletes a reservation.
- `GET /api/admin/export/csv/`
  - Exports all reservations as a CSV file.
- `GET /api/admin/export/pdf/{id}/`
  - Exports an individual reservation as a PDF.

---

## **4. Data Model (PostgreSQL)**

### **Reservations Table**
| Column Name     | Data Type    | Description |
|----------------|-------------|-------------|
| `id`          | Integer (Auto-increment) | Unique identifier |
| `parent_name` | String (Required) | Parent’s name |
| `email`       | String (Required) | Parent’s email |
| `phone_number`| String (Optional) | Parent’s phone |
| `rehearsal_date` | Date (Required) | Selected Friday |
| `num_children` | Integer (Required) | Number of children attending |
| `child_ages`  | JSON/Array (Required) | List of child ages (0-9) |
| `special_notes` | String (Optional) | Additional details |
| `timestamp`   | DateTime (Auto) | Submission timestamp |

### **Admins Table**
| Column Name     | Data Type    | Description |
|----------------|-------------|-------------|
| `id`          | Integer (Auto-increment) | Unique identifier |
| `username`    | String (Unique, Required) | Admin’s username |
| `password_hash` | String (Required) | Hashed password |
| `email`       | String (Required) | Admin’s email |
| `reset_token` | String (Optional) | Password reset token |
| `created_at`  | DateTime (Auto) | Account creation date |

---

## **5. Error Handling & Edge Cases**
- **Invalid input handling** – Reject submissions with missing/incorrect data.
- **Rate limiting** – Prevent spam by limiting frequent submissions.
- **Database integrity checks** – Ensure valid rehearsal dates (only Fridays).
- **Admin authentication failures** – Secure error messages to prevent brute force.

---

## **6. Testing Plan**
### **6.1 Unit Tests**
✅ **Backend API** (Django tests for models, authentication, and API endpoints).  
✅ **Frontend Components** (React unit tests for form validation and admin interactions).  

### **6.2 Integration Tests**
✅ **End-to-end testing of parent reservations** (Submit, store, notify admins).  
✅ **Admin login and dashboard interactions** (List, edit, delete, export).  
✅ **Email notifications via Amazon SES** (Confirmation & admin alerts).  

### **6.3 Deployment Testing**
✅ **Database migrations on AWS RDS**.  
✅ **SSL certificate application via Let’s Encrypt**.  
✅ **Load testing to handle multiple reservations at once**.  

---

## **7. Deployment & DevOps Plan**
### **7.1 Infrastructure Setup (AWS)**
✅ **EC2 instance** for the Django application.  
✅ **RDS (PostgreSQL)** for database storage.  
✅ **Amazon SES** for email notifications.  
✅ **Let’s Encrypt SSL** for secure HTTPS communication.  

### **7.2 CI/CD Pipeline**
- **GitHub Actions** for automated testing & deployment.
- **Auto-deployment to EC2** upon code merge to `main` branch.

---

## **8. Next Steps**
🚀 **Developers can now begin implementation** using this specification!  
- **Step 1:** Set up Django + PostgreSQL + AWS EC2.
- **Step 2:** Build API endpoints & test with Postman.
- **Step 3:** Develop React frontend & integrate backend API.
- **Step 4:** Deploy & secure the app with SSL.

---

This document serves as a complete guide for developers to implement the system efficiently. Let me know if you'd like any refinements! 🎯

