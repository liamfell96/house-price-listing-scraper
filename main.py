import requests
import bs4


url = "https://www.zoopla.co.uk/for-sale/details/59925805/?search_identifier=c49910f3f968999ca250e3b410e51602"


def test_scrape():
    source = requests.get(url).text
    return

test_scrape()
