import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium_stealth import stealth


def get_proxy():
    link = "https://www.sslproxies.org/"
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    proxy = soup.find("textarea").text.split('\n')

    with open("proxy.txt", 'w') as file:
        for string in [proxy[i] for i in range(len(proxy)) if i > 2]:
            file.write(string + "\n")


def set_browser(proxy):
    options = webdriver.ChromeOptions()
    #options.add_argument(f'--proxy-server={proxy}')
    options.add_argument('--proxy-server=190.26.201.194:8080')
#    print(f'--proxy-server={proxy}')
    options.add_argument('start-maximized')
    options.add_argument("user-data-dir=/home/yura/selenium/avtoreg3")
#    options.add_argument('headless')
    global browser
    browser = webdriver.Chrome(chrome_options=options)
    stealth(browser,
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36',
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win64",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )


def send_form():
    browser.switch_to.window(mail_window)
    sleep(1)
    mail = str(browser.find_element(By.CSS_SELECTOR, "#inbox-id").text) + "@sharklasers.com"
    name = "иван иванов"
    username = "ivandj12319q"
    password = "12345678qwertyY"
    browser.switch_to.window(inst_window)
    browser.find_element(By.CSS_SELECTOR, '[name="emailOrPhone"]').send_keys(mail)
    browser.find_element(By.CSS_SELECTOR, '[name="fullName"]').send_keys(name)
    browser.find_element(By.CSS_SELECTOR, '[name="username"]').send_keys(username)
    browser.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys(password)
    browser.find_element(By.XPATH, '//button[text()="Next"]').click()
    sleep(3)
    browser.find_element(By.CSS_SELECTOR, '#react-root > section > main > div > div > div:nth-child(1) > div > div.qF0y9.Igw0E.IwRSH.eGOV_.acqo5._4EzTm.bkEs3.DhRcB > div > div > span > span:nth-child(3) > select').click()
    browser.find_element(By.CSS_SELECTOR, '[title="1990"]').click()
    browser.find_elements(By.CSS_SELECTOR, 'button')[2].click()
    browser.switch_to.window(mail_window)


def reg(proxy):
    set_browser(proxy)
    browser.get("http://www.instagram.com/accounts/emailsignup/")
    try:
        browser.execute_script("window.open('https://www.guerrillamail.com/inbox')")
    except:
        pass
    global inst_window
    global mail_window
    inst_window = browser.window_handles[0]
    mail_window = browser.window_handles[1]
    send_form()


def main():
    try:
#       get_proxy()
        with open("proxy.txt") as file:
            proxies = file.readlines()
            proxies = [i[:-1] for i in proxies]
        reg(proxies[3])

    except Exception as e:
        print(e)
    finally:
        sleep(3000)
        browser.quit()


if __name__ == '__main__':
    main()
