import requests

page1 = requests.get("https://scrapy.org/") #scrapy
if page1.status_code == 200:
    print(page1.url)
else:
    print('Error', page1.status_code)

page2 = requests.get("https://requests.readthedocs.io/en/latest/index.html") #requests
if page2.status_code == 200:
    print(page2.url)

else:
    print('Error', page2.status_code)

page3 = requests.get("https://www.selenium.dev/") #selenium
if page3.status_code == 200:
    print(page3.url)
else:
    print('Error', page3.status_code)

page4 = requests.get("https://kivy.org/") #kivy
if page4.status_code == 200:
    print(page4.url)
else:
    print('Error', page4.status_code)

page5 = requests.get("https://pypi.org/project/pyspider/") #pyspider
if page5.status_code == 200:
    print(page5.url)
else:
    print('Error', page5.status_code)

page6 = requests.get("https://pypi.org/project/beautifulsoup4/") #beautifulsoup
if page6.status_code == 200:
    print(page6.url)
else:
    print('Error', page6.status_code)

page7 = requests.get("https://pypi.org/project/PyDejavu/") #PyDejavu
if page7.status_code == 200:
    print(page7.url)
else:
    print('Error', page7.status_code)

page8 = requests.get("https://pypi.org/project/PyAudio/") #PyAudio
if page8.status_code == 200:
    print(page8.url)
else:
    print('Error', page8.status_code)

page9 = requests.get("https://pypi.org/project/pyo/") #pyo
if page9.status_code == 200:
    print(page9.url)
else:
    print('Error', page9.status_code)