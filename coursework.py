#!/usr/bin/env python
# coding: utf-8

# In[722]:


import pandas as pd
import numpy as np
file = "diabetic_data.csv"
df = pd.read_csv(file)
df.shape


# In[723]:


df = df.drop('encounter_id',axis=1)
df.head()


# In[724]:


df.isnull().sum()


# In[725]:


df.replace('?',np.nan,inplace=True)
df['max_glu_serum'].fillna('None', inplace=True)
df['A1Cresult'].fillna('None', inplace=True)
df.isnull().sum()


# In[726]:


df.head(10)


# In[727]:


df['readmitted'].replace('<30',1,inplace=True)
df['readmitted'].replace('>30',0,inplace=True)
df['readmitted'].replace('NO',0,inplace=True)
df.head(10)
df['readmitted'].value_counts()


# In[728]:


df.dtypes


# In[729]:


# Calculate the percentage of missing values in each column
missing_percentages = (df.isnull().sum() / len(df)) * 100

# Identify columns with more than 90% missing values
columns_to_drop = missing_percentages[missing_percentages >= 90].index
print(columns_to_drop)

# Drop the identified columns
df.drop(columns=columns_to_drop, inplace=True)
df.head(10)


# In[730]:


df.head()


# In[731]:


colummns_with_zero_variance = ['examide','citoglipton']
df.drop(columns = colummns_with_zero_variance, axis=1,inplace = True)
df.head()


# In[732]:


columns_with_near_zero_variance = ['repaglinide','nateglinide','chlorpropamide','glimepiride','acetohexamide','tolbutamide','acarbose','miglitol','troglitazone','tolazamide','glyburide-metformin','glipizide-metformin','glimepiride-pioglitazone','metformin-rosiglitazone','metformin-pioglitazone']
df.drop(columns = columns_with_near_zero_variance, axis=1,inplace = True)

df.head()
df.isnull().sum()
#df.shape


# In[733]:


df.dropna(axis=0, how='any', inplace=True)
df.shape
print(df['number_outpatient'].value_counts())
print(df['number_emergency'].value_counts())
print(df['number_inpatient'].value_counts())
#df['number_diagnoses'].value_counts()


# In[734]:


df.describe()
#df.isnull().sum()
print(df['number_outpatient'].value_counts())
print(df['number_emergency'].value_counts())
print(df['number_inpatient'].value_counts())
df.select_dtypes(include='number')


# In[735]:


from scipy.stats import zscore

# Load your dataset into a pandas DataFrame
# Assuming your DataFrame is named 'df'

# Select numerical columns of type int64 excluding specified columns
numerical_columns = df.select_dtypes(include='int64').drop(columns=['admission_type_id', 'discharge_disposition_id', 'admission_source_id', 'readmitted'])

# Calculate Z-scores for each data point in numerical columns
z_scores = numerical_columns.apply(zscore)

# Set threshold for identifying outliers
threshold = 3

# Identify outliers based on the threshold
outliers = np.abs(z_scores) > threshold

# Remove outliers from the DataFrame
df = df[~outliers.any(axis=1)]

# Print the number of outliers removed
num_outliers_removed = outliers.sum().sum()
print("Number of outliers removed:", num_outliers_removed)

# Optionally, display cleaned DataFrame
print("\nCleaned DataFrame:")
print(cleaned_df)


# In[736]:


df.isnull().sum()
print(df['number_outpatient'].value_counts())
print(df['number_emergency'].value_counts())
print(df['number_inpatient'].value_counts())


# In[737]:


df.shape


# In[738]:


df.head(10)


# In[739]:


df['readmitted'].value_counts()


# In[740]:


df.select_dtypes(include='number')


# In[741]:





# In[ ]:




