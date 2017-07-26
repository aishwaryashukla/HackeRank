from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# driver = webdriver.Remote(
#    command_executor='http://127.0.0.1:4444/wd/hub',
#    desired_capabilities=DesiredCapabilities.CHROME)

print (" i am at lije 3")
import os
print (os.system('chdir'))
#driver = webdriver.Chrome(executable_path="C:\Users\aishw\Downloads\chromedriver_win32")
chromedriver = 'C:\\Users\\aishw\\Downloads\\chromedriver_win32\\chromedriver.exe'
# if (os.path.isdir(chromedriver)):
#     print("found file")
# os.environ["webdriver.chrome.driver"] = chromedriver
# chromedriver = chromedriver.encode('utf-8')
driver = webdriver.Chrome(chromedriver.encode('utf_8'))
# driver.get("http://stackoverflow.com")
# driver.quit()