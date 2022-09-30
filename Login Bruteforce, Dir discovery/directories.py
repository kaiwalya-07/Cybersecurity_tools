import requests


target_url = input('-> Enter the  Target URL: ')
file_name = input('-> Enter Name Of The File having the  Directories: ')


def request(url):
	try:
		return requests.get("http://" + url)
	except requests.exceptions.ConnectionError:
		pass


file = open(file_name, 'r')
for line in file:
	directory = line.strip()
	full_url = target_url + '/' + directory
	response = request(full_url)
	if response:
		print('-> Directory  discovered  at : ' + full_url)

