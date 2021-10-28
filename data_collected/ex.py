from bs4 import BeautifulSoup as soup
import re
from urllib.request import urlopen as uReq
import csv

with open('Country/IND_ODAY.csv','r') as file:
    reade = csv.reader(file)
    for row in reade:
        if row:
            print(row)

