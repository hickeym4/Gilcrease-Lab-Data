import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

HSMFW_Acc = pd.read_csv("HSMFW_Acclimated_NewHeaders.csv")
HSMFW_Acc = HSMFW_Acc.fillna(0)
HSMFW_Unacc = pd.read_csv("HSMFW_Unacclimated_NewHeaders.csv")
HSMFW_Unacc = HSMFW_Unacc.fillna(0)
plt.rcParams["font.family"]= "Times New Roman"
Glu_Acc = pd.read_csv("Glucose_Acclimated_NewHeaders_PerGlucoseFed.csv")
Glu_Acc = Glu_Acc.fillna(0)
Glu_Unacc = pd.read_csv("Glucose_Unacclimated_NewHeaders_PerGlucoseFed.csv")
Glu_Unacc = Glu_Unacc.fillna(0)



#COD Calib
x = 2.0281
b = .0382
HSMFW_Unacc_Lo_COD_raw = .110
HSMFW_Unacc_Hi_COD_raw = .112
Unacc_Dil = 31
HSMFW_Acc_Lo_COD_raw = .202
HSMFW_Acc_Hi_COD_raw = .202
Acc_Dil = 21

HSMFW_Acc_Lo_COD_raw = (HSMFW_Acc_Lo_COD_raw*x+b)*Acc_Dil
HSMFW_Acc_Hi_COD_raw = (HSMFW_Acc_Hi_COD_raw*x+b)*Acc_Dil
HSMFW_Unacc_Lo_COD_raw = (HSMFW_Unacc_Lo_COD_raw*x+b)*Unacc_Dil
HSMFW_Unacc_Hi_COD_raw = (HSMFW_Unacc_Hi_COD_raw*x+b)*Unacc_Dil

HSMFW_Unacc.iloc[:, [3,4,5,6,7]] = HSMFW_Unacc.iloc[:, [3,4,5,6,7]]/HSMFW_Unacc_Lo_COD_raw
HSMFW_Unacc.iloc[:, [8,9,10,11,12]] = HSMFW_Unacc.iloc[:, [8,9,10,11,12]]/HSMFW_Unacc_Hi_COD_raw
HSMFW_Acc.iloc[:, [3,4,5,6,7]] = HSMFW_Acc.iloc[:, [3,4,5,6,7]]/HSMFW_Acc_Lo_COD_raw
HSMFW_Acc.iloc[:, [8,9,10,11]] = HSMFW_Acc.iloc[:, [8,9,10,11]]/HSMFW_Acc_Hi_COD_raw



Glu_Acc["Total (0.37 W/m³)"]=(Glu_Acc["Acetic (0.37 W/m³)"]+Glu_Acc["Butyric (0.37 W/m³)"]+Glu_Acc["Caproic (0.37 W/m³)"])
Glu_Acc["Total (67.92 W/m³)"]=(Glu_Acc["Acetic (67.92 W/m³)"]+Glu_Acc["Butyric (67.92 W/m³)"]+Glu_Acc["Caproic (67.92 W/m³)"])
Glu_Unacc["Total (0.37 W/m³)"]=(Glu_Unacc["Acetic (0.37 W/m³)"]+Glu_Unacc["Butyric (0.37 W/m³)"]+Glu_Unacc["Caproic (0.37 W/m³)"])
Glu_Unacc["Total (67.92 W/m³)"]=(Glu_Unacc["Acetic (67.92 W/m³)"]+Glu_Unacc["Butyric (67.92 W/m³)"]+Glu_Unacc["Caproic (67.92 W/m³)"])
HSMFW_Unacc["Total (0.01 W/m³)"]=(HSMFW_Unacc["Acetic (0.01 W/m³)"]+HSMFW_Unacc["Butyric (0.01 W/m³)"]+HSMFW_Unacc["Caproic (0.01 W/m³)"])
HSMFW_Unacc["Total (67.92 W/m³)"]=(HSMFW_Unacc["Acetic (67.92 W/m³)"]+HSMFW_Unacc["Butyric (67.92 W/m³)"]+HSMFW_Unacc["Caproic (67.92 W/m³)"])
HSMFW_Acc["Total (0.01 W/m³)"]=(HSMFW_Acc["Acetic (0.01 W/m³)"]+HSMFW_Acc["Butyric (0.01 W/m³)"]+HSMFW_Acc["Caproic (0.01 W/m³)"])
HSMFW_Acc["Total (67.92 W/m³)"]=(HSMFW_Acc["Acetic (67.92 W/m³)"]+HSMFW_Acc["Butyric (67.92 W/m³)"]+HSMFW_Acc["Caproic (67.92 W/m³)"])

Total = pd.DataFrame()
Total = pd.concat([Total,HSMFW_Unacc[["Total (0.01 W/m³)","Day"]].head(5)],axis=1)
# Total["HSMFWC UNACC (0.01 W/m³)"] = HSMFW_Unacc[["Total (0.01 W/m³)","Day"]].head(5)
# Total["HSMFWC UNACC (67.92 W/m³)"] = HSMFW_Unacc["Total (67.92 W/m³)"].head(5)
# Total["HSMFWC ACC (0.01 W/m³)"] = HSMFW_Acc["Total (0.01 W/m³)"].head(5)
# Total["HSMFWC ACC (67.92 W/m³)"] = HSMFW_Acc["Total (67.92 W/m³)"].head(5)
# Total["Glucose UNACC (0.37 W/m³)"] = Glu_Unacc["Total (0.37 W/m³)"].head(5)
# Total["Glucose UNACC (0.37 W/m³)"]=Total["Glucose UNACC (0.37 W/m³)"]/1.1
# Total["Glucose UNACC (67.92 W/m³)"] = Glu_Unacc["Total (67.92 W/m³)"].head(5)
# Total["Glucose UNACC (67.92 W/m³)"] = Total["Glucose UNACC (67.92 W/m³)"]/1.1
# Total["Glucose ACC (0.37 W/m³)"] = Glu_Acc["Total (0.37 W/m³)"].head(5)
# Total["Glucose ACC (0.37 W/m³)"] = Total["Glucose ACC (0.37 W/m³)"]/1.1
# Total["Glucose ACC (67.92 W/m³)"] = Glu_Acc["Total (67.92 W/m³)"].head(5)
# Total["Glucose ACC (67.92 W/m³)"] = Total["Glucose ACC (67.92 W/m³)"]/1.1

# x1 = HSMFW_Acc["Day"].head(6)
# x2 = Glu_Acc["Day"].head(8)

# y = HSMFW_Acc["Total (0.01 W/m³)"].head(6)
# y2 = HSMFW_Acc["Total (67.92 W/m³)"].head(6)
# label1_list = "HSMFWC ACC (0.01 W/m³)".split(" (")
# label1 = "HSMFWC ("+label1_list[1]
# label2_list = "HSMFWC ACC (67.92 W/m³)".split(" (")
# label2 = "HSMFWC ("+label2_list[1]
# plt.plot(x1,y,marker='o',color="k",label=label1)
# plt.plot(x1,y2,linestyle='--',marker='x',color="k",label=label2)
# #Unacclimated
# y3 = Glu_Acc["Total (0.37 W/m³)"].head(8)
# y4 = Glu_Acc["Total (67.92 W/m³)"].head(8)
# label3_list = "Glucose ACC (0.37 W/m³)".split(" (")
# label3 = "Glucose ("+label3_list[1]
# label4_list = "Glucose ACC (67.92 W/m³)".split(" (")
# label4 = "Glucose ("+label4_list[1]
# plt.plot(x2,y3,marker="o",color='g',label=label3)
# plt.plot(x2,y4,linestyle='--',marker="x",color='g',label=label4)
# #Titles, axis, etc.
# plt.title("Acclimated Inoculum", loc="left")
# plt.xlabel("Day")
# plt.ylabel("Total VFA's (g/g COD fed)")
# plt.legend(loc="lower right")
# plt.ylim(0,0.4)
# plt.xlim(0,2.5)
# plt.savefig('RLS_Acclimated.png',dpi=1200)

x3 = HSMFW_Unacc["Day"].head(6)
x4 = Glu_Unacc["Day"].head(8)

y5 = HSMFW_Unacc["Total (0.01 W/m³)"].head(6)
y6 = HSMFW_Unacc["Total (67.92 W/m³)"].head(6)
label1_list = "HSMFWC ACC (0.01 W/m³)".split(" (")
label1 = "HSMFWC ("+label1_list[1]
label2_list = "HSMFWC ACC (67.92 W/m³)".split(" (")
label2 = "HSMFWC ("+label2_list[1]
plt.plot(x3,y5,marker='o',color="k",label=label1)
plt.plot(x3,y6,linestyle='--',marker='x',color="k",label=label2)
#Unacclimated
y7 = Glu_Unacc["Total (0.37 W/m³)"].head(8)
y8 = Glu_Unacc["Total (67.92 W/m³)"].head(8)
label3_list = "Glucose ACC (0.37 W/m³)".split(" (")
label3 = "Glucose ("+label3_list[1]
label4_list = "Glucose ACC (67.92 W/m³)".split(" (")
label4 = "Glucose ("+label4_list[1]
plt.plot(x4,y7,marker="o",color='g',label=label3)
plt.plot(x4,y8,linestyle='--',marker="x",color='g',label=label4)
#Titles, axis, etc.
plt.title("Unacclimated Inoculum", loc="left")
plt.xlabel("Day")
plt.ylabel("Total VFA's (g/g COD fed)")
plt.legend(loc="lower right")
plt.ylim(0,0.4)
plt.xlim(0,2.5)
plt.savefig('RLS_Unacclimated.png',dpi=1200)
plt.show()