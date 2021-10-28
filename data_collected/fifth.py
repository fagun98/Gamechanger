from bs4 import BeautifulSoup as soup
import re
from urllib.request import urlopen as uReq
import csv
import pandas as pd
import plotly.express as px

df = pd.read_csv('Country/play.csv',encoding= 'unicode_escape')
df.head()

fig = px.bar(df, x = 'Date', y = 'Runs', hover_data=['Versus', 'Ground','Runs','How Dismissed'],color='Versus',title='blah blah')
fig.show()

#fig = px.bar(data_canada, x='y', y='pop')
#fig.show()



'''
fig = px.pie(df, values='How Dismissed', names='Versus',title='Blah blah')
fig.show()

with open('Country/play.csv','r') as file:
    reader = csv.reader(file)
    y=0
    ch=chr(8224)
    
    caught = 0
    caught_behind = 0
    for r in reader:
        dismissed = r[4]
        if dismissed[0]=='c':
            if ch in dismissed:
                caught_behind = caught_behind + 1
            else:
                caught = caught + 1


    print(caught)
    print(caught_behind)

'''

    

    
    
