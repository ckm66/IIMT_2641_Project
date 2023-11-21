from datetime import datetime
import json

class AuctionRecord: 

    def __init__(self, artwork_name: str, artist: str, information_list: str) -> object:
        self.information_list = information_list
        self.artwork_name = artwork_name # The name of the artwork.
        self.artist = artist
        self.pre_sale_estimate = 0  # The median price of the estimated sale price range.
        self.sale_price = 0  # The actual auction/sale price of the artwork.
        self.medium = "" # The type of medium to which the artwork belongs.
        self.dimensions = 0  # The dimensions of the artwork.
        self.sales_date = datetime.now() # The date on which the auction took place for the artwork.
        self.auction_house = "" # The name of the auction house where the artwork was sold.
        self.sale_location = "" # The location where the auction took place.
        self.sale_name = "" # The name or title associated with the sale event.
        self.lot = "" # The lot number assigned to the artwork in the auction.
        self.url = "" # The URL or web link associated with the artwork or auction.
        self.fail_flag = False
    
    def getEstimatePrice(self) -> int:
        """return the median price of the estimated sales price range"""
        self.pre_sale_estimate = self.information_list[0].text
        

    def getMedium(self) -> str:
        """return the medium of the artwork"""
        self.medium = self.information_list[1].text


    def getDimension(self) -> int:
        """return the dimension of the artwork"""
        self.dimensions = self.information_list[2].text

    def getSaleDate(self) -> datetime:
        """retunr the saledate of this artwork"""
        try:
            self.sales_date = datetime.strptime("self.information_list[3].text", "%b %d, %Y")
        except:
            self.sales_date =  None
            self.fail_flag = True

    def getAuctionHouse(self) -> str:
        """return the Auction house where the auction took place"""
        self.auction_house = self.information_list[4].text

    def getSaleLocation(self) -> str:
        """return the location of the auction"""
        self.sale_location = self.information_list[5].text  

    def getSaleName(self) -> str:
        self.sale_name = self.information_list[6].text

    def getLot(self) -> str:
        self.lot = self.information_list[7].text

    def transform(self):
        self.getEstimatePrice()
        self.getMedium()
        self.getDimension()
        self.getSaleDate()
        self.getAuctionHouse()
        self.getSaleLocation()
        self.getSaleName()
        self.getLot()
        del self.information_list
    



    
