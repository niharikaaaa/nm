#!/usr/bin/env python
# coding: utf-8

# In[2]:


import boto3
from sqlalchemy import create_engine
import pymysql
import pandas as pd
import pyarrow as pa
from zipfile import ZipFile


# In[11]:


session = boto3.Session(
    region_name='us-east-1',
    aws_access_key_id='AKIAQ6HZNXKJYJ7JRENT',
    aws_secret_access_key='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',
)
s3 = session.resource('s3')


# s3 = boto3.resource
# (
# 's3',
# 'us-east-1',
# 'AKIAQ6HZNXKJYJ7JRENT',
# '8LcmiUYXEd/5AwEG6S8EbDFRgcMzAI0blRhNcjPX'
# )


# In[12]:


db_connection_str = 'mysql+pymysql://admin:password@db.cgjpezx3a6v9.us-east-1.rds.amazonaws.com/db1'
db_connection = create_engine(db_connection_str)


# In[15]:


file_metadata_df = pd.read_sql('SELECT * FROM FILE_METADATA WHERE ACTIVE_IND="Y" limit 1', con=db_connection)

##converting FILE_COLUMN_METADATA to a dataframe (all tuples with the required file name from FILE_METADATA)
file_column_metadata_query = 'SELECT * FROM FILE_COLUMN_METADATA'
file_column_metadata_df = pd.read_sql(file_column_metadata_query, con=db_connection)


# In[16]:


file_column_metadata_df


# In[26]:


cols_lengths = file_column_metadata_df['COLUMN_LENGTH'].tolist()


# In[27]:


cols_lengths


# In[ ]:




