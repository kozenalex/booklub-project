import requests
import json

response = requests.get('https://www.googleapis.com/books/v1/volumes?q=%D0%93%D0%BE%D1%80%D0%BE%D0%B4+%D0%A1%D0%B0%D0%B9%D0%BC%D0%B0%D0%BA')
r_j = json.loads(response.text)
print(r_j['items'][0]['volumeInfo']['imageLinks']['thumbnail'])