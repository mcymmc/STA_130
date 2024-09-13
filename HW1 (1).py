#!/usr/bin/env python
# coding: utf-8

# <h1>Pre-Lec</h1>

# ## 1.

# In[3]:


import pandas as pd
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
df = pd.read_csv(url, sep=';')
df.isna().sum()


# ## 2.

# In[5]:


rows, columns = df.shape
print(f'Number of rows: {rows}')
print(f'Number of columns: {columns}')


# Observations are the rows in the data set
# Variables are the columns of the data set

# ## 3.

# In[8]:


summary = df.describe()

print(summary)


# ## 4.

# In[9]:


print(df.dtypes)


# In[12]:


url2 = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"

df2 = pd.read_csv(url2)

print(df2.dtypes)
print(df2.describe())
print(df2.shape)


# A) df2.shape reports the number of rows and columns in the data set. In this case, 891 rows and 15 columns. df2.describe() only works through columns with numerical values. As you can from the df2.dtypes list, only categories with either float64 or int64 are shown in df2.describe()
# 
# B) df2.shape 891 rows because there are 891 rows. "count" in df2.describe() shows the number of non-null values. This is why the numbers provided from each shape and describe may be different. It means there are missing values for "age"

# ## 5. 

# An attribute shows the data or properties of the dataframe. They do not need to access the actual information such as numerical values or categories etc. Instead they give you the data about the structure of the object. In the case of df.shape, it returns the number of rows and columns.
# 
# A method is an action that is performed on the object itself. They do need to access the information and in the case of df.describe(), they do.

# <h1>Post-Lec</h1>

# ## 6.

# Count: Shows the number of non-null values per column. It should be the total number of rows minus the amount of rows that contain missing values for that column.
# 
# Mean: The average of all the values in that column.
# 
# Std: The standard deviation of the values in that column. This shows how far apart the values are from the mean. A lower std means the values are closer to the mean and a higher std means the values are farther from the mean (on average).
# 
# Min: Shows the smallest value in the column
# 
# 25%: Shows the 25th percentile of the values in the column. So that means 25% of the values in the column are below the given value. For example if 100 students took an exam out of 100 points. If the 25% is 50, it means 25% of the students failed the exam.
# 
# 50%: Shows the 50th percentile of the values in the column.
# 
# 75: Shows the 75th percentile of the values in the column.
# 
# Max: Shows the highest value in that column
# 

# ## ChatBot History:

# https://chatgpt.com/share/66e3639a-ca24-8009-90c6-8131c320f98b

# ## 7.

# 1.

# Suppose you want to analyze data about students test and assignment grades but you only want to analyze students who have finished all their tests and assignments. So dropna would be better in this case because it removed all rows (students) who have yet to complete their tests and assignments. deleting a column wouldn't be helpful here because you may be removing data for students who HAVE completed all their tests and assignments (which you want to analyze)

# 2.

# Suppose you want to analyze the students test and assignment grades like above. But the dataset includes student numbers and names which are irrelevant to you because you just want to analyze the students as a group instead of individually. So you can deleted the variables "name" and "id" to get rid of useless data.

# 3.

# Because perhaps the missing data that dropna would've gotten rid of was useless data that you don't need. It would then get rid of the entire observation. That is why deleting redundant data could be important because then you can focus only on what you need to analyze.

# 4.

# In[2]:


import pandas as pd

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"

df = pd.read_csv(url)

df.dropna()


# By using the dropna method, you only consider non-null values, since you do not want to analyze incomplete data in your data analysis. This will prevent several problems, such as those missing values that might spoil the entire consistency of data, which is very important for correct statistical results.

# ## 8.

# In[27]:


url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"

df = pd.read_csv(url)


df.columns


# 1.
# 
# df.groupby("col1")["col2"].describe() takes the values of col1 and turns them into one group per value. Then ["col2"] looks through the data in col2 (you're basically notifying the pandas that you're interested int this column and that you're about to perform an action based on that column. Then .describe() performs the action on col2 per group of col1. So the .describe() method runs on col2 for each col1 group displays that data. 

# In[28]:


df.groupby("survived")["sex"].describe()


# survived = 0 means did not survive and it shows 549. Unique means there are 2 unique categories for sex which are male and female. Top shows male appeared most times and freq shows the frequency of male which was 468.
# 
# survived = 1 means survived and it shows 342. It consists of mostly females and sits at 233 females.

# 2.

# In[29]:


df.describe()


# In[30]:


df.groupby("survived")["age"].describe()


# From what I see, the values of count are just separated into different groups but if you add the totals up per group, it should be the same as the "count" from df.describe()

# 3.

# A)

# In[1]:


url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"

df = pd.read_csv(url)


# The chatbot gave a solution immediately, pointing out I had not imported pandas as pd and providing the code to fix it.

# In[4]:


import pandas as pd

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"

df = pd.read_csv(url)


# B)

# In[8]:


url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanics.csv"
df = pd.read_csv(url)


# The chatbot immediately pointed out that there was a typo in the url. It corrected me on that and provided the code to fix it (it just fixed the typo)

# C)

# In[9]:


df2.groupby("pclassx")["col2"].describe()


# ChatBot told me I need to define df2 before using it. Didn't even need to use google. But at the same time I didn't really need to use the chat either because the error itself explains 'name 'df2' is not defined'

# D)

# In[1]:


import pandas as pd

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"

df = pd.read_csv(url


# Chat said to make sure all parentheses are closed. couldnt find an answer on google. I'm guessing because its such a simple mistake that people usually don't make. Google ended up showing a bunch pof different coding problems.

# E)

# In[3]:


import pandas as pd

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"

df = pd.read_csv(url)


# In[4]:


df.group_by("pclass")["sex"].describle()


# Chat had the answer pretty quickly and even told me which parts of the code is done correctly so I don't mistakenly change the correct parts. Chat pointed out both typos I had. I couldn't find the result on google because its such a specific error.

# F)

# In[8]:


df.groupby("Sex")["age"].describe()


# Chat said to check the column names and then make sure they are spelled correctly whereas google did not show any solutions. Instead, it showed threads where people say "KeyError occurs even though column exists"

# G)

# In[9]:


df.groupby(sex)["age"].describe()


# Chat once again gave the answer quickly and concisely whereas google could not show me a thread with the answer

# ## 9.

# Somewhat

# ## Chat Link

# 
