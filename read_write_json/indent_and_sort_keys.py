# applies indent and sort_keys on json data.

import json

with open('data.txt') as my_file:
	data = json.load(my_file)

result = json.dumps(data, sort_keys=True, indent=4)
print(result)