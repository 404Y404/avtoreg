import requests

inst="""
        <title>
Instagram
</title>
"""
with open("proxy.txt", "r") as file:
	proxies = file.readlines()
	proxies = ['https://' + i[:-1] for i in proxies]

for i in proxies:
	print(i)
	proxy = {"http" : i}
	try:
		response = requests.get("https://www.instagram.com", proxies=proxy, timeout=8)

		if inst in response.text:
			print("valid")
		else:
			print("no valid")
	except Exception as e:
		print(e)
		print("no valid")

