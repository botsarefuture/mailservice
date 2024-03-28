## Email Sending Service API Guide

### Base URL:
- The base URL for accessing the API is `https://mailservice.luova.club`.

### Authentication:
- Authentication is required for certain endpoints. Users must register and login to access these endpoints.

### Endpoints:

1. **Register User**
   - **URL:** `/register`
   - **Method:** `POST`
   - **Description:** Allows users to register for the email sending service.
   - **Request Body:** JSON object with `email` and `password` fields.
     ```json
     {
       "email": "user@example.com",
       "password": "password123"
     }
     ```
   - **Response:** 
     - `201 Created` if registration is successful.
     - `400 Bad Request` if missing required fields.
     - `409 Conflict` if email is already registered.

2. **Login User**
   - **URL:** `/login`
   - **Method:** `POST`
   - **Description:** Allows users to log in to the email sending service.
   - **Request Body:** JSON object with `email` and `password` fields.
     ```json
     {
       "email": "user@example.com",
       "password": "password123"
     }
     ```
   - **Response:** 
     - `200 OK` if login is successful.
     - `400 Bad Request` if missing required fields.
     - `401 Unauthorized` if invalid email or password.

3. **Send Email**
   - **URL:** `/send_email`
   - **Method:** `POST`
   - **Description:** Allows authenticated users to send emails.
   - **Request Body:** JSON object with `sender_email`, `password`, `recipient_email`, `subject`, and `body` fields.
     ```json
     {
       "sender_email": "user@example.com",
       "password": "password123",
       "recipient_email": "recipient@example.com",
       "subject": "Test Email",
       "body": "This is a test email."
     }
     ```
   - **Response:** 
     - `200 OK` if email is sent successfully.
     - `400 Bad Request` if missing required fields.
     - `401 Unauthorized` if invalid password.
     - `403 Forbidden` if domain is not verified.
     - `404 Not Found` if user not found.
     - `500 Internal Server Error` if an error occurs while sending the email.

### Error Handling:
- The API returns appropriate HTTP status codes along with JSON error messages to indicate the success or failure of each request.

### Rate Limiting:
- Rate limiting is not implemented in this version of the API. However, it is recommended to implement rate limiting to prevent abuse and ensure fair usage of the service.

### Example Usage:
- Below is an example of how to send an email using the API with cURL:
  ```
  curl -X POST \
       -H "Content-Type: application/json" \
       -d '{
             "sender_email": "user@example.com",
             "password": "password123",
             "recipient_email": "recipient@example.com",
             "subject": "Test Email",
             "body": "This is a test email."
           }' \
       https://mailservice.luova.club/send_email
  ```

This guide provides an overview of the available API endpoints, their usage, and error handling. Users can interact with the API to register, login, and send emails through the email sending service.
