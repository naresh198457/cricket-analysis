import pandas as pd 
import matplotlib.pyplot as plt

# Test Data 
TestData=pd.read_csv('WholeTestData.csv')



# seperating 
MenTeam=['Australia','England','South Africa','New Zealand','West Indies','India',
 'Pakistan','Sri Lanka','Zimbabwe','Bangladesh','Ireland','Afghanistan']

MenTestData=pd.DataFrame(columns=['No','Date','Team1','Team2','Toss_winner','Result','Ground'])
for team in MenTeam:
    Menteam=TestData.loc[TestData['Team1'].str.contains(team)]
    MenTestData=pd.concat([MenTestData,Menteam],ignore_index=True)
MenTestData['Year']=pd.DatetimeIndex(MenTestData['Date']).year

WomenTestData=TestData.loc[TestData['Team1'].str.contains('Women')]
Under19TestData=TestData.loc[TestData['Team1'].str.contains('Under-19')]

Years=sorted(pd.unique(pd.DatetimeIndex(MenTestData['Date']).year))

TestYearData=pd.DataFrame(columns=['Year','No of Matches','Win','Draw','Cancel','Innings'])
TestYearData['Year']=Years

count=0
for Year in TestYearData['Year']:
    # No of matches played in that year
    Year_Matches=MenTestData[MenTestData['Year']==Year]
    TestYearData['No of Matches'][count]=Year_Matches.shape[0]
    

    # No of win, draw and cancelled games in that year
    Win_game=Year_Matches.loc[Year_Matches['Result'].str.contains('won')].shape[0]
    Draw_game=Year_Matches.loc[Year_Matches['Result'].str.contains('drawn')].shape[0]
    Cancel_game=Year_Matches.shape[0]-Win_game-Draw_game
    
    # No of inn win games
    Inn=Year_Matches.loc[Year_Matches['Result'].str.contains('innings')].shape[0]

    TestYearData['Win'][count]=Win_game
    TestYearData['Draw'][count]=Draw_game
    TestYearData['Cancel'][count]=Cancel_game
    TestYearData['Innings'][count]=Inn

    count=count+1

print(TestYearData)

TestYearData.to_csv('Test_Year_Data.csv', index = False)