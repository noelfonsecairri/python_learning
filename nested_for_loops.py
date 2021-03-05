# looping through two different lists by using outer and inner loops

first_names = ["BlueRay ", "Upchuck ", "Lojack ", "Gizmo ", "Do-Rag "]
last_names = ["Zzz", "Burp", "Dogbone", "Droop"]
full_names = []

for a in first_names:
	for b in last_names:
		print(a + " " + b)

#---------------------
# Code an outer loop that loops through the first list and an innner loop that loops through the second list. The inner loop displays each inner list value.

b = [1, 2, 3, 4, 5, 6]
d = [7, 8, 9, 10, 11]

for b_num in b:
  for d_num in d:
    print(d_num)

# Code nested for loops. When the outer tuple element is 4 and the inner tuple element is "b" display "ok"

nums = (1, 2, 3, 4, 5, 6)
strings = ("a", "b", "c", "d", "e")

for num in nums:
  if num == 4:
    for string in strings:
      if string == "b":
        print("ok")

        