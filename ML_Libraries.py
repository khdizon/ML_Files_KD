#  Libraries - Machine Learning

Version  | Date | Author | Notes |
:-------:|:----:|:-------|:-----:|
0.1 |19 July 2023| Ken Dizon | Initial version |
0.2 |23 July 2023| Ken Dizon | Initial version |

try:
    import numpy as np #math library 
    import scipy #computation
    import scipy.optimize as opt
    import matplotlib.pyplot as plt #visualization
    %matplotlib inline
    import pandas as pd #dataframes

# BASE SK Learn Packages
import sklearn
from sklearn import preprocessing
from sklearn.model_selection import train_test_split # Split our data 
from sklearn import metrics # base metrics

### Regression
from sklearn import linear_model #LinearReg
from sklearn.tree import DecisionTreeRegressor #dtr

### Classification
from sklearn.neighbors import KNeighborsClassifier #KNN
from sklearn.tree import DecisionTreeClassifier #DT
import sklearn.tree as tree 
from sklearn.linear_model import LogisticRegression #LogisticReg
from sklearn import svm #support vector machine

### Evaluation Metrics
from sklearn.metrics import r2_score #linear reg
from sklearn.metrics import jaccard_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import log_loss
import itertools


# Footer
    print('https://scikit-learn.org/stable/')
    print("Libraries imported successfully!")
except ImportError:
    print("Libraries not installed. Please install it to use this library.")
