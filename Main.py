from WebScrapyEngine import WebScrapy

def getAuctionRecord(index):
    WebEngine = WebScrapy()
    WebEngine.login()
    WebEngine.goto(url = f"https://www.artsy.net/auction-result/{index}")
    auction_record, invalid_flag = WebEngine.createAuctionRecord()
    WebEngine.insertToMongoDB(auction_record, invalid_flag)

def main():
    getAuctionRecord(6997635)

if __name__ == "__main__":
    main()