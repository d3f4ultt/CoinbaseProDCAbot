# twitter.com/_d3f4ult
# I host this code on Google Cloud and Google Job Scheduler with cronjob to initiate this code every morning

import cbpro
import time

#Paste your cbpro API keys into the below variables
cbpro_apikey = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
cbpro_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
cbpro_passphrase = 'XXXXXXXXXX'

# Paste your bank account id into the funding_id variable.
# Use print_cbpro_funding_accounts.py to find your banking ID.
# Minimum coinbase deposit is $10.
initiate_deposit_when_run = True
funding_id = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
deposit_amount = 10.00

# Set True/False for each variable and set the amount of each to buy.
buys = {}
buys['BTC-USD'] = {'buy': False, 'amount': 0.00}
buys['ETH-USD'] = {'buy': False, 'amount': 0.00}
buys['LTC-USD'] = {'buy': False, 'amount': 0.00}
buys['SOL-USD'] = {'buy': True, 'amount': 10.00}
buys['AVAX-USD'] = {'buy': False, 'amount': 0.00}
buys['MATIC-USD'] = {'buy': False, 'amount': 0.00}
buys['DOT-USD'] = {'buy': False, 'amount': 0.00}
buys['XRP-USD'] = {'buy': False, 'amount': 0.00}
buys['ADA-USD'] = {'buy': False, 'amount': 0.00}
buys['XLM-USD'] = {'buy': False, 'amount': 0.00}
buys['LINK-USD'] = {'buy': False, 'amount': 0.00}
buys['CRO-USD'] = {'buy': False, 'amount': 0.00}
buys['MANA-USD'] = {'buy': False, 'amount': 0.00}
buys['LRC-USD'] = {'buy': False, 'amount': 0.00}
buys['ALGO-USD'] = {'buy': False, 'amount': 0.00}
buys['AAVE-USD'] = {'buy': False, 'amount': 0.00}
buys['ANKR-USD'] = {'buy': False, 'amount': 0.00}
buys['DOGE-USD'] = {'buy': False, 'amount': 0.00}
buys['USDT-USD'] = {'buy': False, 'amount': 0.00}

# Set True/False for each variable and enter the wallet address
withdraws = {}
withdraws['BTC-USD'] = {'withdraw': False,
                        'address': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'}
withdraws['ETH-USD'] = {'withdraw': False,
                        'address': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'}
withdraws['LTC-USD'] = {'withdraw': False,
                        'address': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'}
withdraws['SOL-USD'] = {'withdraw': False,
                        'address': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'}
withdraws['AVAX-USD'] = {'withdraw': False,
                        'address': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'}
withdraws['MATIC-USD'] = {'withdraw': False,
                        'address': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'}
withdraws['DOT-USD'] = {'withdraw': False,
                        'address': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'}
withdraws['XRP-USD'] = {'withdraw': False,
                        'address': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'}
withdraws['ADA-USD'] = {'withdraw': False,
                        'address': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'}
withdraws['LINK-USD'] = {'withdraw': False,
                        'address': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'}
withdraws['CRO-USD'] = {'withdraw': False,
                        'address': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'}
withdraws['MANA-USD'] = {'withdraw': False,
                        'address': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'}
withdraws['LRC-USD'] = {'withdraw': False,
                        'address': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'}
withdraws['ALGO-USD'] = {'withdraw': False,
                        'address': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'}
withdraws['AAVE-USD'] = {'withdraw': False,
                        'address': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'}
withdraws['ANKR-USD'] = {'withdraw': False,
                        'address': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'}
withdraws['DOGE-USD'] = {'withdraw': False,
                        'address': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'}
withdraws['USDT-USD'] = {'withdraw': False,
                        'address': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'}

# Don't change anything under here
cbpro_api = cbpro.AuthenticatedClient(cbpro_apikey,
                                      cbpro_secret,
                                      cbpro_passphrase)


def automated_purchase(event, context):

    # Make an ACH deposit from your bank
    if initiate_deposit_when_run:
        dep_request = cbpro_api.deposit(amount=deposit_amount,
                                        currency='USD',
                                        payment_method_id=funding_id)
        print('dep_request: {}'.format(dep_request))
    # make crypto purchases
    for key in buys.keys():
        if buys[key]['buy'] is True:
            order = cbpro_api.place_market_order(product_id=key,
                                                 side='buy',
                                                 funds=buys[key]['amount'])
            time.sleep(2)
            qty = float(cbpro_api.get_order(order['id'])['filled_size'])
            withdraws[key]['qty'] = qty

    # withdraw to external wallets
    withdraws['BTC-USD']['base'] = 'BTC'
    withdraws['ETH-USD']['base'] = 'ETH'
    withdraws['LTC-USD']['base'] = 'LTC'
    withdraws['SOL-USD']['base'] = 'SOL'
    withdraws['AVAX-USD']['base'] = 'AVAX'
    withdraws['MATIC-USD']['base'] = 'MATIC'
    withdraws['DOT-USD']['base'] = 'DOT'
    withdraws['XRP-USD']['base'] = 'XRP'
    withdraws['ADA-USD']['base'] = 'ADA'
    withdraws['LINK-USD']['base'] = 'LINK'
    withdraws['CRO-USD']['base'] = 'CRO'
    withdraws['MANA-USD']['base'] = 'MANA'
    withdraws['LRC-USD']['base'] = 'LRC'
    withdraws['ALGO-USD']['base'] = 'ALGO'
    withdraws['AAVE-USD']['base'] = 'AAVE'
    withdraws['ANKR-USD']['base'] = 'ANKR'
    withdraws['DOGE-USD']['base'] = 'DOGE'
    withdraws['USDT-USD']['base'] = 'USDT'

    for key in withdraws.keys():
        if withdraws[key]['withdraw'] is True:
            withdraw = cbpro_api.crypto_withdraw(amount=withdraws[key]['qty'],
                       currency=withdraws[key]['base'],
                       crypto_address=withdraws[key]['address'])
