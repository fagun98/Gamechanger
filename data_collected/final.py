import csv
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import operator

with open('Country/IND_ODAY_RESULT.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = [[row[0],row[1],row[2],float(row[3]),float(row[4]),float(row[5]),row[6]] for row in reader]
    
    batsman=sorted(rows,key=operator.itemgetter(3),reverse=True)
    i=0
    x=[]
    x1=[]
    for r in batsman:
        if i>5: 
            x1=x1+[r[0]]
        else:
            x=x+[r[0]]
        i=i+1

    #print(x)
    i=0
    y=[]
    y1=[]
    for r in batsman:
        if i>5: 
            y1=y1+[r[3]]
        else:
            y=y+[r[3]]
        i=i+1

    #print(y)

    fig = go.Figure()
    fig.add_trace(go.Bar(x=x, y=y,name='best batsman', marker_color='rgb(0, 100, 0)'))
    fig.add_trace(go.Bar(x=x1, y=y1,name='batsman', marker_color='rgb(180,0, 0)'))
    fig.update_layout(
        title='Player Analysis:Batsmen (ODI)',
        xaxis_tickfont_size=14,
        yaxis=dict(
            title='Batting Score',
            titlefont_size=16,
            tickfont_size=14,
        ),
        legend=dict(
            x=0,
            y=1.0,
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)'
        ),
        barmode='group',
        bargap=0.15, # gap between bars of adjacent location coordinates.
        bargroupgap=0.1 # gap between bars of the same location coordinate.
    )
    #fig.show()
    pio.write_html(fig, file='final_batsmen.html', auto_open=False)

    balling=sorted(rows,key=operator.itemgetter(4),reverse=True)
    i=0
    x=[]
    x1=[]
    for r in balling:
        if i>5: 
            x1=x1+[r[0]]
        else:
            x=x+[r[0]]
        i=i+1

    #print(x)
    i=0
    y=[]
    y1=[]
    for r in balling:
        if i>5: 
            y1=y1+[r[4]]
        else:
            y=y+[r[4]]
        i=i+1

    #print(y)

    fig = go.Figure()
    fig.add_trace(go.Bar(x=x, y=y,name='best Bowler', marker_color='rgb(0, 100, 0)'))
    fig.add_trace(go.Bar(x=x1, y=y1,name='Bowler', marker_color='rgb(180,0, 0)'))
    fig.update_layout(
        title='Player Analysis:Bowler (ODI)',
        xaxis_tickfont_size=14,
        yaxis=dict(
            title='Bowling Score',
            titlefont_size=16,
            tickfont_size=14,
        ),
        legend=dict(
            x=0,
            y=1.0,
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)'
        ),
        barmode='group',
        bargap=0.15, # gap between bars of adjacent location coordinates.
        bargroupgap=0.1 # gap between bars of the same location coordinate.
    )
    #fig.show()
    pio.write_html(fig, file='final_balling.html', auto_open=False)

    wicket=sorted(rows,key=operator.itemgetter(5),reverse=True)
    i=0
    x=[]
    x1=[]
    for r in wicket:
        if i>5: 
            x1=x1+[r[0]]
        else:
            x=x+[r[0]]
        i=i+1

    #print(x)
    i=0
    y=[]
    y1=[]
    for r in wicket:
        if i>5: 
            y1=y1+[r[5]]
        else:
            y=y+[r[5]]
        i=i+1

    #print(y)

    fig = go.Figure()
    fig.add_trace(go.Bar(x=x, y=y,name='best Wicket Keeper', marker_color='rgb(0, 100, 0)'))
    fig.add_trace(go.Bar(x=x1, y=y1,name='Wicket Keeper', marker_color='rgb(180,0, 0)'))
    fig.update_layout(
        title='Player Analysis:Wicket Keeper (ODI)',
        xaxis_tickfont_size=14,
        yaxis=dict(
            title='Wicket Keeping Score',
            titlefont_size=16,
            tickfont_size=14,
        ),
        legend=dict(
            x=0,
            y=1.0,
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)'
        ),
        barmode='group',
        bargap=0.15, # gap between bars of adjacent location coordinates.
        bargroupgap=0.1 # gap between bars of the same location coordinate.
    )
    #fig.show()
    pio.write_html(fig, file='final_wicketkeeper.html', auto_open=False)

'''
*******************

df = pd.read_csv('Country/IND_ODAY_RESULT.csv',encoding='unicode_escape')
df.head()
#print(df['Date'])
fig1 = px.bar(df,x='Full Name:',y='', hover_data=['Versus','Ground','Runs','How Dismissed'],color='Versus',title='Runs scored in Every match')
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
'''
