from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# class Person(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)

#     def __repr__(self):
#         return '<Person %r>' % self.username

#     def serialize(self):
#         return {
#             "username": self.username,
#             "email": self.email
#         }

class User(db.Model):
    username = db.Column(db.String(80),primary_key=True)
    email = db.Column(db.String(80),unique=True,nullable=False)
    name = db.Column(db.String(20),nullable=False)
    last_name = db.Column(db.String(20),nullable=False)
    phone = db.Column(db.String(20),nullable=False)
    addres = db.Column(db.String(80),nullable=False)
    orders = db.relationship("Order", backref="user")

    def __repr__(self):
       # return '<user %r>' % self.username
       self.username = username.strip()
    
    def serialize(self):
        return{
            "username": self.username,
            "email": self.email,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "telefono": self.telefono,
            "direccion": self.direccion
        }
        
class Order(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user_username  = db.Column(db.String(80),db.ForeignKey("user.username"),nullable=False)
    date_order = db.Column(db.Date,nullable=False)
    ordered_products = db.relationship("OrderedProduct", backref="order")
    
class Product(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name_product = db.Column(db.String(80),nullable=False)
    url_image = db.Column(db.String(120),nullable=False)
    description = db.Column(db.String(120),nullable=False)
    weight = db.Column(db.Float,nullable=False)
    size = db.Column(db.Float,nullable=False)
    factor = db.Column(db.Float,nullable=False)  
    preparation = db.Column(db.String(280),nullable=False)
    ordered_products = db.relationship("OrderedProduct", back_populates="product") 
    ingredients = db.relationship("Ingredient", back_populates="product")

class OrderedProduct(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    order_id = db.Column(db.Integer,db.ForeignKey("order.id"),nullable=False)
    product_id = db.Column(db.Integer,db.ForeignKey("product.id"),nullable=False)
    quantity = db.Column(db.Integer,nullable=False)
    price = db.Column(db.Float,nullable=False)
    product = db.relationship("Product",back_populates="ordered_products")

class RawMaterial(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    unit_measure = db.Column(db.String(10),nullable=False)
    stock = db.Column(db.Float,nullable=False)
    last_cost = db.Column(db.Float,nullable=False)
    ingredients = db.relationship("Ingredient", backref="raw_material")
    raw_material_buys = db.relationship("RawMaterialBuy", backref="raw_material")

class Ingredient(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    product_id = db.Column(db.Integer,db.ForeignKey("product.id"),nullable=False)
    raw_material_id = db.Column(db.Integer,db.ForeignKey("raw_material.id"),nullable=False)
    quantity_raw_material = db.Column(db.Float,nullable=True)
    product = db.relationship("Product", back_populates="ingredients")

class Buy(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    provider_name = db.Column(db.String(60),nullable=False)
    date = db.Column(db.Date,nullable=False)
    raw_material_buys = db.relationship("RawMaterialBuy",back_populates="buy")

class RawMaterialBuy(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    buy_id = db.Column(db.Integer,db.ForeignKey("buy.id"),nullable=False)
    raw_material_id = db.Column(db.Integer,db.ForeignKey("raw_material.id"),nullable=False)
    quantity = db.Column(db.Float,nullable=False)
    cost = db.Column(db.Float,nullable=False)
    buy = db.relationship("Buy",back_populates="raw_material_buys")
