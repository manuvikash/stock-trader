from dotenv import load_dotenv
import os
import requests

load_dotenv()
apiKey = os.getenv("API_KEY")
url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=INFY&apikey=" +  apiKey

req = requests.get(url)
data = req.json()

print(data)