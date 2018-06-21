import json
from collections import Counter

months = []
num_to_string = {
	1: "January",
	2: "February",
	3: "March", 
	4: "April",
	5: "May",
	6: "June",
	7: "July",
	8: "August",
	9: "September",
	10: "October",
	11: "November",
	12: "December"
}
with open("scientist_birthdays.json", "r") as f:
    data = json.load(f)

for x in data.values():
    month = int(x.split('/')[0])
    months.append(num_to_string[month])

print(Counter(months))