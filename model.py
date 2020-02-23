


import pandas as pd
import XGBoost
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score
import pickle
 
train_data = pd.read_csv('/home/mihirduttaa/Documents/IsoHack/IsoHack/Dataset/Training.csv')
test_data = pd.read_csv('/home/mihirduttaa/Documents/IsoHack/IsoHack/Dataset/Testing.csv')
 
print('Shape of training data :',train_data.shape)
print('Shape of testing data :',test_data.shape)
 
train_x = train_data.drop(columns=['prognosis'],axis=1)
train_y = train_data['prognosis']
 
test_x = test_data.drop(columns=['prognosis'],axis=1)
test_y = test_data['prognosis']

model = XGBClassifier()
 
model.fit(train_x,train_y)
 
predict_train = model.predict(train_x)
print('\nTarget on train data',predict_train) 
 
accuracy_train = accuracy_score(train_y,predict_train)
print('\naccuracy_score on train dataset : ', accuracy_train)
 
predict_test = model.predict(test_x)
print('\nTarget on test data',predict_test) 
 
accuracy_test = accuracy_score(test_y,predict_test)
print('\naccuracy_score on test dataset : ', accuracy_test)


pickle.dump(regressor,open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))