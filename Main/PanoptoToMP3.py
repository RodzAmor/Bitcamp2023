from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from time import sleep
import json

URL = "https://umd.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=5a9fdfcc-31cb-4d4a-8d31-af660118e785"

caps = DesiredCapabilities.CHROME
caps['goog:loggingPrefs'] = {'performance': 'ALL'}
options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome('/Users/andrie/Desktop/chromedriver', desired_capabilities=caps)
driver.get(URL)


# Get to the Login form
print("Please log into the CAS and the Duo authentication.")

def checkLoggedIn():
    if("umd.hosted.panopto.com" in driver.current_url):
        return False
    else:
        return True
    
while(checkLoggedIn()):
    sleep(1)


logs = driver.get_log("performance")

with open("test.json", "w") as f:
    f.write("[")
    # print(perf, file=f)
    for log in logs:
        network_log = json.loads(log["message"])["message"]

        if("Network.response" in network_log["method"]
            or "Network.request" in network_log["method"] or
            "Network.WebSocket" in network_log["method"]):
            
            f.write(json.dumps(network_log) + ",")

    f.write("{}]")

sleep(10)

while(True):
    if(input("Do you want to quit? y/n \n") in ["yes", "Y", "Yes", "y"]):
        driver.quit()
        break
