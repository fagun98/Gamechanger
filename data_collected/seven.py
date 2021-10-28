from bs4 import BeautifulSoup as soup
import re
from urllib.request import urlopen as uReq
import csv
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio


df = pd.read_csv('Country/play.csv',encoding='unicode_escape')
df.head()
#print(df['Date'])
fig1 = px.bar(df,x='Date',y='Runs', hover_data=['Versus','Ground','Runs','How Dismissed'],color='Versus',title='Runs scored in Every match')
#fig1.show()



x = df['Date'] 

y_fours = 4*df['Fours']
y_Sixes = 6*df['Sixes']
y_Runs = df['Runs'] - y_fours - y_Sixes

fig = go.Figure()
fig.add_trace(go.Bar(x=x, y= y_fours,name='fours'))
fig.add_trace(go.Bar(x=x, y= y_Sixes,name='sixes')) 
fig.add_trace(go.Bar(x=x, y=y_Runs,name='others'))
fig.add_trace(go.Scatter(x=x, y=df['Avg'] ,name='Average'))


fig.update_layout(barmode='relative', title_text='Relative Barmode')
fig.show()

caught = 0
caught_behind = 0
lbw = 0
run_out=0
stummed = 0
bowled = 0
hit_wicket=0

with open('Country/play.csv','r') as file:
    reader = csv.reader(file)
    y=0
    ch=chr(8224)
    
    for r in reader:
        dismissed = r[5]
        if dismissed[0]=='c':
            if ch in dismissed:
                caught_behind = caught_behind + 1
            else:
                caught = caught + 1

        elif 'lbw' in dismissed:
            lbw = lbw + 1
        elif 'run out' in  dismissed:
            run_out = run_out + 1
        elif dismissed[:2]=='st':
            stummed = stummed + 1
        elif 'hit wicket' in dismissed:
            hit_wicket = hit_wicket+1
        elif dismissed[0]=='b':
            bowled = bowled + 1
    

    #print(caught)
    #print(caught_behind)
    #print(lbw)
    #print(run_out)
    #print(stummed)
    #print(bowled)
    #print(hit_wicket)

fig2 = px.pie(values=[caught,caught_behind,lbw,run_out,stummed,bowled,hit_wicket],names=['caught','caughtbehind','lbw','run out','stummed','bowled','hit wicket'],title='How dismissed')
pio.write_html(fig2, file='index.html', auto_open=False)
pio.write_html(fig3, file='index.html', auto_open=False)
pio.write_html(fig, file='index.html', auto_open=True)
#fig.show()
