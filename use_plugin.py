from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
try:
    chrome_options = Options()
    #user_data='C://Users//Administrator//AppData//Local//Google//Chrome//User Data//Default'
    chrome_options.add_extension("C://Users//Administrator//Downloads//install.crx")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.maximize_window()
    print('-----------------------------------------------------')
    li=[window for window in driver.window_handles]
    for window in li:
        driver.switch_to.window(window)
        if "DomeCross" in driver.title:
            vip_login=driver.find_element_by_xpath('//*[@id="login_tab"]')
            vip_login.click()
            vip_login.send_keys(Keys.TAB)
            username=driver.switch_to.active_element
            username.send_keys("")
            username.send_keys(Keys.TAB)
            password=driver.switch_to.active_element
            password.send_keys("")
            password.send_keys(Keys.TAB)
            login=driver.switch_to.active_element
            login.click()
    input("press anykey")
    driver.get("https://www.google.com")
    input("press anykey")

finally:
    driver.quit()