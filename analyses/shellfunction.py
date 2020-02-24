#!/usr/bin/env python
# coding: utf-8

# In[1]:


op=''
def p1function(filename, clmns, op):
    import pandas as pd
    import seaborn as sns
    df = pd.read_csv(filename, usecols = clmns)
    op = str(input("What operation would you like to run on this data?:\nAverage(A), Maximum(MX), Minimum(MN), Standard Deviation(STD)\nType A, MX, MN, or STD"))
    if op == "A" or op == "a":
        avg = df.mean(axis=0)
        v1, v2 = df
        sns.lmplot(v1, v2, data=df,fit_reg=True) 
        print(avg)
    elif op == "MX" or op == "mx":
        mx = df.max(axis=0)
        v1, v2 = df
        sns.lmplot(v1, v2, data=df,fit_reg=True)
        print(mx)
    elif op == "MN" or op == "mn":
        mn = df.min(axis=0)
        v1, v2 = df
        sns.lmplot(v1, v2, data=df,fit_reg=True)
        print(mn)
    elif op == "STD" or op == "std":
        stdev = df.std(axis=0)
        v1, v2 = df
        sns.lmplot(v1, v2, data=df,fit_reg=True)
        print(stdev)
    else:
        print("Invalid Input")


# In[2]:


p1function('heart.csv', [0,3], op)


# In[ ]:




