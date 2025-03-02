# In this exercise, you need to use NewsAPI and get the headlines and descriptions as outputs. Ask the user to enter the news that he/she wants to be related with.
# You will have to use requests and JSON module to work this out.
# Search for the JSON module as the NewsAPI is stored in form of JSON file, so you will need the module to access these elements
# This is going to be a little complicated. So make sure you try it out yourself, otherwise the solution is given below.
















import requests
import json 
import time

a = input("You need news? Related to what? ")
newsapi = f"https://newsapi.org/v2/everything?q={a}&from=2023-03-21&sortBy=publishedAt&apiKey=bae169f5c99c4915962ee707d86a26e9"
r = requests.get(newsapi)

news = json.loads(r.text)
for i in news["articles"] : 
    print(i["title"])
    print(i["description"])
    print("-------------------------------")
    time.sleep(5)
    
# The exercise ended!
