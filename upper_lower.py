cleanest_cities = ["cheyenne", "santa fe", "tucson", "great falls", "honolulu"]

city_to_check = input("Enter city name to check: ")

for i in cleanest_cities:
	if i.lower() == city_to_check.lower():
		print(i.title())