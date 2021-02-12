#!/usr/bin/env python3

import PySimpleGUI as sg

#!usr/bin/env python3
"""
THIS SCRIPT IS THE GRAPHIC USER INTERFACE FOR GETTING THE
PRICE HISTORY DATA OF A PARTICULAR STOCK. IT CONTAINS ALMOST
ALL OF THE PARAMETERS THAT TD AMERITRADE OFFERS. AS OF
NOW EACH FUNCTION IS A SEPERATE POPUP WINDOW.

EVENTUALLY I WANT IT TO ALL BE ON ONE GUI WINDOW SO THAT
ALL THE PARAMETERS CAN BE PICKED AT THE SAME TIME.
"""

import PySimpleGUI as sg
from universal import theme


# POP UP THAT GETS THE PERIOD TYPE FOR TDA API CALL
def periodTypeGUI():
    """
    Determine what period type the user wants to use for getting
    historical data. It is based off Day, Month, Year, or YTD
    """
    periodTypes = ['day', 'month', 'year', 'ytd']

    sg.theme(theme) # change the theme in the universal file

    layout = [
        [sg.Text('What overall time period do you want to search by?')],
        [sg.Button(button_text='Daily', enable_events=True),
         sg.Button(button_text='Monthly', enable_events=True),
         sg.Button(button_text='Yearly', enable_events=True),
         sg.Button(button_text='YTD', enable_events=True)]
    ]

    window = sg.Window('periodType Paramaters:', layout)
    event, values = window.read()
    window.close()

    if event == 'Daily':
        return periodTypes[0]
    if event == 'Monthly':
        return periodTypes[1]
    if event == 'Yearly':
        return periodTypes[2]
    elif event == 'YTD':
        return periodTypes[3]


# POP UP THAT GETS THE PERIOD FOR TDA'S API
def periodGUI(periodType):
    """
    Determine what period type the user wants to use for getting
    historical data. It is based off Day, Month, Year, or YTD
    :param: takes in the periodType that is chosen in the window
    before this.
    :returns: a list of buttons with the possible options depending
    upon the periodType that it goes with.
    """

    # These will be used to return the necessary value based off which
    # button is pressed.

    period_values = ['1', '2', '3', '4', '5', '6', '10', '15', '20']

    sg.theme(theme)

    # If statements to determine which layout is displayed. This
    # will be based off the periodType that is passed into the
    # functions parameters (which will be selected during the
    # previous call)

    if periodType == 'day':
        layout = [
            [sg.Text('How many days do you want returned? ')],
            [sg.Button('1-Day', enable_events=True),
             sg.Button('2-Day', enable_events=True),
             sg.Button('3-Day', enable_events=True),
             sg.Button('4-Day', enable_events=True),
             sg.Button('5-Day', enable_events=True),
             sg.Button('10-Day', enable_events=True), ]
        ]

        window = sg.Window('period Paramaters:', layout)
        event, values = window.read()
        window.close()

        if event == '1-Day': return period_values[0]
        if event == '2-Day': return period_values[1]
        if event == '3-Day': return period_values[2]
        if event == '5-Day': return period_values[4]
        if event == '10-Day': return period_values[6]

    if periodType == 'month':
        layout = [
            [sg.Text('How many days do you want returned? ')],
            [sg.Button('1-Month', enable_events=True),
             sg.Button('2-Month', enable_events=True),
             sg.Button('3-Month', enable_events=True),
             sg.Button('6-Month', enable_events=True), ]
        ]
        window = sg.Window('period Paramaters:', layout)
        event, values = window.read()
        window.close()

        if event == '1-Month': return period_values[0]
        if event == '2-Month': return period_values[1]
        if event == '3-Month': return period_values[2]
        if event == '6-Month': return period_values[5]

    if periodType == 'year':
        layout = [
            [sg.Text('How many days do you want returned? ')],
            [sg.Button('1-Year', enable_events=True),
             sg.Button('2-Year', enable_events=True),
             sg.Button('3-Year', enable_events=True),
             sg.Button('5-Year', enable_events=True),
             sg.Button('10-Year', enable_events=True),
             sg.Button('15-Year', enable_events=True),
             sg.Button('20-Year', enable_events=True), ]
        ]

        window = sg.Window('period Paramaters:', layout)
        event, values = window.read()
        window.close()

        if event == '1-Year': return period_values[0]
        if event == '2-Year': return period_values[1]
        if event == '3-Year': return period_values[2]
        if event == '5-Year': return period_values[4]
        if event == '10-Year': return period_values[6]
        if event == '15-Year': return period_values[7]
        if event == '20-Year': return period_values[8]

    if periodType == 'ytd': return period_values[0]


# POPUP THAT GETS THE FREQUENCY TYPE BASED OFF CHOSEN PERIOD TYPE
def frequencyTypeGUI(periodType):
    """
    Determine what frequencyType the user wants to use for getting
    historical data. This is a parameter that determines what each
    candle stick represents(minutes, days, weeks, months)

    :param: takes in the periodType that is chosen in that window.

    :returns: options in the form of buttons with the possible
    options depending upon the periodType that it goes with.
    """

    # These will be used to return the necessary value based off which
    # button is pressed.

    candleStick = ['minute', 'daily', 'weekly', 'monthly']

    sg.theme(theme)

    # If statements to determine which layout is displayed. This
    # will be based off the periodType that is passed into the
    # functions parameters (which will be selected during the
    # previous call)

    if periodType == 'day': return candleStick[0]

    if periodType == 'month':
        layout = [
            [sg.Text('Choose between daily or weekly candle sticks: ')],
            [sg.Button('Daily', enable_events=True),
             sg.Button('Weekly', enable_events=True)],
        ]

        window = sg.Window('Candle Stick frequencyType: ', layout)
        event, values = window.read()
        window.close()

        if event == 'Daily': return candleStick[1]
        if event == 'Weekly': return candleStick[2]

    if periodType == 'year':
        layout = [
            [sg.Text('Choose between Daily, Weekly, or Monthly candle sticks:  ')],
            [sg.Button('Daily', enable_events=True),
             sg.Button('Weekly', enable_events=True),
             sg.Button('Monthly', enable_events=True), ]
        ]

        window = sg.Window('Candle Stick frequencyType: ', layout)
        event, values = window.read()
        window.close()

        if event == 'Daily': return candleStick[1]
        if event == 'Weekly': return candleStick[2]
        if event == 'Monthly': return candleStick[3]

    if periodType == 'ytd':
        layout = [
            [sg.Text('Choose between Daily or Weekly candle sticks: ')],
            [sg.Button('Daily', enable_events=True),
             sg.Button('Weekly', enable_events=True), ]
        ]

        window = sg.Window('Candle Stick frequencyType: ', layout)
        event, values = window.read()
        window.close()

        if event == 'Daily': return candleStick[1]
        if event == 'Weekly': return candleStick[2]


# POPUP WINDOW GETS THE FREQUENCY BASED OFF FREQUENCY TYPE CHOSEN
def frequencyGUI(frequencyType):
    """
    Determine what period type the user wants to use for getting
    historical data. It is based off Day, Month, Year, or YTD
    :param: takes in the periodType that is chosen in the window
    before this.
    :returns: a list of buttons with the possible options depending
    upon the periodType that it goes with.
    """

    # These will be used to return the necessary value based off which
    # button is pressed.

    frequency_values = ['1', '5', '10', '15', '30']

    sg.theme(theme)

    # If statements to determine which layout is displayed. This
    # will be based off the periodType that is passed into the
    # functions parameters (which will be selected during the
    # previous call)

    if frequencyType == 'minute':
        layout = [
            [sg.Text('How many minutes do you want each candle to be? ')],
            [sg.Button('1-Minute', enable_events=True),
             sg.Button('5-Minutes', enable_events=True),
             sg.Button('10-Minutes', enable_events=True),
             sg.Button('15-Minutes', enable_events=True),
             sg.Button('30-Minutes', enable_events=True)],
        ]

        window = sg.Window('Candle Stick Frequency:', layout)
        event, values = window.read()
        window.close()

        if event == '1-Minute': return frequency_values[0]
        if event == '5-Minutes': return frequency_values[1]
        if event == '10-Minutes': return frequency_values[2]
        if event == '15-Minutes': return frequency_values[3]
        if event == '30-Minutes': return frequency_values[4]

    if frequencyType == 'daily': return frequency_values[0]

    if frequencyType == 'weekly': return frequency_values[0]

    if frequencyType == 'monthly': return frequency_values[0]
