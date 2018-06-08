import pandas as pd
import geopandas as gpd
import os
import sys

#Finds the file and sets it to a dataframe
Location = r'insert file path here'
df = pd.read_csv(Location)

#Sets the columns of the data frames with headers
df = pd.read_csv(Location, names=['chainage', 'X', 'Y', 'Z', 'blank1', 'blank2'])

#This will show if any of the columns are the wrong variable type
df.dtypes

#Changes any desired column to numeric variables
df = pd.DataFrame(df, columns=['chainage', 'blank2'])
df[['chainage', 'blank2']] = df[['chainage', 'blank2']].apply(pd.to_numeric)

#Adds any desired number onto the Z column values
df['Z'] = df['Z'] + 46

#Rounds the Z columns values to five decimal places
df.Z = df.Z.round(5)

#Saves the new dataframe to a selected file type and removes the header 
#and index from the file
df.to_csv("insert file path here", 
          header=False, index=False)