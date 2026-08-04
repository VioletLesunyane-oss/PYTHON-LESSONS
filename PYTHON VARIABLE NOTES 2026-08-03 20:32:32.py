# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
# MAGIC %md
# MAGIC 08/03/2026
# MAGIC Facilitator: Rofhiwa Nemukula
# MAGIC
# MAGIC PYTHON PROGRAMMING
# MAGIC Python is a vasetile language that you can build anything with such as apps etc. 
# MAGIC Our lesson will not focus on programming but on data analytics using python.

# COMMAND ----------

# MAGIC %md
# MAGIC PYTHON FUNDAMENTAL
# MAGIC 1.Variables- a variable is a storage container that stores values/data.
# MAGIC e.g name = 'Violet' a 'name' is a variable/container and 'Violet' is a value(data that is astored in the variable)
# MAGIC We then use the print() funtion to display the value 'Violet' that is stored in the variable'name'
# MAGIC see example below:

# COMMAND ----------

name = 'Violet'
print(name) 

# COMMAND ----------

# Variable names are case sensitive. Meaning that 'Name' and 'name' considers them as different
name = 'Rofhiwa'
print(name)
NAME = 'rofhi'
print(NAME)


# COMMAND ----------

name = 'Rofhiwa'
print(name)

# COMMAND ----------

#----Rules for naming Variables--
#Variable names can only contain letters(a-z), numbers (0-9) and underscores(_)
#A variable name cannot start with a number
#Variable names are case sensitive
#Do not use Python keywords as variable names e.g 'print' we can't use it as a variable name.


# COMMAND ----------

# MAGIC %md
# MAGIC Variable Naming Rules
# MAGIC
# MAGIC 1. Variable names must only contain numbers (0-9), letters(a-z) and underscore (_).

# COMMAND ----------

#Underscores are only used in the middle of a variable and a name. And you cannot put any other symbol besides an underscore e.g name#surname
name_surname = 'Elon Musk'


# COMMAND ----------

#A variable name can start with an underscore but it cannot start with a number
_name = 'Rofhiwa'

# COMMAND ----------

# MAGIC %md
# MAGIC 2. Variable names cannot start with a number

# COMMAND ----------

#Outcome is an error because a variable name cannot start with a number
2name = 'Rofhiwa'

Unless you convert a number two into a letter e.g.
two_man = 'Rhofiwa'

# COMMAND ----------

# MAGIC %md
# MAGIC 3. Variable names are case sensitive
# MAGIC

# COMMAND ----------

#Samll letter y and capital letter Y are considered two different things
y = 'Rofhiwa'
Y = 'rofhiwa'

# COMMAND ----------

# MAGIC %md
# MAGIC A variable name, cannot be a python keyword

# COMMAND ----------

# in python, if is a keyword so it cannot be used as a variable name
if = "Rofhiwa Nemukula"

import = "Data Science"

# COMMAND ----------

#Single quotes and double quotes work the same in python
name = 'Mbali'
surname = "Nemukula"