# =============================================================================
# Building Datasets
# =============================================================================

# We can import quandl and use quandl.get() to do more efficiently extract data

import quandl
import pandas as pd

df = quandl.get('FMAC/HPI_AK')
print(df.head())
    # Quandl automatically puts the date as the index (Thanks quandl)

fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    # Get the link fro wikipedia (this could be useful for a lot of stuff)
    # Put ALL data into a lit
#print(fiddy_states)
    # Use above to find the dataframe and column number of abbreviations

print(fiddy_states[0][1])#Gives us the column 1 in the first table

for abbv in fiddy_states[0][1][1:]: # Start from 1 as you dont want header col
    print('FMAC/HPI_'+str(abbv))
    # Gets the right code to request from quandl
    


