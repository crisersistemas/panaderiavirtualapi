"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for, make_response
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from models import db, User, Order, Product, OrderedProduct, RawMaterial, Ingredient, Buy, RawMaterialBuy
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "hello": "world"
    }

    return jsonify(response_body), 200
# Product endpoint!
@app.route("/products",methods=["GET"])

def handle_product():
    headers = {
        "Content-Type": "aplication/json"
     }
    #mostramos todos loes productos para que puedan ser elegidos 
    if request.method == "GET":
        print("Aqui Vemos los Pedidos")
        #Si el usuario tiene pedidos lo vemos aqui
        products = Product.query.all()
        response_body = []
        for product in products:
            response_body.append(product.serialize())
        status_code = 200
    else:
        response_body = "metodo no leido todavia por el testing "
        status_code = 501

    return make_response(
        jsonify(response_body),
        status_code,
        headers
    )
# Order Enpoint
@app.route("/orders/<username>",methods=["POST","PUT","DELETE"])

def handle_order():
    headers = {
        "Content-Type": "aplication/json"
    }
    # Creamos el pedido en la base de datos 
    if request.method == "POST":
        requesting_order = Order.query.filter_by(user_username=Username).all()
        print("Crear Usuario con el primer pedido")
        if len(requesting_order) > 0:
            #Usuario ya tiene un pedido
            response_body = {
                "status" : "HTTP_400_BAD_REQUEST. Pedido No puede ser creado de Nuevo"
            }
            status_code = 400
        else:
            # Usuario no existe se crea con un primer pedido
            print("Se crea el usuario Con el Username y un primer pedido")
            new_order_products = json.loads(request.data)
            first_order = Order(new_order_products["date"],user_username)
            db.session.add(first_order)
            db.session.commit()
            print("Se crean las ordenes de los productos")
            for order_product in new_order_products:
                new_order_product = OrderedProduct(order_product["order_id"],order_product["product_id"],order_pro["quantity"],order_product["price"])
                db.sessio.add(new_order_product)
            db.session.commit()
            response_body = {
                "status": "HTTP_200_OK. Ok "
            }
            status_code = 200           

    # this only runs if `$ python src/main.py` is executed

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
