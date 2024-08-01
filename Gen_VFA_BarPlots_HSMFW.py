import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import VFA_Bar_Functions as flib
plt.rcParams["font.family"]= "Times New Roman"

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
MFW_U = flib.fillVFAdata(MFW_U,"MFW")
MFW_U = flib.COD_Adjust(MFW_U,0.01,HSMFW_Unacc_Lo_COD_raw)
MFW_U = flib.COD_Adjust(MFW_U,67.92,HSMFW_Unacc_Hi_COD_raw)
MFW_U["Day"]=MFW_U_Day["Day"]
MFW_A = flib.fillVFAdata(MFW_A,"MFW")
MFW_A = flib.COD_Adjust(MFW_A,0.01,HSMFW_Acc_Lo_COD_raw)
MFW_A = flib.COD_Adjust(MFW_A,67.92,HSMFW_Acc_Hi_COD_raw)
MFW_A["Day"]=MFW_A_Day["Day"]

#Combine P/V's
MFW_U = flib.combine_PVs(MFW_U,0.01,67.92,1.0,4.5)
MFW_A = flib.combine_PVs(MFW_A,0.01,67.92,1.1,4.7)

MFW = pd.concat([MFW_U,MFW_A])
MFW = MFW.drop(columns=["Glucose"])

print(MFW)















#Generate plots
plt.rcParams["figure.figsize"] = (15,7)
# #(0.37 W/m³)","Day 5 (67.92 W/m³)"
MFW["Sample"] = ["Day 1","Day 1","Day 5","Day 5","Day 1","Day 1","Day 5","Day 5"]
# y1, y2 = dft[dft.columns[1]], dft[dft.columns[2]]

plt.rcParams["font.family"]= "Times New Roman"
plt.rcParams["font.size"] = 14


event_colours = plt.cm.rainbow(np.linspace(0,1,num=8))
ax = MFW.plot(x='Sample',kind='bar',stacked=True,rot=0,color=event_colours)
sec = ax.secondary_xaxis(location=0)
sec.set_xticks([0,1,2,3,4,5,6,7],labels=['\n\n\n0.37 W/m³','\n\n\n67.92 W/m³','\n\n\n0.37 W/m³','\n\n\n67.92 W/m³',\
                                         '\n\n\n0.37 W/m³','\n\n\n67.92 W/m³','\n\n\n0.37 W/m³','\n\n\n67.92 W/m³'])
sec.tick_params('x',length=0,width=0)
sec2 = ax.secondary_xaxis(location=0)
sec2.set_xticks([-0.5,1.5,3.5,5.5,7.5,9.5])
sec2.tick_params('x',length=40,width=0.75)
labelsempty = [item.get_text() for item in sec2.get_xticklabels()]
empty_string_labels = ['']*len(labelsempty)
sec2.set_xticklabels(empty_string_labels)

#Grey Boxes
n = len(MFW)
halfway = n//2
rect = plt.Rectangle((halfway - 0.5, 0), n - halfway, 9, color='gray', alpha=0.2)
ax.add_patch(rect)
textstr = 'Acclimated'
textstr2 = 'Unacclimated'
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0.98, 0.985, textstr, transform=ax.transAxes, fontsize=12,
        verticalalignment='top', horizontalalignment='right',style = 'italic',bbox=props)
ax.text(0.02, 0.985, textstr2, transform=ax.transAxes, fontsize=12,
        verticalalignment='top', horizontalalignment='left',style = 'italic',bbox=props)

# rect = plt.Rectangle((halfway*3 - 0.5, 0), n - halfway*7, 9, color='gray', alpha=0.2)
# ax.add_patch(rect)
# textstr = 'Surfactant'
# props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
# ax.text(0.48, 0.985, textstr, transform=ax.transAxes, fontsize=12,
#         verticalalignment='top', horizontalalignment='right',style = 'italic')

# rect = plt.Rectangle((halfway*5 - 0.5, 0), n - halfway*7, 9, color='gray', alpha=0.2)
# ax.add_patch(rect)
# textstr = 'Surfactant'
# props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
# ax.text(0.73, 0.985, textstr, transform=ax.transAxes, fontsize=12,
#         verticalalignment='top', horizontalalignment='right',style = 'italic')

# rect = plt.Rectangle((halfway*7 - 0.5, 0), n - halfway*7, 9, color='gray', alpha=0.2)
# ax.add_patch(rect)
# textstr = 'Surfactant'
# props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
# ax.text(0.98, 0.985, textstr, transform=ax.transAxes, fontsize=12,
#         verticalalignment='top', horizontalalignment='right',style = 'italic')

# for c in ax.containers:
#     labels=[round(v.get_height(),2) if v.get_height() >0.11 else '' for v in c]
#     ax.bar_label(c,labels=labels, label_type='center')

handles, labels = plt.gca().get_legend_handles_labels()
plt.legend(handles[::-1], labels[::-1] ,bbox_to_anchor=(1.05,1),loc='upper left')
plt.subplots_adjust(right=0.6)
plt.xticks(rotation=45)
plt.subplots_adjust(bottom=0.22)
plt.ylabel("Concentration (g/g COD Fed)")
plt.xlabel("")
plt.title(label="Substrate: HSMFWC",loc='left')
plt.savefig('HSMFW_VFAs_bar.png',dpi=1200)
plt.show()