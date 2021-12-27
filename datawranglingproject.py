#!/usr/bin/env python
# coding: utf-8

# # DATA WRANGLING

# # Project: Covid - 19 Data Analysis Project using Python

# In[2]:


# 1)Importing libraries
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings("ignore")
from IPython.display import Image 


# In[ ]:


#Importing Dataset
df = pd.read_csv('https://raw.githubusercontent.com/SR1608/Datasets/main/covid-data.csv')


# In[4]:


df.head()


# In[5]:


df.tail()


# In[6]:


# 2)a)Find no. of rows & columns in the dataset
print("number of rows : ", df.shape[0])
print("number of columns : ", df.shape[1])


# In[7]:


#2)b)(b) Data types of columns.
for name, dtype in df.dtypes.iteritems():
    print(name,":  ", dtype)


# In[8]:


#2)c) Info & description of data in dataframe.
df.info()


# In[9]:


df.describe()


# In[10]:


#3) a) Find count of unique values in location column.
df['location'].value_counts()


# In[11]:


#3)(b) Find which continent has maximum frequency using values counts.
df['continent'].value_counts()


# ###### conclusion:EUROPE has maximum frequency

# In[12]:


#3) c) Find Maximum & Mean value in 'total_cases'.
maxClm = df['total_cases'].max()
print("Max value 'total_cases': ", maxClm)
mean_value = df['total_cases'].mean()
print("The Mean 'total_cases' is :", mean_value)


# In[17]:


#3) d) Find 25%,50% & 75% quartile value in 'total_deaths'.

#25%
df.total_deaths.quantile(0.25)


# In[18]:


#50%
df.total_deaths.quantile(0.5)


# In[19]:


#75%
df.total_deaths.quantile(0.75)


# In[20]:


# 3) (e) Find which continent has maximum 'human_development_index'.
df.groupby(["continent"]).agg({"human_development_index":"max"})


# In[21]:


#3) f) Find which continent has minimum 'gdp_per_capita'.
df.groupby(["continent"]).agg({"gdp_per_capita":"min"})


# In[22]:


#4.Filter the dataframe with only this columns ['continent','location','date','total_cases','total_deaths','gdp_per_capita','human_development_index'] and update the data frame.
df[['continent', 'location', 'date', 'total_cases', 'total_deaths', 'gdp_per_capita', 'human_development_index']]


# In[24]:


#5.(a) Remove all duplicates observations.
df.drop_duplicates()


# In[25]:


#(b) Find missing values in all columns
df.isnull().head()


# In[26]:


df.isnull().sum()


# In[28]:


#(c) Remove all observations where continent column value is missing.
df[df['continent'].isnull()]


# In[29]:


df.dropna(subset = ['continent'], how = 'all').shape


# In[30]:


#(d) Fill all missing values with 0
df.fillna(0)


# In[31]:


#6.(a) Convert date column in datetime format using pandas.to_datetime
df['date']= pd.to_datetime(df['date'])
df.info()


# In[32]:


#(b) Create new column month after extracting month data from date column.
df['month'] = df["date"].dt.month
df.head()


# In[33]:


#7.(a) Find max value in all columns using groupby function on 'continent' column.
grouped_df = df.groupby("continent")
maximums = grouped_df.max()
maximums = maximums.reset_index()
maximums


# In[34]:


#(b) Store the result in a new dataframe named 'df_groupby'.
maximums


# In[35]:


#8.(a) Create a new feature 'total_deaths_to_total_cases' by ratio of 'total_deaths' column to 'total_cases'.
df = pd.DataFrame(df)
df['total_deaths_to_total_cases']= df["total_deaths"]/df["total_cases"]
df.head(15)


# In[36]:


df_groupby=maximums


# In[37]:


#9.(a) Perform Univariate analysis on 'gdp_per_capita' column by plotting histogram using seaborn dist plot.
plt.figure(figsize=(8,5))
sns.distplot(df_groupby['gdp_per_capita'],kde=False,bins=10, color = "blue")


# In[38]:


#(b) Plot a scatter plot of 'total_cases' & 'gdp_per_capita'
df.plot.scatter(x ='gdp_per_capita', y='total_cases')


# In[ ]:


#(c) Pairplot on df_groupby dataset
sns.pairplot(df)


# In[ ]:


#(d)bar plot of 'continent' column with 'total_cases' .
df_groupby.plot(x="continent", y="total_cases", kind="bar")


# In[ ]:


#10. Save the df_groupby dataframe in your local drive using pandas.to_csv function .
df.to_csv('DataWranglingProject.csv')


# In[ ]:




