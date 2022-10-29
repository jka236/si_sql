from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests


def sqlinjection(host):
    timeToSleep=1
    #create a new Firefox session
    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)

    #driver.implicitly_wait(30)
    driver.maximize_window()
    print("Selenium Success")
    
def send_request(host):
    response = requests.get(host)
    if response.status_code == 200:
        print("Request Success")
    
sqlinjection("http://google.com")
send_request("http://google.com")