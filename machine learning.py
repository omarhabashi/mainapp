import sklearn
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import xgboost as xgb
from sklearn.preprocessing import LabelEncoder
file_path=r'C:\Users\User\OneDrive\Desktop\data1\Mapped_L2N3.csv'
data=pd.read_csv(file_path)
data=data.drop(columns=['Date','location'])
data=data.drop(columns=data.columns[0])
print(data.isnull().sum())
print(data.dtypes)
x=data.drop(columns=['Weather type'])
y=data['Weather type']
x_encoded=pd.get_dummies(x)
x_train,x_test,y_train,y_test=train_test_split(x_encoded,y,test_size=0.25,random_state=42)

rf_classifier=RandomForestClassifier()
rf_classifier.fit(x_train, y_train)

svm_classifier= SVC()
svm_classifier.fit(x_train, y_train)




rf_predictions=rf_classifier.predict(x_test)
svm_predictions=svm_classifier.predict(x_test)

print("Random forest classifier report:")
print(classification_report(y_test,rf_predictions,zero_division=1))


print("small vector classification report :")
print(classification_report(y_test,svm_predictions,zero_division=1))

