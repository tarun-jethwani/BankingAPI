from flask import Flask, request, jsonify
from accounts_manager import *

app = Flask(__name__)

ac = AccountManager()

# from_id = '2'
# to_id = '1'
# transfer_amount = paisa_to_ruppes(2000)


@app.route('/api/transfer/', methods=['GET', 'POST'])
def add_message():
    from_id = request.json['fromAccountId']
    to_id = request.json['toAccountId']
    amount = paisa_to_ruppes(request.json['amount'])

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
