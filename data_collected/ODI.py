from bs4 import BeautifulSoup as soup
import re
from urllib.request import urlopen as uReq
import csv
my_url = 'http://www.howstat.com/cricket/Statistics/Players/PlayerProgressBat_T20.asp?PlayerID=3243'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
#print(page_soup)

containers = page_soup.findAll("table",{"class":"TableLined"})

#print(soup.prettify(containers[0]))
x = containers[0].text.replace("\t","")
x= x.replace("\xa0","")

x=x.splitlines()

#print(type(x))


x = [y.strip(' ') for y in x]

while("" in x):
    x.remove("")


x.remove("Progressive")
#x.remove("No. of Innings Played = 297")
x.pop()
x.insert(0,'No.')
name='play20'
#print(x)
count = 0
for a in x:
    if '*' in a:
        x[count] = a[:-1]
    elif '-' == a:
        x[count]=0

    count = count + 1

#for a in x:
    #print(a)

boundaries = [['Fours','Sixes']]

my_url = 'http://www.howstat.com/cricket/Statistics/Players/PlayerBatGraph2.asp?PlayerID=3243&c=T20'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("area")

#print(len(containers))

date='trashline'
count = 0
for c in containers:

     
    something = str(c['title'])
    if date in something:
        count = count + 1
        continue
        
    
    something = something.replace('\t','')
    something = something.replace('\r','')
    something = something.replace('\n','')
    date = something[something.find('Date:') + 5: something.find('Runs')]

    a=something.find('Fours:')
    b=something.find('(')
    c=something.find('Sixes:')

    boundary4=something[a+6:b]

    something = something[c:]
    b=something.find('(')
    boundary6=something[6:b]

    if not boundary4:
        boundary4=0
    if not boundary6:
        boundary6=0
    boundaries.append([boundary4,boundary6])

print(count)
   
with open(name + '.csv','w',newline='') as file:
    writer = csv.writer(file)
    l = int(len(x)/11)
    print(l)
    c=0
    count = 0
    print(len(boundaries))
    for a in range(l):
        row_content =[x[c],x[c+1],x[c+2],x[c+3],x[c+4],x[c+5],x[c+6],x[c+7],x[c+8],x[c+9],x[c+10]]    

        if c<11 or 'did not bat' not in str(x[c+4]):
            row_content = row_content + boundaries[count]
            count = count + 1
        else:
            print(x[c+4])
            row_content = row_content + [0,0]
            
        writer.writerow(row_content)
        c=c+11
        

#print(x)
#print(len(x))

