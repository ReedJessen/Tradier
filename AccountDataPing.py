import json
import requests
from ConfigParser import SafeConfigParser


#initialize parser to get secret data, end points, etc.
parser = SafeConfigParser()
parser.read('config.ini')


def Get_Balances(Data_Point):
    """get json datapoints at the 'balances' level of the message"""
    #set query args
    endpoint = parser.get('endpoint', 'brokerage') + 'user/balances'
    headers = {'Authorization': parser.get('account', 'Auth'), 'Accept': parser.get('message_format', 'accept_format')}
    
    #send query
    r = requests.get(endpoint, headers = headers)
    #print r.text
    #get parse response
    content = json.loads(r.text)
    return content['accounts']['account']['balances'][Data_Point]


def Get_Margin(Data_Point):
    """get json data points from the 'balances''margin' level"""
    #set query args
    endpoint = parser.get('endpoint', 'brokerage') + 'user/balances'
    headers = {'Authorization': parser.get('account', 'Auth'), 'Accept': parser.get('message_format', 'accept_format')}
    
    #send query
    r = requests.get(endpoint, headers = headers)
    #print r.text
    #get parse response
    content = json.loads(r.text)
    return content['accounts']['account']['balances']['margin'][Data_Point]

def Total_Cash():
    """The total amount of cash in the account."""
    Data_Point = 'total_cash'
    return Get_Balances(Data_Point)

def Total_Equity():
    """The total account value."""
    Data_Point = 'total_equity'
    return Get_Balances(Data_Point)

def Stock_Long_Value():
    """The value of long stocks held in the account."""
    Data_Point = 'stock_long_value'
    return Get_Balances(Data_Point)

def Stock_Short_Value():
    """The value of short stocks held in the account"""
    Data_Point = 'stock_short_value'
    return Get_Margin(Data_Point)

def Stock_Buying_Power():
    """The amount of funds available to purchase fully marginable securities."""
    Data_Point = 'stock_buying_power'
    return Get_Margin(Data_Point)
    
def Option_Buying_Power():
    """The amount of funds available to purchase non-marginable securities."""
    Data_Point = 'option_buying_power'
    return Get_Margin(Data_Point)

def Uncleared_Funds():
    """The amount of funds that are not currently available for trading."""
    Data_Point = 'uncleared_funds'
    return Get_Balances(Data_Point)

def Pending_Orders_Count():
    """The amount of open orders."""
    Data_Point = 'pending_orders_count'
    return Get_Balances(Data_Point)

def Positions():
    """get current position"""
    #set query args
    endpoint = parser.get('endpoint', 'brokerage') + 'accounts/' + parser.get('account', 'AccountNumber') + '/positions'
    headers = {'Authorization': parser.get('account', 'Auth'), 'Accept': parser.get('message_format', 'accept_format')}
    
    #send query
    r = requests.get(endpoint, headers = headers)
    content = json.loads(r.text)
    return content
