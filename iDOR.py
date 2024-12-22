import requests
from random import randrange
import time

while True:
    # Generation of URL
    base_url = "http://static.donationalerts.ru/audiodonations/"
    rint1 = randrange(64000, 65500)
    rint2 = randrange(111, 999)
    url = f"{base_url}{rint1}/{rint1}{rint2}.wav"
    
    try:
        # Response 
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print(f"Found! {url}")
            with open('result.txt', 'a') as file:
                file.write(url + '\n')
        else:
            print(f"Not found: {url} (статус: {response.status_code})")
    except requests.RequestException as e:
        print(f"Error: {e}")
    
    
    time.sleep(0.02)  
