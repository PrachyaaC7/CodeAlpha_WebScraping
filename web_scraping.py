import requests
from bs4 import BeautifulSoup
import pandas as pd
import os


url = "http://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

quotes = []
authors = []

for quote in soup.find_all("div", class_="quote"):
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text
    quotes.append(text)
    authors.append(author)

data = pd.DataFrame({
    "Quote": quotes,
    "Author": authors
})

data.to_csv("quotes_data.csv", index=False)
print("Scraping completed and saved to quotes_data.csv")
print("File saved at:", os.path.abspath("quotes_data.csv"))
