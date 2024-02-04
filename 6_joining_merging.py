# Joining and Merging DFs

import pandas as pd

df1 = pd.DataFrame({'Year':[2001, 2002, 2003, 2004],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2001, 2002, 2003, 2004])

df3 = pd.DataFrame({'Year':[2001, 2003, 2004, 2005],
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   index = [2001, 2002, 2003, 2004])

merged = pd.merge(df1, df3, on=['Year'], how='left'))
    # The 'on' part merges based on those columns
    # warning this duplicates data
    # left merges on the 'left' df and right on the 'right' df
    # 'outer' joins on the union of the keys (includes all NaN)
    # 'inner' only includes indexes where data is in both sets
merged.set_index('Year', inplace=True)

##df1.set_index('HPI', inplace=True)
##df3.set_index('HPI', inplace=True)
##
##joined = df1.join(df3)
##print(joined)

some_data = ['I', 'am', 'so', 'amazing']
print(' '.join(some_data)) # can also use join like ive prevously learned


# Note that merging data on all the columns is the same as joining how=outer
    # Join requires suffixes though and im yet to figure these out

