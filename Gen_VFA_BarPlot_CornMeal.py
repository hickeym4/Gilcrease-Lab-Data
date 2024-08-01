import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
SCMS = pd.read_csv("SCMS_NewHeaders.csv")
SCMS=SCMS.astype('float32')
SCMS = SCMS.fillna(0)
SCMS["Day"] = round(SCMS["Day"],1)

GCM = pd.read_csv("GCM_NewHeaders.csv")
GCM=GCM.astype('float32')
GCM = GCM.fillna(0)
GCM["Day"] = round(GCM["Day"],1)
print(GCM["Day"])
print(GCM.columns)
plt.rcParams["font.family"]= "Times New Roman"


SCMS=SCMS[(SCMS["Day"]==0.9)|(SCMS["Day"]==4.0)]
SCMS[['Caproic (2.61 W/m³)', 'Ethanol (2.61 W/m³)','Lactic (2.61 W/m³)','Ethanol (67.92 W/m³)','Lactic (67.92 W/m³)','Valeric (67.92 W/m³)']]=0
GCM=GCM[(GCM["Day"]==0.9)|(GCM["Day"]==4.1)]
GCM[['Ethanol (2.61 W/m³)','Valeric (2.61 W/m³)','Lactic (2.61 W/m³)','Ethanol (67.92 W/m³)','Lactic (67.92 W/m³)','Valeric (67.92 W/m³)','Caproic (67.92 W/m³)']]=0

SCMS = SCMS[['Day',
       'Acetic (2.61 W/m³)', 'Isobutyric (2.61 W/m³)', 'Butyric (2.61 W/m³)',
       'Isovaleric (2.61 W/m³)','Valeric (2.61 W/m³)', 'Caproic (2.61 W/m³)', 'Lactic (2.61 W/m³)','Ethanol (2.61 W/m³)',
        'Acetic (67.92 W/m³)',
       'Isobutyric (67.92 W/m³)', 'Butyric (67.92 W/m³)',
       'Isovaleric (67.92 W/m³)', 'Valeric (67.92 W/m³)',
       'Caproic (67.92 W/m³)', 'Lactic (67.92 W/m³)','Ethanol (67.92 W/m³)']]
GCM = GCM[['Day',
       'Acetic (2.61 W/m³)', 'Isobutyric (2.61 W/m³)', 'Butyric (2.61 W/m³)',
       'Isovaleric (2.61 W/m³)','Valeric (2.61 W/m³)', 'Caproic (2.61 W/m³)', 'Lactic (2.61 W/m³)','Ethanol (2.61 W/m³)',
        'Acetic (67.92 W/m³)',
       'Isobutyric (67.92 W/m³)', 'Butyric (67.92 W/m³)',
       'Isovaleric (67.92 W/m³)', 'Valeric (67.92 W/m³)',
       'Caproic (67.92 W/m³)', 'Lactic (67.92 W/m³)','Ethanol (67.92 W/m³)']]
data = GCM.astype('float32')







old = ['Acetic (2.61 W/m³)', 'Isobutyric (2.61 W/m³)', 'Butyric (2.61 W/m³)',
       'Isovaleric (2.61 W/m³)','Valeric (2.61 W/m³)', 'Caproic (2.61 W/m³)', 'Ethanol (2.61 W/m³)','Lactic (2.61 W/m³)']
new = ['Acetic',
       'Isobutyric', 'Butyric',
       'Isovaleric', 'Valeric', 'Caproic',
       'Ethanol', 'Lactic']

data_1 = pd.read_csv("scms_manual_edits.csv")
data_2 = pd.read_csv("gcm_manual_edits.csv")
data =pd.concat([data_1,data_2])
rename_dict_acclimated = dict(zip(old, new))
data.rename(columns=rename_dict_acclimated, inplace=True)

data = data[new]
data.reset_index
# df = data.drop(columns="Day")
# #Plotting
plt.rcParams["figure.figsize"] = (15,7)

data["Sample"] = ["Day 1","Day 1","Day 4","Day 4","Day 1","Day 1","Day 4","Day 4"]


plt.rcParams["font.family"]= "Times New Roman"
plt.rcParams["font.size"] = 12


event_colours = plt.cm.rainbow(np.linspace(0,1,num=8))
# # event_colours_2 = plt.cm.rainbow(np.linspace(0,0.8,num=9))
# # # event_colours[-3]=event_colours[-2]
# # event_colours[-1]=event_colours_2[-1]
# # event_colours[-3]=event_colours_2[-8]
ax = data.plot(x='Sample',kind='bar',stacked=True,rot=0,color=event_colours)
sec = ax.secondary_xaxis(location=0)
sec.set_xticks([0,1,2,3,4,5,6,7],labels=['\n\n\n2.61 W/m³','\n\n\n67.92 W/m³','\n\n\n2.61 W/m³','\n\n\n67.92 W/m³',\
                                         '\n\n\n2.61 W/m³','\n\n\n67.92 W/m³','\n\n\n2.61 W/m³','\n\n\n67.92 W/m³'])
sec.tick_params('x',length=0,width=0)
sec2 = ax.secondary_xaxis(location=0)
sec2.set_xticks([-0.5,1.5,3.5,5.5,7.5,9.5])
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
n = len(data)
halfway = n//2
rect = plt.Rectangle((halfway - 0.5, 0), n - halfway, 10, color='gray', alpha=0.2)
ax.add_patch(rect)
textstr = 'GCM'
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0.98, 0.98, textstr, transform=ax.transAxes, fontsize=12,
        verticalalignment='top', horizontalalignment='right', bbox=props)
textstr2 = 'SCMS'
props2 = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0.02, 0.98, textstr2, transform=ax.transAxes, fontsize=12,
        verticalalignment='top', horizontalalignment='left', bbox=props)
plt.savefig('GCM_SCMS_VFAs_bar.png',dpi=1200)
plt.show()