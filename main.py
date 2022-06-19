import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


url = "https://www.zoopla.co.uk/for-sale/details/59925805/?search_identifier=c49910f3f968999ca250e3b410e51602"


def test_scrape():
    driver = webdriver.Chrome(r'C:\Users\liamh\chromedriver_win32\chromedriver.exe')
    driver.get("https://www.zoopla.co.uk/for-sale/details/59925805/?search_identifier=c49910f3f968999ca250e3b410e51602")
    buttons = driver.find_elements(By.TAG_NAME, value="button")
    for button in buttons:
        if button.text == 'Listing history':
            # QUESTION WHY CAN'T i CLICK ON THIS BUTTON???
            button.click()


    driver.quit()

    source = requests.get(url).text

    # # create soup
    # soup = BeautifulSoup(source, 'html.parser')
    # #buttons = soup.findAll('button', 'eksxv420 css-1u1w17g e15i67y70', 'listinghistory-button')
    #
    # buttons = soup.findAll('eksxv420')

    for button in buttons:
        print(button)

    #print(soup.prettify())


    # select listing history
    #first_a_tag = soup.find('a')
    # print(type(first_a_tag))
    # print(first_a_tag.string)

    #listing_history = soup.find_all(id="listing-summary-details-heading")
    #print(listing_history)


    #for link in test_class:
        #print(link.get('href'))
    #print(test_class)




   #class ="c-hofHGG c-hofHGG-glLAqQ-size-large" > Listing History < / h2 >

    #listing_history = soup.select("html.js body div#__next main#main-content.css-6pnluy.e1xakb0y0 div.css-13y8wrb.e1xakb0y1 section.css-1leje2n.ercscmf0 h2#listing-more-information-heading.css-bxxvoc-Heading2.e1s8jdjv4")
    #print(listing_history)
    return

test_scrape()
