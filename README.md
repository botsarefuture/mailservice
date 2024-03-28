# Email Sending Service

## Introduction
This project provides a Flask-based email sending service that allows users to send emails from their domain using a centralized email server. The service supports user registration, login, and domain-specific email sending with SPF and DKIM authentication.

## Features
- User registration and login functionality.
- Domain-specific email sending with SPF and DKIM authentication.
- Centralized email server hosted at "mailservice.luova.club".
- API endpoints for user authentication and email sending.
- Error handling and response codes for API requests.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/email-sending-service.git
   cd email-sending-service
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure Flask app settings in `app.py`, such as SMTP server credentials and MongoDB connection details.

4. Run the Flask app:
   ```bash
   python app.py
   ```

## API Endpoints
- **Register User**: `/register` (POST)
- **Login User**: `/login` (POST)
- **Send Email**: `/send_email` (POST)

For detailed API documentation, refer to [API Guide](api_guide.md).

## Configuration Guide
To configure your domain for sending emails through the email sending service, follow the [Domain Configuration Guide](domain_configuration_guide.md).

## Contributing
Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).

In addition to the main README file, you may want to include separate files for detailed API documentation (`api_guide.md`) and domain configuration guide (`domain_configuration_guide.md`). These files can provide more detailed information about API endpoints and domain configuration steps, respectively.
