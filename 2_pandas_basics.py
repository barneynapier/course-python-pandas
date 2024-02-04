import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style 
import numpy as np
style.use('ggplot')

web_stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[43,34,65,56,29,76],
             'Bounce_Rate':[65,67,78,65,45,52]}

df = pd.DataFrame(web_stats) 
        # df is the standard notation for dataframe and makes it easier for others

print(df.set_index('Day', inplace=True)) 
        # This sets the index equal to day (Just a single instance if you dont use inplace)
        # Note you can also do df = df.set_index, this will do the same thing

print(df['Visitors'])
print(df.Visitors)
        # These two do the same thing, but only the first one can handle spaces 

print(df[['Bounce_Rate', 'Visitors']])
        # You reference multiple columns like this

print(df.Visitors.tolist())
        # Makes the data into a list for you

print(np.array(df[['Bounce_Rate', 'Visitors']]))
        # Can import numpy to make a list in a list (Doesnt work with .tolist() )
        # An array is basically a list of lists

