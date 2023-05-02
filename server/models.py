from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
# from sqlalchemy import MetaData

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    # email and password to come later

    @validates("name")
    def validate_name(self, key, value):
        if value == "":
            raise ValueError("Name cannot be empty.")
        return value

    @validates("age")
    def validate_age(self, key, value):
        if value < 15:
            raise ValueError("Age must be at least 15.")
        return value

    def __repr__(self):
        return f"<User: id={self.id} name={self.name} age={self.age}>"
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age
        }

class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"""<Product: 
            id={self.id} 
            name={self.name} 
            price={self.price} 
            stock={self.stock}>"""
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "stock": self.stock
        }

class CartItem(db.Model):
    __tablename__ = "cart_items"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"""<CartItem: 
            id={self.id} 
            user_id={self.user_id} 
            product_id={self.product_id} 
            quantity={self.quantity}>"""
    
    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "product_id": self.product_id,
            "quantity": self.quantity
        }