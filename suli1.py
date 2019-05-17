from flask import Flask,request,jsonify,Blueprint
from flask_jwt_extended import JWTManager, create_access_token
import suli_signup.suli_signupview
import suli_signup.suli_loginview
import suli_signup.suli_helloview

app = Flask(__name__)
app.config['JWT_SECRET_KEY']='super-secret'
jwt = JWTManager(app)
# user = {}
app.register_blueprint(suli_signup.suli_signupview.bp_suli_signup)
app.register_blueprint(suli_signup.suli_loginview.bp_suli_login)
app.register_blueprint(suli_signup.suli_helloview.bp_suli_hello)
if __name__=='__main__':
    app.run()




