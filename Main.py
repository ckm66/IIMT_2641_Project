from WebScrapyEngine import WebScrapy

def main():
    WebEngine = WebScrapy()
    WebEngine.login()
    auction_record = WebEngine.createAuctionRecord("kk")
    WebEngine.insertToMongoDB(auction_record)

    pass

if __name__ == "__main__":
    main()