# Request module is one the best module if you want to take a HTTP request. It can be used to download images and has many other applications too.
# It is not a built-in module so you need to type 'pip install requests' in the terminal
# Along with bs4 (BeautifulSoup) module, you can do web scraping
# Web scraping is copying html code from a website and using it in your own
# By bs4, you can select whether you want to copy heading, paragraph or anything

import requests

# Taking a url
url = "https://www.wikipedia.com"
r = requests.get(url)

# Printing the html code
print(r.text)

# If you look at the output, the html code seems really messy.
# Thus we can use bs4 module to help ourselves! (Make sure you install bs4 first from the terminal)
from bs4 import BeautifulSoup

# Using a parser file to detect the html texts
a = BeautifulSoup(r.text, "html.parser")

# Printing the beautified version of the HTML code
print(a.prettify())

# Now if you look at the output, the code seems easy to understand (only if you know HTML and CSS)

# To get a desired element only
for b in a.find_all("p") : 
    print(b.text)           # If some HTML code is imported through API then it will not print here. Only those which are genuinly written by the developer will come here
    