import requests

fromAccountId = 1
toAccountId = 1
transfer_amount = 3000
account_type = 'BasicSavings' # optional

if account_type:
    res = requests.post('http://localhost:5000/api/transfer/',
                        json={"fromAccountId": str(fromAccountId), "toAccountId": str(toAccountId),
                              "amount": transfer_amount, "account_type": account_type})
else:
    res = requests.post('http://localhost:5000/api/transfer/',
                        json={"fromAccountId": str(fromAccountId), "toAccountId": str(toAccountId),
                              "amount": transfer_amount})

if res.ok:
    print(res.json())
