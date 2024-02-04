# Pickling
# Using the code from lession 4 again which involves quandl
# Pickling allows you to save dataframes not to a csv

import quandl
import pandas as pd
import pickle # Allows you to save objects as a byte stream (Without using csv etc)

api_key = open('quandl_api_key.txt', 'r').read() # This is why you needed a quandl account

def state_list():
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][1][1:]
	# Get the link from wikipedia (this could be useful for a lot of stuff)
	# Put ALL data into a list
	# Print this off once to find the data from it that you need (col num etc)


def grab_initial_state_data():
    states = state_list()
    main_df = pd.DataFrame()

    for abbv in states: # Start from 1 as you dont want header col
        query = 'FMAC/HPI_'+str(abbv)   
        df = quandl.get(query, authtoken=api_key, index_col='Date')
        df.columns = [abbv] # To stop the suffix error

        if main_df.empty: #Returns boolean of True if it is empty
            main_df = df
        else:
            main_df = main_df.join(df)

    print(main_df.head())

    main_df.to_pickle('fiddy_states.pickle')

# grab_initial_state_data() # Once grabbed once we dont need to do it again

HPI_data = pd.read_pickle('fiddy_states.pickle')

# This is the generic way but its faster with pandas
##pickle_out = open('fiddy_states.pickle', 'wb') # For write bytes
##pickle.dump(main_df, pickle_out)
##pickle_out.close()
##pickle_in = open('fiddy_states.pickle', 'rb') # For read bytes
##HPI_data = pickle.load(pickle_in) # Loads the data from pickle (Waaaay faster)
##print(HPI_data)


















