#  Libraries - Machine Learning

Version  | Date | Author | Notes |
:-------:|:----:|:-------|:-----:|
0.1 |23 July 2023| Ken Dizon | Initial version |

try:
    import numpy as np #math library 
    import scipy #computation
    import matplotlib.pyplot as plt #visualization
    %matplotlib inline
    import pandas as pd #dataframes

 # Base SK ML Packages
    import sklearn
    from sklearn import preprocessing
    from sklearn.model_selection import train_test_split # Split our data 
    '''machine learning library'''
### Models ###
# Regression
    from sklearn import linear_model #lr
    from sklearn.tree import DecisionTreeRegressor #dtr
# Classification
    from sklearn.neighbors import KNeighborsClassifier #KNN
    from sklearn.tree import DecisionTreeClassifier #DT
    import sklearn.tree as tree

    print('https://scikit-learn.org/stable/')
    print("Libraries imported successfully!")
except ImportError:
    print("Libraries not installed. Please install it to use this library.")
