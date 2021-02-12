# THIS SCRIPT ALLOWS ME TO IMPORT MY SECRET DOC HOLDING
# MY USERNAMES AND PASSWORDS
# some_file.py
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'C:/build')

import acctInfo
from acctInfo import API_KEY, REDIRECT_URI, ACCOUNT_ID
from acctInfo import TOKEN_PATH, CHROMEDRIVER_PATH
