import requests
from bs4 import BeautifulSoup
import csv
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def scrape_quotes():

        url = "https://quotes.toscrape.com/"
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for bad responses
        soup = BeautifulSoup(response.content, 'html.parser')

        quotes = soup.find_all('span', class_='text')
        if not quotes:
            logging.warning("No quotes found on the page.")

        # Save quotes to CSV
        with open('quotes.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Quote"])
            for quote in quotes:
                writer.writerow([quote.get_text()])

        logging.info("Quotes successfully saved to 'quotes.csv'.")


if __name__ == "__main__":
    scrape_quotes()
