import undetected_chromedriver as uc
import time


driver = uc.Chrome()
try:
    driver.get('https://anycoindirect.eu')
    time.sleep(10)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()