from flask import Flask,request,jsonify,Blueprint
from flask_jwt_extended import JWTManager, create_access_token

class User(object):
    def __init__(self,username,password):
        self.username = username
        self.password = password

app = Flask(__name__)
app.config['JWT_SECRET_KEY']='super-secret'
jwt = JWTManager(app)
user = {}
bp_suli_signup=Blueprint('bp_suli_signup',__name__)

@bp_suli_signup.route('/signup',methods=['POST'])
def signup():
    if not request.is_json:
        return jsonify({"msg":"Missing JSON in request"}), 400
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username:
        return jsonify({"msg":"Missing username parameter"}), 400
    if not password:
        return jsonify({"msg":"Missing password parameter"}), 400
    if username in user:
        return jsonify({"msg":"This username had used"}), 401
    user[username]=User(username,password)
    return jsonify({"msg":"signup seccess!"}), 200
