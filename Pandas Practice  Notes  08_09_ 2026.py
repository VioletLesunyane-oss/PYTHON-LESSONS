# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
import pandas as pd

# COMMAND ----------

#Creating a table
data = {
    'Cust_id':[1,2,3,4],
    'Name': ['John', 'Rochester', 'Mpho', 'Amanda'],
    'Age': [53,30,39,33]
}

#Converting the table into pandas dataframe
df=pd.DataFrame(data)

display(df)

# COMMAND ----------

#Shows first 3 rows of the table/data
df.head(3)

# COMMAND ----------

#Shows last 3 rows of the table/data
df.tail(3)

# COMMAND ----------

#A python list
my_cars=["BMW","Suzuki","Merc","VW"]

# COMMAND ----------

type(my_cars)

# COMMAND ----------

#Dictionery
my_profile = {
    "Name": "Mpho",
    "Surname": "Lesunyane",
    "Birth_year": 1987,
    "Location": "South_Africa",
    "Age": 39
}

# COMMAND ----------

type(my_profile)

# COMMAND ----------

#Shows names of columns in the table
df.columns

# COMMAND ----------

#Shows number of rows and columns
df.shape

# COMMAND ----------

#Shows columns and the data type
df.dtypes

# COMMAND ----------

#Shows the table overview
df.info()