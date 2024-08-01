import pandas as pd 
import numpy as np
import matplotlib as mp

GluUnacc = pd.read_csv("RawData_Python_Glucose_Unacc.csv")
GluAcc = pd.read_csv("RawData_Python_Glucose_Acc.csv")
HSMFW_mi_Acc = pd.read_csv("RawData_Python_HSMFWmarine_Acc.csv")
HSMFW_mi_Unacc = pd.read_csv("RawData_Python_MI_HSMFW_Unacc.csv")
HSMFW_Acc = pd.read_csv("RawData_Python_HSMFW_Acc.csv")
HSMFW_Unacc = pd.read_csv("RawData_Python_HSMFW_Unacc.csv")
SCSMS = pd.read_csv("RawData_Python_SCMS.csv")
GCM = pd.read_csv("RawData_Python_GCM.csv")
Glu_Surfactant = pd.read_csv("RawData_Glucose_Surfactant.csv")
VFA_HSMFW = ["Glucose","Acetic","Butyric","Caproic","Ethanol","Lactic","Valeric","Isovaleric","Isobutyric"]
VFA_Glu = ["Glucose","Acetic","Butyric","Caproic","Ethanol","Lactic"]

#P/V Calculation
def Power_per_Volume(RPM,Volume,PowerNumber,ImpellerDiameter):
    mu = .001
    rho = 1000
    Re = RPM/60*ImpellerDiameter*ImpellerDiameter*rho/mu
    P= PowerNumber*rho*((RPM/60)**3)*(ImpellerDiameter**5)
    PV = round(P*1000/Volume,2)
    return PV

def RenameCol_toPV(df,colname,colsep,PV):
    list_ = colname.split(colsep)
    PV_str = str(PV)
    newname = str(list_[0])+" (" + PV_str + " W/m\u00B3)"
    df = df.rename(columns={colname:newname})
    return df



# Corn meal experiments
df = GCM
for v in VFA_HSMFW:
    for i in range(0,len(df.columns)-1):
        testname = df.columns[i]  
        list_= testname.split("_")
        if list_[0] == v:
            df = RenameCol_toPV(df,df.columns[i],"_",Power_per_Volume(float(list_[1]),2,0.4,.045)+Power_per_Volume(float(list_[1]),2,3.9,.0397))
Glu_Surfactant_Renamed = df[df.columns.drop(list(df.filter(regex="_")))]
Glu_Surfactant_Renamed.to_csv("GCM_NewHeaders.csv")






