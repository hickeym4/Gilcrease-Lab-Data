import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["font.family"]= "Times New Roman"

Glu_surf = pd.read_csv("Glucose_Surfactant_NewHeaders.csv")
Glu_surf=Glu_surf.astype('float32')
Glu_surf = Glu_surf.fillna(0)
Glu_surf["Day"] = round(Glu_surf["Day"],1)
Glu_Unacc = pd.read_csv("Glucose_Unacclimated_NewHeaders_PerGlucoseFed.csv")
Glu_Unacc = Glu_Unacc.fillna(0)
Glu_Unacc["Day"] = round(Glu_Unacc["Day"],1)

print(Glu_Unacc.columns)
print(Glu_Unacc["Day"])
Glu_Unacc=Glu_Unacc[(Glu_Unacc["Day"]==0.9)|(Glu_Unacc["Day"]==4.5)]
Glu_Unacc[['Isobutyric (0.37 W/m³)','Isovaleric (0.37 W/m³)','Valeric (0.37 W/m³)','Lactic (0.37 W/m³)','Ethanol (0.37 W/m³)',\
           'Isobutyric (67.92 W/m³)','Isovaleric (67.92 W/m³)','Valeric (67.92 W/m³)','Lactic (67.92 W/m³)','Ethanol (67.92 W/m³)']]=0
Glu_Unacc = Glu_Unacc[['Day','Glucose (0.37 W/m³)',
       'Acetic (0.37 W/m³)', 'Isobutyric (0.37 W/m³)', 'Butyric (0.37 W/m³)',
       'Isovaleric (0.37 W/m³)','Valeric (0.37 W/m³)', 'Caproic (0.37 W/m³)', 'Lactic (0.37 W/m³)','Ethanol (0.37 W/m³)',
       'Glucose (67.92 W/m³)', 'Acetic (67.92 W/m³)',
       'Isobutyric (67.92 W/m³)', 'Butyric (67.92 W/m³)',
       'Isovaleric (67.92 W/m³)', 'Valeric (67.92 W/m³)',
       'Caproic (67.92 W/m³)', 'Lactic (67.92 W/m³)','Ethanol (67.92 W/m³)']]
data = Glu_Unacc.astype('float32')

old = ['Acetic (0.37 W/m³)', 'Isobutyric (0.37 W/m³)', 'Butyric (0.37 W/m³)',
       'Isovaleric (0.37 W/m³)','Valeric (0.37 W/m³)', 'Caproic (0.37 W/m³)', 'Lactic (0.37 W/m³)','Ethanol (0.37 W/m³)']
new = ['Acetic',
       'Isobutyric', 'Butyric',
       'Isovaleric', 'Valeric', 'Caproic',
       'Ethanol', 'Lactic']

data = pd.read_csv("Glucose_Unacc_Manual_edits.csv")
rename_dict_acclimated = dict(zip(old, new))
data.rename(columns=rename_dict_acclimated, inplace=True)





print(data)






data = data[new]
data.reset_index
# df = data.drop(columns="Day")
# #Plotting
plt.rcParams["figure.figsize"] = (15,7)
# #(0.37 W/m³)","Day 5 (67.92 W/m³)"
data["Sample"] = ["Day 1","Day 1","Day 1","Day 1","Day 4.5","Day 4.5","Day 4.5","Day 4.5"]
# y1, y2 = dft[dft.columns[1]], dft[dft.columns[2]]

plt.rcParams["font.family"]= "Times New Roman"
plt.rcParams["font.size"] = 12


event_colours = plt.cm.rainbow(np.linspace(0,1,num=8))
# # event_colours_2 = plt.cm.rainbow(np.linspace(0,0.8,num=9))
# # # event_colours[-3]=event_colours[-2]
# # event_colours[-1]=event_colours_2[-1]
# # event_colours[-3]=event_colours_2[-8]
ax = data.plot(x='Sample',kind='bar',stacked=True,rot=0,color=event_colours)
sec = ax.secondary_xaxis(location=0)
sec.set_xticks([0.5,2.5,4.5,6.5],labels=['\n\n\n0.37 W/m³','\n\n\n67.92 W/m³','\n\n\n0.37 W/m³','\n\n\n67.92 W/m³'])
sec.tick_params('x',length=0,width=0)
sec2 = ax.secondary_xaxis(location=0)
sec2.set_xticks([-0.5,1.5,3.5,5.5,7.5,9.5])
sec2.tick_params('x',length=40,width=0.75)
labelsempty = [item.get_text() for item in sec2.get_xticklabels()]
empty_string_labels = ['']*len(labelsempty)
sec2.set_xticklabels(empty_string_labels)

#Grey Boxes
n = len(data)
halfway = n//8
rect = plt.Rectangle((halfway - 0.5, 0), n - halfway*7, 9, color='gray', alpha=0.2)
ax.add_patch(rect)
textstr = 'Surfactant'
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0.23, 0.985, textstr, transform=ax.transAxes, fontsize=12,
        verticalalignment='top', horizontalalignment='right',style = 'italic')

rect = plt.Rectangle((halfway*3 - 0.5, 0), n - halfway*7, 9, color='gray', alpha=0.2)
ax.add_patch(rect)
textstr = 'Surfactant'
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0.48, 0.985, textstr, transform=ax.transAxes, fontsize=12,
        verticalalignment='top', horizontalalignment='right',style = 'italic')

rect = plt.Rectangle((halfway*5 - 0.5, 0), n - halfway*7, 9, color='gray', alpha=0.2)
ax.add_patch(rect)
textstr = 'Surfactant'
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0.73, 0.985, textstr, transform=ax.transAxes, fontsize=12,
        verticalalignment='top', horizontalalignment='right',style = 'italic')

rect = plt.Rectangle((halfway*7 - 0.5, 0), n - halfway*7, 9, color='gray', alpha=0.2)
ax.add_patch(rect)
textstr = 'Surfactant'
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0.98, 0.985, textstr, transform=ax.transAxes, fontsize=12,
        verticalalignment='top', horizontalalignment='right',style = 'italic')

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



plt.savefig('Glucose_Surfactant_VFAs_bar.png',dpi=1200)
plt.show()
