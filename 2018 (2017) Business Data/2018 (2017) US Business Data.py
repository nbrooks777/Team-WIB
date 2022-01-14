#!/usr/bin/env python
# coding: utf-8

# # Load Libraries

# In[14]:


import pandas as pd
import numpy as np


# # Load Data & View Data

# In[15]:


WBiz2018 = pd.read_csv(r"C:\Users\nbroo\OneDrive\Documents\Data Science Final Group Project\Women In Business Before And After The Pandemic\2018 (2017) Census Business Data.csv")


# In[16]:


WBiz2018.head()


# # Rename Columns

# In[17]:


WBiz2018.rename(columns={'NAICS2017' : 'NAICS', 'SEX' : 'Owners_Sex', 'ETH_GROUP' : 'Owners_Ethnicity', 'RACE_GROUP' : 'Owners_Race', 'VET_GROUP' : 'Vet_Status', 'RCPPDEMP' : 'Sales', 'EMP' : 'Employees', 'RCPPDEMP_S' : 'Sales_Std_Error', 'EMP_S' : 'Employees_Std_Error'}, inplace=True)


# In[18]:


WBiz2018.head()


# # Clean Dataset

# ## Drop Columns

# In[19]:


WBiz2018 = WBiz2018.drop(labels=0, axis=0)


# In[20]:


WBiz2018.head()


# # Subset Data

# In[21]:


WBiz2018Sub = WBiz2018[['NAICS','Owners_Sex', 'Owners_Ethnicity', 'Owners_Race', 'Vet_Status', 'Sales', 'Employees', 'Sales_Std_Error', 'Employees_Std_Error']]


# In[22]:


WBiz2018Sub.head()


# # Recode Data

# ## About Dataset

# In[23]:


WBiz2018Sub.info()


# ## Change From Objects To Float

# In[24]:


WBiz2018Sub = WBiz2018Sub.apply (pd.to_numeric, errors='coerce')

print(WBiz2018Sub.info())


# # Use Chi-Squares to determine if Owners_Sex depends on Sales

# In[25]:


from scipy import stats


# ## Subset For Relevant Data

# In[26]:


WBiz2018Sub2 = WBiz2018Sub [['Owners_Sex', 'Owners_Ethnicity', 'Owners_Race', 'Vet_Status', 'Sales', 'Employees', 'Sales_Std_Error', 'Employees_Std_Error']]


# In[27]:


WBiz2018Sub2.info()


# ## Create a contingency table:

# In[28]:


from scipy import stats


# In[29]:


WB2018_crosstab = pd.crosstab(WBiz2018Sub2['Owners_Sex'], WBiz2018Sub2['Sales'])


# In[30]:


stats.chi2_contingency(WB2018_crosstab)


# ### p-value < 0.05, therefore there is a significant relationship between owners_sex and the number of sales. The values in the array are more than 5 and therefore meet the assumption.

# ##  Run a correlation matrix

# In[31]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[32]:


WBiz2018Sub2.corr(method='pearson')


# In[33]:


sns.heatmap(WBiz2018Sub2.corr(), annot=True)


# ### Strong, positive correlations between owners_sex, owners_ethnicity, & vet_status.

# # Determine Dependent t-Test

# In[34]:


from scipy import stats


# ## Test assumptions:

# In[35]:


WBiz2018Sub2['Owners_Sex'].hist()


# In[36]:


WBiz2018Sub2['Owners_Ethnicity'].hist()


# In[37]:


WBiz2018Sub2['Vet_Status'].hist()


# In[38]:


WBiz2018Sub2['Sales'].hist()


# ### Data is not normally distributed and therefore violates assumptions.

# In[ ]:




