import requests

with requests.post("https://ad0afb9f6cd24ce8918665b9a9747057.apig.ru-moscow-1.hc.sbercloud.ru/", data="123") as res:
    print(res.text)
