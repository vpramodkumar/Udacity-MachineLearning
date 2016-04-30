# Predicting Boston Housing
Model Evaluation And Validation

## Project Overview
In this project, you will apply basic machine learning concepts on data collected for housing prices in the Boston, Massachusetts area to predict the selling price of a new home. You will first explore the data to obtain important features and descriptive statistics about the dataset. Next, you will properly split the data into testing and training subsets, and determine a suitable performance metric for this problem. You will then analyze performance graphs for a learning algorithm with varying parameters and training set sizes. This will enable you to pick the optimal model that best generalizes for unseen data. Finally, you will test this optimal model on a new sample and compare the predicted selling price to your statistics.

## Project Description
The Boston housing market is highly competitive, and you want to be the best real estate agent in the area. To compete with your peers, you decide to leverage a few basic machine learning concepts to assist you and a client with finding the best selling price for their home. Luckily, you’ve come across the Boston Housing dataset which contains aggregated data on various features for houses in Greater Boston communities, including the median value of homes for each of those areas. Your task is to build an optimal model based on a statistical analysis with the tools available. This model will then be used to estimate the best selling price for your client’s home.
For this assignment, you can find the boston_housing.ipynb file as a downloadable in the Resources section. You may also visit our Projects GitHub to have access to all of the projects available for this Nanodegree. While some code has already been implemented to get you started, you will need to implement additional functionality to successfully answer all of the questions included in the notebook. You can find the included questions for reference on the following slide. Unless requested, do not modify code that has already been included.

## Project Report Questions
Use this slide as reference to the project questions you will encounter in the notebook. These questions (and your answers) must be present in your included PDF report.
Statistical Analysis and Data Exploration
This question is integrated into the project notebook output.
Using the NumPy library, calculate a few meaningful statistics about the dataset:
How many data points (houses) were collected?
How many features are present for each house?
What is the minimum housing price? The maximum?
What is the mean housing price? The median?
What is the standard deviation of all housing prices?
1) Of the available features for a given home, choose three you feel are significant and give a brief description for each of what they measure.
2) Using your client’s feature set CLIENT_FEATURES in the template code, which values correspond to the chosen features?
Evaluating Model Performance
3) Why do we split the data into training and testing subsets?
4) Which performance metric below is most appropriate for predicting housing prices and analyzing error? Why?
Accuracy
Precision
Recall
F1 score
Mean Squared Error (MSE)
Mean Absolute Error (MAE)
5) What is the grid search algorithm and when is it applicable?
6) What is cross-validation and how is it performed on a model? Why would cross-validation be helpful when using grid search?
Analyzing Model Performance
7) Choose one of the learning curve graphs your code creates. What is the max depth for the model? As the size of the training set increases, what happens to the training error? Describe what happens to the testing error.
8) Look at the learning curve graphs for the model with a max depth of 1 and a max depth of 10. When the model is using the full training set, does it suffer from high bias or high variance when the max depth is 1? What about when the max depth is 10?
9) From the model complexity graph, describe the training and testing errors as the max depth increases. Based on your interpretation of the graph, which max depth results in a model that best generalizes the dataset? Why?
Model Prediction
To answer the following questions, it is recommended that you run your notebook several times and use the median or mean value as your result.
10) Using grid search, what is the optimal max depth for your model? How does this result compare to your initial intuition?
11) With your parameter-tuned model, what is the best selling price for your client’s home? How does this selling price compare to the statistics you calculated on the dataset?
12) In a few sentences, discuss whether you would use this model or not to predict the selling price of future clients’ homes in the Boston area.


## Data Set Information:

Concerns housing values in suburbs of Boston.


### Attribute Information:

1. CRIM: per capita crime rate by town 
2. ZN: proportion of residential land zoned for lots over 25,000 sq.ft. 
3. INDUS: proportion of non-retail business acres per town 
4. CHAS: Charles River dummy variable (= 1 if tract bounds river; 0 otherwise) 
5. NOX: nitric oxides concentration (parts per 10 million) 
6. RM: average number of rooms per dwelling 
7. AGE: proportion of owner-occupied units built prior to 1940 
8. DIS: weighted distances to five Boston employment centres 
9. RAD: index of accessibility to radial highways 
10. TAX: full-value property-tax rate per $10,000 
11. PTRATIO: pupil-teacher ratio by town 
12. B: 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town 
13. LSTAT: % lower status of the population 
14. MEDV: Median value of owner-occupied homes in $1000's
