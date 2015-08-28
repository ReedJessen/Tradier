
import json
import requests
from ConfigParser import SafeConfigParser


#initialize parser to get secret data, end points, etc.
parser = SafeConfigParser()
parser.read('config.ini')

def Get_Quote(ticker):
    """returns full order quote for given ticker, function used internally in functions like 'Get_Open' and 'Get_Ask'"""
    #set query args
    endpoint = parser.get('endpoint', 'brokerage') + 'markets/quotes'
    headers = {'Authorization': parser.get('account', 'Auth'), 'Accept': parser.get('message_format', 'accept_format')}
    payload = {'symbols' : ticker}
    
    #send query
    r = requests.get(endpoint, headers = headers , params = payload)
    #print r.text
    #get parse response
    content = json.loads(r.text)
    return content

def Get_Market_Status():
    """Checks if market is open or closed, 1 if open, 0 if not open"""
    endpoint = parser.get('endpoint', 'brokerage') + 'markets/clock'
    headers = {'Authorization': parser.get('account', 'Auth'), 'Accept': parser.get('message_format', 'accept_format')}
    
     #send query
    r = requests.get(endpoint, headers = headers)
    #print r.text
    #get parse response
    content = json.loads(r.text)
    
    if content['clock']['state'] == 'open':
        return 1
    else:
        return 0

def Get_Open(ticker):
    """returns opening price of target security"""
    content = Get_Quote(ticker)
    open_price = content['quotes']['quote']['open']
    return open_price

def Get_Ask(ticker):
    """returns current best ask price of  target security""" 
    content = Get_Quote(ticker)
    ask_price = content['quotes']['quote']['ask']
    ask_size = content['quotes']['quote']['asksize']
    return {'ask_price':ask_price, 'ask_size':ask_size}

def Get_Bid(ticker):
    """returns current best bid priceof  target security"""
    content = Get_Quote(ticker)
    bid_price = content['quotes']['quote']['bid']
    bid_size = content['quotes']['quote']['bidsize']
    return {'bid_price':bid_price, 'bid_size':bid_size}
