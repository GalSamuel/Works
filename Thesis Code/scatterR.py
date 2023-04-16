#Plots scatter plots and computes r between target and dependant variables.
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