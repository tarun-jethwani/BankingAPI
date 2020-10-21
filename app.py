from flask import Flask, request, jsonify
from accounts_manager import *

app = Flask(__name__)

ac = AccountManager()


@app.route('/api/transfer/', methods=['GET', 'POST'])
def add_message():
    from_id = request.json['fromAccountId']
    to_id = request.json['toAccountId']
    amount = paisa_to_ruppes(request.json['amount'])

    if not check_transfer_validty(to_id, from_id):
        return jsonify(ERRORS_CODES[ERROR_FOR_SAME_ACCOUNT_ID])

    if request.json['account_type']:
        output = ac.transfer_amount(from_id, to_id, amount, request.json['account_type'])
    else:
        output = ac.transfer_amount(from_id, to_id, amount)

    return jsonify(output)


@app.route('/', methods=['GET', 'POST'])
def home():
    return jsonify({"app": "running on localhost"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
