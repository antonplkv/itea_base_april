import requests


images_list = ["https://cdn.eso.org/images/thumb300y/eso1907a.jpg"] * 5


for idx, file in enumerate(images_list):
    response = requests.get('https://cdn.eso.org/images/thumb300y/eso1907a.jpg')

    with open(f'{file.split("/")[-1]}', 'wb') as image:
        image.write(response.content)
