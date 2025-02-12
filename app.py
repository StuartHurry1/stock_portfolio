import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)

# Configure the database - Uses Heroku DATABASE_URL if available, else falls back to local PostgreSQL
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://postgres:Blue1234%21@localhost/stock_portfolio')

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Database models
class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ticker = db.Column(db.String(10), nullable=False)
    purchase_date = db.Column(db.Date, nullable=True)
    shares = db.Column(db.Integer, nullable=False)
    cost_per_share = db.Column(db.Float, nullable=False)
    fees = db.Column(db.Float, nullable=True)

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "ticker": self.ticker,
            "purchase_date": self.purchase_date,
            "shares": self.shares,
            "cost_per_share": self.cost_per_share,
            "fees": self.fees,
        }

# Home route (Health check)
@app.route('/')
def home():
    return "Stock Website API is running successfully!"

# API Routes
@app.route('/api/portfolio', methods=['GET'])
def get_portfolio():
    try:
        stocks = Stock.query.all()
        return jsonify([stock.as_dict() for stock in stocks])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/portfolio', methods=['POST'])
def add_stock():
    data = request.json
    try:
        stock = Stock(**data)
        db.session.add(stock)
        db.session.commit()
        return jsonify({"message": "Stock added successfully!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Database Initialization Route
@app.route('/api/init-db', methods=['POST'])
def init_db():
    try:
        db.create_all()
        return jsonify({"message": "Database tables created successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
