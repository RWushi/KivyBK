import requests

SERVER_URL = "https://0621-5-251-52-7.ngrok-free.app"
#Это временный публичный адрес, если нужно запустить сервер с БД, то его нужно поменять


def send_location(latitude, longitude):
    url = f"{SERVER_URL}/location/"
    data = {
        "latitude": latitude,
        "longitude": longitude
    }
    response = requests.post(url, json=data)

    if response.status_code == 200:
        print("Локация сохранена в БД")
    else:
        print(f"Произошла ошибка: {response.status_code}")
