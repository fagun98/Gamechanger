from bs4 import BeautifulSoup as soup
import re
from urllib.request import urlopen as uReq
import csv

my_url = 'http://www.howstat.com/cricket/Statistics/Players/PlayerDismissBowlGraph.asp?PlayerID=3243&c=ODI'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

#print(page_soup)

containers = page_soup.find("table",{"class":"BorderedBoxGraph"})

context = str(containers)

context = '<div align="center"> <h1>How Wickets Obtained</h1>' + context + '</div>'

my_url = 'http://www.howstat.com/cricket/Statistics/Players/PlayerWicketAnalysisGraph.asp?PlayerID=3243&c=ODI'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

#print(page_soup)

containers = page_soup.find("table",{"class":"BorderedBoxGraph"})

context = context + '<div align="center"> <h1>Wickets by batting order</h1>' + str(containers) + '</div>'


f = open('Country/something3.html','w')


f.write(context)

f.close()    

'''
containers = page_soup.findAll("area")
#print(containers[:10])

#print(len(containers))
something = str(containers[0]['title'])

#print(something)

something = str(containers[0]['title'])
something = something.replace('\t','')
something = something.replace('\r','')
something = something.replace('\n','')
#something = something.split(' ')

print(something)
print(something.find('Date:'))
date = something[something.find('Date:') + 5: something.find('Runs')]
##print(something.find('Runs'))
#print(something.find('Versus:'))
a=something.find('Fours:')
b=something.find('(')
c=something.find('Sixes:')
print(something[a+6:b])
something = something[c:]
b=something.find('(')
print(something[6:b])
print(date)

#for c in containers:
#    c = str(c)
#    print(c)

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
'''
  
