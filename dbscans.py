from numpy._core.fromnumeric import shape
import numpy as np
import pandas as pd
def Euclidean_distance(x1,x2,y1,y2):
  return np.sqrt(np.square((x2-x1))+np.square((y2-y1)))
data_points=np.array([[4.5,8],[5,7],[6,6.5],[7,5],[9,4],[7,3],[8,3.5],[9,5],[4,4],[3,7.5],[4,6],[3.5,5]])

x,_=data_points.shape
matrix=np.zeros((x,x))
print(matrix)
for i in range(0,x):
 for j in range(0,x):
  distance=Euclidean_distance(data_points[i][0],data_points[j][0],data_points[i][1],data_points[j][1])
  matrix[i][j]=np.round(distance,2)
print(matrix)
#e=1.9
e=1.9
list=[]
for i in range (0,x):
  groups=[]
  center=data_points[i]
  groups.append(center)
  for j in range (0,x):
    if matrix[i][j]<e :
       if center[0]!=data_points[j][0] and center[1]!=data_points[j][1]:
        groups.append(data_points[j])
  
  list.append(groups)
#define min_points;
min_points=4
clusters=[]
for g in list:
  if len(g)>=min_points:
    clusters.append(g)
# print(clusters)
import matplotlib.pyplot as plt
colors = plt.cm.tab10  
for i in range(0,len(clusters)):
  for data in clusters[i]:

    plt.scatter(data[0],data[1],color=colors(i),label=f"cluster{i}")
plt.legend()
plt.title(" visualization of  clusters")
plt.show()
noise=[]
print(list)
for d in data_points:
  noise_chk=True
  for c in clusters:
    for d2 in c:
      if np.array_equal(d, d2):
        noise_chk=False
  if noise_chk==True:
    noise.append(d)
print(noise)

border=[]
for d in data_points:
  border_chk=True
  for g in clusters:
    for idx,data in g:
      if idx!=0 and np.array_equal(d,data):
        border_chk=False
  border.append(d)
print(border)
for g in clusters:
  for i in range(0,len(g)):
    
    if i==0:
       plt.scatter(g[i][0],g[i][1],color='red')
    else:
       plt.scatter(g[i][0],g[i][1],color='blue')
plt.title("visualisation of centers and borders")
plt.show()
for g in clusters:
  print(g)
plt.scatter(noise[0][0],noise[0][1])
plt.title("noise data_points")
plt.show()
``