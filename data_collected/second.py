from bs4 import BeautifulSoup as soup
import re
from urllib.request import urlopen as uReq
import csv
import os.path
from os import path
'''
with open('Country/IND.csv','r') as file:
    reade = csv.reader(file)
    for row in reade:
        if len(row)!=0:
            print(row[0])
'''
def File_Collection(player_id):    
    my_url = 'http://www.howstat.com/cricket/Statistics/Players/PlayerOverviewSummary.asp?PlayerID=' + player_id
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    #print(page_soup.get_text())
    x=page_soup.get_text().replace("\t","")
    x=x.replace("\xa0","")

    x=x.splitlines()

    #print(type(x))


    x = [y.strip(' ') for y in x]

    while("" in x):
        x.remove("")

    x=x[3:]
    x=x[:-47]

    Test = False
    ODI = False
    T20 = False
    IPL = False


    #print(x)

    DEL = ['Detailed Test Profile & Statistics','Detailed ODI Profile & Statistics','Detailed T20 Profile & Statistics','Detailed IPL Profile & Statistics']
    MATCHES = []
    y=0
    z=0

    for d in DEL:
        try:
            y=y+1
            ind = x.index(d)
            x.pop(ind)
            if(y==1):
                Test=True
            elif(y==2):
                ODI=True
            elif(y==3):
                T20=True
            else:
                IPL=True
        except ValueError:
             z=z+1

    y=y-z
    z=0
    #print(x)

    while(z<y):
        x.pop(10)
        MATCHES.append(x[10])
        x.pop(10)
        x.pop(10)
        x.remove('Batting')
        x.remove('Bowling')
        x.remove('Wicket Keeping')
        x.remove('Fielding')
        x.remove('Captaincy')
        z=z+1
    z=0
    for m in MATCHES:
        m=m.translate({ord('('):None})
        MATCHES[z]=int(m)
        z=z+1
    
    #print(MATCHES)

    if Test==True:
        if(x[45]=='Best - Match:'):
            x.pop(44)
            x.pop(44)
        else:
            x.pop(44)
            x.pop(44)
            x.pop(44)
            x.pop(44)
        ind = x.index('Most Catches in Match:')
        if x[ind + 1] == 'Catches:':
            x.pop(ind)
            x.pop(ind)
        else:
            x.pop(ind)

    z=1
    while(z<y):
        rem = x.index('Best:') + 1
        if(x[rem] != 'Economy Rate:'):
            x.pop(rem)
        x.remove('Best:')
        z=z+1

    y1=11
    while y1<len(x):
        
        if(x[y1] == 'N/A'):
            x[y1]=0
        elif(x[y1-1] == 'Won/Lost:'):
            if(x[y1] == 'Innings:'):
                x.insert(y1,0)
            else:
                a=0
                b=0
                c=0
                z1=x[y1]
                while c<len(z1):
                    try:
                        a=a*10
                        a= a + int(z1[c])
                    except ValueError:
                        b=a/10
                        a=0
                    c=c+1
                if a==0:
                    a=1
                x[y1]=round(b/a,2)
                        
        else:
            try:
                x[y1]=float(x[y1])
            except ValueError:
                if(x[y1].find('*')==-1):
                    x.insert(y1,0)

        y1=y1+2

    #print(x)
    
    if(Test == True):
        y=0
        row_content=[]

        if not path.isfile('Country/IND_TEST.csv'):
            while y<67:
                row_content.append(x[y])
                y=y+2
            row_content.append('Matches')
            with open('Country/IND_TEST.csv','w',newline='') as file:
                writer = csv.writer(file)
                writer.writerow(row_content)
                row_content=[]
                y=0
                while y<67:
                    row_content.append(x[y+1])
                    y=y+2
                row_content.append(MATCHES[0])
                writer.writerow(row_content)
                file.close()

            del x[10:68]
            MATCHES.pop(0)
            
        else:
            
            while y<67:
                row_content.append(x[y+1])
                y=y+2

            row_content.append(MATCHES[0])
             #print(row_content)
            MATCHES.pop(0)
            del x[10:68]

            with open('Country/IND_TEST.csv','a',newline='') as file:
                writer = csv.writer(file)
                writer.writerow(row_content)
                file.close()
            


    if(ODI == True):
        y=0
        row_content=[]
        if not path.isfile('Country/IND_ODAY.csv'):
            while y<62:
                row_content.append(x[y])
                y=y+2
                
            row_content.append('Matches')
            with open('Country/IND_ODAY.csv','w',newline='') as file:
                writer = csv.writer(file)
                writer.writerow(row_content)
                y=0
                row_content=[]
                while y<62:
                    row_content.append(x[y+1])
                    y=y+2
                row_content.append(MATCHES[0])
                writer.writerow(row_content)
                file.close()
            del x[10:62]
            MATCHES.pop(0)
            
        else:
            while y<62:
                row_content.append(x[y+1])
                y=y+2
            row_content.append(MATCHES[0])
             #print(row_content)
            MATCHES.pop(0)
            del x[10:62]

            with open('Country/IND_ODAY.csv','a',newline='') as file:
                writer = csv.writer(file)
                writer.writerow(row_content)
                file.close()   

    if(T20 == True):
        y=0
        row_content=[]
        if not path.isfile('Country/IND_T20.csv'):
            while y<62:
                row_content.append(x[y])
                y=y+2
                
            row_content.append('Matches')
            with open('Country/IND_T20.csv','w',newline='') as file:
                writer = csv.writer(file)
                writer.writerow(row_content)
                y=0
                row_content=[]
                while y<62:
                    row_content.append(x[y+1])
                    y=y+2
                row_content.append(MATCHES[0])
                writer.writerow(row_content)
                file.close()
            del x[10:62]
            MATCHES.pop(0)
            
        else:
            while y<62:
                row_content.append(x[y+1])
                y=y+2
            row_content.append(MATCHES[0])
             #print(row_content)
            MATCHES.pop(0)
            del x[10:62]

            with open('Country/IND_T20.csv','a',newline='') as file:
                writer = csv.writer(file)
                writer.writerow(row_content)
                file.close()
           
            
#print(x)    

with open('Country/IND.csv','r') as file:
    reader = csv.reader(file)
    for r in reader:
        if r:
            File_Collection(r[0])


#File_Collection('3600')
