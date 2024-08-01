import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

MFW_MI_Acc = pd.read_csv("HSMFW_MI_Acclimated_NewHeaders.csv")
MFW_MI_Acc = MFW_MI_Acc.fillna(0)
MFW_MI_Acc["Day"] = round(MFW_MI_Acc["Day"],1)
MFW_MI_Unacc = pd.read_csv("HSMFW_MI_Unacclimated_NewHeaders.csv")
MFW_MI_Unacc = MFW_MI_Unacc.fillna(0)
MFW_MI_Unacc["Day"] = round(MFW_MI_Unacc["Day"],1)
Glu_surf = pd.read_csv("Glucose_Surfactant_NewHeaders.csv")
Glu_surf = Glu_surf.fillna(0)
Glu_surf["Day"] = round(Glu_surf["Day"],1)
print(Glu_surf.columns)
plt.rcParams["font.family"]= "Times New Roman"

MFW_MI_Acc=MFW_MI_Acc[(MFW_MI_Acc["Day"]==1.8)|(MFW_MI_Acc["Day"]==2.9)]
MFW_MI_Acc[['Ethanol (76.49 W/m³)', 'Lactic (76.49 W/m³)']]=0
MFW_MI_Unacc = MFW_MI_Unacc[(MFW_MI_Unacc["Day"]==0.9)|(MFW_MI_Unacc["Day"]==3.9)]
MFW_MI_Unacc[['Ethanol (76.49 W/m³)', 'Caproic (76.49 W/m³)','Valeric (76.49 W/m³)','Ethanol (7.64 W/m³)',\
              'Valeric (7.64 W/m³)','Isovaleric (7.64 W/m³)','Caproic (7.64 W/m³)']]=0
data = MFW_MI_Unacc.astype('float32')


old = ['Acetic (7.64 W/m³)',
       'Isobutyric (7.64 W/m³)', 'Butyric (7.64 W/m³)',
       'Isovaleric (7.64 W/m³)', 'Valeric (7.64 W/m³)', 'Caproic (7.64 W/m³)',
       'Ethanol (7.64 W/m³)', 'Lactic (7.64 W/m³)']
new = ['Acetic',
       'Isobutyric', 'Butyric',
       'Isovaleric', 'Valeric', 'Caproic',
       'Ethanol', 'Lactic']
manualdf_acc = pd.read_csv("issue_VFA_bar_MFW_screening.csv")
manualdf_unacc = pd.read_csv("issue_VFA_bar_MFW_screening_2.csv")
rename_dict_acclimated = dict(zip(old, new))
manualdf_acc.rename(columns=rename_dict_acclimated, inplace=True)
manualdf_unacc.rename(columns=rename_dict_acclimated, inplace=True)

df = pd.concat([manualdf_acc,manualdf_unacc])
df.reset_index
df = df.drop(columns="Day")
# #Plotting
plt.rcParams["figure.figsize"] = (15,7)
# #(0.37 W/m³)","Day 5 (67.92 W/m³)"
df["Sample"] = ["Day 2","Day 2","Day 4","Day 4","Day 1","Day 1","Day 3","Day 3"]
# y1, y2 = dft[dft.columns[1]], dft[dft.columns[2]]

plt.rcParams["font.family"]= "Times New Roman"
plt.rcParams["font.size"] = 12


event_colours = plt.cm.rainbow(np.linspace(0,1,num=8))
# event_colours_2 = plt.cm.rainbow(np.linspace(0,0.8,num=9))
# # event_colours[-3]=event_colours[-2]
# event_colours[-1]=event_colours_2[-1]
# event_colours[-3]=event_colours_2[-8]
ax = df.plot(x='Sample',kind='bar',stacked=True,rot=0,color=event_colours)
sec = ax.secondary_xaxis(location=0)
sec.set_xticks([0,1,2,3,4,5,6,7],labels=['\n\n\n7.64 W/m³','\n\n\n76.49 W/m³','\n\n\n7.64 W/m³','\n\n\n76.49 W/m³',\
                                 '\n\n\n7.64 W/m³','\n\n\n76.49 W/m³','\n\n\n7.64 W/m³','\n\n\n76.49 W/m³'])
sec.tick_params('x',length=0,width=0)
sec2 = ax.secondary_xaxis(location=0)
sec2.set_xticks([-0.5,1.5,3.5,5.5,7.5])
sec2.tick_params('x',length=40,width=0.75)
labelsempty = [item.get_text() for item in sec2.get_xticklabels()]
empty_string_labels = ['']*len(labelsempty)
sec2.set_xticklabels(empty_string_labels)

# for c in ax.containers:
#     labels=[round(v.get_height(),2) if v.get_height() >0.11 else '' for v in c]
#     ax.bar_label(c,labels=labels, label_type='center')
handles, labels = plt.gca().get_legend_handles_labels()
plt.legend(handles[::-1], labels[::-1] ,bbox_to_anchor=(1.05,1),loc='upper left')
plt.subplots_adjust(right=0.6)
plt.xticks(rotation=45)
plt.subplots_adjust(bottom=0.22)
plt.ylabel("Concentration (g/L)")
plt.xlabel("")

n = len(df)
halfway = n//2
rect = plt.Rectangle((halfway - 0.5, 0), n - halfway, 9, color='gray', alpha=0.2)
ax.add_patch(rect)
textstr = 'Unacclimated'
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0.98, 0.98, textstr, transform=ax.transAxes, fontsize=12,
        verticalalignment='top', horizontalalignment='right', bbox=props)
textstr2 = 'Acclimated'
props2 = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0.02, 0.98, textstr2, transform=ax.transAxes, fontsize=12,
        verticalalignment='top', horizontalalignment='left', bbox=props)
# # ax.set_ylim(0, 1.1)
plt.savefig('MFW_MI_AccUnacc_VFAs.png',dpi=1200)
plt.show()