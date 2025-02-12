import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)  # Define Flask app instance only once
CORS(app)  # Apply CORS to allow frontend connections

# Supabase API Configuration
SUPABASE_URL = "https://jnlfelelukyytqsxsfxy.supabase.co/rest/v1/"
SUPABASE_API_KEY = os.getenv("SUPABASE_API_KEY")  # Corrected retrieval

HEADERS = {
    "apikey": SUPABASE_API_KEY,
    "Authorization": f"Bearer {SUPABASE_API_KEY}",
    "Content-Type": "application/json"
}

# Home Route (to check if server is running)
@app.route('/')
def home():
    return "Flask server is running!"

# Fetch all portfolio stocks
@app.route('/api/portfolio', methods=['GET'])
def get_portfolio():
    response = requests.get(f"{SUPABASE_URL}portfolio", headers=HEADERS)
    return jsonify(response.json()), response.status_code

# Add a new stock to portfolio
@app.route('/api/portfolio', methods=['POST'])
def add_stock():
    data = request.json
    response = requests.post(f"{SUPABASE_URL}portfolio", headers=HEADERS, json=data)
    return jsonify(response.json()), response.status_code

# Fetch all dividends
@app.route('/api/dividends', methods=['GET'])
def get_dividends():
    response = requests.get(f"{SUPABASE_URL}dividends", headers=HEADERS)
    return jsonify(response.json()), response.status_code

# Add a new dividend entry
@app.route('/api/dividends', methods=['POST'])
def add_dividend():
    data = request.json
    response = requests.post(f"{SUPABASE_URL}dividends", headers=HEADERS, json=data)
    return jsonify(response.json()), response.status_code

@app.route("/api/health")
def health_check():
    return "OK", 200

if __name__ == "__main__":
    app.run(debug=True)
