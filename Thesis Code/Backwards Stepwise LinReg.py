#%% Backwards Stepwise regression, by MSE
def BackwardsStepwise(df, target, todrop=[]):
    from sklearn.preprocessing import StandardScaler
    from sklearn import linear_model
    from sklearn.model_selection import LeaveOneOut
    from scipy.stats import pearsonr
    from sklearn.model_selection import cross_val_score
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