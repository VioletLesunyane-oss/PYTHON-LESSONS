# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
df = spark.table("pandas_practice.default.viewership_analysis")

df=df.toPandas()

df.head(5)

# COMMAND ----------

df.isnull()

# COMMAND ----------

df.isnull().sum()

# COMMAND ----------

#It gives you a total number of rows and columns
df.shape

# COMMAND ----------

df.info()

# COMMAND ----------

df.astype({"TotalTimeWatched": "int"})


# COMMAND ----------

display(df)

# COMMAND ----------

df["TotalTimeWatched"] = df["TotalTimeWatched"].astype(int)

# COMMAND ----------

df.dtypes

# COMMAND ----------

df.duplicated()