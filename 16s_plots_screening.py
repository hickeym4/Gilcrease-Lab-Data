import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

data = pd.read_csv("AA2_AA3_16s_raw.csv")


Acclimated = ["AA2 T0 ","AA2 T3 355","AA2 T3 765","AA2 T7 355","AA2 T7 765"]
Acclimated_new = ["Time Zero","Day 2 (7.64 W/m³)","Day 2 (76.49 W/m³)","Day 4 (7.64 W/m³)","Day 4 (76.49 W/m³)"]
Unacclimated = ["AA3 T3 355","AA3 T3 765","AA3 T6 355","AA3 T6 765"]
Unacclimated_new = ["Day 1 (7.64 W/m³)","Day 1 (76.49 W/m³)","Day 3 (7.64 W/m³)","Day 3 (76.49 W/m³)"]
rename_dict_acclimated = dict(zip(Acclimated, Acclimated_new))
rename_dict_unacclimated = dict(zip(Unacclimated, Unacclimated_new))
data.rename(columns=rename_dict_acclimated, inplace=True)
data.rename(columns=rename_dict_unacclimated, inplace=True)
sample_list = data.columns[-9:]


threshold=.02
df = pd.DataFrame()
genus_list = ["Caproiciproducens","Clostridium_sensu_stricto_1","Clostridium_sensu_stricto_11","Clostridium_sensu_stricto_5","Leuconostoc","Lactococcus","Lactobacillus"]
color_list = [(1,1,1,1),(1,1,0,1),(1,0.5,0.5,1),(1,0,1,1),(0,0,1,1),(0.3,0,1,0.35),(0,0,0,0.35)]

for i in sample_list:
    newcol = str(i)+" MC?"
    df['Genus']=data.groupby(['int.slv.Genus'], as_index=False)[i].sum()['int.slv.Genus']
    df[i] = data.groupby(['int.slv.Genus'], as_index=False)[i].sum()[i] 
    df[newcol]=(df[i]/df[i]).where(df[i]>threshold,0)
sample_list_ = [name + " MC?" for name in sample_list]

df["Any_Meet_Criteria?"] = (df[sample_list_[0]]-df[sample_list_[0]]+1).where((df[sample_list_[0]]==1)|(df[sample_list_[1]]==1)|(df[sample_list_[2]]==1)|\
                                              (df[sample_list_[3]]==1)|(df[sample_list_[4]]==1)|(df[sample_list_[5]]==1)|(df[sample_list_[6]]==1)|\
                                               (df[sample_list_[7]]==1)|(df[sample_list_[8]]==1))
# df.to_csv("check_16s.csv")
df=df[df["Any_Meet_Criteria?"]==1]
# # All samples
sample_list=sample_list.insert(0,"Genus")
df = df[sample_list]


# #Plotting
plt.rcParams["figure.figsize"] = (18,8)
index_ = df["Genus"]
df.index = index_
df = df.drop(columns="Genus")
dft = df.transpose()
dft = dft[dft.columns].apply(pd.to_numeric)
dft["Other"] = 1- dft[list(dft.columns)].sum(axis=1)
#change below code if unclutured or unassigned is included
dft["Other/Uncultured/Unassigned"] = dft["Other"]+dft["Unassigned"]
dft = dft.drop(columns = ['Other','Unassigned'])
dft["Check"] = dft[list(dft.columns)].sum(axis=1)
print(dft["Caproiciproducens"])
# #(0.37 W/m³)","Day 5 (67.92 W/m³)"
dft["Sample"] = ["Day 0","Day 2","Day 2","Day 4","Day 4","Day 1","Day 1","Day 3","Day 3"]
# y1, y2 = dft[dft.columns[1]], dft[dft.columns[2]]

plt.rcParams["font.family"]= "Times New Roman"
plt.rcParams["font.size"] = 14

dft = dft.drop(columns="Check")
event_colours = plt.cm.rainbow(np.linspace(0,1,num=len(dft.columns)))
# event_colours_2 = plt.cm.rainbow(np.linspace(0,0.8,num=9))
# event_colours[1]=(1,1,0,1)
# event_colours[-1]=event_colours_2[-1]
# event_colours[-3]=event_colours_2[-8]
print(dft.columns)
for s in dft.columns:
    if s in genus_list:
        print(str(s)+" is in list")
        pos = genus_list.index(s)
        color = color_list[pos]
        event_colours[dft.columns.to_list().index(s)]=color
ax = dft.plot(x='Sample',kind='bar',stacked=True,rot=0,color=event_colours,edgecolor="black")
sec = ax.secondary_xaxis(location=0)
sec.set_xticks([1,2,3,4,5,6,7,8],labels=['\n\n\n7.64 W/m³','\n\n\n76.49 W/m³','\n\n\n7.64 W/m³','\n\n\n76.49 W/m³',\
                                 '\n\n\n7.64 W/m³','\n\n\n76.49 W/m³','\n\n\n7.64 W/m³','\n\n\n76.49 W/m³'])
sec.tick_params('x',length=0,width=0)
sec2 = ax.secondary_xaxis(location=0)
sec2.set_xticks([-0.5,0.5,2.5,4.5,6.5])
sec2.tick_params('x',length=40,width=0.75)
labelsempty = [item.get_text() for item in sec2.get_xticklabels()]
empty_string_labels = ['']*len(labelsempty)
sec2.set_xticklabels(empty_string_labels)

for c in ax.containers:
    labels=[round(v.get_height(),2) if v.get_height() >0.11 else '' for v in c]
    ax.bar_label(c,labels=labels, label_type='center')
handles, labels = plt.gca().get_legend_handles_labels()
plt.legend(handles[::-1], labels[::-1] ,bbox_to_anchor=(1.05,1),loc='upper left')
plt.subplots_adjust(right=0.6)
plt.xticks(rotation=45)
plt.subplots_adjust(bottom=0.22)
plt.ylabel("Relative Abundance")
plt.xlabel("")

n = len(dft)
halfway = n*5/9
rect = plt.Rectangle((halfway - 0.5, 0), n - halfway, 1.1, color='gray', alpha=0.2)
ax.add_patch(rect)
textstr = 'Unacclimated'
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0.98, 0.98, textstr, transform=ax.transAxes, fontsize=12,
        verticalalignment='top', horizontalalignment='right', bbox=props)
textstr2 = 'Acclimated'
props2 = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0.02, 0.98, textstr2, transform=ax.transAxes, fontsize=12,
        verticalalignment='top', horizontalalignment='left', bbox=props)
ax.set_ylim(0, 1.1)
plt.savefig('MFW_MI_AccUnacc_16s.svg',dpi=1200,bbox_inches='tight')
plt.show()
# plt.show()
# # #H1
# # plt.rcParams["figure.figsize"] = (18,7)
# # index_ = df["Genus"]
# # df.index = index_
# # df = df.drop(columns="Genus")
# # dft = df.transpose()
# # dft = dft[dft.columns].apply(pd.to_numeric)
# # dft["Other"] = 1- dft[list(dft.columns)].sum(axis=1)
# # #change below code if unclutured or unassigned is included
# # dft["Other/Uncultured/Unassigned"] = dft["Other"]+dft["Unassigned"]+dft["uncultured"]
# # dft = dft.drop(columns = ['Other'])
# # dft = dft.drop(columns = ['Unassigned'])
# # dft = dft.drop(columns = ['uncultured'])
# # dft["Check"] = dft[list(dft.columns)].sum(axis=1)
# # #(0.37 W/m³)","Day 5 (67.92 W/m³)"
# # dft["Sample"] = ["Day 0","Day 2","Day 2","Day 4","Day 4","Day 8","Day 8"]
# # y1, y2,y3, y4,y5, y6,y7, y8,y9, y10 = dft[dft.columns[1]], dft[dft.columns[2]],dft[dft.columns[3]], dft[dft.columns[4]],dft[dft.columns[5]], dft[dft.columns[6]],\
# # dft[dft.columns[7]], dft[dft.columns[8]],dft[dft.columns[9]], dft[dft.columns[10]]

# # plt.rcParams["font.family"]= "Times New Roman"
# # plt.rcParams["font.size"] = 8

# # dft = dft.drop(columns="Check")
# # ax = dft.plot(x='Sample',kind='bar',stacked=True,rot=0)
# # sec = ax.secondary_xaxis(location=0)
# # sec.set_xticks([1,2,3,4,5,6],labels=['\n\n\n0.37 W/m³','\n\n\n67.92 W/m³','\n\n\n0.37 W/m³','\n\n\n67.92 W/m³','\n\n\n0.37 W/m³','\n\n\n67.92 W/m³'],rotation=0)
# # sec.tick_params('x',length=0,width=0)
# # sec2 = ax.secondary_xaxis(location=0)
# # sec2.set_xticks([-0.5,0.5,2.5,4.5])
# # sec2.tick_params('x',length=40,width=0.75)


# # for c in ax.containers:
# #     labels=[round(v.get_height(),2) if v.get_height() >0.09 else '' for v in c]
# #     ax.bar_label(c,labels=labels, label_type='center')
# # handles, labels = plt.gca().get_legend_handles_labels()
# # plt.legend(handles[::-1], labels[::-1] ,bbox_to_anchor=(1.05,1),loc='upper left')
# # plt.subplots_adjust(right=0.6)
# # plt.xticks(rotation=45)
# # plt.subplots_adjust(bottom=0.22)
# # plt.ylabel("Relative Abundance")
# # plt.xlabel("")
# # plt.savefig('16s_MFW_acc.png',dpi=1200)

# plt.show()
