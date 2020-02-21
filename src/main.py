"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
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
# ShoppingCar endpoint!
@app.route("/shoppingcar/<username>",methods=["GET","POST","PUT","DELETE"])

def handle_shoppingcar(username):
    headers = {
        "Content-Type": "aplication/json"
     }
    #chequeamos si el usuario existe
    requeting_user = User.query.filter_by(username=username).all()
    # Se busca el pedido del Usuario o se crea un primer pedido
    if request.method == "GET":
        print("Aqui Vemos los Pedidos")
        #Si el usuario tiene pedidos lo vemos aqui
        if len(requesting_user) > 0:
            products = Product.query.all()
            response_body = []
            for product in products:
                response_body.append(product.serialize())
            status_code = 200
        else:
            #usuario no existe 
            print("usuaio no existe")
            response_body = {
                "status" : "HTTP_404_NOT_FOUND. usuario no existe"
            }
            status_code = 404
    else:
        response_body = "metodo no leido todavia por el testing "
        status_code = 501

    return make_response(
        jsonify(response_body),
        status_code,
        headers
    )
    
    # this only runs if `$ python src/main.py` is executed

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
