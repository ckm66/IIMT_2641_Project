from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from Model import AuctionRecord
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv
load_dotenv()

class WebScrapy:
    def __init__(self) -> None:
        """This function defines webdriver parameter"""
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.uri = os.getenv('CONNECTION_STRING')
        self.database = MongoClient(os.getenv('CONNECTION_STRING')).get_database('Auction_Analysis')
        self.collection = self.database['Auction_Records']
        self.invalid_collection = self.database['Auction_Records_Invalid']

    
    def login(self) -> None:
        """This function login the website using user credentials"""
        self.driver.get("https://www.artsy.net/auction-result/4849966")
        user_name = self.driver.find_element(By.CSS_SELECTOR, "input[type='email'][name='email'][placeholder='Enter your email address']")
        user_name.send_keys(os.getenv("REGISTERED_EMAIL"))

        user_password = self.driver.find_element(By.CSS_SELECTOR, "input[type='password'][name='password'][placeholder='Enter your password']")
        user_password.send_keys(os.getenv("REGISTERED_PASSWORD"))

        login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()


    def goto(self, url: str) -> None:
        """This function will direct the webdriver to the url provided"""
        self.driver.get(url)

    def getArtworkNameandPrice(self):
        artwork_name = self.driver.find_element(By.CSS_SELECTOR, 'a[class = "RouterLink__RouterAwareLink-sc-1nwbtp5-0 dikvRF"]').text
        try: # If the artwork is Bought in
            if self.driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/div[3]/div[2]/i').text == "Bought In":
                sale_price = "Bought In"
                tag_price = 0
                return artwork_name, sale_price, tag_price
        except:
            pass

        try: # If the tag price is not stated with US Dollar
            tag_price = self.driver.find_elements(By.CSS_SELECTOR, 'div[class = "Box-sc-15se88d-0 Flex-cw39ct-0 LbPWX"]')[1].text.split("\n")[0]
            sale_price = self.driver.find_element(By.CSS_SELECTOR, 'div[class = "Box-sc-15se88d-0 Text-sc-18gcpao-0 caIGcn egIqXp"]').text
        except:
            tag_price = 0
            sale_price = self.driver.find_elements(By.CSS_SELECTOR, 'div[class = "Box-sc-15se88d-0 Flex-cw39ct-0 LbPWX"]')[1].text.split("\n")[0]
        return artwork_name, sale_price, tag_price


    def getArtworkDetails(self, artist: str) -> list:
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class="Box-sc-15se88d-0 Text-sc-18gcpao-0 MyCollectionArtworkSidebarMetadata__WrappedText-sc-5mms7r-0 eXbAnU jYhtRb cqzlmg"]')))
        artwork_name, sale_price, tag_price = self.getArtworkNameandPrice()
        information_list = [information.text for information in self.driver.find_elements(By.CSS_SELECTOR, 'div[class="Box-sc-15se88d-0 Text-sc-18gcpao-0 MyCollectionArtworkSidebarMetadata__WrappedText-sc-5mms7r-0 eXbAnU jYhtRb cqzlmg"]')]
        return artist, artwork_name, sale_price, tag_price, information_list

    def createAuctionRecord(self, artist: str):
        artist, artwork_name, sale_price, tag_price, information_list = self.getArtworkDetails(artist)
        auction_record = AuctionRecord(artwork_name, artist, sale_price, tag_price, information_list)
        auction_record.transform()
        return auction_record, auction_record.fail_flag

    def insertToMongoDB(self, auction_record, invalid_flag):
        if invalid_flag == True:
            self.invalid_collection.insert_one(auction_record.__dict__)
            return
        self.collection.insert_one(auction_record.__dict__)

        


        
