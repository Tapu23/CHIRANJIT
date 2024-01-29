#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd # used to "tidy" up and manipulate our data
import numpy as np # used for matrix and numerical calculations; foundation of pandas
from scipy import stats # contains stats functions and is used to visualise probability distributions
import matplotlib.pyplot as plt # used for visualisations
import seaborn as sns # a more user-friendly library used for visualisations


# In[2]:


df=pd.read_csv('Downloads/CENSUS_INCOME.csv')
df.head()


# In[3]:


df.tail()


# In[29]:


df1=df.describe().T
df1


# In[5]:


df.info()


# In[6]:


df.shape


# In[7]:


df.isnull().sum()


# In[8]:


df.duplicated().sum()


# In[9]:


df.nunique()


# In[10]:


df['WORKCLASS'].value_counts()


# In[11]:


df['OCCUPATION'] = df['OCCUPATION'].replace('?', 'Other-service')
df['NATIVE COUNTRY'] = df['NATIVE COUNTRY'].replace('?', 'United-States')
df['WORKCLASS'] = df['WORKCLASS'].replace('?', 'Private')


# In[12]:


df['OCCUPATION'].value_counts()


# In[13]:


df['OCCUPATION'].value_counts()


# In[14]:


df['NATIVE COUNTRY'].value_counts()


# In[15]:


df.columns


# In[16]:


df['MARITAL-STATUS'] = df['MARITAL-STATUS'].replace(['Married-civ-spouse','Married-AF-spouse'], 'Married')
df['MARITAL-STATUS'] = df['MARITAL-STATUS'].replace(['Never-married'], 'Single')
df['MARITAL-STATUS'] = df['MARITAL-STATUS'].replace(['Married-spouse-absent'], 'Separated')


# In[17]:


df['MARITAL-STATUS'].value_counts()


# In[18]:


df['EDUCATION'].value_counts()


# In[19]:


df['EDUCATION'] = df['EDUCATION'].replace(['Preschool','1st-4th','5th-6th','7th-8th','12th','9th','10th','11th'],'School')
df['EDUCATION'] = df['EDUCATION'].replace(['Assoc-voc','Assoc-acdm','Prof-school','Some-college'],'High School')
df['EDUCATION'].value_counts()


# In[20]:


df['MARITAL-STATUS'].value_counts()


# In[22]:


df['EDUCATION'].value_counts()


# In[23]:


Average= df.groupby('AGE')['HOURS-PER-WEEK']\
              .agg(['count', 'mean'])\
              .sort_values(by='count', ascending=True)\
              .head(10) #to keep only the 10 most popular Subjects

Average['mean'].sort_values().plot.bar()
plt.title('Average hours');


# In[30]:


df1.corr()


# In[40]:


#sns.heatmap(df1.corr(),annot=True)
#plt.show();
plt.figure(figsize=(15,5), facecolor="#ECEFF4")
sns.heatmap(df1.corr(),cmap="RdBu",annot=True);


# In[32]:


df.boxplot(figsize=(30,20));


# In[33]:


df['AGE'].plot(kind='hist',bins=110,title='Age');


# In[34]:


sns.scatterplot(x='AGE',y='RELATIONSHIP',hue='SEX',data=df);


# In[50]:


sns.countplot(x='INCOME', palette='magma', hue='RELATIONSHIP',data=df);


# In[62]:


sns.countplot( x='INCOME', hue='RACE', data=df,figsize(30,20));


# In[65]:


sns.countplot(x ='INCOME', hue= 'WORKCLASS', data=df);


# In[75]:


sns.pairplot(x_vars=['CAPITAL-GAIN','INCOME'],
             y_vars=['EDUCATION-NUM'], 
             hue='RACE', 
             height=5.5,
             data=df);


# In[ ]:




