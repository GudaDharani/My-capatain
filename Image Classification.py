import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
%matplotlib inline

data=pd.read_csv("https://github.com/GudaDharani/My-capatain/blob/master/mnist_test.csv")
print(data.head())
a=data.iloc[3,1:].values
a.reshape(28,28).reshape('uint8')
plt.imshow(a)
df_x=data.iloc[:,1:]
df_y=data.iloc[:,0]
x_train,x_test,y_train,y_test=train_test_split(df_x,df_y,test_size=0.2,random_state=4)
rf=RandomForestClassifier(n_estimators=100)
rf.fit(x_train,y_train)
pred=rf.predict(x_test)

s=y_test.values

count=0
for i in range(len(pred)):
    if(pred[i]==s[i]):
        count+=1

print("count=",count)
print("len(pred)=",len(pred))
print("% of accuracy =",count/pred)
