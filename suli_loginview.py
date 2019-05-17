from flask import Flask,request,jsonify,Blueprint
from flask_jwt_extended import JWTManager, create_access_token
import suli_signup.suli_signupview
bp_suli_login= Blueprint('bp_suli_login',__name__)
@bp_suli_login.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg":"Missing JSON in request"}), 400
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username:
        return jsonify({"msg":"Missing username parameter"}), 400
    if not password:
        return jsonify({"msg":"Missing password parameter"}), 400
    loginuser =suli_signup.suli_signupview.user.get(username,None)
    if not loginuser:
        return jsonify({"msg" : "user not exists"}), 400
    elif loginuser.password == password:
        return jsonify(access_token=create_access_token(identity=username)), 400
    else:
        return jsonify({"msg":"username or password is not correct"}), 401