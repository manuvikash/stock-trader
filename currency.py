from bs4 import BeautifulSoup
import requests


def usdToInr(usd):
    response = requests.get("https://in.investing.com/currencies/usd-inr")
    soup = BeautifulSoup(response.content, 'html.parser')

    inr = soup.find(attrs={"class": "last-price-value js-streamable-element"})

    return usd*inr
