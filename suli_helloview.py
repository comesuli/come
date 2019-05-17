from flask import Blueprint

bp_suli_hello= Blueprint('bp_suli_hello',__name__)
@bp_suli_hello.route('/take', methods=['POST'])
def take():
    return "hello world"

