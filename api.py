from flask import Blueprint,request,jsonify,Flask
from flask_jwt_extended import JWTManager, create_access_token
import test.testview


class User(object):
    def __init__(self,username, password):
        self.username = username
        self.password = password
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)
users = {}
@app.route('/signup', methods=['POST'])
def signup():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400
    if username in users:
        return jsonify({"msg": "This username have used!"}),201
    users[username]=User(username,password)
    return jsonify({"msg": "Signup success!"}), 200

@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if (not username) or (not password):
        return jsonify({"msg": "Missing username or password parameter"}), 400
    loginuser = users.get(username, None)
    if not loginuser:
        return jsonify({"msg":"User not exists"}), 401
    elif loginuser.password==password:
        return jsonify(access_token=create_access_token(identity=username)), 200
    else:
        return jsonify({"msg": "Username or password is not correct!"}), 401

app.register_blueprint(test.testview.bp_test)
@app.rotu('/take'.methods = ['POST'])
def take():
    return "hello word"

if __name__ == "__main__":
    app.run()