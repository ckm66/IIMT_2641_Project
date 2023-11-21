from datetime import datetime
import json
import math
import re

class AuctionRecord: 

    def __init__(self, artwork_name: str, artist: str, sale_price: str, tag_price, information_list: str) -> object:
        self.information_list = information_list
        self.artwork_name = artwork_name # The name of the artwork.
        self.artist = artist
        self.tag_price = tag_price
        self.sale_price = sale_price  # The actual auction/sale price of the artwork.
        self.pre_sale_estimate = None  # The median price of the estimated sale price range.
        self.percentage_difference = None
        self.medium = None # The type of medium to which the artwork belongs.
        self.dimensions = None  # The dimensions of the artwork.
        self.size = None # The size group that the artwork belongs to (Self defined)
        self.sales_date = None # The date on which the auction took place for the artwork.
        self.auction_house = None # The name of the auction house where the artwork was sold.
        self.sale_location = None # The location where the auction took place.
        self.sale_name = None # The name or title associated with the sale event.
        self.lot = None # The lot number assigned to the artwork in the auction.
        self.url = None # The URL or web link associated with the artwork or auction.
        self.fail_flag = False
    
    def isNull(self, data) -> bool:
        """This function check if the data is not availiable"""
        if data == "----":
            self.fail_flag = True
            return True
        return False
    
    def getSalePrice(self) -> int: 
        """This function find the auction price of the artwork"""
        # If sales price is not avaliable -> Null
        if not any(char.isdigit() for char in self.sale_price):
            self.fail_flag = True
            return
        
        if self.sale_price[:2] == "US":
            self.sale_price = int(''.join(filter(str.isdigit, self.sale_price)))
            return


    def getEstimatePrice(self) -> None:
        """This function find the median price of the estimated auction price range"""
        # If estimated price is not availiable -> Return
        if self.isNull(self.information_list[0]) or (not any(char.isdigit() for char in self.information_list[0])) or type(self.sale_price ) == str:
            return
        
        # If the estimate price is written in US Dollar -> Find Upper and Lower Limit -> Add both and divide by two
        if self.information_list[0][:2] == "US":
            price_range = self.information_list[0].split("US$")
            lower_limit = price_range[1][:-1].replace(",", "")
            upper_limit = price_range[2].replace(",", "")
            exchange_rate = 1
        
        # For estimate price is stated in other currency
        else:
            currency_symbol = ""
            for char in self.information_list[0]: # Example String = YEN100-YEN200; This will be convert to 100-200 with currency symbol = YEN
                if (char.isdigit()):
                    break
                currency_symbol += char
            print(currency_symbol)

            price_range = self.information_list[0].split(currency_symbol)
            lower_limit = price_range[1][:-1].replace(",", "")
            upper_limit = price_range[2].replace(",", "")

            tag_price = self.tag_price.split(currency_symbol)[1].replace(",", "")
            exchange_rate = self.sale_price / int(tag_price)
            print(exchange_rate)

        self.pre_sale_estimate = ((int(lower_limit) + int(upper_limit)) / 2) * exchange_rate
        return
    
    def getPercentage(self):
        """This function finds the percentage increase or decrease comparing to median sale price"""
        if (self.sale_price == None or self.pre_sale_estimate == None):
            return
        difference = self.sale_price - self.pre_sale_estimate
        self.percentage_difference = (difference / self.pre_sale_estimate)



    def getMedium(self) -> str:
        """This function finds the medium of the artwork"""
        if (self.isNull(self.information_list[1])):
            self.medium = None
            return
        self.medium = self.information_list[1]

    def getDimension(self) -> int:
        """This function finds the dimension of the artwork. (Remark: String)"""
        if (self.isNull(self.information_list[2])):
            self.dimensions = None
            return
        self.dimensions = self.information_list[2]

    def getSize(self) -> None:
        """This function will class the size of the artwork"""
        if (self.dimensions == None):
            return

        pattern_1 = r"^\d+(\.\d+)? x \d+(\.\d+)? cm$" # 30 x 40 cm
        
        if (re.match(pattern_1, self.dimensions) is not None):  
            values = self.dimensions.split(" x ")
            variable1 = float(values[0])
            variable2 = float(values[1].split(" ")[0])

            if (variable1 > 100 or variable2 > 100):
                self.size = "Large"
            
            elif (variable1 > 40 or variable2 > 40):
                self.size = "Medium"
            
            else:
                self.size = "Small"
            return
        
        pattern_2 = r"^\d+(\.\d+)? cm$"
        if (re.match(pattern_2, self.dimensions) is not None):
            value = self.dimensions[:-4]

            if (value > 100 or value > 100):
                self.size = "Large"
            
            elif (value > 40 or value > 40):
                self.size = "Medium"
            
            else:
                self.size = "Small"
            return
        
        self.fail_flag = True


    def getSaleDate(self) -> datetime:
        """This function will get the sale date of the artwork"""
        # Check if the sale date is availiable 
        try:
            self.sales_date = datetime.strptime(self.information_list[3], "%b %d, %Y")
        except:
            self.sales_date =  None
            self.fail_flag = True

    def inflation_adjustment(self):
        """This function will adjust sale price and pre-sale estimate according to inflation"""
        if (self.sale_price == None or self.pre_sale_estimate == None):
            return
        inflation_rate = 1.032
        number_of_year = datetime.now().year - self.sales_date.year 
        self.pre_sale_estimate *= math.pow(inflation_rate, number_of_year)
        self.sale_price *= math.pow(inflation_rate, number_of_year)

    def getAuctionHouse(self) -> str:
        """This function finds the auction house that auction happen"""
        if (self.isNull(self.information_list[4])):
            self.auction_house = None
            return
        self.auction_house = self.information_list[4]

    def getSaleLocation(self) -> str:
        """This function will finds where the auction happen"""
        if (self.isNull(self.information_list[5])):
            self.sale_location = None
            return 
        
        self.sale_location = self.information_list[5]  

    def getSaleName(self) -> str:
        """This function finds that sales name of the auction"""
        if (self.isNull(self.information_list[6])):
            self.sale_name = None
            return
        self.sale_name = self.information_list[6]

    def getLot(self) -> str:
        """This function finds the lot of the auction"""
        if (self.isNull(self.information_list[7])):
            self.lot = None
            return
        self.lot = self.information_list[7]

    def transform(self):
        self.getSalePrice()
        self.getEstimatePrice()
        self.getPercentage()
        self.getMedium()
        self.getDimension()
        self.getSize()
        self.getSaleDate()
        self.inflation_adjustment()
        self.getAuctionHouse()
        self.getSaleLocation()
        self.getSaleName()
        self.getLot()
        del self.information_list
        del self.tag_price
    



    
