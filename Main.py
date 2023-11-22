from WebScrapyEngine import WebScrapy

def startDriver():
    WebEngine = WebScrapy()
    WebEngine.login()
    for index in range(4000103, 5000000):
        fail_to_reach = WebEngine.goto(url = f"https://www.artsy.net/auction-result/{index}")
        if fail_to_reach:
            continue
        auction_record, invalid_flag = WebEngine.createAuctionRecord()
        WebEngine.insertToMongoDB(auction_record, invalid_flag)

def main():
    startDriver()

if __name__ == "__main__":
    main()