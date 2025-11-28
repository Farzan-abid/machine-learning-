import pandas as pd
import  numpy as np
# import Matplot.lib as plt

data = {
    "Area (sqft)": [
        850, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700,
        1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700
    ],
    "Price (USD)": [
        120000, 130000, 150000, 165000, 180000, 200000, 220000, 240000, 260000, 280000,
        300000, 320000, 340000, 360000, 380000, 400000, 420000, 440000, 460000, 480000
    ]
}
data=pd.DataFrame(data)
data=np.array(data)
print(data)
X=data[:,0]
print(X)
#prices
Y=data[:,1].reshape(X.size,1)
X=np.vstack((np.ones((X.size,)),X)).T



def model(x,y,lr,iters):
    m=y.size
    theta=np.zeros((2,1))
    for i in range(iters):
        y_pred=np.dot(x,theta)
        cost=(1/(2*m)*np.sum(np.square(y_pred-y)))
        d_theta=(1/m)*np.dot(x.T,y_pred-y)
        theta=theta-lr*d_theta
    return theta

theta=model(X,Y,0.00001,100)
print(theta)





