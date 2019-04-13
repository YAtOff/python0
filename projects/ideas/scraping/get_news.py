"""
Преди да стартирате инсталирайте:
pip install requests
pip install BeautifulSoup4

Повече информация тук: https://realpython.com/python-web-scraping-practical-introduction/
"""

import requests
from bs4 import BeautifulSoup


def load_html(url):
    response = requests.get(url)
    return response.content


raw_html = load_html("https://elsys-bg.org/")
html = BeautifulSoup(raw_html, "html.parser")
for item in html.select(".news-list li"):
    time = item.find("time").text
    title = item.find("a").text
    print("На {}: {}".format(time, title))
