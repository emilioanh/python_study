'''
Use the BeautifulSoup and requests Python packages to print out a list of all the article titles
on the New York Times homepage.
'''

import requests
from bs4 import BeautifulSoup
 
base_url = 'http://www.nytimes.com' #setting the page
r = requests.get(base_url) #HTTP GET the url
soup = BeautifulSoup(r.text) #read the html with BeautifulSoup
 
for story_heading in soup.find_all(class_="story-heading"): #find in the html the tag with class "story-heading"
    if story_heading.a: 
        print(story_heading.a.text.replace("\n", " ").strip()) #replace new line necessary with a white space and
    else:                                                      #strip all necessary white-space
        print(story_heading.contents[0].strip())
'''
data_soup.find_all(attrs={"data-foo": "value"})
data-* attribute cannot be use like soup.find_all(data-foo="abcd")
but can be replaced by "attrs={"data-*":"value"}"
.replace("\n", " ")
'''
