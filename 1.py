import json
import requests


def read_file(name):
	numbers = []
	with open(name) as f:
		for line in f:
			numbers.append(line.strip())
	return(numbers)


api_url = "http://numbersapi.com/{}"
numbers = read_file("test.txt")
categories = ['trivia', 'math', 'date', 'year']
for num in numbers:
	api_url = 'http://numbersapi.com/{}/math'.format(num)
	param = {
		'json': 'true'
		}
	req = requests.get(api_url, params=param)
	json_data = json.loads(req.text)
	if json_data["found"]:
		print("Boring")
	else:
		print("Interesting")
