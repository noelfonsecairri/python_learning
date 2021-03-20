from csv import DictWriter
from itertools import zip_longest

example = {"A" : [1,2,3], "B" : [1], "C": [4,5,6,7,8,9]}
headers = example.keys()

values = (example.get(key, []) for key in headers)
print(values)