#!/usr/bin/env python3

from app import app
from models import db, User, Product, CartItem

with app.app_context():

    print("seeding database...")

    User.query.delete()
    Product.query.delete()
    CartItem.query.delete()

    users = []
    jim = User(name="Jim", age=20)
    ezekiel = User(name="Ezekiel", age=20)
    freddy = User(name="Freddy", age=78)
    sandy = User(name="Sandy", age=34)
    ricardo = User(name="Ricardo", age=40)

    users.append(jim)    
    users.append(ezekiel)    
    users.append(freddy)    
    users.append(sandy)    
    users.append(ricardo)    
    db.session.add_all(users)

    products = []
    prod_1 = Product(name="Soap", price=2.99, stock=100)
    prod_2 = Product(name="Jordan 8s", price=200.00, stock=15)
    prod_3 = Product(name="Printer", price=149.00, stock=75)
    prod_4 = Product(name="Pens, 10 count", price=12.99, stock=300)
    prod_5 = Product(name="Gatorade, case of 24", price=39.99, stock=50)

    products.append(prod_1)
    products.append(prod_2)
    products.append(prod_3)
    products.append(prod_4)
    products.append(prod_5)
    db.session.add_all(products)

    cart_items = []

    item_1 = CartItem(user_id=1, product_id=2, quantity=6)
    item_2 = CartItem(user_id=2, product_id=2, quantity=6)
    item_3 = CartItem(user_id=3, product_id=1, quantity=18)
    item_4 = CartItem(user_id=4, product_id=4, quantity=100)
    item_5 = CartItem(user_id=5, product_id=3, quantity=1)

    cart_items.append(item_5)
    cart_items.append(item_4)
    cart_items.append(item_3)
    cart_items.append(item_2)
    cart_items.append(item_1)

    db.session.add_all(cart_items)
    
    db.session.commit()

    print("done seeding!")