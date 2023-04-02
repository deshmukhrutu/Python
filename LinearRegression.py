
import pandas as pd 
import seaborn as sns
df=pd.read_csv(r"C:\Users\dell\Downloads\SalaryData.csv")
print(df)
df.dropna()
print(df.columns)
X=df.drop(['Gender', 'Education Level', 'Job Title', 'Years of Experience'  ,'Salary'],axis=1 )
print(X)
X=X.fillna('34.0')
y=df['Salary']
y=y.fillna('45000.0')
print(y)
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=0.70)
print(X_train.shape)
from sklearn.linear_model import LinearRegression
lr=LinearRegression()
model=lr.fit(X_train,y_train)
print(model.intercept_)
print(model.coef_)
y_pred =model.predict(X_test)
m=sns.scatterplot(y_test,y_pred)
print(model.score(X_test,y_test))
