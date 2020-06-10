import os
import pickle
from get_credentials import get_creds
from selenium import webdriver

if os.path.exists('credentials.pickle'):
    with open('credentials.pickle','rb') as f:  
        credentials = pickle.load(f)
else:
    get_creds()
    with open('credentials.pickle','rb') as f:  
    	credentials = pickle.load(f)

TEAMS_PATH = r'https://login.microsoftonline.com/common/oauth2/authorize?response_type=id_token&client_id=5e3ce6c0-2b1f-4285-8d4b-75ee78787346&redirect_uri=https%3A%2F%2Fteams.microsoft.com%2Fgo&state=00b8dd1b-8f5d-4eb3-8f77-5c76ff40e3b2&&client-request-id=d2afe301-0371-4fb6-b185-1ad0345268b5&x-client-SKU=Js&x-client-Ver=1.0.9&nonce=3afa9b8e-d754-4aae-bb73-ab6fd6bc2f33&domain_hint='
EXECUTABLE_PATH = credentials['EXECUTABLE_PATH']
EMAIL_ID = credentials['Email_or_phone_no']
PASSWORD = credentials['Password']

driver = webdriver.Firefox(executable_path=EXECUTABLE_PATH)
driver.get(TEAMS_PATH)

# driver.find_element_by_link_text('Sign in').click()
