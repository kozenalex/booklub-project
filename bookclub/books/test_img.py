import requests
import json

response = requests.get(
                        url='https://www.googleapis.com/books/v1/volumes',
                        params={
                            'q':'Дети хурина',
                            'printType': 'books',
                            'projection':'lite'
                        })
r_j = json.loads(response.text)
thumbs = [
    x['volumeInfo']['imageLinks']['thumbnail'] for x in r_j['items'] if x['volumeInfo'].get('imageLinks')
    ]
print(thumbs)