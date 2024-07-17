from flask import Flask, jsonify, request
from flask_cors import CORS

import core.request.request as req
import core.auth.auth as user

from controller.test import test

app = Flask(__name__)
app.register_blueprint(test)
CORS(app)

@app.route('/swagger')
def hello_world():
    return 'Hello, Docker!'


# Exemple token + connexion
# @app.delete('/<page>/<int:index>')
# def delete<Page>(index):

#     # Fonction vérif token
#     checkToken = user.check_token(request)
#     if (checkToken != True):
#         return checkToken

#     json = request.get_json()
    
#     if (attraction.delete_attraction(index)):
#         return "Element supprimé.", 200
#     return jsonify({"message": "Erreur lors de la suppression."}), 500

# @app.post('/login')
# def login():
#     json = request.get_json()

#     if (not 'name' in json or not 'password' in json):
#         result = jsonify({'messages': ["Nom ou/et mot de passe incorrect"]})
#         return result, 400
    
#     cur, conn = req.get_db_connection()
#     requete = f"SELECT * FROM users WHERE name = '{json['name']}' AND password = '{json['password']}';"
#     cur.execute(requete)
#     records = cur.fetchall()
#     conn.close()

#     result = jsonify({"token": user.encode_auth_token(list(records[0])[0]), "name": json['name']})
#     return result, 200