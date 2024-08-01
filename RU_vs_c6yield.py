import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import VFA_Bar_Functions as flib
plt.rcParams["font.family"]= "Times New Roman"

MFW_RU = pd.read_csv("MFW_Acc_ReadyFiltered_16s.csv")
MFW_RU = MFW_RU.iloc[1:]

MFW_U = pd.read_csv("HSMFW_Unacclimated_NewHeaders.csv")
MFW_U=MFW_U.astype('float32')
MFW_U = MFW_U.fillna(0)
MFW_U_Day =pd.DataFrame()
MFW_U_Day["Day"] = round(MFW_U["Day"],1)

MFW_A = pd.read_csv("HSMFW_Acclimated_NewHeaders.csv")
MFW_A=MFW_A.astype('float32')
MFW_A = MFW_A.fillna(0)
MFW_A_Day =pd.DataFrame()
MFW_A_Day["Day"] = round(MFW_A["Day"],1)

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

# Change units of data
MFW_U = flib.fillVFAdata(MFW_U)
MFW_U = flib.COD_Adjust(MFW_U,0.01,HSMFW_Unacc_Lo_COD_raw)
MFW_U = flib.COD_Adjust(MFW_U,67.92,HSMFW_Unacc_Hi_COD_raw)
MFW_U["Day"]=MFW_U_Day["Day"]
MFW_A = flib.fillVFAdata(MFW_A)
MFW_A = flib.COD_Adjust(MFW_A,0.01,HSMFW_Acc_Lo_COD_raw)
MFW_A = flib.COD_Adjust(MFW_A,67.92,HSMFW_Acc_Hi_COD_raw)
MFW_A["Day"]=MFW_A_Day["Day"]

# Change units of data
MFW_U = flib.fillVFAdata(MFW_U)
MFW_U = flib.COD_Adjust(MFW_U,0.01,HSMFW_Unacc_Lo_COD_raw)
MFW_U = flib.COD_Adjust(MFW_U,67.92,HSMFW_Unacc_Hi_COD_raw)
MFW_U["Day"]=MFW_U_Day["Day"]
MFW_A = flib.fillVFAdata(MFW_A)
MFW_A = flib.COD_Adjust(MFW_A,0.01,HSMFW_Acc_Lo_COD_raw)
MFW_A = flib.COD_Adjust(MFW_A,67.92,HSMFW_Acc_Hi_COD_raw)
MFW_A["Day"]=MFW_A_Day["Day"]

#Combine P/V's
MFW_U = flib.combine_PVs(MFW_U,0.01,67.92,1.5,4.5)

MFW_A_1 = flib.combine_PVs(MFW_A,0.01,67.92,2.1,3.7)
MFW_A_2 = flib.combine_PVs(MFW_A,0.01,67.92,2.1,7.7)
MFW_A_2 = MFW_A_2.iloc[2:]
MFW_A = pd.concat([MFW_A_1,MFW_A_2])
MFW_A = MFW_A.reset_index()
MFW_A["Caproiciproducens"] = MFW_RU["Caproiciproducens"]

print(MFW_A)