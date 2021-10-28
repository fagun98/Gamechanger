from bs4 import BeautifulSoup as soup
import re
from urllib.request import urlopen as uReq
import csv

with open('Country/IND_TEST.csv','r') as file, \
    open('Country/IND_ODAY_RESULT.csv','w',newline='') as rfile:
    reader = csv.reader(file)
    y=0

    weight_A = 0.5
    weight_B = 50.0
    weight_C = 100.00
    weight_D = 200.00
    weight_E = 0.1
    weight_F = 0.01
    weight_G = 1.0
    weight_H = 25.00
    weight_I = 30.0
    weight_J = 10.0
    weight_K = 5.0
    
    writer =csv.writer(rfile)
    
    for r in reader:
        row_content=[]
        if r:
            print(len(r))
            if r[0]=='':
                continue
            row_content.append(r[0])
            row_content.append(r[3])
            row_content.append(r[4])
            if y==0:
                row_content= row_content + ['Score_batting','Score_bowling','Score_WicketKeeper','Player_id']
                y=y=1
            else:
                #print(r[5])
                inn = float(r[5])

                if inn==0:
                    inn=1.0
                matches = float(r[34])
                Nout = float(r[6])
                bat_avg = float(r[9])
                fiftys = float(r[10])
                hundreds = float(r[11])
                duck = float(r[12])
                bat_strikeRate = float(r[15])

                wickets=float(r[18])
                ball_avg=float(r[19])
                four_wickets=float(r[20])
                five_wickets=float(r[21])
                eco=float(r[22])
                ball_strikeRate=float(r[23])

                catches=float(r[24])

                wicket_keeper_catches = float(r[26])
                wicket_keeper_stumping = float(r[27])

                Score_batting = weight_A*bat_avg + weight_A*bat_strikeRate + weight_B*(fiftys/inn) + weight_C*(hundreds/inn) - weight_D*(duck/inn)
                Score_batting = Score_batting + weight_B*(Nout/inn) + weight_E*(inn)

                Score_balling = weight_G*(wickets/matches) + weight_K*(four_wickets/matches) + weight_K*(five_wickets/matches) 

                #print([ball_avg,ball_strikeRate,eco])

                if ball_avg!=0.0 and eco!=0.0 and ball_strikeRate!=0.0:
                    Score_balling = Score_balling + weight_H*(1/ball_avg) + weight_I*(1/ball_strikeRate) + weight_J*(1/eco)
                else:
                    if ball_avg!=0:
                        Score_balling = Score_balling + weight_H*(1/ball_avg)

                    if ball_strikeRate!=0:
                        Score_balling = Score_balling + weight_I*(1/ball_strikeRate)

                    if eco!=0:
                        Score_balling = Score_balling + weight_J*(1/eco)



                Score_WicketKeeper = weight_G*(wicket_keeper_catches/matches) + weight_G*(wicket_keeper_stumping/matches) + weight_F*matches

                row_content= row_content + [Score_batting,Score_balling,Score_WicketKeeper,r[33]]
            if row_content:
                writer.writerow(row_content)
    
                
