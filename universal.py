#!usr/bin/env python3
import PySimpleGUI as sg

"""
I ONLY MADE THIS A "UNIVERSAL" GUI FILE BECAUSE I AM HOPING TO MAKE ALL OF THE GUI
FUNCTIONS EVENTUALLY BE IN THIS FILE. I WANT THIS TO EVENTUALLY BE A CLASS OF
GUI METHODS THAT I CAN CALL ANYWHERE I WANT IN THE PROGRAM AND EASILY REUSE THEM.
I JUST HAVEN'T LEARNED THAT MUCH YET.

I KNOW I CAN BUT ITS GOING TO TAKE ME LONGER SINCE I HAVE TO CONSTANTLY READ
DOCUMENTATION WHILE I DO IT SO FOR THE SAKE OF JUST GETTING A SOMEWHAT WORKING
PROGRAM OUT ONTO GITHUB I WILL WAIT TO UPGRADE THIS FILE.
"""

# CREATE A THEME VARIABLE
theme = sg.theme('darkamber')

# POP UP WINDOW THAT GETS THE COMPANY NAME AND SYMBOL
def symbolGUI():
    sg.theme(theme)

    layout = [
        [sg.Text('Please enter the Company Name and Symbol: ')],
        [sg.Text('Company Name', size=(15, 1)), sg.InputText()],
        [sg.Text('Symbol', size=(15, 1)), sg.InputText()],
        [sg.Submit(), sg.Cancel()]
    ]

    window = sg.Window('Company Information', layout)
    event, values = window.read()
    window.close()
    GUI_Event = event[0]
    company = values[0]
    symbol = values[1]

    return symbol, company
