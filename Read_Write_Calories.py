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




with open('test/DailySnackTracker.json') as json_file:
		data = json.load(json_file)

		data['counter_healthy'] = "10"




write_json(data)