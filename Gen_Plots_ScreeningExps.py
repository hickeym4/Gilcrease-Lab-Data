import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

HSMFW_Acc_MI = pd.read_csv("HSMFW_MI_Acclimated_NewHeaders.csv")
HSMFW_Acc_MI = HSMFW_Acc_MI.fillna(0)
HSMFW_Unacc_MI = pd.read_csv("HSMFW_MI_Unacclimated_NewHeaders.csv")
HSMFW_Unacc_MI = HSMFW_Unacc_MI.fillna(0)
Glucose_Surfactant = pd.read_csv("Glucose_Surfactant_NewHeaders.csv")
Glucose_Surfactant = Glucose_Surfactant.fillna(0)
SMCS = pd.read_csv("SCMS_NewHeaders.csv")
SMCS=SMCS.fillna(0)
GCM = pd.read_csv("GCM_NewHeaders.csv")
GCM=GCM.fillna(0)
Glu_Unacc = pd.read_csv("Glucose_Unacclimated_NewHeaders_PerGlucoseFed.csv")
Glu_Unacc = Glu_Unacc.fillna(0)
plt.rcParams["font.family"]= "Times New Roman"

######################################
#Not converted to per-gram-substrate
######################################

#COD Calib
# x = 2.0281
# b = .0382
# HSMFW_Unacc_Lo_COD_raw = .110
# HSMFW_Unacc_Hi_COD_raw = .112
# Unacc_Dil = 31
# HSMFW_Acc_Lo_COD_raw = .202
# HSMFW_Acc_Hi_COD_raw = .202
# Acc_Dil = 21

# HSMFW_Acc_Lo_COD_raw = (HSMFW_Acc_Lo_COD_raw*x+b)*Acc_Dil
# HSMFW_Acc_Hi_COD_raw = (HSMFW_Acc_Hi_COD_raw*x+b)*Acc_Dil
# HSMFW_Unacc_Lo_COD_raw = (HSMFW_Unacc_Lo_COD_raw*x+b)*Unacc_Dil
# HSMFW_Unacc_Hi_COD_raw = (HSMFW_Unacc_Hi_COD_raw*x+b)*Unacc_Dil




# HSMFW_Unacc.iloc[:, [3,4,5,6,7]] = HSMFW_Unacc.iloc[:, [3,4,5,6,7]]/HSMFW_Unacc_Lo_COD_raw
# HSMFW_Unacc.iloc[:, [8,9,10,11,12]] = HSMFW_Unacc.iloc[:, [8,9,10,11,12]]/HSMFW_Unacc_Hi_COD_raw
# HSMFW_Acc.iloc[:, [3,4,5,6,7]] = HSMFW_Acc.iloc[:, [3,4,5,6,7]]/HSMFW_Acc_Lo_COD_raw
# HSMFW_Acc.iloc[:, [8,9,10,11]] = HSMFW_Acc.iloc[:, [8,9,10,11]]/HSMFW_Acc_Hi_COD_raw


#HSMFW w/ MI only
HSMFW_Acc_MI["Total (7.64 W/m³)"]=HSMFW_Acc_MI["Butyric (7.64 W/m³)"]+HSMFW_Acc_MI["Acetic (7.64 W/m³)"]+HSMFW_Acc_MI["Caproic (7.64 W/m³)"]
HSMFW_Acc_MI["Total (76.49 W/m³)"]=HSMFW_Acc_MI["Butyric (76.49 W/m³)"]+HSMFW_Acc_MI["Acetic (76.49 W/m³)"]+HSMFW_Acc_MI["Caproic (76.49 W/m³)"]
HSMFW_Unacc_MI["Total (7.64 W/m³)"]=HSMFW_Unacc_MI["Butyric (7.64 W/m³)"]+HSMFW_Unacc_MI["Acetic (7.64 W/m³)"]+HSMFW_Unacc_MI["Isobutyric (7.64 W/m³)"]
HSMFW_Unacc_MI["Total (76.49 W/m³)"]=HSMFW_Unacc_MI["Butyric (76.49 W/m³)"]+HSMFW_Unacc_MI["Acetic (76.49 W/m³)"]+HSMFW_Unacc_MI["Isovaleric (76.49 W/m³)"]+HSMFW_Unacc_MI["Isobutyric (76.49 W/m³)"]


#COMPARE Total
#Acclimated
# x1 = HSMFW_Acc_MI["Day"]
# x2 = HSMFW_Unacc_MI["Day"]
# y = HSMFW_Acc_MI.iloc[:,17]
# y2 = HSMFW_Acc_MI.iloc[:,18]
# label1_list = HSMFW_Acc_MI.columns[17].split(" (")
# label1 = "Acclimated ("+label1_list[1]
# label2_list = HSMFW_Acc_MI.columns[18].split(" (")
# label2 = "Acclimated ("+label2_list[1]
# plt.plot(x1,y,marker='o',color="b",label=label1)
# plt.plot(x1,y2,linestyle='--',marker='x',color="b",label=label2)
# #Unacclimated
# y3 = HSMFW_Unacc_MI.iloc[:,12]
# y4 = HSMFW_Unacc_MI.iloc[:,13]
# label3_list = HSMFW_Unacc_MI.columns[12].split(" (")
# label3 = "Unacclimated ("+label3_list[1]
# label4_list = HSMFW_Unacc_MI.columns[13].split(" (")
# label4 = "Unacclimated ("+label4_list[1]
# plt.plot(x2,y3,marker="o",color='r',label=label3)
# plt.plot(x2,y4,linestyle='--',marker="x",color='r',label=label4)
# #Titles, axis, etc.
# # plt.title("Substrate: HSMFW",loc="right")
# plt.xlabel("Day")
# plt.ylabel("Total VFA's (g/L)")
# plt.legend(loc="lower right")
# plt.ylim(0,5.5)
# plt.xlim(0,6)
# plt.savefig('TotalVFAs_HSMFW_MI_Acc_Unacc.png',dpi=1200)
# plt.show()


#Glucose w/ surfactant
Glucose_Surfactant_Init_Lo = Glucose_Surfactant["Glucose (0.37 W/m³)"].iloc[0]
Glucose_Surfactant_Init_Hi = Glucose_Surfactant["Glucose (67.92 W/m³)"].iloc[0]
Glucose_Surfactant.iloc[:, [3,4,5,6,7,8,9]] = Glucose_Surfactant.iloc[:, [3,4,5,6,7,8,9]]/Glucose_Surfactant_Init_Lo
Glucose_Surfactant.iloc[:, [10,11,12,13,14,15,16,17]] = Glucose_Surfactant.iloc[:, [10,11,12,13,14,15,16,17]]/Glucose_Surfactant_Init_Hi
Glucose_Surfactant["Total (0.37 W/m³)"]=Glucose_Surfactant["Butyric (0.37 W/m³)"]+Glucose_Surfactant["Acetic (0.37 W/m³)"]+Glucose_Surfactant["Isobutyric (0.37 W/m³)"]+Glucose_Surfactant["Isovaleric (0.37 W/m³)"]+Glucose_Surfactant["Caproic (0.37 W/m³)"]
Glucose_Surfactant["Total (67.92 W/m³)"]=Glucose_Surfactant["Butyric (67.92 W/m³)"]+Glucose_Surfactant["Acetic (67.92 W/m³)"]+Glucose_Surfactant["Isovaleric (67.92 W/m³)"]+Glucose_Surfactant["Isobutyric (67.92 W/m³)"]+Glucose_Surfactant["Caproic (67.92 W/m³)"]+Glucose_Surfactant["Valeric (67.92 W/m³)"]
Glucose_Surfactant.to_csv("Glucose_Surfactant_PerGluFed.csv")
# Glucose_Surfactant=Glucose_Surfactant.drop(columns=['Unnamed: 19',
#        'Unnamed: 20', 'Unnamed: 21', 'Unnamed: 22', 'Unnamed: 23',
#        'Unnamed: 24', 'Unnamed: 25', 'Unnamed: 26'])



x1 = Glucose_Surfactant["Day"]
x2 = Glu_Unacc["Day"]
#No srufactant, unacc
#Unacclimated
y = Glu_Unacc.iloc[:,3]
y2 = Glu_Unacc.iloc[:,8]
label1_list = Glu_Unacc.columns[3].split(" (")
label1 = "No Surfactant ("+label1_list[1]
label2_list = Glu_Unacc.columns[8].split(" (")
label2 = "No Surfactant ("+label2_list[1]
plt.plot(x2,y,marker="o",color='k',label=label1)
plt.plot(x2,y2,linestyle='--',marker="x",color='k',label=label2)
#Glucose
y3 = Glucose_Surfactant["Glucose (0.37 W/m³)"]
y4 = Glucose_Surfactant["Glucose (67.92 W/m³)"]

label3_list = "Surfactant (0.37 W/m³)"
label4_list = "Surfactant (67.92 W/m³)"

plt.plot(x1,y3,marker="o",color='c',label=label3_list)
plt.plot(x1,y4,linestyle='--',marker="x",color='c',label=label4_list)




#Titles, axis, etc.
plt.title("Substrate: Glucose",loc="left")
plt.xlabel("Day")
plt.ylabel("Glucose (g/g glucose fed)")
plt.legend(loc="upper right")
plt.ylim(0,1)
plt.xlim(0,3)
plt.savefig('SubstrateUptake_Surfactant_NoSurfactant.png',dpi=1200)
plt.show()


#SCMS
# SMCS["Total (2.61 W/m³)"]=SMCS["Butyric (2.61 W/m³)"]+SMCS["Acetic (2.61 W/m³)"]+SMCS["Isobutyric (2.61 W/m³)"]\
#     +SMCS["Isovaleric (2.61 W/m³)"]+SMCS["Valeric (2.61 W/m³)"]
# SMCS["Total (67.92 W/m³)"]=SMCS["Butyric (67.92 W/m³)"]+SMCS["Acetic (67.92 W/m³)"]+SMCS["Isovaleric (67.92 W/m³)"]\
#     +SMCS["Isobutyric (67.92 W/m³)"]+SMCS["Caproic (67.92 W/m³)"]
# #GCM
# print(GCM.columns)
# GCM["Total (2.61 W/m³)"]=GCM["Butyric (2.61 W/m³)"]+GCM["Acetic (2.61 W/m³)"]+GCM["Isobutyric (2.61 W/m³)"]\
#     +GCM["Isovaleric (2.61 W/m³)"]+GCM["Caproic (2.61 W/m³)"]
# GCM["Total (67.92 W/m³)"]=GCM["Butyric (67.92 W/m³)"]+GCM["Acetic (67.92 W/m³)"]+GCM["Isovaleric (67.92 W/m³)"]\
#     +GCM["Isobutyric (67.92 W/m³)"]

# x1 = SMCS["Day"]
# x2 = GCM["Day"]
# # #Total VFA's
# y = SMCS["Total (2.61 W/m³)"]
# y2 = SMCS["Total (67.92 W/m³)"]
# # label1_list = Glucose_Surfactant["Total (0.37 W/m³)"].split(" (")
# label1_list = "SCMS (2.61 W/m³)"
# # label1 = "Acclimated ("+label1_list[1]
# # label2_list = Glucose_Surfactant["Total (67.92 W/m³)"].split(" (")
# label2_list = "SCMS (67.92 W/m³)"
# # label2 = "Acclimated ("+label2_list[1]
# plt.plot(x1,y,marker='o',color="k",label=label1_list)
# plt.plot(x1,y2,linestyle='--',marker='x',color="k",label=label2_list)
# #Glucose
# y3 = GCM["Total (2.61 W/m³)"]
# y4 = GCM["Total (67.92 W/m³)"]
# # label3_list = Glucose_Surfactant["Glucose (0.37 W/m³)"].split(" (")
# label3_list = "GCM (2.61 W/m³)"
# # label3 = "Unacclimated ("+label3_list[1]
# # label4_list = Glucose_Surfactant["Glucose (67.92 W/m³)"].split(" (")
# label4_list = "GCM (67.92 W/m³)"
# # label4 = "Unacclimated ("+label4_list[1]
# plt.plot(x2,y3,marker="o",color='y',label=label3_list)
# plt.plot(x2,y4,linestyle='--',marker="x",color='y',label=label4_list)
# #Titles, axis, etc.
# plt.title("Substrate: Insoluble/Soluble Corn Meal",loc="left")
# plt.xlabel("Day")
# plt.ylabel("Total VFA's (g/L)")
# plt.legend(loc="lower right")
# plt.ylim(0,10)
# plt.xlim(0,9)
# plt.savefig('TotalVFAs_GCM_SMCS_Surfactant.png',dpi=1200)
# plt.show()
