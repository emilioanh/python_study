from string import ascii_lowercase
from collections import Counter
'''
Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, and print out
the results to the screen. I have a .txt file for you, if you want to use it!
Extra:
Instead of using the .txt file from above (or instead of, if you want the challenge), take this .txt file, and count how many of each
“category” of each image there are. This text file is actually a list of files corresponding to the SUN database scene recognition database,
and lists the file directory hierarchy for the images. Once you take a look at the first line or two of the file, it will be clear which
part represents the scene category. To do this, you’re going to have to remember a bit about string parsing in Python 3.
I talked a little bit about it in this post.
'''
# with open('nameslist.txt','r') as f:
#     allText = f.readlines()
#     for index in range(0,len(allText)-1): #last sentence does not have \n therefore don't need to strip
#         if '\n' in allText[index]:
#             allText[index] = allText[index].strip()
#     print (Counter(word for word in allText ))

#Extra:
counter_dict = {}
with open('Training_01.txt','r') as f:
	line = f.readline()
	while line:
		line = line[3:-26] #count category and +1 for every pic in that dir because no pic can exist in the same dir with duplicated name
		if line in counter_dict:
			counter_dict[line] += 1
		else:
			counter_dict[line] = 1
		line = f.readline()

print(counter_dict)
