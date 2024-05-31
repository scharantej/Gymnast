
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(120))
    price = db.Column(db.Float)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)
    quantity = db.Column(db.Integer)

@app.route('/')
def home():
    products = Product.query.all()
    return render_template('home.html', products=products)

@app.route('/cart')
def cart():
    orders = Order.query.filter_by(user_id=1).all()
    return render_template('cart.html', orders=orders)

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/product/<int:product_id>')
def product_details(product_id):
    product = Product.query.get(product_id)
    return render_template('product_details.html', product=product)

@app.route('/admin')
def admin():
    return render_template('admin.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
