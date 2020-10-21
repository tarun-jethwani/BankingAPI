import json
import datetime
from constants import *


def paisa_to_ruppes(amount):
    return amount / 100


def check_transfer_validty(to_id, from_id):
    if to_id == from_id:
        return False


class AccountManager:

    def check_suff_balance(self, from_id, records, transfer_amount, account_type):
        if float(records['accounts'][0][from_id][account_type]) - transfer_amount < 0:
            return False
        else:
            return True

    def __load_accounts(self):
        with open('accounts.json') as accounts_db:
            records = json.load(accounts_db)
            accounts_db.close()
            return records

    def __update_accounts(self, records):
        with open('accounts.json', 'w') as accounts_db:
            json.dump(records, accounts_db, indent=4)
            accounts_db.close()

    def __handle_transaction(self, from_id, to_id, records, transfer_amount, account_type):
        records['accounts'][0][to_id][account_type] = str(
            float(records['accounts'][0][to_id][account_type]) + transfer_amount)
        records['accounts'][0][from_id][account_type] = str(
            float(records['accounts'][0][from_id][account_type]) - transfer_amount)

    def get_success_message(self, from_id, to_id, records, account_type):
        message = {'newSrcBalance': records['accounts'][0][from_id][account_type],
                   'totalDestBalance': str(float(records['accounts'][0][to_id]['Savings']) \
                                           + float(records['accounts'][0][to_id]['Current']) \
                                           + float(records['accounts'][0][to_id]['BasicSavings'])), \
                   'timestamp': str(datetime.datetime.now())}
        return message

    def check_limit_for_BasicSavings(self, to_id, transfer_amount, records):
        if float(records['accounts'][0][to_id]['BasicSavings']) + transfer_amount > 50000:
            return True
        else:
            return False

    def transfer_amount(self, from_id, to_id, transfer_amount, account_type='Savings'):
        records = self.__load_accounts()

        if account_type == 'BasicSavings':
            if self.check_limit_for_BasicSavings(to_id, transfer_amount, records):
                return ERRORS_CODES[ERROR_FOR_BASIC_SAVINGS]

        if not self.check_suff_balance(from_id, records, transfer_amount, account_type):
            return ERRORS_CODES[ERROR_FOR_INSUFFICIENT_BALANCE]

        else:
            self.__handle_transaction(from_id, to_id, records, transfer_amount, account_type)
            self.__update_accounts(records)
            return self.get_success_message(from_id, to_id, records, account_type)

