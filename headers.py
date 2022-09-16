s="""accept-encoding: gzip, deflate, br
accept-language: en-US,en;q=0.9
content-length: 76
content-type: application/x-www-form-urlencoded
cookie: csrftoken=v8lEJcJGqe7LBN1KIUdjSWTzjwR6a4QY; mid=YuK0AQALAAF9YMW6sforJ7mdLlAV; ig_did=8F67FE9E-0877-4A94-998F-70F3D68A0BF1
origin: https://www.instagram.com
referer: https://www.instagram.com/accounts/emailsignup/
sec-fetch-dest: empty
sec-fetch-mode: cors
sec-fetch-site: same-origin
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36
x-asbd-id: 198387
x-csrftoken: v8lEJcJGqe7LBN1KIUdjSWTzjwR6a4QY
x-ig-app-id: 936619743392459
x-ig-www-claim: 0
x-instagram-ajax: 1a27fb615712
x-requested-with: XMLHttpRequest"""
for i in s.split("\n"):
	i2 = i.replace(':','":"')
	print(f'"{i2}",')