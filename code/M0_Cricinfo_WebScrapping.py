from espncricinfo.summary import Summary
from espncricinfo.match import Match
import pandas as pd
pd.options.mode.chained_assignment = None
import os

# creat
TestData=pd.DataFrame(columns=['No','Date','Team1','Team2','Toss_winner','Result','Ground'])
ODIData=pd.DataFrame(columns=['No','Date','Team1','Team2','Toss_winner','Result','Ground'])
T20IData=pd.DataFrame(columns=['No','Date','Team1','Team2','Toss_winner','Result','Ground'])
Test_count=0

for id in range(62396,1578787,1):
    FileName=str(id)+'.csv'

    TestPath='C:/Users/ezzns5/Dropbox/DataScientist/Cricket/Histrory_to_T20VsTestMatchAnalysis/Data/Test'
    ODIPath='C:/Users/ezzns5/Dropbox/DataScientist/Cricket/Histrory_to_T20VsTestMatchAnalysis/Data/ODI'
    T20IPath='C:/Users/ezzns5/Dropbox/DataScientist/Cricket/Histrory_to_T20VsTestMatchAnalysis/Data/T20I'

    try:
        m=Match(str(id))
        Des=m.description

        # collecting the team in
        Team1=m.team_1['team_name']
        Team1_id=m.team_1['team_id']
        Team2=m.team_2['team_name']
        Team2_id=m.team_2['team_id']
        team_df=pd.DataFrame([[Team1,Team1_id],[Team2,Team2_id]],columns=['Country','No'])

        # convert the number to team name
        TossWinner=team_df.loc[team_df['No']==m.toss_winner,'Country'].values[0]
        
        # Converting results to information
        Result=m.result
        Date=m.date
        Ground=m.ground_name       

        if 'Test' in Des:

            # replacing the team no with the names
            df1=pd.DataFrame(m.innings)
            for i in range(0,len(m.innings),1):
                df1['batting_team_id'][i]=team_df.loc[team_df['No']==str(df1['batting_team_id'][i]),'Country'].values[0]
                df1['bowling_team_id'][i]=team_df.loc[team_df['No']==str(df1['bowling_team_id'][i]),'Country'].values[0]

            # save the file of the inn data into csv
            TestFile=os.path.join(TestPath,FileName)
            df1.to_csv(TestFile)

            # save the information of the whole data
            d1=[[id,Date,Team1,Team2,TossWinner,Result,Ground]]
            T1=pd.DataFrame(d1,columns=['No','Date','Team1','Team2','Toss_winner','Result','Ground'])
            TestData=pd.concat([TestData,T1])

            print(id,' Test match data saved')

        elif 'ODI' in Des:
            # replacing the team no with the names
            df1=pd.DataFrame(m.innings)
            for i in range(0,len(m.innings),1):
                df1['batting_team_id'][i]=team_df.loc[team_df['No']==str(df1['batting_team_id'][i]),'Country'].values[0]
                df1['bowling_team_id'][i]=team_df.loc[team_df['No']==str(df1['bowling_team_id'][i]),'Country'].values[0]

            # save the file of the inn data into csv
            ODIFile=os.path.join(ODIPath,FileName)
            df1.to_csv(ODIFile)

            # save the information of the whole data
            d1=[[id,Date,Team1,Team2,TossWinner,Result,Ground]]
            T1=pd.DataFrame(d1,columns=['No','Date','Team1','Team2','Toss_winner','Result','Ground'])
            ODIData=pd.concat([ODIData,T1])

            print(id,' ODI match data saved')

        elif 'T20I' in Des:
            # replacing the team no with the names
            df1=pd.DataFrame(m.innings)
            for i in range(0,len(m.innings),1):
                df1['batting_team_id'][i]=team_df.loc[team_df['No']==str(df1['batting_team_id'][i]),'Country'].values[0]
                df1['bowling_team_id'][i]=team_df.loc[team_df['No']==str(df1['bowling_team_id'][i]),'Country'].values[0]

            # save the file of the inn data into csv
            T20IFile=os.path.join(T20IPath,FileName)
            df1.to_csv(T20IFile)

            # save the information of the whole data
            d1=[[id,Date,Team1,Team2,TossWinner,Result,Ground]]
            T1=pd.DataFrame(d1,columns=['No','Date','Team1','Team2','Toss_winner','Result','Ground'])
            T20IData=pd.concat([T20IData,T1])

            print(id,' T20I match data saved')

    except:
        print(id,' There is an error of reading the file')

TestData.to_csv('WholeTestData.csv')
ODIData.to_csv('WholeODIData.csv')
T20IData.to_csv('WholeT20IData.csv')