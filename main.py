import time
import scraper

if __name__ == "__main__":
    print("Welcome to Dan's Web Scraper!")
    time.sleep(1)
    print("This tool is in development and may not work.")
    time.sleep(1)
    print("Please enter the url you would like to scrape.")
    url = input()
    print("Now scraping...")
    scraper.scraper(url)