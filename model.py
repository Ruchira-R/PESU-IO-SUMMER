
# Average Accuracy : 84.946


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
#Algos
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier


df=pd.read_csv("dataset.csv")
cat_f = [x for x in df.columns if df[x].dtype == 'object']

for name in cat_f:
    enc = preprocessing.LabelEncoder()
    enc.fit(list(df[name].values.astype('str')) + list(df[name].values.astype('str')))
    df[name] = enc.transform(df[name].values.astype('str'))

X_train = df.drop(['Date','RainTomorrow','RISK_MM'], axis=1)
y_train = df['RainTomorrow']

X_train.fillna(-1000, inplace=True)
x_train, x_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.2)

clf3 = XGBClassifier()
clf3.fit(x_train, y_train)
def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
    n_vars = 1 if type(data) is list else data.shape[1]
    df = pd.DataFrame(data)
    cols, names = list(), list()
    for i in range(n_in, 0, -1):
        cols.append(df.shift(i))
        names += [('var%d(t-%d)' % (j+1, i)) for j in range(n_vars)]
    for i in range(0, n_out):
        cols.append(df.shift(-i))
        if i == 0:
            names += [('var%d(t)' % (j+1)) for j in range(n_vars)]
        else:
            names += [('var%d(t+%d)' % (j+1, i)) for j in range(n_vars)]
    agg = pd.concat(cols, axis=1)
    agg.columns = names
    if dropnan:
        agg.dropna(inplace=True)
    return agg

def run_preds_supervised(df, forecast_period, groupby='Date'):
    combined_df = df.groupby([groupby]).mean()
    combined_df['RainfallPred'] = combined_df['Rainfall'].shift(1)
    combined_df.drop(['Rainfall'], axis=1, inplace=True)
    combined_df.dropna(inplace=True)
    lstm_dataset = combined_df.values
    lstm_dataset = lstm_dataset.astype('float32')

    reframed = series_to_supervised(lstm_dataset, 1, 1)

    column_names = reframed.columns
    scaler = MinMaxScaler(feature_range=(-1, 1))
    reframed = scaler.fit_transform(reframed)
    reframed = pd.DataFrame(reframed, columns=column_names)
    values = reframed.values
    train = values[:forecast_period, :]
    test = values[forecast_period:, :]
    train_X, train_y = train[:, :-1], train[:, -1]
    test_X, test_y = test[:, :-1], test[:, -1]

    train_X = train_X.reshape((train_X.shape[0], 1, train_X.shape[1]))
    test_X = test_X.reshape((test_X.shape[0], 1, test_X.shape[1]))

    lstm_model = Sequential()
    lstm_model.add(LSTM(50, input_shape=(train_X.shape[1], train_X.shape[2])))
    lstm_model.add(Dense(1))
    lstm_model.compile(loss='mae', optimizer='adam')
    # history = lstm_model.fit(train_X, train_y, epochs=50, batch_size=120, validation_data=(test_X, test_y), verbose=0,shuffle=False)
    prediction = lstm_model.predict(test_X)
run_preds_supervised(df,700, 'Date')
print("Average Accuracy = ", clf3.score(x_test, y_test))