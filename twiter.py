from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
import csv        

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


file_path = r'twitter_links.csv'
df = pd.read_csv(file_path)
for i in df.values:
    for r in i:
        
        driver.get(r)
        sleep(10)
        try:
            bio = driver.find_element(By.XPATH ,'(//span[@class="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0"])[11]').text
        except:
            bio = ""
        try:
            following = driver.find_element(By.XPATH, "//span[@class='css-911oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0']").text
        except:
            following = 0
        try:
            followers = driver.find_element(By.XPATH, "(//span[@class='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'])[17]").text
        except:
            followers = 0
        try:
            location = driver.find_element(By.XPATH , '(//span[@class="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0"])[13]').text
        except:
            location = ""
        try:
            website = driver.find_element(By.XPATH , '(//span[@class="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0"])[14]').text
        except Exception as e:
            print(e)
            website = ""
        

        count=0
        with open('Twitter scraper.csv', "a" ) as file:
                    writer = csv.writer(file)
                    #writer.writerow(["biography", "followers_count", "following_count","location" , "website"])
                    writer.writerow([ bio, followers, following ,location,website])
                    print("file written")