# Using quandl data
import pandas as pd

df = pd.read_csv('ZILLOW-Z77006_ZRIMFRR.csv')
        # You have to put .csv after the name
        # This works when the data is in the same dir() as this python file
print(df.head())
df.set_index('Date', inplace=True)
df.to_csv('newcsv2.csv')
        # Saves the data with the date index in a new csv in the same dir() as this code

df = pd.read_csv('newcsv2.csv', index_col=0)
        # the index_col=0 gets rid of the index's column status (Rid of it), makes date the index
        # Note index_col=0 doesnt work on excel file

df.columns = ['Austin_HPI']
        # Renames the value column, but why doesnt it change the date column? (Because its your index)
print(df.head())

df.to_csv('newcsv3.csv', header=False)
        # Gets rid of the headers in the csv file

df = pd.read_csv('newcsv3.csv', names=['Date', 'Austin_HPI'], index_col=0)
        # Use names=[] to give a headerless csv headers
print(df.head())

# Note when manipulating the data you are doing so to a pandas dataframe which you then save as csv

#df.to_excel('example.xlsx')
df.to_html('example.html')
        # This is how =you can convert the data to excel or html

df = pd.read_csv('newcsv3.csv', names=['Date', 'Austin_HPI'])
        # Must give the same number of names as there are columns
print(df.head())

df.rename(columns={'Austin_HPI':'77006_HPI'}, inplace=True)
        # Renamed a single column, watch out though it still does it if you make an error in the name
print(df.head())


