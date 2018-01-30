import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

# Predictions for 2018

df = pd.read_csv("Training-Test-Dataset.csv")
df.drop(["Unnamed: 0"], axis = 1, inplace = True)

df.iloc[362]

df.capCluster.value_counts()
plt.hist(df['capCluster'])
X_var = df.drop(["name", "Salary", "Cluster", "PercentCap", "capCluster"], axis = 1)
y_var = df["capCluster"]

def model_fit(model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)
    train_acc = round(model.score(X_train, y_train) * 100, 5)
    test_acc = round(model.score(X_test, y_test) * 100, 5)
    y_test_pred = model.predict(X_test)
    average_error = np.mean(abs(y_test - y_test_pred))
    
    data = {"y_test": y_test, "y_test_pred": y_test_pred}
    predictions_df = pd.DataFrame(columns = ["y_test", "y_test_pred"], data = data)        
    
    print('Train accuracy (R^2): ', train_acc, '\nTest accuracy (R^2): ', test_acc, '\nTest error (average error): ', average_error, '\n', predictions_df)

X_train, X_test, y_train, y_test = train_test_split(X_var, y_var, test_size = .2, random_state = 1)

y_train.value_counts()

model_fit(KNeighborsClassifier(), X_train, X_test, y_train, y_test)

X_2018 = pd.read_csv("../Final-dataset/2018-Final.csv")
names = X_2018.name
X_2018.drop(['Unnamed: 0', 'name'], axis = 1, inplace = True)


X_2018.head()


model = KNeighborsClassifier()
model.fit(X_train, y_train)
final_pred = model.predict(X_2018)

final_df = pd.DataFrame(names)
final_df['salary'] = final_pred


final_df.to_csv(path_or_buf = "2018-predictions.csv")


# Timing and Cluster Optimization

import time
from sklearn.model_selection import GridSearchCV, StratifiedKFold

kfold = StratifiedKFold(n_splits=10)
knn = KNeighborsRegressor()

param_grid = {"n_neighbors": [1,3,5,7,9,11,13,15,17,19],
              "weights": ["uniform", "distance"], 
              "leaf_size": [30,50,70]}
            
start_time = time.time()
# run grid search
grid_search = GridSearchCV(knn, param_grid=param_grid, cv = 10)
grid_search.fit(X_train, y_train)

time = time.time() - start_time
print("Hyperparameter tuning took {} seconds".format(time))


print(grid_search.best_estimator_)


print(grid_search.best_score_)



