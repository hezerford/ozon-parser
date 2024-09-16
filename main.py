import json
import time
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def get_products_links(item_name='наушники hyperx'):
    driver = uc.Chrome()
    driver.implicitly_wait(5)

    driver.get(url='https://ozon.ru')
    time.sleep(2)

    find_input = driver.find_element(By.NAME, 'text')
    find_input.clear()
    find_input.send_keys(item_name)
    time.sleep(2)

    find_input.send_keys(Keys.Enter)
    time.sleep(2)

    current_url = f'{driver.current_url}&sorting=rating'
    driver.get(url=current_url)
    time.sleep(2)

    driver.close()
    driver.quit()

def main():
    get_products_links()

if __name__ == '__main__':
    main()