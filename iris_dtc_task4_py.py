# -*- coding: utf-8 -*-
"""Iris_DTC_task4.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1I2p5hWK_rpMjAUiyCxqx8soodObqbrjV
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("Iris.csv")

df

df.info()

df.describe()

df.isnull().sum()

from sklearn.preprocessing import LabelEncoder
lab=LabelEncoder()
df.iloc[:,-1]=lab.fit_transform(df.iloc[:,-1])

df

X=df.iloc[:,1:5].values
y=df.iloc[:,-1].values

print("Dependent Variables:", df.columns[1:5])
print("Target Variable:", df.columns[-1])

sns.pairplot(df,hue='Species')
plt.show()

plt.figure(figsize=(12,12))
plt.subplot(2,2,1)
sns.boxplot(x='Species',y='SepalLengthCm',data=df)
plt.subplot(2,2,2)
sns.boxplot(x="Species",y="SepalWidthCm",data=df)
plt.subplot(2,2,3)
sns.boxplot(x="Species",y="PetalLengthCm",data=df)
plt.subplot(2,2,4)
sns.boxplot(x="Species",y="PetalWidthCm",data=df)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)

print("X_train :",X_train.shape)
print("X_test :",X_test.shape)
print("y_train :",y_train.shape)
print("y_test :",y_test.shape)

from sklearn.tree import DecisionTreeClassifier
dct=DecisionTreeClassifier()
dct.fit(X_train,y_train)

dct.score(X_test,y_test)

y_pred=dct.predict(X_test)

y_pred

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)
cm

from sklearn import metrics

from sklearn.metrics import accuracy_score

print('Accuracy Score:', accuracy_score(y_test, y_pred))

from sklearn.tree import export_graphviz
export_graphviz(dct,out_file="tree.dot")

import graphviz
with open("tree.dot") as f:
 dot_graph = f.read()
 graphviz.Source(dot_graph)

from sklearn.externals.six import StringIO  
from IPython.display import Image  
import pydotplus

dot_data = StringIO()
export_graphviz(dct, out_file=dot_data, feature_names=df.columns[1:5],  
                filled=True, rounded=True
                )
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
Image(graph.create_png())

