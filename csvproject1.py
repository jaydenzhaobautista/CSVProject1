#reading data from the hurricanes.csv file. 

import csv
import pandas as pd
from pandas import *

# this is a DataFrame. A DataFrame is a data structure that organizes data into a 2-dimensional table of rows and columns, much like a spreadsheet. 
df = pd.read_csv('hurricanes.csv')


# df.head() returns the top five lines of the csv file
print(df.head())

# df.tail() returns the bottom five lines of the csv file
print(df.tail())

# df.head(n) returns the first n lines
print(df.head(3))

# df.tail(n) returns the last n lines
print(df.tail(3))

# reading each column of the CSV file
print(df[["2005", "2006", "2007"]])

# readomg each row of the CSV file
print(df.iloc[0:4])

# reading of one column of the CSV file
df2 = print(df["2005"])

# turning every column of the CSV file into a list
hurricaneList2005 = df["2005"].tolist()
hurricaneList2006 = df["2006"].tolist()
hurricaneList2007 = df["2007"].tolist()
hurricaneList2008 = df["2008"].tolist()
hurricaneList2009 = df["2009"].tolist()
hurricaneList2010 = df["2010"].tolist()
hurricaneList2011 = df["2011"].tolist()
hurricaneList2012 = df["2012"].tolist()
hurricaneList2013 = df["2013"].tolist()
hurricaneList2014 = df["2014"].tolist()
hurricaneList2015 = df["2015"].tolist()


# creating a dictionary

myDict = {}


# totaling the number of hurricanes in every year
sum = 0
for i in hurricaneList2005:
    sum = sum + i
myDict["2005"] = sum

sum = 0
for i in hurricaneList2006:
    sum = sum + i
myDict["2006"] = sum

sum = 0
for i in hurricaneList2007:
    sum = sum + i
myDict["2007"] = sum

sum = 0
for i in hurricaneList2008:
    sum = sum + i
myDict["2008"] = sum

sum = 0
for i in hurricaneList2009:
    sum = sum + i
myDict["2009"] = sum

sum = 0
for i in hurricaneList2010:
    sum = sum + i
myDict["2010"] = sum

sum = 0
for i in hurricaneList2011:
    sum = sum + i
myDict["2011"] = sum

sum = 0
for i in hurricaneList2012:
    sum = sum + i
myDict["2012"] = sum

sum = 0
for i in hurricaneList2013:
    sum = sum + i
myDict["2013"] = sum

sum = 0
for i in hurricaneList2014:
    sum = sum + i
myDict["2014"] = sum

sum = 0
for i in hurricaneList2015:
    sum = sum + i
myDict["2015"] = sum

print(myDict)







