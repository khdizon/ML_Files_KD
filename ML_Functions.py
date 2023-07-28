#  Machine Learning Functions

Version  | Date | Author | Notes |
:-------:|:----:|:-------|:-----:|
0.1 |19 July 2023| Ken Dizon | Initial version |
0.2 |23 July 2023| Ken Dizon | Refined |
0.2 |28 July 2023| Ken Dizon | Alpha |

### LIBRARIES ###

## standard Data Science
try:
    import numpy as np #math library
    import scipy #computation
    import scipy.optimize as opt
    import matplotlib.pyplot as plt #visualization
    %matplotlib inline
    import pandas as pd #dataframes
    
    '''Machine Learning''' 
    # standard libraries
    import sklearn
    from sklearn import preprocessing # standardization of dataset
    from sklearn.model_selection import train_test_split # Split our data 
    from sklearn import metrics # standard evaluation
    # insert algorithm
    # insert metric
    
    # Footer
    print('https://scikit-learn.org/stable/')
    print("Libraries imported successfully!")
except ImportError:
    print("Libraries not installed. Please install it to use this library.")
    
    
### SKLEARN Packages ###
'''ML Algorithms'''

# Regression
from sklearn import linear_model #LinearReg
from sklearn.tree import DecisionTreeRegressor #dtr

# Classification
from sklearn.neighbors import KNeighborsClassifier #KNN
from sklearn.tree import DecisionTreeClassifier #DT
import sklearn.tree as tree 
from sklearn.linear_model import LogisticRegression #LogisticReg
from sklearn import svm #support vector machine

# Clustering 
from sklearn.cluster import KMeans

# Evaluation Metrics
from sklearn.metrics import r2_score #linear reg
from sklearn.metrics import jaccard_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import log_loss
from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn.metrics import (mean_absolute_error, mean_squared_error, r2_score)


### FUNCTIONS ###
'''Standardization of dataset'''
X = preprocessing.StandardScaler().fit(X).transform(X)

'''Feature Select'''
X = #
Y = #

'''Spliting data - Train & Test'''
X_train, X_test, y_train, y_test = train_test_split(X, Y,
                                                    test_size=.2, #ratio of the testing dataset
                                                    random_state=n) # ensures that we obtain the same splits


# Understanding Metric Packaegs
from sklearn.metrics import (mean_absolute_error, # np.mean(np.absolute(predictions - y_test))
                             mean_squared_error, # np.mean((predictions - y_test) ** 2)
                             r2_score) # r2_score(y_test, predictions)

# Regression metrics
Model_MAE = mean_absolute_error(y_test, predictions)
Model_MSE = mean_squared_error(y_test, predictions)
Model_R2 = r2_score(y_test, predictions)

print("Mean absolute error: ", Model_MAE)
print("Residual sum of squares (MSE): ", Model_MSE)
print("R2-score: " , Model_R2)


# Classification metrics
Model_Accuracy_Score = accuracy_score(y_test, predictions)
Model_JaccardIndex = jaccard_score(y_test, predictions)
Model_F1_Score = f1_score(y_test, predictions)

print("KNN Accuracy Score:", Model_Accuracy_Score)
print("Jaccard Index:", Model_JaccardIndex)
print("F1 Score:", Model_F1_Score)
    
    
### Other ###
import itertools
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Aximport 

import seaborn as sns
sns.set()
