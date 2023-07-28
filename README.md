# Machine Learning Startup File.ReadMe

Version  | Date | Author | Notes |
:-------:|:----:|:-------|:-----:|
0.1 |19 July 2023| Ken Dizon | Initial version
0.2 |26 July 2023| Ken Dizon | Refined all ML categories
1.0 |28 July 2023| Ken Dizon | Alpha phase

**Objective:** write a sample ML script for initial start up. ML gives _computers the ability to learn without being explicitly programmed_. 

**CONTENT**
- Libraries
- Types of Machine Learning
    * Use Cases
    * Algorithms
- Models & Math
- Startup sample content
____________________________

## TYPES: Supervised vs Unsupervised
- Supervised
    - Regression: predicts trends using labeled data
    - Classification: classifies labeled data
- Unsupervised
    - Clustering: finds patterns and groupings from unlabeled data

### ML
**Data > Feature Extraction > ML Model > Outcome**

ML Techniques | Types | Case Prediction | 
:------------:|:-----:|:---------------:|
Regression | Simple, Multiple | continuos numerical value |
Classification | Binary, Multi-class | class label for unlabled test case | 
Clustering | Partitioned, Hierarchial, Density | grouping data points by similarity |

### Use Cases

Regression | Classification | Clustering | 
:---------|:--------------|:----------|
`Numeric` prediction, estimation, forecasting | detection, retension, daignostic | segmentation, target market, recommender systems |

### Algorithms
Regression | Classification | Clustering | 
:---------|:--------------|:----------|
ordinal, poisson, linear, polynomial, lasso, bayesian, NNR, decision forest R, KNNR | DT, naive bayes, Linear discriminant analysis, KNN, logistic regression, NN, SVM | K-means, k-Median, Fuzzy c-Means, agglomerative, divisive, DBSCAN | 

______________________________

## Models & Math  

Regression Model | Evaluation | Selection | 
:----|:----------|:----|
Linear Regression | MAE, MSE, R2, RSS, Variance Score | Influence of Xs to predict a continuous numeric Y value|
Decision Tree Regression [DTR] | mse, mae accuracy | ... |
Multiclass Prediction | ... | ... |


Classification Model | Evaluation | Selection |
:----|:----------|:----|
DT | DT classification Accuracy | Categorical identification based on characteristics |
KNN | mean acc, std acc | ...|
Logistic Regression | Jaccard index, Confusion matrix (F1-score), logloss | predict probability of categorical dependent variable |
SVM | ... | Image recognition, text category assignment, detecting spam, sentiment analysis, gene expression |

 
Clustering Model | Evaluation | Selection |
:----|:----------|:----|
k-means | non-overlaps to minimize 'intra' & max 'inter' cluster distance | relatively efficient (med/large data) |
... |... | trees of clusters |
... |... | arbitrary shaped clusters |
___________
# Machine Learning TYPE `Model Name` Startup File

#### Content
- Libraries
1. **Load Data**
    * 1.1 Data Exploration
2. **Data Preprocessing**
    * 2.1 Cleaning
    * 2.2 Missing Data
    * 2.3 Scaling
    * 2.4 Feature Engineering/Selection
3. **Split - Test & Train**
4. **Model Selection**
5. **Model Training**
5. **Model Evaluation**


