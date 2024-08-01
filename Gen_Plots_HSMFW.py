import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

HSMFW_Acc = pd.read_csv("HSMFW_Acclimated_NewHeaders.csv")
HSMFW_Acc = HSMFW_Acc.fillna(0)
HSMFW_Unacc = pd.read_csv("HSMFW_Unacclimated_NewHeaders.csv")
HSMFW_Unacc = HSMFW_Unacc.fillna(0)
plt.rcParams["font.family"]= "Times New Roman"
x1 = HSMFW_Acc["Day"]
x2 = HSMFW_Unacc["Day"]
Glu_Acc = pd.read_csv("Glucose_Acclimated_NewHeaders_PerGlucoseFed.csv")
Glu_Acc = Glu_Acc.fillna(0)
Glu_Unacc = pd.read_csv("Glucose_Unacclimated_NewHeaders_PerGlucoseFed.csv")
Glu_Unacc = Glu_Unacc.fillna(0)
x3 = Glu_Acc["Day"]
x4 = Glu_Unacc["Day"]
######################################
#Not converted to per-gram-substrate
######################################

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

print(HSMFW_Acc.columns)
print(HSMFW_Unacc.columns)
print(HSMFW_Unacc[["Caproic (67.92 W/m³)","Day"]])
#New Dataframes have per COD axis
#COMPARE ACETIC
#Acclimated
# y = HSMFW_Acc.iloc[:,3]
# y2 = HSMFW_Acc.iloc[:,8]
# label1_list = HSMFW_Acc.columns[3].split(" (")
# label1 = "Acclimated ("+label1_list[1]
# label2_list = HSMFW_Acc.columns[8].split(" (")
# label2 = "Acclimated ("+label2_list[1]
# plt.plot(x1,y,marker='o',color="b",label=label1)
# plt.plot(x1,y2,linestyle='--',marker='x',color="b",label=label2)
# #Unacclimated
# y3 = HSMFW_Unacc.iloc[:,4]
# y4 = HSMFW_Unacc.iloc[:,9]
# label3_list = HSMFW_Unacc.columns[4].split(" (")
# label3 = "Unacclimated ("+label3_list[1]
# label4_list = HSMFW_Unacc.columns[9].split(" (")
# label4 = "Unacclimated ("+label4_list[1]
# plt.plot(x2,y3,marker="o",color='r',label=label3)
# plt.plot(x2,y4,linestyle='--',marker="x",color='r',label=label4)
# #Titles, axis, etc.
# # plt.title("Substrate: HSMFW",loc="right")
# plt.xlabel("Day")
# plt.ylabel("Acetic Acid (g/g COD fed)")
# plt.legend(loc="lower right")
# plt.ylim(0,0.25)
# plt.xlim(0,12)
# plt.savefig('Acetic_HSMFW_Acc_Unacc.png',dpi=1200)
# plt.show()

# COMPARE BUTYRIC
# Acclimated
# y = HSMFW_Acc.iloc[:,4]
# y2 = HSMFW_Acc.iloc[:,9]
# label1_list = HSMFW_Acc.columns[5].split(" (")
# label1 = "Acclimated ("+label1_list[1]
# label2_list = HSMFW_Acc.columns[10].split(" (")
# label2 = "Acclimated ("+label2_list[1]
# plt.plot(x1,y,marker='o',color="b",label=label1)
# plt.plot(x1,y2,linestyle='--',marker='x',color="b",label=label2)
# #Unacclimated
# y3 = HSMFW_Unacc.iloc[:,5]
# y4 = HSMFW_Unacc.iloc[:,10]
# label3_list = HSMFW_Unacc.columns[5].split(" (")
# label3 = "Unacclimated ("+label3_list[1]
# label4_list = HSMFW_Unacc.columns[10].split(" (")
# label4 = "Unacclimated ("+label4_list[1]
# plt.plot(x2,y3,marker="o",color='r',label=label3)
# plt.plot(x2,y4,linestyle='--',marker="x",color='r',label=label4)
# #Titles, axis, etc.
# plt.title("Substrate: HSMFW", loc="left")
# plt.xlabel("Day")
# plt.ylabel("Butyric Acid (g/g COD fed)")
# # plt.legend(loc="lower right")
# plt.ylim(0,0.25)
# plt.xlim(0,12)
# plt.savefig('Butyric_HSMFW_Acc_Unacc.png',dpi=1200)
# plt.show()

#COMPARE CAPROIC
# Acclimated
# y = HSMFW_Acc.iloc[:,5]
# y2 = HSMFW_Acc.iloc[:,10]
# label1_list = HSMFW_Acc.columns[5].split(" (")
# label1 = "Acclimated ("+label1_list[1]
# label2_list = HSMFW_Acc.columns[10].split(" (")
# label2 = "Acclimated ("+label2_list[1]
# plt.plot(x1,y,marker='o',color="b",label=label1)
# plt.plot(x1,y2,linestyle='--',marker='x',color="b",label=label2)
# #Unacclimated
# y3 = HSMFW_Unacc.iloc[:,7]
# y4 = HSMFW_Unacc.iloc[:,12]
# print(y)
# print(y2)
# label3_list = HSMFW_Unacc.columns[7].split(" (")
# label3 = "Unacclimated ("+label3_list[1]
# label4_list = HSMFW_Unacc.columns[12].split(" (")
# label4 = "Unacclimated ("+label4_list[1]
# plt.plot(x2,y3,marker="o",color='r',label=label3)
# plt.plot(x2,y4,linestyle='--',marker="x",color='r',label=label4)
# #Titles, axis, etc.
# plt.title("Substrate: HSMFW", loc="left")
# plt.xlabel("Day")
# plt.ylabel("Caproic Acid (g/g COD fed)")
# plt.legend(loc="upper right")
# plt.ylim(0,0.08)
# plt.xlim(0,12)
# plt.savefig('Caproic_HSMFW_Acc_Unacc.png',dpi=1200)
# plt.show()

# #COMPARE Total VFA's
# #Acclimated
y = HSMFW_Acc[HSMFW_Acc.columns[3]]+HSMFW_Acc[HSMFW_Acc.columns[4]]+HSMFW_Acc[HSMFW_Acc.columns[5]]
y2 = HSMFW_Acc[HSMFW_Acc.columns[8]]+HSMFW_Acc[HSMFW_Acc.columns[9]]+HSMFW_Acc[HSMFW_Acc.columns[10]]
label1_list = HSMFW_Acc.columns[3].split(" (")
label1 = "Acclimated ("+label1_list[1]
label2_list = HSMFW_Acc.columns[8].split(" (")
label2 = "Acclimated ("+label2_list[1]
plt.plot(x1,y,marker='o',color="b",label=label1)
plt.plot(x1,y2,linestyle='--',marker='x',color="b",label=label2)
#Unacclimated
y3 = HSMFW_Unacc[HSMFW_Unacc.columns[4]]+HSMFW_Unacc[HSMFW_Unacc.columns[5]]+HSMFW_Unacc[HSMFW_Unacc.columns[7]]
y4 = HSMFW_Unacc[HSMFW_Unacc.columns[9]]+HSMFW_Unacc[HSMFW_Unacc.columns[10]]+HSMFW_Unacc[HSMFW_Unacc.columns[12]]
label3_list = HSMFW_Unacc.columns[3].split(" (")
label3 = "Unacclimated ("+label3_list[1]
label4_list = HSMFW_Unacc.columns[8].split(" (")
label4 = "Unacclimated ("+label4_list[1]
plt.plot(x2,y3,marker="o",color='r',label=label3)
plt.plot(x2,y4,linestyle='--',marker="x",color='r',label=label4)
#Titles, axis, etc.
plt.title("Substrate: HSMFW", loc="left")
plt.xlabel("Day")
plt.ylabel("Total VFA's (g/g COD fed)")
plt.legend(loc="lower right")
plt.ylim(0,0.5)
plt.xlim(0,12)
plt.savefig('TotalVFA_HSMFW_Acc_Unacc.png',dpi=1200)
plt.show()

# # #COMPARE Lactic
# #Add in 0 columns to END of dataframes
# HSMFW_Acc['Lactic (67.92 W/m³)'] = 0
# # #Acclimated
# y = HSMFW_Acc.iloc[:,7]
# y2 = HSMFW_Acc.iloc[:,12]
# label1_list = HSMFW_Acc.columns[7].split(" (")
# label1 = "Acclimated ("+label1_list[1]
# label2_list = HSMFW_Acc.columns[12].split(" (")
# label2 = "Acclimated ("+label2_list[1]
# plt.plot(x1,y,marker='o',color="b",label=label1)
# plt.plot(x1,y2,linestyle='--',marker='x',color="b",label=label2)
# #Unacclimated
# y3 = HSMFW_Unacc.iloc[:,3]
# y4 = HSMFW_Unacc.iloc[:,8]
# print(y)
# print(y2)
# label3_list = HSMFW_Unacc.columns[3].split(" (")
# label3 = "Unacclimated ("+label3_list[1]
# label4_list = HSMFW_Unacc.columns[8].split(" (")
# label4 = "Unacclimated ("+label4_list[1]
# plt.plot(x2,y3,marker="o",color='r',label=label3)
# plt.plot(x2,y4,linestyle='--',marker="x",color='r',label=label4)
# #Titles, axis, etc.
# plt.title("Substrate: HSMFW", loc="left")
# plt.xlabel("Day")
# plt.ylabel("Lactic Acid (g/g COD fed)")
# plt.legend(loc="upper right")
# plt.ylim(0,0.2)
# plt.xlim(0,12)
# plt.savefig('Lactic_HSMFW_Acc_Unacc.png',dpi=1200)
# plt.show()

# # #COMPARE ETHOH
# # #Acclimated
# y = HSMFW_Acc.iloc[:,6]
# y2 = HSMFW_Acc.iloc[:,11]
# label1_list = HSMFW_Acc.columns[6].split(" (")
# label1 = "Acclimated ("+label1_list[1]
# label2_list = HSMFW_Acc.columns[11].split(" (")
# label2 = "Acclimated ("+label2_list[1]
# plt.plot(x1,y,marker='o',color="b",label=label1)
# plt.plot(x1,y2,linestyle='--',marker='x',color="b",label=label2)
# #Unacclimated
# y3 = HSMFW_Unacc.iloc[:,6]
# y4 = HSMFW_Unacc.iloc[:,11]
# print(y)
# print(y2)
# label3_list = HSMFW_Unacc.columns[6].split(" (")
# label3 = "Unacclimated ("+label3_list[1]
# label4_list = HSMFW_Unacc.columns[11].split(" (")
# label4 = "Unacclimated ("+label4_list[1]
# plt.plot(x2,y3,marker="o",color='r',label=label3)
# plt.plot(x2,y4,linestyle='--',marker="x",color='r',label=label4)
# #Titles, axis, etc.
# plt.title("Substrate: HSMFW", loc="left")
# plt.xlabel("Day")
# plt.ylabel("Ethanol (g/g COD fed)")
# plt.legend(loc="upper right")
# plt.ylim(0,0.05)
# plt.xlim(0,12)
# plt.savefig('Ethanol_HSMFW_Acc_Unacc.png',dpi=1200)
# plt.show()

# unacc_temp = HSMFW_Unacc[["Day",'Caproic (0.01 W/m³)','Caproic (67.92 W/m³)']]
# unacc_temp["lo_c6_rate"]=(unacc_temp['Caproic (0.01 W/m³)']-unacc_temp['Caproic (0.01 W/m³)'].shift(1))/(unacc_temp["Day"]-unacc_temp["Day"].shift(1))
# unacc_temp["hi_c6_rate"]=(unacc_temp['Caproic (67.92 W/m³)']-unacc_temp['Caproic (67.92 W/m³)'].shift(1))/(unacc_temp["Day"]-unacc_temp["Day"].shift(1))
# unacc_temp=unacc_temp[unacc_temp["Day"]<7]
# unacc_temp["low_avg"]=unacc_temp[unacc_temp["lo_c6_rate"]>0]["lo_c6_rate"].mean()
# unacc_temp["hi_avg"]=unacc_temp[unacc_temp["hi_c6_rate"]>0]["hi_c6_rate"].mean()
# print(unacc_temp)