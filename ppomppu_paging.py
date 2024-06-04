from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time
import random

def page1_crawling(driver):
    titles = []
    urls = []
    start_num = 9
    end_num = 47
    for i in range(start_num, end_num + 1, 2):
        title_css_path = '#revolution_main_table > tbody > tr:nth-child(' + str(i) + ') > td:nth-child(3) > table > tbody > tr > td:nth-child(2) > div > a > font'
        titles.append(driver.find_element(By.CSS_SELECTOR, title_css_path).text)
        
        url_css_path = '#revolution_main_table > tbody > tr:nth-child(' + str(i) + ') > td:nth-child(3) > table > tbody > tr > td:nth-child(2) > div > a'
        urls.append(driver.find_element(By.CSS_SELECTOR, url_css_path).get_attribute('href'))

    return pd.DataFrame({"title": titles, "urls": urls})

def other_crawling(driver):
    titles = []
    urls = []
    start_num = 6
    end_num = 44
    #revolution_main_table > tbody > tr:nth-child(6) > td:nth-child(3) > table > tbody > tr > td:nth-child(2) > div > a > font
    #revolution_main_table > tbody > tr:nth-child(8) > td:nth-child(3) > table > tbody > tr > td:nth-child(2) > div > a > font
    #revolution_main_table > tbody > tr:nth-child(44) > td:nth-child(3) > table > tbody > tr > td:nth-child(2) > div > a > font
    for i in range(start_num, end_num + 1, 2):
        title_css_path = '#revolution_main_table > tbody > tr:nth-child(' + str(i) + ') > td:nth-child(3) > table > tbody > tr > td:nth-child(2) > div > a > font'
        titles.append(driver.find_element(By.CSS_SELECTOR, title_css_path).text)
        
        url_css_path = '#revolution_main_table > tbody > tr:nth-child(' + str(i) + ') > td:nth-child(3) > table > tbody > tr > td:nth-child(2) > div > a'
        urls.append(driver.find_element(By.CSS_SELECTOR, url_css_path).get_attribute('href'))

    return pd.DataFrame({"title": titles, "urls": urls})

def main():
    CHROME_DRIVER_PATH = './drivers/chromedriver.exe'
    service = Service(executable_path=CHROME_DRIVER_PATH)
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    URL = 'https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu&page=1&divpage=85'
    driver.get(url=URL)
    df = page1_crawling(driver)
    for i in range(2, 10):
        URL = 'https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu&page='+ str(i) + '&divpage=85'
        print(URL)
        driver.get(url=URL)
        df = pd.concat([df, other_crawling(driver)], ignore_index=True)
        time.sleep(random.uniform(2, 5))   # 2 ~ 5초 무작위로 설정
        
    df.to_csv("핫딜.csv", index=False)
    driver.quit()
if __name__ == "__main__":
    main()