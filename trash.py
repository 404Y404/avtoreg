import requests
f = open("proxy.txt", 'r')
good = open("good.html", 'r').read()
for prox in f.readlines():
    proxies = {
        'http': prox,
        'https': prox,
    }

    #r = requests.post("http://www.instagram.com/accounts/web_create_ajax/attempt/", data=data, headers=headers, proxies=proxies)
    try:
        r=requests.get("http://httpbin.smp.io/", proxies=proxies, timeout=5)
        if r.text == good:
            print(f"good {prox[:-1]}")
        else:
            print("bad")
    except Exception as e:
        print("bad")

