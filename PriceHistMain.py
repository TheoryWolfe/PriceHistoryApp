#!/usr/bin/env python3

# MAIN SCRIPT: (PRACTICE ATTEMPT)
"""
I need to try and layout a mini program that
allows the user to get any stocks price history
data. I need a GUI, the api call to TD Ameritrade,
the data returned, sort the data (using pandas df),
create a database, create a table in that db for
the given company and time parameter, insert the
data into a table in that database

---> most of the work is done already as part of a
bigger program i was trying to create. I couldn't figure
it out so I am going with a smaller program and sticking
with one api call instead of all of them.

---> Improve the GUI and make sure everything can
be run over and over until the user quits.
"""
from ph_gui import *
from universal import *
from get_price_history import rdata

# TODO: CREATE A GRAPHICAL USER INTERFACE

# I MOVED THESE VARIABLE ASSIGNMENTS TO THE get_price_history MODULE
# TO SEE IF IT MAKES IT EASIER. IF I LIKE IT BETTER THIS WAY I
# WILL DELETE THE BELOW INFORMATION
"""
symbol, name =  symbolGUI()
periodType = periodTypeGUI()
period = periodGUI(periodType)
frequencyType = frequencyTypeGUI(periodType)
frequency = frequencyGUI(frequencyType)
"""

# TODO: CREATE THE GET CALL FUNCTION TO TD Ameritrade
# COPY LINE BELOW AND PASTE TO TOP WHEN SCRIPT IS READY.
# from get_price_history import get_price_history


# TODO: ASSIGN THE GET CALL FUNC TO A VAR TO PASS TO OTHER FUNC
#pricehistory = fetch_price_history(symbol,
    #period, periodType, frequency, frequencyType)
pricehistory = rdata
"""
THIS IS A GOOD TESTING POINT TO MAKE SURE EVERYTHING IS WORKING
UP UNTIL THIS POINT. ONCE IT IS WORKING I WILL COMMENT OUT
THE BELOW TEST:
"""
print(pricehistory)

# TODO: CREATE A CLASS TO SORT RETURNED JSON DATA FOR STORING

# TODO: CREATE A DB CLASS IN ORDER TO DYNAMICALLY CREATE A DB

# TODO: ADD METHOD TO CREATE A TABLE IN THAT DATABASE

# TODO: ADD NOTHER METHOD TO INSERT THE DATA TO THE CORRECT TABLE

# TODO: CREATE THE WHILE LOOP LOGIC THAT WILL KEEP THIS RUNNING
