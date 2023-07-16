#!/usr/bin/env python
# coding: utf-8

# # SQL

# SQL is programming language used w/ databases. BigQuery is web service that lets you apply SQL to huge datasets.

# To use BigQuery:

# In[1]:


from google.cloud import bigquery


# To install package:

# In[ ]:


# pip install --upgrade google-cloud
# pip install --upgrade google-cloud-bigquery
# pip install --upgrade google-cloud-storage


# Create `Client` object - used to retrieve information from BigQuery datasets.

# In[ ]:


# Create a "Client" object
client = bigquery.Client()


# 
