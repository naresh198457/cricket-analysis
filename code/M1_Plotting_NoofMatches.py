import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Extract data of the ODI, T20 and test as a function of year
Test=pd.read_csv('Test_Year_Data.csv')
ODI=pd.read_csv('ODI_Year_Data.csv')
T20I=pd.read_csv('T20I_Year_Data.csv')

fig,axs=plt.subplots(figsize=(8.8, 4), constrained_layout=True)
axs.plot(Test['Year'],Test['No of Matches'].cumsum(),'ok')
axs.plot(ODI['Year'],ODI['No of Matches'].cumsum(),'or')
axs.plot(T20I['Year'],T20I['No of Matches'].cumsum(),'ob')
axs.set_xlim(1880,2021)
axs.set_ylim(0,4500)
axs.set_xlabel('Year')
axs.set_ylabel('Total games')

# adding the inset with fiting with poly(3)
TestFitCoeff=np.polyfit(Test['Year'],Test['No of Matches'],3)
TestFit=np.poly1d(TestFitCoeff)
TestFitY=TestFit(Test['Year'])

ODIFitCoeff=np.polyfit(ODI['Year'],ODI['No of Matches'],3)
ODIFit=np.poly1d(ODIFitCoeff)
ODIFitY=ODIFit(ODI['Year'])

T20IFitCoeff=np.polyfit(T20I['Year'],T20I['No of Matches'],3)
T20IFit=np.poly1d(T20IFitCoeff)
T20IFitY=T20IFit(T20I['Year'])

left, bottom, width, height = [0.078, 0.425, 0.55, 0.55]
ax2 = fig.add_axes([left, bottom, width, height])
ax2.plot(Test['Year'],Test['No of Matches'],'ok')
ax2.plot(Test['Year'],TestFitY,'-k')
ax2.plot(ODI['Year'],ODI['No of Matches'],'or')
ax2.plot(ODI['Year'],ODIFitY,'-r')
ax2.plot(T20I['Year'],T20I['No of Matches'],'ob')
ax2.plot(T20I['Year'],T20IFitY,'-b')
ax2.set_xlim(1975,2021)
ax2.set_ylim(0,220)
ax2.set_xlabel('Year')
ax2.set_ylabel('No of Games')
ax2.yaxis.tick_right()
ax2.yaxis.set_label_position("right")
plt.show()

fig.savefig('AnalysedGraphs/NoofMatches.png',dpi=400)
plt.close()