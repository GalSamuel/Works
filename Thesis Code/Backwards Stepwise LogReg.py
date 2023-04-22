#Backwards Stepwise Classification
def BackwardsStepwiseClass(dfab, target, to_drop=[]):
    """
    dfab = a dataframe with all features and the target variable.
    target = target (variable to be classified), variable with high/low values only.
    todrop = list of columns to be dropped.
    """
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import LeaveOneOut
    from sklearn.metrics import roc_curve, auc
    from sklearn.preprocessing import StandardScaler
    if len(todrop)>0:
        dfab=dfab.drop(todrop, axis=1)

    l=list(dfab.drop(target, axis=1).head(0))
    nl=l[:]
    temp=0
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

    loo = LeaveOneOut()
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
    plt.savefig("/ROC/"+target+'.png')
    plt.clf()
    return (temp,nl)
