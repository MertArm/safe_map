import csv
import json
import pandas as pd
from pandas import DataFrame

data = pd.read_csv("Crimes_-_Map.csv", index_col ="DATE  OF OCCURRENCE" )
data.drop(["CASE#",
           "BLOCK",
           " IUCR",
           " SECONDARY DESCRIPTION",
           " LOCATION DESCRIPTION",
           "ARREST",
           "DOMESTIC",
           "BEAT",
           "WARD",
           "FBI CD",
           "X COORDINATE",
           "Y COORDINATE",
           "LOCATION",
           "Historical Wards 2003-2015",
           "Zip Codes",
           "Community Areas",
           "Census Tracts",
           "Wards"], axis = 1, inplace = True)

df = DataFrame(data, columns= [' PRIMARY DESCRIPTION','LATITUDE','LONGITUDE'])
df.to_csv("crimes.csv", sep=",")

csvfile = open('crimes.csv', 'r')
jsonfile = open('crimes.json', 'w')

fieldnames = ('DATE  OF OCCURRENCE', ' PRIMARY DESCRIPTION','LATITUDE','LONGITUDE')
reader = csv.DictReader( csvfile, fieldnames)
out = json.dumps( [ row for row in reader ] )
jsonfile.write(out)