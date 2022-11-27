import time
from selenium.webdriver import Chrome 
from selenium.webdriver.chrome.options import Options

driver= Chrome( executable_path="C:\\Users\\marti\\OneDrive\\Escritorio\\chromedriver_win32\\chromedriver.exe")
driver.get("https://magento.softwaretestingboard.com/customer/account/login/")

driver.maximize_window()

user=driver.find_element(by="id",value="email").send_keys('ceeciliamartinezz@gmail.com')

password=driver.find_element(by="id",value="pass").send_keys('Ceeci2908')

btn=driver.find_element(by="id",value="send2").click()

time.sleep(5)
driver.close()
