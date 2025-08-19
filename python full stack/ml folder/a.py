import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model
from sklearn.model_selection import train_test_split
iris = pd.read_csv("iris.csv")
print(iris.shape)
print(iris.head())
iris
print(iris.species)
from sklearn import preprocessing
le= preprocessing.LabelEncoder()
le.fit(iris.species)
iris['species']=le.transform(iris.species)
print(iris)
print(iris.species)
X=iris.iloc[:,0:4]
y=iris.iloc[:,4]
y
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
sc=sc.fit(X)
X=sc.transform(X)
x_train,x_test,y_train,y_test=train_test_split(X,y,train_size=0.70,random_state=101)
from sklearn.neighbors import KNeighborsClassifier
ne=KNeighborsClassifier(n_neighbors=3)
ne.fit(x_train,y_train)
y_pred=ne.predict(x_test)
y_pred[:10]
import sklearn.metrics as metrics
confusion =metrics.confusion_matrix(y_true=y_test,y_pred=y_pred)
confusion
metrics.accuracy_score(y_true=y_test,y_pred=y_pred)
class_wise= metrics.classification_report(y_true=y_test,y_pred=y_pred)
print(class_wise)
