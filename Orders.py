import json
import requests
from ConfigParser import SafeConfigParser

#initialize parser to get secret data, end points, etc.
#put you API Key and Endpoints in file called config.ini
parser = SafeConfigParser()
parser.read('config.ini')

def Buy_Stock_Limit(target, quantity, limit_price, duration):
    #set query args
    endpoint = parser.get('endpoint', 'brokerage') + 'accounts/' + parser.get('account', 'AccountNumber') + '/orders'
    headers = {'Authorization': parser.get('account', 'Auth'), 'Accept': parser.get('message_format', 'accept_format')}
    payload = {'class' : 'equity',
                'symbol' : target,
                'duration' : duration,
                'side' : 'buy',
                'quantity' : quantity,
                'type' : 'limit',
                'price' : limit_price,
                'preview' : parser.get('message_format', 'preview')}
    
    #send query
    r = requests.post(endpoint, headers = headers , params = payload)
    
    #get parse response
    content = json.loads(r.text)
    return content

def Sell_Stock_Limit(target, quantity, limit_price, duration):
    #set query args
    endpoint = parser.get('endpoint', 'brokerage') + 'accounts/' + parser.get('account', 'AccountNumber') + '/orders'
    headers = {'Authorization': parser.get('account', 'Auth'), 'Accept': parser.get('message_format', 'accept_format')}
    payload = {'class' : 'equity',
                'symbol' : target,
                'duration' : duration,
                'side' : 'sell',
                'quantity' : quantity,
                'type' : 'limit',
                'price' : limit_price,
                'preview' : parser.get('message_format', 'preview')}
    
    #send query
    r = requests.post(endpoint, headers = headers , params = payload)
    
    #get parse response
    content = json.loads(r.text)
    return content

    
def Cancel_Order(Order_Number):
    endpoint = parser.get('endpoint', 'brokerage') + 'accounts/' + parser.get('account', 'AccountNumber') + '/orders' + Order_Number
    headers = {'Authorization': parser.get('account', 'Auth'), 'Accept': parser.get('message_format', 'accept_format')}
    
    #send query
    r = requests.delete(endpoint, headers = headers)
    #get parse response
    content = json.loads(r.text)
    
    if (content['order']['id'] == Order_Number and 
        content['order']['status'] == 'ok'):
        print 'Order ' + Order_Number + ' Canceled'
    else:
        print 'Order Failed to Cancel.  Status: ' + content['order']['status']


def Check_Order_Status(order_id):
    #set query args
    endpoint = parser.get('endpoint', 'brokerage') + 'accounts/' + parser.get('account', 'AccountNumber') + '/orders/' + order_id
    headers = {'Authorization': parser.get('account', 'Auth'), 'Accept': parser.get('message_format', 'accept_format')}
    payload = {'account_id' :  parser.get('account', 'AccountNumber'), 'id' : order_id}
    
    #send query
    r = requests.get(endpoint, headers = headers , params = payload)
    
    #get parse response
    content = json.loads(r.text)
    return content

                
