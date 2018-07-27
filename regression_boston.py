import numpy as np
import pandas as pd
df=pd.read_csv('boston.csv')
print('***************** DataFrame head')
print(df.head())
print('*****************DataFrame description')
print(df.describe())
X=df.drop('MEDV',axis=1)
y=df['MEDV']
import seaborn as sb
sb.heatmap(df.corr(),square=True,cmap='RdYlGn')
# RM has possitive correlation with MEDV while LSTAT,PTRATIO,CRIM,NX have negative correlation
# select RM, LSTAT, PTRATIO as feature
# MEDV as label
X=df[['RM','LSTAT','PTRATIO','CRIM','NX']].values
y=df['MEDV'].values

from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=0.3,random_state=42)

reg = linear_model.LinearRegression()
reg.fit(X_train,y_train)
y_pred=reg.predict(X_test)

print("R squared: {}".format(reg.score(X_test, y_test)))
rmse = np.sqrt(mean_squared_error(y_test,y_pred))
print("Root Mean Squared Error: {}".format(rmse))
y_pred.shape, X_test.shape
y_pred=y_pred.reshape(-1,1)
y_test=y_test.reshape(-1,1)
result=np.append(X_test,y_test,axis=1)
result=np.append(result,y_pred,axis=1)
print('********************compare Actual MEDV with Predicted MEDV')
print(pd.DataFrame(result,columns=['RM','LSTAT','PTRATIO','CRIM','NX','Actual MEDV','Predicted MEDV']))