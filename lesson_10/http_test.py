import requests

r = requests.get('https://github.com/')

with open('index.html', 'w', encoding='utf-8') as file:
    file.write(r.text)