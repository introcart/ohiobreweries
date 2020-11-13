import requests
from bs4 import BeautifulSoup
import csv

page_2 = "https://www.brewerydb.com/browse/regional/index/locality//region/ohio/countryIsoCode/US/page/2"
pages = 7
def get_links(not_home, pages)
    for page in range(2,pages+1)
        webpage_response = requests.get(f"https://www.brewerydb.com/browse/regional/index/locality//region/ohio/countryIsoCode/US/page/{page}")
    webpage += webpage_response.content
    soup += BeautifulSoup(webpage, "html.parser")
    return soup.find_all("a")
    









