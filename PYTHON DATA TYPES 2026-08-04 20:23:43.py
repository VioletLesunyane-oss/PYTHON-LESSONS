# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
# MAGIC %md
# MAGIC PYTHON DATA TYPES
# MAGIC
# MAGIC 1. Text Type
# MAGIC - Its a combination of characters
# MAGIC - It is a string(str) or an object
# MAGIC - We indicate that something is a string if it has 'single' or "double" quotes
# MAGIC

# COMMAND ----------

school_name = 'BrightLearn'

# COMMAND ----------

#The type () Function is used to check the data type contained in a specific variable
type(school_name) - #school_name is a string

# COMMAND ----------

#We use tripple double quotes at the starts and end of the variable if it is a multiline. 
love_message = """
             Hello Baby

             I miss you

             I want you back
             """
print(love_message)
            

# COMMAND ----------

#As long as its in inverted commas, its considered a string
df = "93409u12jpojmf-0wqr2;p3i[m]"

print(df)

# COMMAND ----------

# MAGIC %md
# MAGIC 2. NUMERIC TYPES
# MAGIC In nemric data types we have tree things
# MAGIC -An integer(int) - a number without a decimal e.g age = 39
# MAGIC -A float (float) - is a number with a decimal

# COMMAND ----------

#We use type() to display the name of the value
x = 28
type(x)
 #another example
x = 28.5
type(x)
#Outcome would be the string (float) cause 28.5 is a float

# COMMAND ----------

# MAGIC %md
# MAGIC 3.Sequence
# MAGIC - It is an array
# MAGIC - Multiple values stored in one variable
# MAGIC - List
# MAGIC - Tuple
# MAGIC - Range

# COMMAND ----------

#example
my_cars = ["BMW", "SUZUKI", "VW", "CHERY"]
type(my_cars)
#Outcome will return the word list which is the description on the value that is within the variable

# COMMAND ----------

#example
my_cars = {"BMW", "SUZUKI", "VW", "CHERY"}
type(my_cars)
#Outcome will return the word set which is the description on the value that is within the variable

# COMMAND ----------

#example
my_cars = ("BMW", "SUZUKI", "VW", "CHERY")
type(my_cars)
#Outcome will return the word tuple which is the description on the value that is within the variable

# COMMAND ----------

# MAGIC %md
# MAGIC 4.Mapping
# MAGIC - We call this a dictionery (dict)
# MAGIC - Key: Value pair

# COMMAND ----------

#A PYTHON Dictionery is a key value pair
{"name" : "John Doe",
 "age" : 30,
 "email" : "john.m@gmail.com"
 }

# COMMAND ----------

my_profile = {
    "First Name":"Violet",
    "Last Name":"Lesunyane",
    "Age":39,
    "Position":"Data Analyst",
    "Company":"FNB"
}
print(my_profile)
type(my_profile)

# COMMAND ----------

# MAGIC %md
# MAGIC