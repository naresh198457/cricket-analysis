import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

# Data history of the cricket and international cups 
HistData=pd.read_excel('Data\HistoryData.xlsx')
CupData=pd.read_csv('Data\HistoryCup.csv')

# Important dates of the cricket 
StDate=HistData['Start Date']

# international cups dates
ODICup=pd.to_datetime(CupData['ODI'],format='%d/%m/%Y')
T20Cup=pd.to_datetime(CupData['T20'].dropna(axis=0),format='%d/%m/%Y')
CTCup=pd.to_datetime(CupData['CT'].dropna(axis=0),format='%d/%m/%Y')

# ploting the data 
fig, ax = plt.subplots(figsize=(8.8, 4), constrained_layout=True)
ax.set(title="Cricket History")

levels = np.tile([8, 6, 4, 2, 4, 6],int(np.ceil(len(StDate)/6)))[:len(StDate)]
ax.vlines(StDate, 0, levels, color="tab:red")
ax.plot(StDate, np.zeros_like(StDate), "-o", color="k", markerfacecolor="w")

for d, l, r in zip(StDate, levels, HistData['Match']):
    print(d,l,r)
    ax.annotate(r, xy=(d, l),
                xytext=(3, np.sign(l)*3), textcoords="offset points",
                horizontalalignment="left",
                verticalalignment="bottom" if l > 0 else "top")

ax.xaxis.set_major_locator(mdates.MonthLocator(interval=100))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
Date1=pd.to_datetime('01/01/1950',format='%d/%m/%Y')
Date2=pd.to_datetime('01/01/2022',format='%d/%m/%Y')

#ax.set_xlim([Date1,Date2])
plt.setp(ax.get_xticklabels(), rotation=30, ha="right")

# remove y axis and spines
ax.yaxis.set_visible(False)
ax.spines[["left", "top", "right"]].set_visible(False)

ax.margins(y=0.1)

ax.plot(ODICup,np.zeros_like(ODICup),'-o',color='k',markerfacecolor='k')
ax.vlines(ODICup,0,1,color="k",label='ODI World Cup')

ax.plot(T20Cup,np.zeros_like(T20Cup),'-p',color='k',markerfacecolor='g')
ax.vlines(T20Cup,0,1,color="g",label='T20 World Cup')

ax.plot(CTCup,np.zeros_like(CTCup),'-d',color='k',markerfacecolor='b')
ax.vlines(CTCup,0,-1,color="b",label='Challenge Trophy')

ax.legend(loc='upper left',frameon=False)
plt.show()
fig.savefig('AnalysedGraphs/History.png',dpi=400)   # save the figure to file
plt.close(fig)  