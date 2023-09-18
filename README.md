# [Laptop-Price-Predictor](https://harsh-laptop-price-predictor.streamlit.app/)
<ul>
  <li>Designed a web app that predicts the price of the laptop given the configurations. </li>
  <li>Developed Linear, Lasso, and Random Forest Regressors KNN, Decision Tree Regressor and Gradient Boost Regressor to get the best model.</li>
  <li>Deployed the Machine Learning model using streamlit library in Heroku</li>
</ul>

# Features
 - Company (Laptop Company)
 - TypeName (for ex.Notebook)
 - Inches (size in inches)
 - ScreenResolution (for ex. 1366x768)
 - Cpu (for ex. Intel Core i5 7200U 2.5GHz)
 - Ram(Random Access Memory in MegaBytes)
 - Memory (Internal Storage HDD or SDD in Gigabytes)
 - Gpu (for ex. Intel HD Graphics 520)
 - OpSys (Operating System)
 - Weight (Weight of the laptop)
 - Price (price of laptop)

# Traditional Method
Used scikit-learn library for the Machine Learning tasks. Applied label encoding and converted the categorical variables into numerical ones.Then I splited the data into training and test sets with a test size of 20%. I tried three different models ( Linear Regression, Random Forest Regression, XGBoost) and evaluated them using Mean Absolute Error. 

# Model Deployment
Deployed the model using Streamlit library on Heroku which is a Platform As A Service(PAAS)


