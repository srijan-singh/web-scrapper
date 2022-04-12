import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def get_details(driver, url):

    # No Such Element Exception Handling
    try:
        # Product Title
        title_xpath = r'/html/body/div[2]/div[2]/div[5]/div[4]/div[4]/div[1]/div/h1/span'
        title = driver.find_element(by=By.XPATH, value=title_xpath).text
    except NoSuchElementException:
        # Returning empty JSON
        print("{} not available".format(url))
        return {}
    
    # Product Image URL    
    image_xpath = r'/html/body/div[2]/div[2]/div[5]/div[4]/div[3]/div[1]/div[1]/div/div/div[2]/div[1]/div[1]/ul/li[1]/span/span/div/img'
    image_url = driver.find_element(by=By.XPATH, value=image_xpath).get_attribute('src')

    # Price of the Product
    price_xpath = r'/html/body/div[2]/div[2]/div[5]/div[4]/div[4]/div[10]/div[1]/div/table/tbody/tr[2]/td[2]/span[1]/span[2]'
    price = driver.find_element(by=By.XPATH, value=price_xpath).text
    
    # Product Details
    product_xpath = r'//*[@id="feature-bullets"]'
    product_details = driver.find_element(by=By.XPATH, value=product_xpath).text
    
    return{
        "Product Title" : title,
        "Product Image URL" : image_url,
        "Price of the Product" : price,
        "Product Details" : product_details
    }



if __name__ == "__main__":

    country = 'ca' 
    asin = 'B07YYNX5X6'

    url = "https://www.amazon.{}/dp/{}".format(country,asin)

    # Chrome Version : 100.0.4896.75  
    driver = webdriver.Chrome('driver/chromedriver')

    driver.get(url)

    json = get_details(driver, url)

    if json != {}:
        print(json)

    driver.close()