import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Glu_Acc = pd.read_csv("Glucose_Acclimated_NewHeaders_PerGlucoseFed.csv")
Glu_Acc = Glu_Acc.fillna(0)
Glu_Unacc = pd.read_csv("Glucose_Unacclimated_NewHeaders_PerGlucoseFed.csv")
Glu_Unacc = Glu_Unacc.fillna(0)
plt.rcParams["font.family"]= "Times New Roman"
x1 = Glu_Acc["Day"]
x2 = Glu_Unacc["Day"]


#COMPARE SUBSTRATE UPTAKE
#Acclimated
y = Glu_Acc.iloc[:,3]
y2 = Glu_Acc.iloc[:,9]
label1_list = Glu_Acc.columns[3].split(" (")
label1 = "Acclimated ("+label1_list[1]
label2_list = Glu_Acc.columns[9].split(" (")
label2 = "Acclimated ("+label2_list[1]
plt.plot(x1,y,marker='o',color="b",label=label1)
plt.plot(x1,y2,marker='x',linestyle='--',color="b",label=label2)
#Unacclimated
y3 = Glu_Unacc.iloc[:,3]
y4 = Glu_Unacc.iloc[:,8]
label3_list = Glu_Unacc.columns[3].split(" (")
label3 = "Unacclimated ("+label3_list[1]
label4_list = Glu_Unacc.columns[8].split(" (")
label4 = "Unacclimated ("+label4_list[1]
plt.plot(x2,y3,marker="o",color='r',label=label3)
plt.plot(x2,y4,linestyle='--',marker="x",color='r',label=label4)
#Titles, axis, etc.
plt.title("Substrate: Glucose",loc="left")
plt.xlabel("Day")
plt.ylabel("Glucose (g/g Substrate Fed)")
plt.legend(loc="upper right")
plt.ylim(0,1)
plt.xlim(0,3)
plt.savefig('Glucose_Uptake_Acc_Unacc.png',dpi=1200)
plt.show()

# #COMPARE ACETIC
# #Acclimated
# y = Glu_Acc.iloc[:,4]
# y2 = Glu_Acc.iloc[:,10]
# label1_list = Glu_Acc.columns[4].split(" (")
# label1 = "Acclimated ("+label1_list[1]
# label2_list = Glu_Acc.columns[10].split(" (")
# label2 = "Acclimated ("+label2_list[1]
# plt.plot(x1,y,marker='o',color="b",label=label1)
# plt.plot(x1,y2,marker='x',linestyle='--',color="b",label=label2)
# #Unacclimated
# y3 = Glu_Unacc.iloc[:,4]
# y4 = Glu_Unacc.iloc[:,9]
# label3_list = Glu_Unacc.columns[4].split(" (")
# label3 = "Unacclimated ("+label3_list[1]
# label4_list = Glu_Unacc.columns[9].split(" (")
# label4 = "Unacclimated ("+label4_list[1]
# plt.plot(x2,y3,marker="o",color='r',label=label3)
# plt.plot(x2,y4,linestyle='--',marker="x",color='r',label=label4)
# #Titles, axis, etc.
# plt.title("Substrate: Glucose",loc="right")
# plt.xlabel("Day")
# plt.ylabel("Acetic Acid (g/g Substrate Fed)")
# plt.legend(loc="upper right")
# plt.ylim(0,0.3)
# plt.xlim(0,12)
# plt.savefig('Acetic_Glucose_Acc_Unacc.png',dpi=1200)
# plt.show()

#COMPARE BUTYRIC
#Acclimated
# y = Glu_Acc.iloc[:,5]
# y2 = Glu_Acc.iloc[:,11]
# label1_list = Glu_Acc.columns[5].split(" (")
# label1 = "Acclimated ("+label1_list[1]
# label2_list = Glu_Acc.columns[11].split(" (")
# label2 = "Acclimated ("+label2_list[1]
# plt.plot(x1,y,marker='o',color="b",label=label1)
# plt.plot(x1,y2,marker='x',linestyle='--',color="b",label=label2)
# #Unacclimated
# y3 = Glu_Unacc.iloc[:,5]
# y4 = Glu_Unacc.iloc[:,10]
# label3_list = Glu_Unacc.columns[5].split(" (")
# label3 = "Unacclimated ("+label3_list[1]
# label4_list = Glu_Unacc.columns[10].split(" (")
# label4 = "Unacclimated ("+label4_list[1]
# plt.plot(x2,y3,marker="o",color='r',label=label3)
# plt.plot(x2,y4,linestyle='--',marker="x",color='r',label=label4)
# #Titles, axis, etc.
# # plt.title("Substrate: Glucose", loc="left")
# plt.xlabel("Day")
# plt.ylabel("Butyric Acid (g/g Substrate Fed)")
# # plt.legend(loc="lower right")
# plt.ylim(0,0.3)
# plt.xlim(0,12)
# plt.savefig('Butyric_Glucose_Acc_Unacc.png',dpi=1200)
# plt.show()

# #COMPARE CAPROIC
# #Acclimated
# y = Glu_Acc.iloc[:,6]
# y2 = Glu_Acc.iloc[:,12]
# label1_list = Glu_Acc.columns[6].split(" (")
# label1 = "Acclimated ("+label1_list[1]
# label2_list = Glu_Acc.columns[12].split(" (")
# label2 = "Acclimated ("+label2_list[1]
# plt.plot(x1,y,marker='o',color="b",label=label1)
# plt.plot(x1,y2,marker='x',linestyle='--',color="b",label=label2)
# #Unacclimated
# y3 = Glu_Unacc.iloc[:,6]
# y4 = Glu_Unacc.iloc[:,11]
# label3_list = Glu_Unacc.columns[6].split(" (")
# label3 = "Unacclimated ("+label3_list[1]
# label4_list = Glu_Unacc.columns[11].split(" (")
# label4 = "Unacclimated ("+label4_list[1]
# plt.plot(x2,y3,marker="o",color='r',label=label3)
# plt.plot(x2,y4,linestyle='--',marker="x",color='r',label=label4)
# #Titles, axis, etc.
# plt.title("Substrate: Glucose", loc="left")
# plt.xlabel("Day")
# plt.ylabel("Caproic Acid (g/g Substrate Fed)")
# plt.legend(loc="upper right")
# plt.ylim(0,0.06)
# plt.xlim(0,12)
# plt.savefig('Caproic_Glucose_Acc_Unacc.png',dpi=1200)
# plt.show()

# #COMPARE Total VFA's
# #Acclimated
y = Glu_Acc[Glu_Acc.columns[-4]]+Glu_Acc[Glu_Acc.columns[-3]]+Glu_Acc[Glu_Acc.columns[-2]]
y2 = Glu_Acc[Glu_Acc.columns[4]]+Glu_Acc[Glu_Acc.columns[5]]+Glu_Acc[Glu_Acc.columns[6]]
label1_list = Glu_Acc.columns[6].split(" (")
label1 = "Acclimated ("+label1_list[1]
label2_list = Glu_Acc.columns[12].split(" (")
label2 = "Acclimated ("+label2_list[1]
plt.plot(x1,y,marker='o',color="b",label=label1)
plt.plot(x1,y2,marker='x',linestyle='--',color="b",label=label2)
#Unacclimated
y3 = Glu_Unacc[Glu_Unacc.columns[-3]]+Glu_Unacc[Glu_Unacc.columns[-2]]+Glu_Unacc[Glu_Unacc.columns[-1]]
y4 = Glu_Unacc[Glu_Unacc.columns[4]]+Glu_Unacc[Glu_Unacc.columns[5]]+Glu_Unacc[Glu_Unacc.columns[6]]
label3_list = Glu_Unacc.columns[6].split(" (")
label3 = "Unacclimated ("+label3_list[1]
label4_list = Glu_Unacc.columns[11].split(" (")
label4 = "Unacclimated ("+label4_list[1]
plt.plot(x2,y3,marker="o",color='r',label=label3)
plt.plot(x2,y4,linestyle='--',marker="x",color='r',label=label4)
#Titles, axis, etc.
plt.title("Substrate: Glucose", loc="left")
plt.xlabel("Day")
plt.ylabel("Total VFA's (g/g Substrate Fed)")
plt.legend(loc="lower right")
plt.ylim(0,0.45)
plt.xlim(0,12)
plt.savefig('TotalVFA_Glucose_Acc_Unacc.png',dpi=1200)
plt.show()

# #COMPARE Lactic
#Add 0 column to END of dataframe
# Glu_Acc['Lactic (67.91 W/m³)'] = 0
# Glu_Unacc['Lactic (67.91 W/m³)'] = 0
# # #Acclimated
# y = Glu_Acc[Glu_Acc.columns[8]]
# y2 = Glu_Acc[Glu_Acc.columns[14]]
# label1_list = Glu_Acc.columns[8].split(" (")
# label1 = "Acclimated ("+label1_list[1]
# label2_list = Glu_Acc.columns[14].split(" (")
# label2 = "Acclimated ("+label2_list[1]
# plt.plot(x1,y,marker='o',color="b",label=label1)
# plt.plot(x1,y2,marker='x',linestyle='--',color="b",label=label2)
# #Unacclimated
# y3 = Glu_Unacc[Glu_Unacc.columns[7]]
# y4 = Glu_Unacc[Glu_Unacc.columns[12]]
# label3_list = Glu_Unacc.columns[7].split(" (")
# label3 = "Unacclimated ("+label3_list[1]
# label4_list = Glu_Unacc.columns[12].split(" (")
# label4 = "Unacclimated ("+label4_list[1]
# plt.plot(x2,y3,marker="o",color='r',label=label3)
# plt.plot(x2,y4,linestyle='--',marker="x",color='r',label=label4)
# #Titles, axis, etc.
# plt.title("Substrate: Glucose", loc="left")
# plt.xlabel("Day")
# plt.ylabel("Lactic Acid (g/g Substrate Fed)")
# plt.legend(loc="upper right")
# plt.ylim(0,0.025)
# plt.xlim(0,12)
# plt.savefig('Lactic_Glucose_Acc_Unacc.png',dpi=1200)
# plt.show()