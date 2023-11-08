from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
import os
from dotenv import load_dotenv
load_dotenv()

class WebScrapy:
    
    
    def __init__(self) -> None:
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(options=chrome_options)
    
    def login(self) -> None:
        """This function login the website using user credentials"""
        self.driver.get("https://www.artsy.net/auction-result/4725374")
        user_name = self.driver.find_element(By.CSS_SELECTOR, "input[type='email'][name='email'][placeholder='Enter your email address'][class='Input__StyledInput-bysdh7-0 cghdAZ']")
        user_name.send_keys(os.getenv("REGISTER_EMAIL"))

        user_password = self.driver.find_element(By.CSS_SELECTOR, "input[type='password'][name='password'][placeholder='Enter your password'][class='Input__StyledInput-bysdh7-0 cghdAZ']")
        user_password.send_keys(os.getenv("PASSWORD"))

        
    def getArtWorkName(self) -> str:
        """return the name of the artwork"""
        artwork_name = self.driver.find_element(By.CSS_SELECTOR, 'h1.Box-sc-15se88d-0.Text-sc-18gcpao-0.OfSrA.gyuZDD[font-family="sans"]').text
        return artwork_name
    
    def getEstimatePrice(self) -> float:
        """return the median price of the estimated sales price range"""
        pass

    def getMedium(self) -> str:
        """return the medium of the artwork"""
        medium = self.driver

    def getDimension(self) -> float:
        """return the dimension of the artwork"""
        pass

    def getSaleDate(self) -> datetime:
        pass

    def getAuctionHouse(self) -> str:
        """return the Auction house where the auction took place"""
        pass

    def getSaleLocation(self) -> str:
        """return the location of the auction"""
        pass

    def getSaleName(self) -> str:
        pass

    def getLot(self) -> str:
        pass
    
    def getAuctionInformation(self):
        pass

    

        



WebScrap = WebScrapy()
WebScrap.login()
WebScrap.getArtWorkName()


