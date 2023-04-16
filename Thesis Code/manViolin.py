#Comparison between low and high target groups - Violin plots and Mann Whitney U.
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