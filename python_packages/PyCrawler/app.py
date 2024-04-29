'''
Web Scrapping
'''
import requests
from bs4 import BeautifulSoup

response = requests.get("https://stackoverflow.com/questions")
soup = BeautifulSoup(response.text, "html.parser")

questions = soup.select(".s-post-summary")
print(questions[0].get("id", 0))
print(questions[0].select_one(".s-link").getText())
