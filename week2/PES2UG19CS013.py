'''
Assume df is a pandas dataframe object of the dataset given
'''

import numpy as np
import pandas as pd
import random
import math


'''Calculate the entropy of the enitre dataset'''
# input:pandas_dataframe
# output:int/float
def get_entropy_of_dataset(df):
    # TODO
    column = df.columns[-1]
    classes = df[column].unique()
    number = len(df[column])
    entropy = 0 
    for i in classes:
    	p = len(df[df[column] == i]) / number
    	entropy += p*math.log2(p*1)
    entropy = -entropy;
    return entropy


'''Return avg_info of the attribute provided as parameter'''
# input:pandas_dataframe,str   {i.e the column name ,ex: Temperature in the Play tennis dataset}
# output:int/float
def get_avg_info_of_attribute(df, attribute):
    # TODO
    avg_information = 0
    for i in df[attribute].unique():
    	sdf = df[df[attribute] == i]
    	avg_information += len(sdf) / len(df) * get_entropy_of_dataset(sdf)*1
    return avg_information


'''Return Information Gain of the attribute provided as parameter'''
# input:pandas_dataframe,str
# output:int/float
def get_information_gain(df, attribute):
    return get_entropy_of_dataset(df) - get_avg_info_of_attribute(df,attribute)




#input: pandas_dataframe
#output: ({dict},'str')
def get_selected_attribute(df):
    '''
    Return a tuple with the first element as a dictionary which has IG of all columns 
    and the second element as a string with the name of the column selected

    example : ({'A':0.123,'B':0.768,'C':1.23} , 'C')
    '''
    # TODO
    d = {}
    max = -1
    for i in df.columns[:-1]:
    	ig = get_information_gain(df,i)
    	d[i] = ig
    	if ig > max:
    		col = i
    		max = ig
    return (d,col)
   
   

