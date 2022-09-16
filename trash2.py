import requests
prox = "185.18.52.9:8090"
proxies = {
    'http': prox,
    'https': prox,
}
r = requests.get("https://who.is", proxies=proxies, timeout=15)
print(r)