import pandas as pd
import matplotlib.pyplot as plt

# ODI Data 
WholeData=pd.read_csv('WholeODIData.csv')

MenTeams=['Australia','New Zealand','Pakistan','West Indies','India',
'Sri Lanka','Zimbabwe','South Africa','Bangladesh','Kenya','England',
'Namibia','Ireland','Scotland','Netherlands','Canada','Afghanistan',
'Hong Kong','Papua New Guinea','Nepal','United States of America']

# seperating the data 
MenODIData=pd.DataFrame(columns=['No','Date','Team1','Team2','Toss_winner','Result','Ground'])
for team in MenTeams:
    Menteam=WholeData.loc[WholeData['Team1'].str.contains(team)]
    MenODIData=pd.concat([MenODIData,Menteam],ignore_index=True)
MenODIData['Year']=pd.DatetimeIndex(MenODIData['Date']).year

# covert the date into year information 
Years=sorted(pd.unique(pd.DatetimeIndex(MenODIData['Date']).year))
NoofMatches=[MenODIData[MenODIData['Year']==year].shape[0] for year in Years]

ODIYearData=pd.DataFrame(columns=['Year','No of Matches'])
ODIYearData['Year']=Years
ODIYearData['No of Matches']=NoofMatches

ODIYearData.to_csv('ODI_Year_Data.csv', index = False)