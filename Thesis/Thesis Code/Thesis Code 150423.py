import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy

comf=pd.read_csv("C:/Users/galsa/Desktop/תואר שני/תזה ומנחה/ניסוי 2/finalcomf.csv")
comf=comf.drop("Unnamed: 0", axis=1)


#Originality=MaxDist.groupby(["ID","prompt"]).mean("maxDist").groupby("ID").mean("maxDist").reset_index().drop('Unnamed: 0', axis=1)
GPTDist=pd.read_csv("C:/Users/galsa/Desktop/תואר שני/תזה ומנחה/ניסוי 2/AFTERGPT.csv")
Originality_GPT=GPTDist.groupby(["ID","prompt"]).max("originality").groupby("ID").mean("originality").reset_index()

#change ID for one participant-
#Originality["ID"][Originality["ID"]=="5c2a7509a4694800019815c7@email.prolific.co"]="5c2a7509a4694800019815c7"
Originality_GPT["ID"][Originality_GPT["ID"]=="5c2a7509a4694800019815c7@email.prolific.co"]="5c2a7509a4694800019815c7"

#comf=comf.merge(Originality,how="inner", on="ID")
comf=comf.merge(Originality_GPT,how="inner", on="ID")


dfAnim = pd.read_csv("C:/Users/galsa/Desktop/תואר שני/תזה ומנחה/ניסוי 2/AnimalStudy2.txt", sep='\t', encoding='ISO-8859-1')
dfHot = pd.read_csv("C:/Users/galsa/Desktop/תואר שני/תזה ומנחה/ניסוי 2/HotStudy2.txt", sep='\t', encoding='ISO-8859-1')

dfAnim["ID"]=comf["ID"]
dfHot["ID"]=comf["ID"]

dfAnim=dfAnim.drop(["2","3"], axis=1)
dfHot=dfHot.drop(["2","3"], axis=1)

#df = dfAnim.merge(dfHot,how="inner", on="ID", suffixes=('_Anim', '_Hot'))
#df=df.merge(comf,how="inner", on="ID")

dfsemdis=pd.read_csv("C:/Users/galsa/Desktop/תואר שני/תזה ומנחה/ניסוי 2/dfstart.csv")
#%%
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy

#extracting the 3 columns and creating new table
d={x:[] for x in range(1,51)}
dfsemdis= pd.read_csv("C:/Users/galsa/Desktop/תואר שני/תזה ומנחה/ניסוי 2/Afteredit.csv")
dfsemdisn = pd.DataFrame({"ID":[], "Object":[], "Response":[]})
dfsemdis["ID"][dfsemdis["ID"]=="5c2a7509a4694800019815c7@email.prolific.co"]="5c2a7509a4694800019815c7"
#Sub. 5c9604d579a68c0001a16496 didn't reply AUT
dfsemdis=dfsemdis[dfsemdis["ID"]!="5c9604d579a68c0001a16496"]
prog=0
remlist=[]
comf=dfsemdis.loc[:,"ID":"Q358_First Click"]
comf=comf.iloc[2:]

for i in dfsemdis["ID"].values[2:]:
    prog+=1
    if prog%24==0:
        print("Done "+str(round((prog+1)*100/len(dfsemdis["ID"].values[2:])))+"%")
    for j in dfsemdis.columns:
        if (("Belt" in j) | ("pencil" in j) | ("Broom" in j))&(j not in remlist):
            remlist.append(j)
        
        if pd.notna(dfsemdis[j][dfsemdis["ID"]==i].values[0]):
            if ("Belt" in j):
                dfsemdisn.loc[len(dfsemdisn.index)] = [i,"Belt",dfsemdis[j][dfsemdis["ID"]==i].values[0]]
            elif ("pencil" in j):
                dfsemdisn.loc[len(dfsemdisn.index)]= [i,"Pencil",dfsemdis[j][dfsemdis["ID"]==i].values[0]]
            elif ("Broom" in j):
                dfsemdisn.loc[len(dfsemdisn.index)]= [i,"Broom",dfsemdis[j][dfsemdis["ID"]==i].values[0]]
print("Done "+str(round((prog+1)*100/len(dfsemdis["ID"].values[2:])))+"%!")

count=1
count2=1
HotRes=dfsemdis[["ID",]].iloc[2:]
AnimalRes=dfsemdis[["ID",]].iloc[2:]
for j in dfsemdis.columns:
    if "Hot" in j:
        HotRes["Hot_"+str(count)]=dfsemdis[j].iloc[2:]
        remlist.append(j)
        count+=1
    elif "Anim" in j:
        AnimalRes["Animal_"+str(count2)]=dfsemdis[j].iloc[2:]
        remlist.append(j)
        count2+=1
comf=comf.drop(remlist, axis=1)

#AnimalRes.to_csv('animal_synonyms.csv')
#HotRes.to_csv('hot_synonyms.csv')
#After editing in Excel, came back to edit to ready for Mathematica -
#AnimalRes=pd.read_csv("C:/Users/galsa/Desktop/תואר שני/תזה ומנחה/ניסוי 2/animal_synonyms.csv")
#HotRes=pd.read_csv("C:/Users/galsa/Desktop/תואר שני/תזה ומנחה/ניסוי 2/hot_synonyms.csv")
#AnimalRes=AnimalRes.fillna("NA")
#HotRes=HotRes.fillna("NA")
#AnimalRes.to_csv("C:/Users/galsa/Desktop/תואר שני/תזה ומנחה/ניסוי 2/animal_synonyms.csv")
#HotRes.to_csv("C:/Users/galsa/Desktop/תואר שני/תזה ומנחה/ניסוי 2/hot_synonyms.csv")
#comf.to_csv("C:/Users/galsa/Desktop/תואר שני/תזה ומנחה/ניסוי 2/comf.csv")
#dfsemdis.to_csv("C:/Users/galsa/Desktop/תואר שני/תזה ומנחה/ניסוי 2/dfstart.csv")
dfsemdis=pd.read_csv("C:/Users/galsa/Desktop/תואר שני/תזה ומנחה/ניסוי 2/dfstart.csv")
#%%
#dfsemdisn.rename(columns = {'Object':'prompt',"Response":"response"}, inplace = True)
#dfsemdisn.to_csv('s1_data_long.csv')

comf=pd.read_csv("C:/Users/galsa/Desktop/תואר שני/תזה ומנחה/ניסוי 2/comf.csv")

MaxDist=pd.read_csv("C:/Users/galsa/Desktop/תואר שני/תזה ומנחה/ניסוי 2/s1_data_long_maxDist.csv")
Originality=MaxDist.groupby(["ID","prompt"]).mean("maxDist").groupby("ID").mean("maxDist").reset_index().drop('Unnamed: 0', axis=1)
GPTDist=pd.read_csv("C:/Users/galsa/Desktop/תואר שני/תזה ומנחה/ניסוי 2/AFTERGPT.csv")
Originality_GPT=GPTDist.groupby(["ID","prompt"]).mean("originality").groupby("ID").mean("originality").reset_index()

#change ID for one participant-
Originality["ID"][Originality["ID"]=="5c2a7509a4694800019815c7@email.prolific.co"]="5c2a7509a4694800019815c7"
Originality_GPT["ID"][Originality_GPT["ID"]=="5c2a7509a4694800019815c7@email.prolific.co"]="5c2a7509a4694800019815c7"

comf=comf.merge(Originality,how="inner", on="ID")
comf=comf.merge(Originality_GPT,how="inner", on="ID")
#%%
# Curiosity
temp=0
remlist=[]
dfsemdis["Curiosity_Score"]=0
for j in dfsemdis["ID"].values[2:]: 
    temp=0
    for i in list(range(22)):
        if (i+1)!=9:
            if i+1<10:
                z='Q10'+str(i+1)
                temp+=int(dfsemdis[z][dfsemdis["ID"]==j])
            elif i+1>9:
                z='Q1'+str(i+1)
                temp+=int(dfsemdis[z][dfsemdis["ID"]==j])
        else:
            temp=temp+(5-int(dfsemdis['Q109'][dfsemdis["ID"]==j]))
            remlist.append('Q109')
        if j==dfsemdis["ID"].iloc[2]:
            remlist.append(z)
    dfsemdis["Curiosity_Score"][dfsemdis["ID"]==j]=temp/22
comf=comf.drop(remlist, axis=1)
comf=comf.merge(dfsemdis[["ID","Curiosity_Score"]],how="inner", on="ID")
#%% Intelligence
comf.loc[:,"Q332.1":"Q356.1"] #letters
check=comf.loc[:,"Q3":"Q17"] #numbers
CfCorrect=["b", "c", "b", "d", "e", "b", "d", "b", "f", "c", "b", "b", "e"]
NumberCorrect=[1, 1, 5, 1, 3, 2, 1, 1, 4, 4, 3, 3, 4, 5, 2]

count=0
remlist=[]
for i in comf.loc[:,"Q3":"Q17"]:
    comf[i]=(comf[i]==NumberCorrect[count])
    count+=1
    remlist.append(i)
comf["IntNumScore"]=comf.loc[:,"Q3":"Q17"].sum(axis=1)/15

count=0
for i in comf.loc[:,"Q332.1":"Q356.1"]:
    comf[i]=(comf[i].str.lower()==CfCorrect[count])
    count+=1
    remlist.append(i)
comf["CfScore"]=comf.loc[:,"Q332.1":"Q356.1"].sum(axis=1)/13

comf=comf.drop(remlist, axis=1)
#%% Creativity Questionnaire

comf["Creativity"]=0
comf["Creativity"]=comf.loc[:,"Q330_1":"Q330_6"].fillna(0).astype(int).sum(axis=1)
comf["Creativity"]=comf["Creativity"]+comf.loc[:,"Q336_1":"Q336_6"].fillna(0).astype(int).sum(axis=1)
comf["Creativity"]=comf["Creativity"]+comf.loc[:,"Q342_1":"Q342_6"].fillna(0).astype(int).sum(axis=1)
comf["Creativity"]=comf["Creativity"]+comf.loc[:,"Q348_1":"Q348_6"].fillna(0).astype(int).sum(axis=1)
comf["Creativity"]=comf["Creativity"]+comf.loc[:,"Q354_1":"Q354_6"].fillna(0).astype(int).sum(axis=1)
comf["Creativity"]=comf["Creativity"]+comf.loc[:,"Q360_1":"Q360_6"].fillna(0).astype(int).sum(axis=1)
comf["Creativity"]=comf["Creativity"]+comf.loc[:,"Q366_1":"Q366_6"].fillna(0).astype(int).sum(axis=1)
comf["Creativity"]=comf["Creativity"]+comf.loc[:,"Q372_1":"Q372_6"].fillna(0).astype(int).sum(axis=1)

comf[["Q332","Q338","Q344","Q350","Q356","Q362","Q368","Q374"]]=comf[["Q332","Q338","Q344","Q350","Q356","Q362","Q368","Q374"]].fillna('s')
y=""
total=0
for j in comf["ID"]:
    for i in comf[["Q332","Q338","Q344","Q350","Q356","Q362","Q368","Q374"]].columns:
        for x in comf[i][comf["ID"]==j].values[0]:
            if x.isdigit():
                if y.isdigit():
                    total+=10
                else:
                    total+=int(x)
            y=x
    comf["Creativity"][comf["ID"]==j]=comf["Creativity"]+total
    total=0
    
comf=comf.drop(comf[comf.loc[:,"Q330_1":"Q358_First Click"].columns], axis=1)

#%% Getting FF ready to analyse
Bear=comf.loc[:,"ID":"FF Table_19"]
Table=Bear.drop(Bear.loc[:,"Informed Consent":"Q400_Click Count"].columns, axis=1)
Candle=Bear.drop(Bear.loc[:,"Informed Consent":"Q398_Click Count"].columns, axis=1)
Candle=Candle.drop(Candle.loc[:,"Q400_First Click":], axis=1)
Bear=Bear.drop(Bear.loc[:,"Q398_First Click":].columns, axis=1)
Bear=Bear.drop(["Informed Consent"], axis=1)

for i in range(len(Bear.columns)-1):
    Bear.iloc[:,i+1]=Bear.iloc[:,i+1].str.lower()
    Candle.iloc[:,i+1]=Candle.iloc[:,i+1].str.lower()
    Table.iloc[:,i+1]=Table.iloc[:,i+1].str.lower()
    
#Bear.to_csv('bear.csv')
#Candle.to_csv('candle.csv')
#Table.to_csv('table.csv')

comf=comf.drop(comf.loc[:,"FF Bear_1":"FF Table_19"].columns, axis=1)
comf=comf.drop(comf.iloc[:,1:6].columns, axis=1)
#%% Personality Questionnaire
revdict=[1,0,0,1,0,0,1,1,0,1,1,0,0,1,0,0,1,1,0,1,1,0,0,1,0,0,1,1,0,1,0,1,1,0,1,1,0,0,1,0,0,1,1,0,1,1,0,0,1,0,0,1,1,0,1,1,0,0,1,0,1,0,0,1,0,0,1,1,0,1,1,0,0,1,0,0,1,1,0,1,1,0,0,1,0,0,1,1,0,1,0,1,1,0,1,1,0,0,1,0,0,1,1,0,1,1,0,0,1,0,0,1,1,0,1,1,0,0,1,0,1,0,0,1,0,0,1,1,0,1,0,0,0,1,0,0,1,1,0,1,1,0,0,1,0,0,1,1,0,1,0,0,1,0,1,1,0,0,1,0,0,1,1,0,0,1,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,1,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,1,1,0,0,0,0,1,0,0,0,0,0,1,1,0,1,0,0,0,0,0,1,1,0,1,0,0,1,0,1,0,1,0,0]
Pers=comf.loc[:,"ID":"240_NEO Replies"]

#for i in range(len(Pers.columns)-1):
#    if revdict[i]==1:
#        Pers.iloc[:,i+1]=6-Pers.iloc[:,i+1]

#Pers.to_csv("C:/Users/galsa/Desktop/תואר שני/תזה ומנחה/ניסוי 2/Pers.csv")

Pers=pd.read_csv("C:/Users/galsa/Desktop/תואר שני/תזה ומנחה/ניסוי 2/analyzing_NEO-240.csv")
Pers=Pers.drop(Pers.iloc[:,1:-5], axis=1)
#%% comf empt
comf=comf.drop(comf.loc[:,"Fluency Anim rep_1":"Q14_Click Count"].columns, axis=1)
comf=comf.drop(comf.loc[:,"1_NEO Replies":"240_NEO Replies"],axis=1)
#%%
#Importing after Mathematica data

dfAnim = pd.read_csv("C:/Users/galsa/Desktop/תואר שני/תזה ומנחה/ניסוי 2/AnimalStudy2.txt", sep='\t', encoding='ISO-8859-1')
dfHot = pd.read_csv("C:/Users/galsa/Desktop/תואר שני/תזה ומנחה/ניסוי 2/HotStudy2.txt", sep='\t', encoding='ISO-8859-1')

dfAnim["ID"]=comf["ID"]
dfHot["ID"]=comf["ID"]

dfAnim=dfAnim.drop(["2","3"], axis=1)
dfHot=dfHot.drop(["2","3"], axis=1)
#df=df.merge(dfopen, how='inner', on='ID')

#%% FF
FFBear = pd.read_csv("C:/Users/galsa/Desktop/תואר שני/תזה ומנחה/ניסוי 2/bear_all_FF.csv")
FFCandle = pd.read_csv("C:/Users/galsa/Desktop/תואר שני/תזה ומנחה/ניסוי 2/candle_all_FF.csv")
FFTable = pd.read_csv("C:/Users/galsa/Desktop/תואר שני/תזה ומנחה/ניסוי 2/table_all_FF.csv")

FFBear=FFBear.rename(columns={"FF_MEAN": "FFBear"})
FFCandle=FFCandle.rename(columns={"FF_MEAN": "FFCandle"})
FFTable=FFTable.rename(columns={"FF_MEAN": "FFTable"})

comf=comf.merge(FFBear[["ID","FFBear"]],how="outer", on="ID")
comf=comf.merge(FFCandle[["ID","FFCandle"]],how="outer", on="ID")
comf=comf.merge(FFTable[["ID","FFTable"]],how="outer", on="ID")
#%%
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy

comf=pd.read_csv("C:/Users/galsa/Desktop/תואר שני/תזה ומנחה/ניסוי 2/finalcomf.csv")
comf=comf.drop("Unnamed: 0", axis=1)
#comf=comf.merge(Pers,how="inner", on="ID")
comf["FF"]=(comf["FFBear"]+comf["FFTable"]+comf["FFCandle"])/3
comf=comf.drop(["FFBear","FFTable","FFCandle"], axis=1)

comf["Int"]=(comf["IntNumScore"]+comf["CfScore"])/2
comf=comf.drop(["IntNumScore","CfScore"], axis=1)

#%%
#changing to numeric if possible, if not, change to nan
#comf.to_csv("C:/Users/galsa/Desktop/תואר שני/תזה ומנחה/ניסוי 2/finalcomf.csv")

for column in dfAnim.loc[:,"Number of Responses":]:
    dfAnim[column]=pd.to_numeric(dfAnim[column],errors='coerce')
for column in dfHot.loc[:,"Number of Responses":]:        
    dfHot[column]=pd.to_numeric(dfHot[column],errors='coerce')
    #print(scipy.stats.normaltest(df[column], nan_policy='omit')[1])
#change bool to int
dfAnim["Fraction of Incorrect Spellings"]=dfAnim["Fraction of Incorrect Spellings"].astype(int)
dfAnim["Start in LVC"]=dfAnim["Start in LVC"].astype(int)
dfHot["Fraction of Incorrect Spellings"]=dfAnim["Fraction of Incorrect Spellings"].astype(int)
dfHot["Start in LVC"]=dfAnim["Start in LVC"].astype(int)

dfAnim["Max Out"][dfAnim["Max Out"]==float('-inf')]
dfHot["Max Out"][dfHot["Max Out"]==float('-inf')]

print(dfAnim.shape)
print(dfHot.shape)
#%% This is where I am
df = dfAnim.merge(dfHot,how="inner", on="ID", suffixes=('_Anim', '_Hot'))
df=df.merge(comf,how="inner", on="ID")

#%%
#high and low 30% Creativity in descending order
df=df.sort_values('maxDist',ascending=False)
num30per=int(df.shape[0]*.3)
a=df.head(num30per)
a["maxDist"]='high'
b=df.tail(num30per)
b["maxDist"]='low'
dfab1=b.append(a)
dfab1=dfab1.merge(dfsemdis[["ID","Age","Sex"]], how="inner", on="ID")
dfab1["Age"]=pd.to_numeric(dfab1["Age"],errors='coerce')
dfab1["Sex"]=pd.to_numeric(dfab1["Sex"],errors='coerce')


df=df.sort_values('Creativity',ascending=False)
num30per=int(df.shape[0]*.3)
a=df.head(num30per)
a["Creativity"]='high'
b=df.tail(num30per)
b["Creativity"]='low'
dfab2=b.append(a)
dfab2=dfab2.merge(dfsemdis[["ID","Age","Sex"]], how="inner", on="ID")
dfab2["Age"]=pd.to_numeric(dfab2["Age"],errors='coerce')
dfab2["Sex"]=pd.to_numeric(dfab2["Sex"],errors='coerce')

df=df.sort_values('o_neo',ascending=False)
num30per=int(df.shape[0]*.3)
a=df.head(num30per)
a['o_neo']='high'
b=df.tail(num30per)
b['o_neo']='low'
dfab3=b.append(a)
dfab3=dfab3.merge(dfsemdis[["ID","Age","Sex"]], how="inner", on="ID")
dfab3["Age"]=pd.to_numeric(dfab3["Age"],errors='coerce')
dfab3["Sex"]=pd.to_numeric(dfab3["Sex"],errors='coerce')

df=df.sort_values('originality',ascending=False)
num30per=int(df.shape[0]*.3)
a=df.head(num30per)
a['originality']='high'
b=df.tail(num30per)
b['originality']='low'
dfab4=b.append(a)
dfab4=dfab4.merge(dfsemdis[["ID","Age","Sex"]], how="inner", on="ID")
dfab4["Age"]=pd.to_numeric(dfab4["Age"],errors='coerce')
dfab4["Sex"]=pd.to_numeric(dfab4["Sex"],errors='coerce')

df=df.sort_values('Int',ascending=False)
num30per=int(df.shape[0]*.3)
a=df.head(num30per)
a['Int']='high'
b=df.tail(num30per)
b['Int']='low'
dfab5=b.append(a)
dfab5=dfab5.merge(dfsemdis[["ID","Age","Sex"]], how="inner", on="ID")
dfab5["Age"]=pd.to_numeric(dfab5["Age"],errors='coerce')
dfab5["Sex"]=pd.to_numeric(dfab5["Sex"],errors='coerce')
#%%
#plotting the violin plots including or excluding */** for significance, printing and saving mann whitney and pearson data
def manviolin(shortdf,longdf,target):
    sns.set_palette("OrRd", 2)
    left, width = .25, .5
    bottom, height = .25, .5
    right = left + width
    top = bottom + height
    paper2 = pd.DataFrame({"Variable":[], "N":[], "r":[], "p-value":[], "Nlow":[], "Nhigh":[], "Mann-Whitney U":[], "p-valueM":[]})
    
    for column in shortdf.drop(target, axis=1):
        if (column=="Max Out_Anim")|(column=="Max Out_Hot"):
            m=scipy.stats.mannwhitneyu(shortdf[column][(shortdf[column]!=float('-inf'))&(shortdf[target]=="low")].dropna(),shortdf[column][(shortdf[column]!=float('-inf'))&(shortdf[target]=="high")].dropna())
            k=scipy.stats.pearsonr(longdf[target][(pd.notna(longdf[column]))&(longdf[column]!=float('-inf'))], longdf[column][(pd.notna(longdf[column]))&(longdf[column]!=float('-inf'))])
            llow=len(shortdf[column][shortdf[target]=="low"].dropna())
            lhigh=len(shortdf[column][shortdf[target]=="high"].dropna())
            N=len(longdf[target][(pd.notna(longdf[column])&(longdf[column]!=float('-inf')))])
            paper2.loc[len(paper2.index)] = [column, N, k[0], k[1], llow, lhigh, m[0], m[1]]
            print(column+", Nlow="+str(llow)+", Nhigh="+str(lhigh)+", U={:.2f}".format(m[0])+", p={:.3f}".format(m[1]), end =", ")
            print(column+", N="+str(N)+", r={:.2f}".format(k[0])+", p={:.3f}".format(k[1]), end =", ")
            #ax = sns.violinplot(x=target,y=column, data=shortdf[shortdf[column]!=float('-inf')])
            #if m[1]<0.01:
            #    ax.text(0.5*(left+right), 0.8*(bottom+top), '**',horizontalalignment='center',verticalalignment='center',fontsize=20,transform=ax.transAxes)
            #elif m[1]<0.05:
            #    ax.text(0.5*(left+right), 0.8*(bottom+top), '*',horizontalalignment='center',verticalalignment='center',fontsize=20,transform=ax.transAxes)
            #plt.savefig("C:/Users/galsa/Desktop/תואר שני/תזה ומנחה/ניסוי 2/Violin/"+target+"/"+column+'.png')
            #plt.clf()
        elif column != 'ID':
            #ax = sns.catplot(x="Openness",y=column, data=dfab, kind="violin")
            m=scipy.stats.mannwhitneyu(shortdf[column][shortdf[target]=="low"].dropna(),shortdf[column][shortdf[target]=="high"].dropna())
            k=scipy.stats.pearsonr(longdf[target][pd.notna(longdf[column])], longdf[column][pd.notna(longdf[column])])
            llow=len(shortdf[column][shortdf[target]=="low"].dropna())
            lhigh=len(shortdf[column][shortdf[target]=="high"].dropna())
            N=len(longdf[target][pd.notna(longdf[column])])
            paper2.loc[len(paper2.index)] = [column, N, k[0], k[1], llow, lhigh, m[0], m[1]]
    #        Print the text for paper, initial analysis:
            print(column+", Nlow="+str(llow)+", Nhigh="+str(lhigh)+", U={:.2f}".format(m[0])+", p={:.3f}".format(m[1]) , end =", ")
            print(column+", N="+str(N)+", r={:.2f}".format(k[0])+", p={:.3f}".format(k[1]) , end =", ")
            #ax = sns.violinplot(x=target,y=column, data=shortdf)
            #if m[1]<0.01:
            #    ax.text(0.5*(left+right), 0.8*(bottom+top), '**',horizontalalignment='center',verticalalignment='center',fontsize=20,transform=ax.transAxes)
            #elif m[1]<0.05:
            #    ax.text(0.5*(left+right), 0.8*(bottom+top), '*',horizontalalignment='center',verticalalignment='center',fontsize=20,transform=ax.transAxes)
            #plt.savefig("C:/Users/galsa/Desktop/תואר שני/תזה ומנחה/ניסוי 2/Violin/"+target+"/"+column+'.png')
            #plt.clf()

    paper2.to_excel("C:/Users/galsa/Desktop/תואר שני/תזה ומנחה/ניסוי 2/Violin/"+target+"/results.xlsx", sheet_name='resultsGPT')
    return paper2
    
#manviolin(dfab4.loc[:, :'originality'],df,'originality')
#%%
#plotting the scatter plots
def scat(df,target):
    sns.set_palette("RdYlGn", 3)
    for column in df:
        if (column!='Max Out_Anim')&(column!='Max Out_Hot')&(column!=target)&(column!='ID'):
            ax = sns.regplot(x=target,y=column, data=df)
            k=scipy.stats.pearsonr(df[target][pd.notna(df[column])], df[column][pd.notna(df[column])])
            #       Remove sulamit for text on plot:
            ax.text(0.02, 0.98, "r={:.2f}".format(k[0]), horizontalalignment="left", verticalalignment="top",transform=ax.transAxes, fontsize=12, weight="bold", style='italic')
            ax.text(0.02, 0.90, "p-value={:.3f}".format(k[1]), horizontalalignment="left", verticalalignment="top",transform=ax.transAxes, fontsize=12, weight="bold", style='italic')
            #ax.text(0.02, 0.94, "r^2={:.4f}".format(k[0]**2), ha="left", va="top",transform=ax.transAxes)
            plt.savefig("C:/Users/galsa/Desktop/תואר שני/תזה ומנחה/ניסוי 2/Scatter/"+target+"/"+column+'.png')
            plt.clf()
        
    ax = sns.regplot(x=target,y="Max Out_Anim", data=df[df["Max Out_Anim"]!=float("-inf")])
    k=scipy.stats.pearsonr(df[target][df["Max Out_Anim"]!=float("-inf")], df[column][df["Max Out_Anim"]!=float("-inf")])
    ax.text(0.02, 0.98, "r={:.2f}".format(k[0]), ha="left", va="top",transform=ax.transAxes, weight="bold", fontsize=12, style='italic')
    ax.text(0.02, 0.90, "p-value={:.3f}".format(k[1]), ha="left", va="top",transform=ax.transAxes, weight="bold", fontsize=12, style='italic')
    plt.savefig("C:/Users/galsa/Desktop/תואר שני/תזה ומנחה/ניסוי 2/Scatter/"+target+"/"+"Max Out_Anim"+'.png')
    plt.clf()
    ax = sns.regplot(x=target,y="Max Out_Hot", data=df[df["Max Out_Hot"]!=float("-inf")])
    k=scipy.stats.pearsonr(df[target][df["Max Out_Hot"]!=float("-inf")], df[column][df["Max Out_Hot"]!=float("-inf")])
    ax.text(0.02, 0.98, "r={:.2f}".format(k[0]), horizontalalignment="left", verticalalignment="top",transform=ax.transAxes, weight="bold", fontsize=12, style='italic')
    ax.text(0.02, 0.90, "p-value={:.3f}".format(k[1]), horizontalalignment="left", verticalalignment="top",transform=ax.transAxes, weight="bold", fontsize=12, style='italic')
    plt.savefig("C:/Users/galsa/Desktop/תואר שני/תזה ומנחה/ניסוי 2/Scatter/"+target+"/"+"Max Out_Hot"+'.png')
    plt.clf()

#%% Backwards Stepwise regression, by MSE
from sklearn import linear_model
from sklearn.model_selection import LeaveOneOut
from scipy.stats import pearsonr
from sklearn.model_selection import cross_val_score
def BackwardsStepwise(df, target, hotoranimal):
    from sklearn.preprocessing import StandardScaler
    scaler=StandardScaler()
    sns.set_palette("RdYlGn", 3)
    if hotoranimal=="hot":
        df=df.drop(df.loc[:,"Number of Responses_Anim":"Norm2_Anim"], axis=1)
        df=df.drop(["Max Out_Hot", "Median Out_Hot"], axis=1)
    elif hotoranimal=="animal":
        df=df.drop(df.loc[:,"Number of Responses_Hot":"Norm2_Hot"], axis=1)
        df=df.drop(["Max Out_Anim", "Median Out_Anim"], axis=1)
    else:
        return("wrong input, enter either hot or animal")
    tor=["maxDist","Creativity","o_neo","originality", "Int"]
    tor.remove(target)
    df=df.drop(tor, axis=1)
    featurespred=df
    featurespred=featurespred.drop(["ID",target], axis=1).dropna()
    featurespred=featurespred[featurespred!="Indeterminate"]
    featurespred=featurespred[featurespred!='1.*Entropy[False[[False,False]]]']
    l=list(featurespred.head(0))
    loo = LeaveOneOut()
    nl=l[:]
    temp=6000
    count=0
    count1=0
    save1=[]
    save2=[]
    for j in range(len(l)):
        for i in l:
            nl1=nl[:]
            nl1.remove(i)
            nl1.append(target)
            lp2=[]
            lr2=[]
            df[nl1]=scaler.fit_transform(df[nl1])
            if len(nl1)>1:
                X=df[nl1].dropna()
                Y = X[target]
                X=X.drop(target, axis=1)
                X=np.array(X)
            else:
                print("kazabubu")
                break
            Y=Y.astype('float')
            Y = np.array(Y)
            regressor = linear_model.LinearRegression()
            predictions = []
            actual = []
            for train_index, test_index in loo.split(X):
                X_train, X_test = X[train_index], X[test_index]
                Y_train, Y_test = Y[train_index], Y[test_index]       
                prediction = regressor.fit(X_train, Y_train).predict(X_test)
                predictions.extend(prediction)
                actual.extend(Y_test)
            temp1=temp
        #temp=pearsonr(predictions, actual)[1]
            temp=np.mean((np.array(actual)-np.array(predictions))**2)
            if temp<temp1:
                best=i
                count1=1
                print("average p = {:.6f}".format(pearsonr(predictions, actual)[1]))
                print("average r = {:.4f}".format(abs(pearsonr(predictions, actual)[0])))
                print("loss = {:.4f}".format(np.mean((np.array(actual)-np.array(predictions))**2)))
                save1=predictions
                save2=actual
            else:
                temp=temp1
        if count1==1:
            print(best)
            nl.remove(best)
            l.remove(best)
        else:
            forp=pd.DataFrame()
            forp["Actual"]=save2
            forp["Predictions"]=save1
            ax = sns.regplot(x="Actual",y="Predictions", data=forp)
            ax.text(0.02, 0.98, "r={:.2f}".format(pearsonr(save1, save2)[0]), horizontalalignment="left", verticalalignment="top",transform=ax.transAxes, fontsize=12, weight="bold", style='italic')
            if pearsonr(save1, save2)[1]<0.001:
                ax.text(0.02, 0.90, "p-value<.001", horizontalalignment="left", verticalalignment="top",transform=ax.transAxes, fontsize=12, weight="bold", style='italic')
            else:
                ax.text(0.02, 0.90, "p-value={:.3f}".format(pearsonr(save1, save2)[1]), horizontalalignment="left", verticalalignment="top",transform=ax.transAxes, fontsize=12, weight="bold", style='italic')
            plt.savefig("C:/Users/galsa/Desktop/תואר שני/תזה ומנחה/ניסוי 2/Scatter/"+target+"/"+hotoranimal+"_.png")
            plt.clf()
            return (temp, pearsonr(save1, save2)[0], pearsonr(save1, save2)[1], nl)
        count1=0
    predictions=save1
    actual=save2
    print("Here")
    return (temp, save1, save2, nl)
    
#%% Backwards Stepwise Log Regression, classification model

def BackwardsStepwiseClass(dfab,target, hotoranimal):
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import LeaveOneOut
    from sklearn.metrics import roc_curve, auc
    from sklearn.preprocessing import StandardScaler
    if hotoranimal=="hot":
        dfab=dfab.drop(dfab.loc[:,"Number of Responses_Anim":"Norm2_Anim"], axis=1)
        dfab=dfab.drop(["Max Out_Hot", "Median Out_Hot"], axis=1)
    elif hotoranimal=="animal":
        dfab=dfab.drop(dfab.loc[:,"Number of Responses_Hot":"Norm2_Hot"], axis=1)
        dfab=dfab.drop(["Max Out_Anim", "Median Out_Anim"], axis=1)
    else:
        return("wrong input, enter either hot or animal")
    featuresclass=dfab
    featuresclass=featuresclass.drop(["ID","maxDist", "Creativity", "o_neo","originality", "Int"], axis=1).dropna()
    featuresclass=featuresclass[featuresclass!="Indeterminate"]
    l=list(featuresclass.head(0))
    loo = LeaveOneOut()
    nl=l[:]
    temp=0
    count=0
    count1=0
    nl.append(target)
    dfab[target][dfab[target]=='high']=1
    dfab[target][dfab[target]=='low']=0
    scaler=StandardScaler()
    dfab[nl]=scaler.fit_transform(dfab[nl])
    X=dfab[nl].dropna()
    Y = X[target]
    X=X.drop(target, axis=1)
    X=np.array(X)
    nl.remove(target)
    Y=Y.astype('float')
    Y = np.array(Y)
    classifier = LogisticRegression(max_iter=1000)
    predictions = []
    actual = []
    for train_index, test_index in loo.split(X):
        X_train, X_test = X[train_index], X[test_index]
        Y_train, Y_test = Y[train_index], Y[test_index]       
        prediction = classifier.fit(X_train, Y_train).predict_proba(X_test)
        predictions.extend(prediction[:,1])
        actual.extend(Y_test)
    fpr, tpr, t = roc_curve(actual, predictions)
    roc_auc = auc(fpr, tpr)
    
    for j in range(len(l)):
        for i in l:
            nl1=nl[:]
            nl1.remove(i)
            nl1.append(target)
            lp2=[]
            lr2=[]
            if len(nl1)>1:
                X=dfab[nl1].dropna()
                Y = X[target]
                X=X.drop(target, axis=1)
                X=np.array(X)
            else:
                print("kazabubu")
                break
            Y=Y.astype('float')
            Y = np.array(Y)
            classifier = LogisticRegression(max_iter=1000)
            predictions = []
            actual = []
            for train_index, test_index in loo.split(X):
                X_train, X_test = X[train_index], X[test_index]
                Y_train, Y_test = Y[train_index], Y[test_index]       
                prediction = classifier.fit(X_train, Y_train).predict_proba(X_test)
                predictions.extend(prediction[:,1])
                actual.extend(Y_test)
            fpr, tpr, t = roc_curve(actual, predictions)
            roc_auc = auc(fpr, tpr)
            temp1=temp
            temp=roc_auc
            if temp>temp1:
                best=i
                count1=1
                print("roc_auc = {:.6f}".format(roc_auc))
            else:
                temp=temp1
        if count1==1:
            print(best)
            nl.remove(best)
            l.remove(best)
            save1=fpr
            save2=tpr
        else:
            break
        count1=0
    sns.set_palette("OrRd", 2)
    sns.set_palette("RdYlGn", 4)
    plt.figure()
    plt.plot(save1, save2)
    plt.plot([0, 1], [0, 1], 'k:') # create the diagonal line. k is for black color and : is for a dotted line style
    plt.xlim(0, 1.01)
    plt.ylim(0, 1.01)
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.savefig("C:/Users/galsa/Desktop/תואר שני/תזה ומנחה/ניסוי 2/ROC/"+target+"_"+hotoranimal+'.png')
    plt.clf()
    return (temp,nl)


#%%
[auc1,l1]=BackwardsStepwiseClass(dfab1,"maxDist", "animal")
[auc2,l2]=BackwardsStepwiseClass(dfab1,"maxDist", "hot")

[auc3,l3]=BackwardsStepwiseClass(dfab2,"Creativity", "animal")
[auc4,l4]=BackwardsStepwiseClass(dfab2,"Creativity", "hot")
[auc5,l5]=BackwardsStepwiseClass(dfab3,"o_neo", "animal")
[auc6,l6]=BackwardsStepwiseClass(dfab3,"o_neo", "hot")

[auc7,l7]=BackwardsStepwiseClass(dfab4,"originality", "animal")
[auc8,l8]=BackwardsStepwiseClass(dfab4,"originality", "hot")

[auc9,l9]=BackwardsStepwiseClass(dfab5,"Int", "animal")
[auc10,l10]=BackwardsStepwiseClass(dfab5,"Int", "hot")

#%%
[temp1, save11, save21, nl1]=BackwardsStepwise(df, "o_neo", "hot")
[temp2, save12, save22, nl2]=BackwardsStepwise(df, "maxDist", "hot")
[temp3, save13, save23, nl3]=BackwardsStepwise(df, "Creativity", "hot")
[temp4, save14, save24, nl4]=BackwardsStepwise(df, "o_neo", "animal")
[temp5, save15, save25, nl5]=BackwardsStepwise(df, "maxDist", "animal")
[temp6, save16, save26, nl6]=BackwardsStepwise(df, "Creativity", "animal")
#GPT
[temp7, save17, save27, nl7]=BackwardsStepwise(df, "originality", "animal")
[temp8, save18, save28, nl8]=BackwardsStepwise(df, "originality", "hot")
#intelligence
[temp9, save19, save29, nl7]=BackwardsStepwise(df, "Int", "animal")
[temp10, save20, save30, nl8]=BackwardsStepwise(df, "Int", "hot")