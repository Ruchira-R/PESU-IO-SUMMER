import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn import preprocessing, datasets
from keras.utils import np_utils
#reading data
data=datasets.load_iris()
x_data=data.data[:,0:4]
y_data=data.target
#ONE HARD ENCODING
#encoder=preprocessing.LabelEncoder()
#encoder.fit(Y)
#Y_encoded=encoder.transform(Y)
Y_one_hot=np_utils.to_categorical(y_data)
#SPLITTING DATA INTO TRAINING AND TESTING SET
seed=5
X_train,X_test,Y_train,Y_test=train_test_split(x_data,Y_one_hot,test_size=0.33,random_state=seed)#test_size-HOW MUCH YOURE SENDING TO TRAIN AND TEST
#CREATING NN MODEL DENSE - CONNECTS ONE TO EVERYTHING SOFTMAX  - MAX PROBABILITY TOTAL THING GETS ADDED UP TO ONE
model=Sequential()
model.add(Dense(8,input_dim=4,activation='relu'))
model.add(Dense(3,input_dim=8,activation='softmax'))
#ADDING ADDITIONAL ATTRIBUTES TO THE MODEL USING COMPILE
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
#TRAINING
trained=model.fit(X_train,Y_train,epochs=200,batch_size=10)#STOCHASTIC - BATCH_SIZE= 1
score=model.evaluate(X_test,Y_test,batch_size=10)
#softmax
prediction=model.predict(X_test)
print("1st prediction : "+str(prediction[0][0])+" "+str(prediction[0][1])+" "+str(prediction[0][2]))
print("%1.3f"%(sum(prediction[0])))
#SONAR DATASET