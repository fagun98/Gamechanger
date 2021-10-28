from bs4 import BeautifulSoup as soup
import re
from urllib.request import urlopen as uReq
import csv
import operator
import pandas 


with open('Country/IND_ODAY_RESULT.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = [[row[0],row[1],row[2],float(row[3]),float(row[4]),float(row[5]),row[6]] for row in reader]
    final_team=[]
    
    final_team = final_team + sorted(rows,key=operator.itemgetter(5),reverse=True)[:1]

    y=0
    for row in sorted(rows,key=operator.itemgetter(3),reverse=True):
        if row not in final_team:
           final_team.append(row)
           y=y+1
           
        if y==5:
            break
    
    y=0
    spinner = 2
    pacer = 3
    for row in sorted(rows,key=operator.itemgetter(4),reverse=True):
        if row not in final_team:
            if 'Medium' in row[2] or 'Fast' in row[2] and pacer>0:
               final_team.append(row)
               pacer = pacer - 1
            else:
               if 'Does Not Bowl' not in row[2] and spinner >0:
                   final_team.append(row)
                   spinner = spinner - 1
        if spinner == 0 and pacer == 0:
            break
                 
    
    for f in final_team:
        print(f[0])
