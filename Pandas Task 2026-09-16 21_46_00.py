# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
import pandas as pd

# COMMAND ----------

# MAGIC %md
# MAGIC 1. CREATING A DICTIONERY
# MAGIC - A dictionary in Python is a way of storing information using a key and a value also known as KEY-VALUE PAIRS.
# MAGIC - Dictioneries are created using curly braces {} to tell python that we are creating a dictionery. Basically, curly braces contain the whole dictionery.
# MAGIC - Inside the curly braces, that's where we put our key-value pairs, e.g, name (Key):Violet(value)
# MAGIC - The colon (:) connects the key to the value. In simple terms, it tells python that "This key (name)belongs to this value (Violet)".

# COMMAND ----------

# 1.Creating a table
df={
    'name':["Alice","Bob","Carol","David"],
    'age':[22,35,28,40],
    'city':["JHB","CPT","DBN","JHB"],
    'salary':[150,300,250,400]
}

# 2. Creating a new variable
employees=pd.DataFrame(df)

# 3. Displaying the DataFrame
display(employees)

# COMMAND ----------

# This code shows only the employees whose age is greater than 30. employees["age"] looks at the age column, and > 30 checks which employees are older than 30. 

# The outside employees[...] then filters the table and shows only those matching rows. 
# In simple terms: “Show me all employees who are older than 30.”

employees[employees["age"]>30]

# COMMAND ----------

# The cosde show only the employees whose city is JHB. employees["city"] looks at the city column, and == "JHB" checks which employees have JHB as their city. 

# The outside employees[...] then filters the table to show only those employees. 
# In simple terms: “Show me all employees who are from JHB.”

employees[employees["city"] == "JHB"]

# COMMAND ----------

# The code tells Python to show only employees who meet both conditions: their age is greater than 25 AND their salary is greater than 300.

# employees["age"] > 25 → checks who is older than 25.
# employees["salary"] > 300 → checks who earns more than 300.
# & → means AND, so both conditions must be true.
# employees[...] → filters the table and shows only the matching employees.
# In simple terms: “Show me employees who are older than 25 and earn more than 300.”

employees[(employees["age"] > 25) & (employees["salary"] > 300)]



# COMMAND ----------

# The code tells Python to filter the employees table and show employees who meet at least one of the two conditions. 

# The first condition, employees["city"] == "JHB", checks whether the employee is from JHB, while the second condition, employees["age"] >= 30, checks whether the employee is 30 years old or older. 

# The | symbol means OR, so an employee will be included if they are from JHB, if they are 30 or older, or if both are true. In simple terms: “Show me employees who are from JHB OR are 30 years old or older.”

employees[(employees["city"] == "JHB") | (employees["age"] >= 30)]


# COMMAND ----------

# This code tells Python to show only the employees whose city is NOT JHB or CPT. 

# The .isin(["JHB", "CPT"]) checks whether each employee’s city is JHB or CPT, while the ~ means “not”, so it reverses the result. 
# In simple terms, it means: “Give me all employees who do not live in JHB or CPT.”

employees[~employees["city"].isin(["JHB", "CPT"])]


# COMMAND ----------

# The code tells Python to filter the employees table and show only employees whose age falls between 0 and 30. employees["age"] tells Python to look at the age column, while .between(0,30) checks whether each age is within the range 0 to 30, including both 0 and 30. 

# The outside employees[...] then displays only the rows that meet this condition. 
# In simple terms: “Show me all employees who are between 0 and 30 years old.”

employees[employees["age"].between(0,30)]


# COMMAND ----------

# The code checks the salary column for missing values. employees["salary"] tells Python to look at the salary column, while .isna() checks each row to see whether the salary is missing. 

# Python will return True when the salary is missing and False when a salary is present. 
# In simple terms: “Check which employees do not have a salary recorded.”

employees["salary"].isna()


# COMMAND ----------

# The code shows only the employees who have a salary recorded. employees["salary"] tells Python to look at the salary column, while .notna() checks whether each salary is not missing. 

# The outside employees[...] then filters the table and displays only the rows where a salary value exists. 
# In simple terms: “Show me all employees who have a salary recorded.”

employees[employees["salary"].notna()]