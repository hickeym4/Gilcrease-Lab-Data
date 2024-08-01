import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Glu_Acc = pd.read_csv("Glucose_Acclimated_NewHeaders_PerGlucoseFed.csv")
Glu_Acc = Glu_Acc.fillna(0)
Glu_Unacc = pd.read_csv("Glucose_Unacclimated_NewHeaders_PerGlucoseFed.csv")
Glu_Unacc = Glu_Unacc.fillna(0)
HSMFW_Acc = pd.read_csv("HSMFW_Acclimated_NewHeaders.csv")
HSMFW_Acc = HSMFW_Acc.fillna(0)
plt.rcParams["font.family"]= "Times New Roman"
x1 = Glu_Acc["Day"]
x2 = Glu_Unacc["Day"]
x3 = HSMFW_Acc["Day"]

#COMPARE CAPROIC
#Acclimated Glucose
y = Glu_Acc.iloc[:,6]
y2 = Glu_Acc.iloc[:,12]
label1_list = Glu_Acc.columns[6].split(" (")
label1 = "Acclimated ("+label1_list[1]
label2_list = Glu_Acc.columns[12].split(" (")
label2 = "Acclimated ("+label2_list[1]
plt.plot(x1,y,marker='o',color="b",label=label1)
plt.plot(x1,y2,marker='x',color="r",label=label2)
#Unacclimated Glucose
y3 = Glu_Unacc.iloc[:,6]
y4 = Glu_Unacc.iloc[:,11]
label3_list = Glu_Unacc.columns[6].split(" (")
label3 = "Unacclimated ("+label3_list[1]
label4_list = Glu_Unacc.columns[11].split(" (")
label4 = "Unacclimated ("+label4_list[1]
plt.plot(x2,y3,linestyle='--',marker="o",color='b',label=label3)
plt.plot(x2,y4,linestyle='--',marker="x",color='r',label=label4)
#Acclimated HSMFW
y3 = Glu_Unacc.iloc[:,6]
y4 = Glu_Unacc.iloc[:,11]
label3_list = Glu_Unacc.columns[6].split(" (")
label3 = "Unacclimated ("+label3_list[1]
label4_list = Glu_Unacc.columns[11].split(" (")
label4 = "Unacclimated ("+label4_list[1]
plt.plot(x2,y3,linestyle='--',marker="o",color='b',label=label3)
plt.plot(x2,y4,linestyle='--',marker="x",color='r',label=label4)
#Titles, axis, etc.
plt.title("Substrate: Glucose", loc="left")
plt.xlabel("Day")
plt.ylabel("Caproic Acid (g/g Substrate Fed)")
plt.legend(loc="upper right")
plt.ylim(0,0.06)
plt.xlim(0,12)
plt.savefig('Caproic_Glucose_Acc_Unacc.png',dpi=1200)
plt.show()