import json
from datetime import datetime

with open('test/Counter.json') as f:
   data = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
print(data)


def write_json(data, filename='test/Counter.json'):
	print("coming here")
	with open(filename, 'w') as f:
			json.dump(data, f, indent=4)




with open('test/Counter.json') as json_file:
		data = json.load(json_file)
		print("coming here now")
		data['counter_healthy'] = int(data['counter_healthy']) + int("1")
		data['last_updated'] = today = datetime.today().__str__()
		write_json(data)