import quandl
import pandas as pd
import pickle # Allows you to save objects as a byte stream (Without using csv etc)
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

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
        # df.pct_change() gives you % change from last value (Flat at around 1%)
        df[abbv] = (df[abbv] - df[abbv][0]) / df[abbv][0] * 100.0 # Gives % change on initial value (Uptrend)

        if main_df.empty: #Returns boolean of True if it is empty
            main_df = df
        else:
            main_df = main_df.join(df)

    main_df.to_pickle('fiddy_states.pickle')

def HPI_Benchmark():
    df = quandl.get('FMAC/HPI_USA', authtoken=api_key)
    df['Value'] = (df['Value'] - df['Value'][0]) / df['Value'][0] * 100.0
    return df

#grab_initial_state_data()

#-----------------------------------------------------------------------------
# Code same up until here
# resampling from days to hours will just give you the same data repeated (Useless)

fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))
HPI_data = pd.read_pickle('fiddy_states.pickle')

TX1yr = HPI_data['TX'].resample('A', how='mean')
    # Annual=A, Monthly=M, Daily=D, Weekly=W etc (See documentation)
    # the how='' is where you decide mean, sum or ohlc (open high low close)
print(TX1yr.head())

HPI_data['TX'].plot(ax=ax1) # Can add label='' to say what the legend refers to it as
TX1yr.plot(ax=ax1) # This is how you can plot them on the same axis

plt.legend().remove() # Put loc=4 inside legend function to relocate it to the bottom right 
plt.show()



