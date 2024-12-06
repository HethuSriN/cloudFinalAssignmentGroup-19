# from flask import Flask, render_template, request, redirect, url_for

# app = Flask(__name__)

# VALID_USERNAME = "admin"
# VALID_PASSWORD = "password123"

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/login', methods=['POST'])
# def login():
#     username = request.form.get('username')
#     password = request.form.get('password')
#     if username == VALID_USERNAME and password == VALID_PASSWORD:
#         return render_template('chatbot.html')  # Serve the chatbot interface
#     else:
#         return "Invalid credentials. Please go back and try again.", 401
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8080)

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')
    return f"Welcome {username}, your data has been submitted!"

if __name__ == "__main__":
    app.run(debug=True)