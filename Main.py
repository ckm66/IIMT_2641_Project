from WebScrapyEngine import WebScrapy

def main():
    WebEngine = WebScrapy()
    WebEngine.login()
    auction_record, invalid_flag = WebEngine.createAuctionRecord("kk")
    WebEngine.insertToMongoDB(auction_record, invalid_flag)

if __name__ == "__main__":
    main()