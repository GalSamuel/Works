#Comparison between low and high target groups - Violin Plots.
def violins(shortdf,longdf,target):
    sns.set_palette("OrRd", 2)
    left, width = .25, .5
    bottom, height = .25, .5
    right = left + width
    top = bottom + height
    
    for column in shortdf.drop(target, axis=1):
        if (column=="Max Out_Anim")|(column=="Max Out_Hot"):  #Max out variable was with -inf values, required a special treatment.
            m=scipy.stats.mannwhitneyu(shortdf[column][(shortdf[column]!=float('-inf'))&(shortdf[target]=="low")].dropna(),shortdf[column][(shortdf[column]!=float('-inf'))&(shortdf[target]=="high")].dropna())
            ax = sns.violinplot(x=target,y=column, data=shortdf[shortdf[column]!=float('-inf')])
            if m[1]<0.01:
                ax.text(0.5*(left+right), 0.8*(bottom+top), '**',horizontalalignment='center',verticalalignment='center',fontsize=20,transform=ax.transAxes)
            elif m[1]<0.05:
                ax.text(0.5*(left+right), 0.8*(bottom+top), '*',horizontalalignment='center',verticalalignment='center',fontsize=20,transform=ax.transAxes)
            plt.savefig("/Violin/"+target+"/"+column+'.png')
            plt.clf()
        elif column != 'ID':
            #ax = sns.catplot(x="Openness",y=column, data=dfab, kind="violin")  # Optional change in plot for different properties.
            m=scipy.stats.mannwhitneyu(shortdf[column][shortdf[target]=="low"].dropna(),shortdf[column][shortdf[target]=="high"].dropna())
            ax = sns.violinplot(x=target,y=column, data=shortdf)
            if m[1]<0.01:
                ax.text(0.5*(left+right), 0.8*(bottom+top), '**',horizontalalignment='center',verticalalignment='center',fontsize=20,transform=ax.transAxes)
            elif m[1]<0.05:
                ax.text(0.5*(left+right), 0.8*(bottom+top), '*',horizontalalignment='center',verticalalignment='center',fontsize=20,transform=ax.transAxes)
            plt.savefig("/Violin/"+target+"/"+column+'.png')
            plt.clf()
