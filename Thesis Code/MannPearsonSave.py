#Comparison between low and high target groups - Mann Whitney U
#Correlation between target (dependent/predicted) variable and features - Pearson's R.
def MannWhitneySave(shortdf,longdf,target):
    paper2 = pd.DataFrame({"Variable":[], "N":[], "r":[], "p-value":[], "Nlow":[], "Nhigh":[], "Mann-Whitney U":[], "p-value":[]})
    for column in shortdf.drop(target, axis=1):
        if (column=="Max Out_Anim")|(column=="Max Out_Hot"):
            m=scipy.stats.mannwhitneyu(shortdf[column][(shortdf[column]!=float('-inf'))&(shortdf[target]=="low")].dropna(),shortdf[column][(shortdf[column]!=float('-inf'))&(shortdf[target]=="high")].dropna())
            k=scipy.stats.pearsonr(longdf[target][(pd.notna(longdf[column]))&(longdf[column]!=float('-inf'))], longdf[column][(pd.notna(longdf[column]))&(longdf[column]!=float('-inf'))])
            llow=len(shortdf[column][shortdf[target]=="low"].dropna())
            lhigh=len(shortdf[column][shortdf[target]=="high"].dropna())
            N=len(longdf[target][(pd.notna(longdf[column])&(longdf[column]!=float('-inf')))])
            paper2.loc[len(paper2.index)] = [column, N, k[0], k[1], llow, lhigh, m[0], m[1]]
            #The following prints are (almost) ready text for thesis and paper:
            print(column+", Nlow="+str(llow)+", Nhigh="+str(lhigh)+", U={:.2f}".format(m[0])+", p={:.3f}".format(m[1]), end =", ")
            print(column+", N="+str(N)+", r={:.2f}".format(k[0])+", p={:.3f}".format(k[1]), end =", ")
        elif column != 'ID':
            m=scipy.stats.mannwhitneyu(shortdf[column][shortdf[target]=="low"].dropna(),shortdf[column][shortdf[target]=="high"].dropna())
            k=scipy.stats.pearsonr(longdf[target][pd.notna(longdf[column])], longdf[column][pd.notna(longdf[column])])
            llow=len(shortdf[column][shortdf[target]=="low"].dropna())
            lhigh=len(shortdf[column][shortdf[target]=="high"].dropna())
            N=len(longdf[target][pd.notna(longdf[column])])
            paper2.loc[len(paper2.index)] = [column, N, k[0], k[1], llow, lhigh, m[0], m[1]]
    #       #The following prints are (almost) ready text for thesis and paper:
            print(column+", Nlow="+str(llow)+", Nhigh="+str(lhigh)+", U={:.2f}".format(m[0])+", p={:.3f}".format(m[1]) , end =", ")
            print(column+", N="+str(N)+", r={:.2f}".format(k[0])+", p={:.3f}".format(k[1]) , end =", ")

    paper2.to_excel("/Violin/"+target+"/results.xlsx", sheet_name='results')
    return paper2
