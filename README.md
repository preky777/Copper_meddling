# Industrial Copper Modeling

## Project Overview
The copper industry deals with data related to sales and pricing, which can be complex due to issues like skewness and noisy data. This project aims to address these challenges by developing machine learning models for predicting selling prices and classifying leads. The solution includes data cleaning, normalization, feature scaling, and outlier detection, utilizing regression and classification algorithms robust to skewed and noisy data.

## Objectives

    1.Explore skewness and outliers in the dataset.
    2.Transform and clean the data.
    3.Develop a machine learning regression model to predict the continuous variable ‘Selling_Price’.
    4.Develop a machine learning classification model to predict the Status: WON or LOST.
    5.Create a Streamlit page to input column values and get the predicted Selling_Price or Status (Won/Lost).


## Repository Structure

    .
    ├── copper_project.py
    ├── prediction.ipynb
    ├── README.md
    └── requirements.txt
    

# Project Approach

## Data Understanding

    •Identify variable types (continuous, categorical) and distributions.
    •Convert invalid 'Material_Reference' values starting with ‘00000’ to null.
    •Treat reference columns as categorical variables.

## Data Preprocessing

    •Handle missing values with mean/median/mode.
    •Treat outliers using IQR or Isolation Forest from sklearn.
    •Identify and treat skewness with log transformation, boxcox transformation, or other techniques.
    •Encode categorical variables using one-hot encoding, label encoding, or ordinal encoding.
    •Visualize outliers and skewness using Seaborn's boxplot, distplot, and violinplot.

## Feature Engineering

    •Engineer new features if applicable.
    •Drop highly correlated columns using a heatmap.

## Model Building and Evaluation

    •Split the dataset into training and testing/validation sets.
    •Train and evaluate classification models (ExtraTreesClassifier, XGBClassifier, Logistic Regression) using accuracy, precision, recall, F1 score, and AUC curve.
    •Optimize model hyperparameters using cross-validation and grid search.
    •Train and evaluate regression models, noting the dataset's noise and linearity, preferring tree-based models.

## Model GUI

    •Using Streamlit, create an interactive page with:
    •Task input (Regression or Classification).
    •Input fields for each column value except ‘Selling_Price’ (for regression) and ‘Status’ (for classification).
    •Apply feature engineering, scaling, and transformations used in training.
    •Predict and display the output for new data.

## Tips

    •Use the pickle module to dump and load models such as encoders, scalers, and machine learning models.
    •Fit models in separate lines and use transform only for unseen data.


## Installation

To run this project locally, follow these steps:

    1.Clone the repository:
    
    git clone https://github.com/your_username/industrial-copper-modeling.git
    
    2.Navigate to the project directory:
    
    cd industrial-copper-modeling
    
    3.Install the required libraries:
    
    pip install -r requirements.txt


## Usage

    1.Run the Streamlit application:
    streamlit run copper_project.py
    
    2.Open your web browser and navigate to the local host URL provided by Streamlit.
    
    

## Requirements

The required Python libraries for this project are listed in the requirements.txt file.



## Model Saving and Loading

    Regression Model:
    
        import pickle
        with open('model.pkl', 'wb') as file:
            pickle.dump(rf_regressor, file)
        with open('scaler.pkl', 'wb') as f:
            pickle.dump(scaler, f)
        with open('t.pkl', 'wb') as f:
            pickle.dump(ohe, f)
        with open('s.pkl', 'wb') as f:
            pickle.dump(ohe2, f)
    
    Classification Model:
    
        import pickle
        with open('cmodel.pkl', 'wb') as file:
            pickle.dump(random_forest, file)
        with open('cscaler.pkl', 'wb') as f:
            pickle.dump(scaler, f)
        with open('ct.pkl', 'wb') as f:
            pickle.dump(ohe, f)
