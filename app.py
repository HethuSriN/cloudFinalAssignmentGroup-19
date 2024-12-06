from flask import Flask, render_template, request, redirect, url_for, flash, session
import pyodbc  # type: ignore
import pandas as pd
import os
import plotly.express as px
import plotly.graph_objects as go

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/submit', methods=['POST'])
# def submit():
#     username = request.form.get('username')
#     password = request.form.get('password')
#     email = request.form.get('email')
#     return f"Welcome {username}, your data has been submitted!"

# if __name__ == "__main__":
#     app.run(debug=True)

valid_username = "admin"
valid_password = "password123"
valid_email = "admin@example.com"

@app.route('/')
def index():
    return render_template('index.html')  # Render the HTML form

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')

    # Check if the details are correct
    if username == valid_username and password == valid_password and email == valid_email:
        return redirect(url_for('dashboard'))  # Redirect to dashboard page if credentials are correct
    else:
        return render_template('index.html', error_message="Invalid credentials, please try again.")

@app.route('/logout')
def logout():
    session.clear()  # Clear the session
    return redirect(url_for('index'))  # Redirect to the login or home page
