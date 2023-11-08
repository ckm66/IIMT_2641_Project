import datetime
import json

class AuctionRecord: 

    def __init__(self, artwork_name: str, pre_sale_estimate: float, sale_price: float, medium: str, dimensions: float, sales_date: datetime, auction_house: str, sale_location: str, sale_name: str, lot: str, url: str) -> object:
        """
        The constructor for the AuctionRecord class. \n
        Parameters: 
        artwork_name (str): The name of the artwork.
        pre_sale_estimate (float): The median price of the estimated sale price range.
        sale_price (float): The actual auction/sale price of the artwork.
        medium (str): The type of medium to which the artwork belongs.
        dimensions (float): The dimensions of the artwork.
        sales_date (datetime): The date on which the auction took place for the artwork.
        auction_house (str): The name of the auction house where the artwork was sold.
        sale_location (str): The location where the auction took place.
        sale_name (str): The name or title associated with the sale event.
        lot (str): The lot number assigned to the artwork in the auction.
        url (str): The URL or web link associated with the artwork or auction. \n
        Return: 
        AuctionRecord (Object)
        """
        self.artwork_name = artwork_name
        self.pre_sale_estimate = pre_sale_estimate
        self.sale_price = sale_price
        self.medium = medium
        self.dimensions = dimensions
        self.sales_date = sales_date
        self.auction_house = auction_house
        self.sale_location = sale_location
        self.sale_name = sale_name
        self.lot = lot
        self.url = url

    def to_Document(self):
        """Return a json instant of the object"""
        return json.dumps(self.__dict__)
    



    
