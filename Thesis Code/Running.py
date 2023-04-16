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