import pandas as pd
import matplotlib.pyplot as plt

WholeData=pd.read_csv('WholeT20IData.csv')
Team=['England','New Zealand','South Africa','Australia',
'Bangladesh','India','West Indies', 'Pakistan', 'Sri Lanka',
'Zimbabwe','Namibia','Kenya','Ireland' 'Netherlands','Canada',
'Afghanistan', 'Scotland','Hong Kong','United Arab Emirates',
'Oman','Spain','Germany',  'Belgium','Guernsey','Malaysia',
'Maldives','Qatar','Denmark','Finland','Nepal','Malawi',
'Bulgaria','Romania','Malta','Rwanda','Cyprus', 
'Papua New Guinea','Nigeria','United States of America',
'Cayman Islands','Austria','Luxembourg']

MenData=pd.DataFrame(columns=['No','Date','Team1','Team2','Toss_winner','Result','Ground'])
for team in Team: 
    MenData=pd.concat([MenData,WholeData.loc[WholeData['Team1'].str.contains(team)]])
MenData['Year']=pd.DatetimeIndex(MenData['Date']).year

# convert the date to year 
Years=sorted(pd.unique(pd.DatetimeIndex(MenData['Date']).year))
NoofMatches=[MenData.loc[MenData['Year']==year].shape[0] for year in Years]

T20IYearData=pd.DataFrame(columns=['Year','No of Matches'])
T20IYearData['Year']=Years
T20IYearData['No of Matches']=NoofMatches

print(T20IYearData.columns)

T20IYearData.to_csv('T20I_Year_Data.csv', index = False)

plt.plot(Years,NoofMatches,'ok')
plt.show()