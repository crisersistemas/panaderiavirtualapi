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
# @app.route("/shoppingcar/<username>",methods=["GET","POST","PUT","DELETE"])

# def handle_shoppingcar(username):
#     headers = {
#         "Content-Type": "aplication/json"
#     }
#     #chequeamos si el usuario existe
#     requeting_user = User.query.filter_by(username=username).all()
#     # Se busca el pedido del Usuario o se crea un primer pedido
#     if request.method == "GET":
#         print("Aqui Vemos los Pedidos")
#         #Si el usuario tiene pedidos lo vemos aqui
#         if len(requesting_user) > 0:
#             #El usuario existe y regresa los pedidos 
#             print("Usuario Existe")
#             user_order = Order.query.filter_by(user_username=username).all()
#             response_body = []
#             for order in user_order:
#                 response_body.append(order.serialize())
#             status_code = 200
#         else:
#              #usuario no existe, devuelve 404 no existe 
#              print("Usuario no existe")
#              response_body{
#                  "status" : "HTTP_404_NOT_FOUND. usuario no existe "
#              }
#              status_code = 404
#     # El usuario sera creado se chequea si existe primero
#     elif request.method == "POST":
#         print("Crear Usuario Con primer pedido")
#         if len(requeting_user) > 0:
#             #usuario existe 
#             response_body = {
#                 "status": "HTTP_400_BAD_REQUEST.usuario ya fue creado" 
#             }
#             status_code = 400
#         else
#             #username no pertenece a ningun usuario. crea usuario con un primer pedido
#             print("creando usuario con username y primer pedido")
#             new_user = User(username)
#             db.session.add(new_user)
#             first_order=order(id_product,quantity,username)
#             db.session(first_order)
#             db.session.commit()
#             response_body = {
#                 "sttua":  "HTTP_200_OK:OK"
#             }
#             status_code = 200
#     elif request.method = "PUT"
#         #Actualizar los pedidos. se chequea que el usuario exista
#         print("actualizando pedidos de {username]")
#         if len(requeting_user) > 0:
#             #usuario exite actualizar pedidos
#             order.query.filter_by(user_username=UserWarning).delete()
#             new_ordered_product = json.loads(request.data)
#             #Chequea que la lista a actualizar no este vacia 
#             if len(new_ordered_product) > 0:
#                 #lista de pedidod actualizada no vacia 
#                 for product in new_product
#                     #Productos pedidos por el usuario
#                     new_ordered_product(ordered_product[id_puduct],username)
#                 db.session.add(new_ordered_product) 
#                 result = f"El pedido con {len(new_ordered_product)} productod a sido guardada"
#             else:
                #No hay pedidos




    # this only runs if `$ python src/main.py` is executed

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
