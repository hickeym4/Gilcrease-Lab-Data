import pandas as pd
import numpy as np
list = ['Glucose','Acetic',
       'Isobutyric', 'Butyric',
       'Isovaleric', 'Valeric', 'Caproic',
       'Ethanol', 'Lactic']
start_list_25rpm = ['Day','Glucose (0.01 W/m³)',
       'Acetic (0.01 W/m³)', 'Isobutyric (0.01 W/m³)', 'Butyric (0.01 W/m³)',
       'Isovaleric (0.01 W/m³)','Valeric (0.01 W/m³)', 'Caproic (0.01 W/m³)', 'Lactic (0.01 W/m³)','Ethanol (0.01 W/m³)',
       'Glucose (67.92 W/m³)', 'Acetic (67.92 W/m³)',
       'Isobutyric (67.92 W/m³)', 'Butyric (67.92 W/m³)',
       'Isovaleric (67.92 W/m³)', 'Valeric (67.92 W/m³)',
       'Caproic (67.92 W/m³)', 'Lactic (67.92 W/m³)','Ethanol (67.92 W/m³)']

def fillVFAdata(df,glu_or_MFW):
    if glu_or_MFW=="MFW":
        start_list_25rpm = ['Glucose (0.01 W/m³)',
        'Acetic (0.01 W/m³)', 'Isobutyric (0.01 W/m³)', 'Butyric (0.01 W/m³)',
        'Isovaleric (0.01 W/m³)','Valeric (0.01 W/m³)', 'Caproic (0.01 W/m³)', 'Lactic (0.01 W/m³)','Ethanol (0.01 W/m³)',
        'Glucose (67.92 W/m³)', 'Acetic (67.92 W/m³)',
        'Isobutyric (67.92 W/m³)', 'Butyric (67.92 W/m³)',
        'Isovaleric (67.92 W/m³)', 'Valeric (67.92 W/m³)',
        'Caproic (67.92 W/m³)', 'Lactic (67.92 W/m³)','Ethanol (67.92 W/m³)']
    if glu_or_MFW=="Glucose":
        start_list_25rpm = ['Glucose (0.37 W/m³)',
        'Acetic (0.37 W/m³)', 'Isobutyric (0.37 W/m³)', 'Butyric (0.37 W/m³)',
        'Isovaleric (0.37 W/m³)','Valeric (0.37 W/m³)', 'Caproic (0.37 W/m³)', 'Lactic (0.37 W/m³)','Ethanol (0.37 W/m³)',
        'Glucose (67.92 W/m³)', 'Acetic (67.92 W/m³)',
        'Isobutyric (67.92 W/m³)', 'Butyric (67.92 W/m³)',
        'Isovaleric (67.92 W/m³)', 'Valeric (67.92 W/m³)',
        'Caproic (67.92 W/m³)', 'Lactic (67.92 W/m³)','Ethanol (67.92 W/m³)']
    for i in start_list_25rpm:
        if i not in df.columns:
            df[i] = 0
    df = df[start_list_25rpm]
    return df

def COD_Adjust(df,PV,COD_init):
    column_list = df.columns
    for i in column_list:
        if str(PV) in i:
            df[i] = df[i]/COD_init
    return df

def combine_PVs(df,PV1,PV2,tp_1,tp_2):
    df = df.astype('float32')
    list = ['Glucose','Acetic',
       'Isobutyric', 'Butyric',
       'Isovaleric', 'Valeric', 'Caproic',
       'Ethanol', 'Lactic']
    df1 = pd.DataFrame()
    df2 = pd.DataFrame()
    df = df[(df["Day"]==tp_1)|(df["Day"]==tp_2)]
    columns_ = df.columns
    #Low P/V
    for i in columns_:
        if str(PV1) in i:
            df1[i] = df[i]
    #High P/V
    for j in columns_:
        if str(PV2) in j:
            df2[j] = df[j]
    #rename both dataframes 
    for n in df1.columns:
        for x in list:
            if x in n:
                df1 = df1.rename(columns={n:x})
    for k in df2.columns:
        for x in list:
            if x in k:
                df2 = df2.rename(columns={k:x})
    #Assign numbers to each row for future sorting
    df1["Sort_val"]=[1,3]
    df2["Sort_val"]=[2,4]
    df = pd.concat([df1,df2])
    df = df.sort_values(by="Sort_val")
    df = df[list]
    return df
