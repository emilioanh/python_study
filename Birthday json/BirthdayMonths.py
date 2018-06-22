import json
from collections import Counter
from bokeh.plotting import figure, show, output_file #can only run by env because library is not install on machine
#for installing bokeh: pip install virtualenv
#						virtualenv env

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

a=Counter(months)
print(a.values())
print(months)
output_file("plot.html")
x_categories = ["a", "b", "c", "d", "e"]
x = ["a", "d", "e"]
y = [4, 5, 6]

p = figure(x_range=list(num_to_string.values()))
p.vbar(x=list(a.keys()), top=list(a.values()), width=0.5)

show(p)