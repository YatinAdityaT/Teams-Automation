import pickle

print('Please enter the following information:')
credentials = {}

print('Please enter the path to geckodriver')
credentials['EXECUTABLE_PATH'] = input()

print("Please enter your Teams Email Id")
credentials['Email_or_phone_no'] = input()

print("Please enter your password")
credentials['Password'] = input()

with open('credentials.pickle','wb') as f:	
	pickle.dump(credentials,f)