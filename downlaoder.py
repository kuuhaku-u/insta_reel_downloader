
from time import sleep
import sys
from tracemalloc import stop
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())

#d1 ={"download.defa

##-URLS + START-##

base_url = "https://www.instagram.com/"
#profile_url = ""


##-URLS + END-##


driver.get(base_url)


user_name = sys.argv[-2]
password = sys.argv[-1]

#print (user_name + password)


find_username = "//input[@name='username']"
find_pass = "//input[@name='password']"
login_button = "//*[text()='Log In']"

sleep(5)
username = driver.find_element(By.XPATH,find_username).send_keys(user_name)
password = driver.find_element(By.XPATH,find_pass).send_keys(password)
login_button_click= driver.find_element(By.XPATH,login_button).click()
sleep(5)

saving_page = driver.find_element(By.XPATH,"//*[text()='Not Now']").click()
sleep(5)
notification_page = driver.find_element(By.XPATH,"//*[text()='Not Now']").click()
sleep(5)


#profile_go = driver.find_element(By.XPATH)

driver.get(base_url+user_name+'/saved/all-posts/')

sleep(5)

while driver.find_element_by_tag_name('div'):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    Divs=driver.find_element_by_tag_name('div').text
    if 'End of Results' in Divs:
        print ("end")
        break
    else:
        continue
sleep(5)

#driver.quit()