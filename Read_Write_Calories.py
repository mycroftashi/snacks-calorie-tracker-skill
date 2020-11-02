import json

with open('test/Calorie_Master.json') as f:
  data = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
print(data)


def write_json(data, filename='test/DailySnackTracker.json'):
	with open(filename, 'w') as f:
		json.dump(data, f, indent=4)


with open('test/DailySnackTracker.json') as json_file:
	data = json.load(json_file)

	temp = data['Snacks']

	# python object to be appended
	y = {"snack": 'something',
	     "quantity": "1",
	     "consumed": "900"
	     }

	# appending data to emp_details
	temp.append(y)

write_json(data)