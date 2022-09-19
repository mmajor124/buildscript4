#Date - 9/15/22 
#Build Script 4
#Description - This is a complimentary script to the bash script, buildscript4va.sh.  This script imports the API data as json and converts it to the downloaded .csv file.
#author: Mike Major

#Imports json, sys, and csv modules into existing script.  This will make it easaier for specific data types to be converted.
import json
import sys
import csv

#Converts the json string to a dictionary.
dictgot=json.loads(sys.argv[1])
#Stores selected Game of Thrones character data.
gotindex={}

print(dictgot)
#If the length of the dictionary list exceeds 1, then remove the first listed dictionary.  This was done due to an error with Daenerys Targaryen.  
if len(dictgot) > 1 : 
    dictgot.pop(0)
#Extract specific API values from the indexed variable.
gotindex['name'] = dictgot[0]['name']
gotindex['gender'] = dictgot[0]['gender']
gotindex['born'] = dictgot[0]['born']
gotindex['culture'] = dictgot[0]['culture']
gotindex['titles'] = ' * '.join(dictgot[0]['titles'])
gotindex['playedBy'] = ' * '.join(dictgot[0]['playedBy']).replace(",", " *")
gotindex['aliases'] = ' * '.join(dictgot[0]['aliases'])
print(gotindex)


#with open(gotindex) as json_file:
	#gotjson = json.load(json_file)
#Uses the csv module to write to the csv file named "got.csv"
gotdata = open('/home/jax/Desktop/got.csv', 'w', newline='')
csv_writer = csv.writer(gotdata)

#count = 0
#for data in gotindex:
	#if count == 0:
header = gotindex.keys()
csv_writer.writerow(header)
#count += 1
csv_writer.writerow(gotindex.values())

gotdata.close()


