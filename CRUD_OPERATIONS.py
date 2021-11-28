#!/usr/bin/env python
# coding: utf-8

# In[1]:


#establish the connection between python and mysql
import mysql.connector as sql
connection=sql.connect(host="localhost",user="root",password="sql003")
print(connection) #gives the memory address of the established connection


# In[6]:


#creating the database

cursor=connection.cursor() #cursor allows us to execute the queries of mysql in python

cursor.execute("CREATE DATABASE prognoz_sreejith_database")


# In[7]:


#entering into the database created
connection=sql.connect(host="localhost",user="root",password="scorpiosql003",database="prognoz_sreejith_database")


# In[8]:


#creating tables inside the database created
cursor=connection.cursor() #cursor allows us to execute the queries of mysql in python

cursor.execute("CREATE TABLE data_students(name varchar(20), subject varchar(20), marks int)")


# In[11]:


#inserting records inside the table

query="INSERT INTO data_students(name, subject, marks) VALUES (%s,%s,%s)" #%s is going to act as placeholder

values=[('john','statistics',78),
       ('Meera','deep learning', 93),
       ('George','machine learning', 88),
       ('Muskan','computer vision', 87)]

cursor.executemany(query, values)


# In[12]:


connection.commit()  #saves the changes made since the last checkpoint


# In[13]:


# Update Records in table

cursor=connection.cursor()        

query="update data_students set name='Michel' where subject='machine learning'"

cursor.execute(query)

connection.commit()


# In[14]:


# Update Records in table

cursor=connection.cursor()

query="update data_students set name='Tyler' where subject ='statistics'"

cursor.execute(query)

connection.commit()


# In[15]:


# Deleting a record from the table

cursor=connection.cursor()

query=" delete from data_students where name='Muskan'"

cursor.execute(query)

connection.commit()


# In[16]:


# drop the table

cursor= connection.cursor()

query=" drop table data_students"

cursor.execute(query)

connection.commit()


# In[19]:





# In[20]:





# In[21]:





# In[22]:





# In[23]:





# In[ ]:




