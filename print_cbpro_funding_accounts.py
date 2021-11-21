# twitter.com/_d3f4ult
# This script will help you find your bank id needed for the DCA bot.
# Replace the values below with Coinbase Pro API credentials

import cbpro

cbpro_apikey = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
cbpro_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
cbpro_passphrase = 'XXXXXXXXXX'

def print_cbpro_funding_accounts(requests):

    cbpro_api = cbpro.AuthenticatedClient(cbpro_apikey,
                                          cbpro_secret,
                                          cbpro_passphrase)

    for funding_account in cbpro_api.get_payment_methods():
        print('the id number for {} is: {}'.format(funding_account['name'],
              funding_account['id']))
