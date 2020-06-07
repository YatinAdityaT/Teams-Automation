import os
import pickle
import get_credentials
from selenium import webdriver

if os.path.exists('credentials.pickle'):
    with open('credentials.pickle','rb') as f:  
        credentials = pickle.load(f)
else:
    get_credentials()
    with open('credentials.pickle','rb') as f:  
    	credentials = pickle.load(f)

TEAMS_PATH = 'https://www.microsoft.com/en-in/microsoft-365/microsoft-teams/group-chat-software'
EXECUTABLE_PATH = credentials['EXECUTABLE_PATH']
EMAIL_ID = credentials['Email_or_phone_no']
PASSWORD = credentials['Password']

webdriver = webdriver.Firefox(executable_path=EXECUTABLE_PATH)
webdriver.get(TEAMS_PATH)

'/html/body/section/div[1]/div/section/div/div/div/div/div/div[1]/div[2]/a'