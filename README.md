# Machine Learning Startup File

Version  | Date | Author | Notes |
:-------:|:----:|:-------|:-----:|
0.1 |19 July 2023| Ken Dizon | Initial version

**Objective**
Write a sample ML script for the initial start-up

- Libraries
- Type of Machine Learning + Algorithms
- 
______
### TYPES: Supervised vs Unsupervised
- Supervised
    - Regression: predicts tredns using labled data
    - Classification: classifies labled data
- Unsupervised
    - Clustering: finds patterns and groupings from unlabeled data

### ML

ML Problem | Types | Case Prediction | 
:---------:|:-----:|:---------------:|
Regression | Simple, Multiple | continuos numerical value |
Classification | Binary, Multi-class | class label for unlabled test case | 
Clustering | ... | grouping data points by similarity |


### Algorithms
Regression | Classification | Clustering | 
:---------:|:--------------:|:----------:|
ordinal, poisson, linear, polynomial, lasso, bayesian, NNR, decsion forest, KNNR | DT, naive bayes, KNN, logistic, NN, SVM | 

### Table structure 
- `Columns` = Features [Vertical]
- `Rows` = Attributes [Horizontal]

______________________
#### General Content
1. **Load data**
2. **Data preprocessing**
    * 2.1 Cleaning
    * 2.2 Missing Data
    * 2.3 Scaling
3. **Split - Test & Train**
4. **Model Selection**
5. **Model Training**
5. **Model Evaluation**

______
# Models & Evaluation 

### Regression 
Model | Evaluation | 
:----:|:----------:|
Linear Regression | RSS, Variance Score |
Regression Tree | mse, mae accuracy | 

### Classification 
Model | Evaluation | 
:----:|:----------:|
DT | DT Accuracy |
