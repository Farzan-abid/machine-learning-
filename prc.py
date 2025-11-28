import pandas as pd
import numpy as np
import matplotlib.pyplot as pt


class LG:
    def __init__(self,lr,epochs):
        self.lr=lr
        self.epochs=epochs
        self.weights=None
        self.bias=None
        
    def fit(self,X,Y):
        #initizlize weights
        self.weights=0
        #initialise bias
        self.bias=0
        for _ in range(self.epochs):
           
            #predict Y
            y_pred=(self.weights*X)+self.bias
        #calualate error
        #costfunction
            cost=(1/x.shape[0])*np.sum(np.square(y-y_pred))
        #calculate derivatives
            dw=(1/x.shape[0])*np.matmul(x.T,(y_pred-Y))
            db=(1/x.shape[0])*np.sum((y_pred-Y))
        #correct error 
            self.weights=self.weights-self.lr*dw
            self.bias=self.bias-self.lr*db
        #repeat
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

x=data[:,0]
y=data[:,1]

x=x.reshape((x.size,1))
y=y.reshape((y.size,1))
reg=LG(0.0000000001,10000)
reg.fit(x,y)
p=input("enter the area of house for prediction:")
print(f"Price:{int(reg.weights*float(p)+reg.bias)}")

# pt.scatter(x,y)
# # pt.plot(x,y)
# pt.show()

