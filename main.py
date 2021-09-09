##Step 0: Creating new env and installation
##created an environment: conda activate webscrap
##Installation
#pip install requests
#pip install html5lib
#pip install bs4

import requests
from bs4 import BeautifulSoup
url= "https://www.codewithharry.com"

#STEP1: Get the HTMLCode
r=requests.get (url)
html_content=r.content
print(html_content)   ##Output will be displayed in our console
#Step2: Parse the HTML
soup=BeautifulSoup(html_Content,'html.parser')
print(soup)
print(soup.prettify) ##IT WIL BEAUTIFY THE HTML CODE


#step3: HTML  Tree traversal  ***there r many things to learn in treetraverse
##Our soup is something like a tree
##Commonly used type of objects (There r many more)
#1.Tag
#2.NavigableString
#3.BeautifulSoup
# 4.Comment 

#Get the title of the HTML page
title= soup.title

print(title) 
print(type(title))  ### 1.prints  Tag
print(type(title.string)) ## 2.gives navigable string
print(type(soup)) ## 3.Beautiful Soup object

#Get all the paragraphs or(anchors or anything)
paras= soup.find_all('p')
print(paras)
#Get all the anchors tag
anchors = soup.find_all('a')
print(anchors)
###Get all the links on the page: But we cant access the links
for link in anchors:
    print(link.get('href'))

###Get all the links on the page: To access the links
all_links=set()  ##To store all links; we camn give list also; but set will give unique elements
for link in anchors:
    if (link.get('href')!='#'):
        #all_links.add("https://codewithharry.com"+link.get('href')
        link_text = "https://codewithharry.com"+link.get('href')
        all_links.add(link)
        print(link_text)  ##We click these (Control+click)links in console they will open in browser
exit()

navbarsupportedContent= soup.find('navbarSupportContent') ###copy id from html dsource code
print(navbarsupportedContent)
print(navbarsupportedContent.children)
print(navbarsupportedContent.contents)

##Dif b/w content and chidren:
# #contents:tags r available as a list; stored in memory
# #children:tags r available as a generator;# not stored in memory and we can use  ###For large files
##if there r multiple contents use forloop
for elem in navbarsupportedContent.contents:
    print(elem)


##When we use strings
from item in navbarsupportedContent.strings:
    print(item) ##prints string

from items in navbarsupportedContent.stripped_strings:
    print(items) ##prints string

print(navbarsupportedContent.parent)  ##parent tag
print(navbarsupportedContent.parents)  ##generates genetor so we can use iterator

for itemss in navbarsupportedContent.parents:
    print(itemss)
    print(itemss.name)

##########  Previous and next sibling
print(navbarsupportedContent.next_sibling)  #no o/p
print(navbarsupportedContent.next_sibling.next_sibling) ##these next and previous will also give spaces as element
print(navbarsupportedContent.previous_sibling.previous_sibling)

##Lets get login mode id ###CSS
elem2=soup.select('.modal-footer')   ##.modal-footer is a css class
print(elem2)

####Read stackoverflow and google and beautifulsoup documentation

##Get first element from hyml page
print(soup.find('p')) ##prints first paragraph
##Get classes of all html pages
print(soup.find('p')) ['class']

#find all elements with class: lead
soup.find_all("p", class_="lead")  ###Here p is element we want to find

##Get text from the tags/soup
print(soup.find('p').get_text())
##Get text from the soup
print(soup.get_text())   ###all texts 

##4.Comment
##lET HAVE A MARHKUP IS APRAGRAPH WITH HTML COMMENT
markup= "<p><!-- This si a comment---> </p>"
soup2=BeautifulSoup(markup)
print(soup2.p)##paragaphs
print(soup2.p.string)
print(type(soup2.p.string))
##use exit() when u want torun upto that extebt