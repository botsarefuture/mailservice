from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from pymongo import MongoClient
from dns.resolver import query, NoAnswer, NXDOMAIN
import bcrypt

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'mail.luova.club'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@example.com'  # Update with your SMTP username
app.config['MAIL_PASSWORD'] = 'your_email_password'  # Update with your SMTP password
mail = Mail(app)

# MongoDB configuration
client = MongoClient('mongodb://localhost:27017/')
db = client['email_service']
users_collection = db['users']

# Dictionary to store verified domains
verified_domains = {}

def verify_domain(domain):
    try:
        # Check if the domain has the verification record
        txt_records = query(f'_email-verification.{domain}', 'TXT')
        for txt_record in txt_records:
            if 'mailservice.luova.club' in txt_record.to_text():
                return True
    except (NoAnswer, NXDOMAIN):
        pass
    return False

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    domain = email.split('@')[1]

    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    if users_collection.find_one({'email': email}):
        return jsonify({'error': 'Email already registered'}), 409

    users_collection.insert_one({'email': email, 'password': bcrypt.hashpw(password.encode(), bcrypt.gensalt())})
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    user = users_collection.find_one({'email': email})
    if not user or not bcrypt.checkpw(password.encode(), user['password']):
        return jsonify({'error': 'Invalid email or password'}), 401

    return jsonify({'message': 'Login successful'}), 200

@app.route('/send_email', methods=['POST'])
def send_email():
    data = request.json
    sender_email = data.get('sender_email')
    recipient_email = data.get('recipient_email')
    subject = data.get('subject')
    body = data.get('body')

    if not sender_email or not recipient_email or not subject or not body:
        return jsonify({'error': 'Missing required fields'}), 400

    domain = sender_email.split('@')[1]
    user = users_collection.find_one({'email': sender_email})

    if not user:
        return jsonify({'error': 'User not found'}), 404

    if not bcrypt.checkpw(data.get('password').encode(), user['password']):
        return jsonify({'error': 'Invalid password'}), 401

    if domain not in verified_domains:
        if not verify_domain(domain):
            return jsonify({'error': 'Domain not verified'}), 403
        verified_domains[domain] = True

    msg = Message(subject, sender=sender_email, recipients=[recipient_email])
    msg.body = body

    try:
        mail.send(msg)
        return jsonify({'message': 'Email sent successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
