# Import pandas
import pandas as pd

# Import Twitter data as DataFrame: df
tweets_df = pd.read_csv('tweets.csv')
#pd.set_option("display.max_rows", None, "display.max_columns", None)
#print(df.loc[:,'lang']) prints all rows and the column labelled name
#print(df.iloc[1:3,2]) #prints 1rst & 2nd rows and the 20th column
#print(df['lang']) prints the column labelled 'lang'

def count_entries(df, col_name):
# Initialize an empty dictionary: langs_count
    langs_count = {}

# Extract column from DataFrame: col
    col = df[col_name]

# Iterate over lang column in DataFrame
    for entry in col:

    # If the language is in langs_count, add 1 
        if entry in langs_count.keys():
            langs_count[entry] += 1
    # Else add the language to langs_count, set the value to 1
        else:
            langs_count[entry] = 1

# Return the langs_count dictionary
    return langs_count

# Call count_entries(): result
result = count_entries(tweets_df, 'lang')

# Print the result
print(result)