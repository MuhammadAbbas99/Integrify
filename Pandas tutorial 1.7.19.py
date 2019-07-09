# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 09:32:23 2019

@author: Hashim
"""

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
#%matplotlib inline
from sklearn.linear_model import LinearRegression


pd.read_csv('pandas_tutorial_read.csv', delimiter = ';')
article_read = pd.read_csv('pandas_tutorial_read.csv', delimiter=';', names = ['my_datetime', 'event', 'country', 'user_id', 'source', 'topic'])
article_read
article_read.head()
article_read.tail()
article_read.sample(5)
#article_read[['country', 'user_id']]
#article_read.user_id
article_read['user_id']

article_read[article_read.source == 'SEO']

article_read.source == 'SEO'

#the output of the first function is he input to the second function.
article_read.head()[['country', 'user_id']]    #same commands
article_read[['country', 'user_id']].head()

article_read.tail()[['country', 'user_id']]    #same commands
article_read[['country', 'user_id']].tail()

article_read.sample(5)[['country', 'user_id']] #same commands
article_read[['country', 'user_id']].sample(5)

# Select the user_id, the country and the topic columns for the users who are from country_2! 
# Print the first five rows only!

article_read[['user_id', 'country']][article_read.country=='country_2'].head()  # onle liner solution


# folowing are multi-line solutions.
usid_country = article_read[['user_id','country']]
Country_2 = usid_country[article_read.country=='country_2']
o_p = Country_2.head()
o_p



######################   iloc is an mportant function            ############################




'''
Task:
    Question 3)
    Parial data can be read usng the command sample(n), whereas n respresents the numeber of 
    
    '''