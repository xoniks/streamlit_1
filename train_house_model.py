import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

input_data_set_name= input("Please enter location and file name of training data: ")
df = pd.read_csv(input_data_set_name)

X=[ i for i in df.columns.values if i not in ['Price','Address']]
y='Price'

X_train, X_test, y_train, y_test = train_test_split(df[X],df[y], test_size=0.3, random_state=2023)

machine = LinearRegression()

machine.fit(X_train,y_train)


filename = input('Please enter model name and location to extract the model: ')
pickle.dump(machine, open(filename, 'wb'))
