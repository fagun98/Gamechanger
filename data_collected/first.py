from bs4 import BeautifulSoup as soup
import re
from urllib.request import urlopen as uReq
import csv

c=input("Enter the Country: ")
my_url = 'http://www.howstat.com/cricket/Statistics/Players/PlayerCountryList.asp?Country='+c
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
#print(page_soup)

containers = page_soup.findAll("a",{"class":"LinkNormal"})

y=len(containers)
#print(y)
fi=[]
for x in range(y):
    containers[x]=str(containers[x])
    if(containers[x].find('*')!=-1):
        fi.append(containers[x])


res=[]
for x in range(len(fi)):
    temp = re.findall(r'\d+', fi[x]) 
    res=res+temp

with open('Country/' + c + '.csv','w') as file:
    writer = csv.writer(file)
    for a in range(len(res)):
        writer.writerow([res[a]])

  
