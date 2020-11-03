import json
from datetime import datetime

with open('test/Calorie_Master.json') as f:
  data = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
print(data)


def write_json(data,temp1, filename='test/DailySnackTracker.json'):
	print("coming here")
	with open(filename, 'w') as f:
			json.dump(data, f, indent=4)
			json.dump(temp1, f, indent=4)



with open('test/DailySnackTracker.json') as json_file:
		data = json.load(json_file)

		temp = data['Snacks']
		today = datetime.today().__str__()
		# python object to be appended
		y = {
							"snack": "Apple",
	                        "quantity": "1",
	                         "choice" : "good",
	                        "consumed": "95",
	                       "date and time": today
		     }
		temp.append(y)

	

		for data_set in data.get("Counter", {}):
			_extract = data_set.get("count_unhealthy", None)
			print (_extract)
		#print(temp1['count_unhealthy'] +"Asha")
		#temp1["count_unhealthy"] = int(temp1["count_unhealthy"]) + 1
		#temp1["date and time"] = today


write_json(data,temp1)