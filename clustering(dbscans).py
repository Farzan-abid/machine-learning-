import numpy as np
import pandas as pd
from sklearn.datasets import make_blobs
data_points,labels=make_blobs(n_features=2,centers=3,n_samples=300)
# data_points,labels=make_blobs(n_features=2,n_samples=50,random_state=42,cluster_std=0.5)
import matplotlib.pyplot as plt
X=data_points
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
x_scaled=scaler.fit_transform(X)
plt.scatter(X[:,0],X[:,1],c=labels)

from sklearn.cluster import DBSCAN
model=DBSCAN(eps=2,min_samples=10,metric="euclidean")

d=[data_points[0:5]]
# print(d)
# print(d[:][0][:,0])
print(d[:][0][:,0])
plt.scatter(d[:][0][:,0],d[:][0][:,1],color="red")
plt.show()
l=model.fit_predict(data_points)

print(labels)
print(l)
