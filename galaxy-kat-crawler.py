from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--headless')
driver = webdriver.Chrome('./chromedriver', chrome_options=options)
driver.get("https://www.paraland.world/parastar")
print(driver.get_window_size())
driver.set_window_size(800,600)
# time.sleep(10)
print(f"======== render done ======")
# button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'Animal')))

driver.implicitly_wait(20)
button = driver.find_element_by_id('Animal')

desired_y = (button.size['height'] / 2) + button.location['y']
print("======== target position:",button.size['height'],button.location['y'])
# current_y = (driver.execute_script('return window.innerHeight') / 2) + driver.execute_script('return window.pageYOffset')
print("======= current_y:",driver.execute_script('return window.pageYOffset'))
# scroll_y_by = desired_y - current_y
# print("======scroll_y_by:",scroll_y_by)
driver.execute_script("window.scrollTo(0,1310);")
time.sleep(3)
print("======= current_y2:",driver.execute_script('return window.pageYOffset'))

ActionChains(driver).move_to_element_with_offset(button,5,5).click(button).perform()



print(f"======== go to animal page ======")
# driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/span[2]').click()
# time.sleep(20)
print(f"======== starting press button ======")
# vote = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/table/tr[1]/td[5]/button')
time = 0
while True: 
    try:
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/table/tr[1]/td[5]/button').click()
        print("press success count",time)
        time += 1
    except Exception as e:
        print(e)    

dirver.quit()