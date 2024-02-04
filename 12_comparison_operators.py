import quandl
import pandas as pd
import pickle # Allows you to save objects as a byte stream (Without using csv etc)
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

# HOW TO GET RID OF ERONEOUS DATA

bridge_height = {'meters':[10.26, 10.31, 10.27, 10.22, 10.23, 6212.42, 10.28, 10.25, 10.31]}
    # Note the outlier in the data

df = pd.DataFrame(bridge_height) # Convert the dictionary to a dataframe so you can manipulate
df['STD'] = df['meters'].rolling(window=2).std()
print(df)

df_std = df.describe()['meters']['std'] # To get mean standard deviation
print(df_std)

df = df[ (df['STD'] < df_std) ] # [(Comparison Operator)] used to change dataframe

df['meters'].plot()
plt.show()



