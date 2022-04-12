from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from scrap import get_details

import csv
import json



if __name__ == "__main__":

    file = open('resource\Amazon Scraping.csv')
    
    csvreader = csv.reader(file)
    header = next(csvreader)

    # Chrome Version : 100.0.4896.75  
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome('driver/chromedriver', options=options)
    
    index = 0
    limit = 100

    for row in csvreader:

        if index==limit:
            break

        index+=1
        
        country = row[0] 
        asin = row[1]

        #print(country, asin)

        url = "https://www.amazon.{}/dp/{}/".format(country,asin)

        driver.implicitly_wait(10)
        driver.get(url)

        json_object = get_details(driver, url)

        if json_object != {}:
            print(True)
            
            # Writing to sample.json
            with open(r'resource/result.json', 'a') as outfile:
                json.dump(json_object, outfile)

        

    driver.close()
    file.close()


