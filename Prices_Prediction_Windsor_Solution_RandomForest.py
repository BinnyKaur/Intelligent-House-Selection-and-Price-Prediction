#!/usr/bin/env python
# coding: utf-8

# In[150]:


import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn import metrics
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.metrics import mean_squared_error
import numpy as np
from sklearn.preprocessing import StandardScaler
import scipy
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn import metrics
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.metrics import mean_squared_error
import numpy as np
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt
import scipy


# In[151]:


# Load the data into a DataFrame
data = pd.read_csv('HousePrices.csv')
data['price'] = data['price']*10


# In[152]:


data.isna().sum()


# In[153]:


data = data.drop('Unnamed: 0',axis=1)
men = 0.3
# data = data.drop('driveway',axis=1)
# data = data.drop('recreation',axis=1)
# data = data.drop('fullbase',axis=1)
# data = data.drop('gasheat',axis=1)
# data = data.drop('aircon',axis=1)
# data = data.drop('prefer',axis=1)


# In[154]:


sns.boxplot(data['price'])
plt.tight_layout()


# In[155]:


#visualizing square footage of (home,lot,above and basement)
fig = plt.figure(figsize=(16,7))
fig.add_subplot(2,2,1)
sns.scatterplot(data=data,x=data['lotsize'],y=data['price'])


# In[156]:


fig = plt.figure(figsize=(15,7))
fig.add_subplot(2,2,1)
sns.countplot(x=data['bedrooms'])
fig.add_subplot(2,2,2)
sns.countplot(x=data['stories'])
fig.add_subplot(2,2,3)
sns.countplot(x=data['bathrooms'])
fig.add_subplot(2,2,4)
sns.countplot(x=data['garage'])
plt.tight_layout()


# In[116]:


data.query("price <=500000 and bathrooms > 1 and stories == 2 ")


# In[117]:


# Split the data into input features (X) and target variable (y)
X = data.drop('price', axis=1)
y = data['price']


# In[118]:


# Perform one-hot encoding on the categorical variables
cat_cols = ['driveway', 'recreation', 'fullbase', 'gasheat', 'aircon', 'prefer']
X_encoded = pd.get_dummies(X, columns=cat_cols, drop_first=True)


# In[119]:


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)


# In[120]:


# Create a Random Forest regression model
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)


# # Train the model
# rf_model.fit(X_train, y_train)

# In[121]:


rf_model.fit(X_train, y_train)


# In[122]:


# Make predictions on the test set
y_pred = rf_model.predict(X_test)


# In[139]:


Final_DF = X_test


# In[140]:


Final_DF["Predicted_Prices"] = y_pred


# In[141]:


y_test


# In[142]:


Final_DF["Actual_Prices"] = y_test


# In[143]:


Final_DF


# In[144]:


Final_DF['Mean_Square_Error'] = (Final_DF["Predicted_Prices"]-Final_DF["Actual_Prices"])*(Final_DF["Predicted_Prices"]-Final_DF["Actual_Prices"])


# In[145]:


Final_DF = Final_DF.sort_values("Mean_Square_Error")


# In[146]:


Final_DF = Final_DF.iloc[:,:-2]
Final_DF


# In[131]:


Final_DF.info()
Final_DF.describe().transpose()


# In[147]:


Final_DF = Final_DF.query("prefer_yes == 1 and 800000 <= Predicted_Prices <= 900000 and stories == 1")


# In[148]:


Final_DF.style.background_gradient()

