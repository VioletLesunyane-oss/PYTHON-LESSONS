# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
# MAGIC %md
# MAGIC ##MATPLOTLIB
# MAGIC - Matplotlib is a comprehensive open source library for creating static, animated, and interactive visualizations in Python.
# MAGIC - It makes easy things easy and hard things possible.

# COMMAND ----------

# MAGIC %md
# MAGIC ###Import Libraries

# COMMAND ----------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# COMMAND ----------

# MAGIC %md
# MAGIC ####Data Ingestion

# COMMAND ----------

df=spark.table("bright_coffee_analysis.default.bright_coffee_shop_eda_1")

df=df.toPandas()
display(df)