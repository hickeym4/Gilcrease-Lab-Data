import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import VFA_Bar_Functions as flib

Glu_Acc = pd.read_csv("Glucose_Acclimated_NewHeaders_PerGlucoseFed.csv")
Glu_Acc = Glu_Acc.fillna(0)
Glu_Unacc = pd.read_csv("Glucose_Unacclimated_NewHeaders_PerGlucoseFed.csv")
Glu_Unacc = Glu_Unacc.fillna(0)
plt.rcParams["font.family"]= "Times New Roman"

Glu_U_Day =pd.DataFrame()
Glu_U_Day["Day"] = round(Glu_Unacc["Day"],1)
Glu_A_Day =pd.DataFrame()
Glu_A_Day["Day"] = round(Glu_Acc["Day"],1)
print(Glu_Unacc.columns)
print(Glu_Acc.columns)
# Change units of data
Glu_Unacc = flib.fillVFAdata(Glu_Unacc,"Glucose")
Glu_Unacc["Day"]=Glu_U_Day["Day"]
Glu_Acc = flib.fillVFAdata(Glu_Acc,"Glucose")
Glu_Acc["Day"]=Glu_A_Day["Day"]


Glu_Unacc = flib.combine_PVs(Glu_Unacc,0.37,67.92,0.9,4.5)
Glu_Acc = flib.combine_PVs(Glu_Acc,0.37,67.92,1.0,4.8)

Glu = pd.concat([Glu_Unacc,Glu_Acc])
Glu = Glu.drop(columns=["Glucose"])

#Generate plots
plt.rcParams["figure.figsize"] = (15,7)
# #(0.37 W/m³)","Day 5 (67.92 W/m³)"
Glu["Sample"] = ["Day 1","Day 1","Day 5","Day 5","Day 1","Day 1","Day 5","Day 5"]
# y1, y2 = dft[dft.columns[1]], dft[dft.columns[2]]

plt.rcParams["font.family"]= "Times New Roman"
plt.rcParams["font.size"] = 12


event_colours = plt.cm.rainbow(np.linspace(0,1,num=8))
ax = Glu.plot(x='Sample',kind='bar',stacked=True,rot=0,color=event_colours)
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
n = len(Glu)
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



handles, labels = plt.gca().get_legend_handles_labels()
plt.legend(handles[::-1], labels[::-1] ,bbox_to_anchor=(1.05,1),loc='upper left')
plt.subplots_adjust(right=0.6)
plt.xticks(rotation=45)
plt.subplots_adjust(bottom=0.22)
plt.ylabel("Concentration (g/g COD Fed)")
plt.ylim(top=0.4)
plt.xlabel("")
plt.title(label="Substrate: Glucose",loc='left')
plt.savefig('Glucose_AccUnacc_VFAs_bar.png',dpi=1200)
plt.show()