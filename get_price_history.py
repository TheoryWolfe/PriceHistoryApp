#!/usr/bin/env python3

from ph_gui import *
from universal import *
import requests
from config.secret import API_KEY

# TODO: CREATE THE GET CALL FUNCTION TO TD Ameritrade
def fetch_price_history(**kwargs):

    """
    send a GET request to TD Ameritrade for a
    given stock's price history data.

    :params: **kwargs (period, periodType, frequency,
    frequencyType, symbol)
    """


    url = """https://api.tdameritrade.com/v1/marketdata/
        {}/pricehistory""".format(kwargs.get('symbol'))

    params = {}
    params.update({'apikey': API_KEY})

    # CREATE FOR LOOP TO INSERT KEY:VALUE PAIRS THAT
    # ARE PASSED AS PARAMS TO THE GET CALL INTO
    # THE PARAMS DICTIONARY SO THEY CAN BE INSERTED
    # INTO THE url VARIABLE ABOVE.

    for arg in kwargs:
        parameter = {arg: kwargs.get(arg)}
        params.update(parameter)

    # NOW RETURN THE DESIRED params
    return requests.get(url, params=params).json()


# ADD THE ENTIRE GET PRICE HISTORY PROCESS TO THIS SCRIPT
# SO THAT I CAN SAVE SPACE IN THE MAIN SCRIPT AND JUST IMPORT
# THE RESULTS.

symbol, name = symbolGUI()
periodType = periodTypeGUI()
period = periodGUI(periodType)
frequencyType = frequencyTypeGUI(periodType)
frequency = frequencyGUI(frequencyType)

"""
USING ASSIGNED VARIABLES TO MAKE A GET CALL TO THE
TD AMERITRADE FOR PRICE HISTORY
"""
rdata = fetch_price_history(symbol=symbol,
                           period=period,
                           periodType=periodType,
                           frequencyType=frequencyType,
                           frequency=frequency)
