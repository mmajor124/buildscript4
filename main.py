# Python program to demonstrate
# sys.argv
import json
import sys
import csv

#print("This is the name of the program:", sys.argv[1])

#print("Argument List:", str(sys.argv))

dictgot=json.loads(sys.argv[1])
print(dictgot)
gotindex={}


#My Game of Thrones dictionary
if len(dictgot) > 1 : 
    dictgot.pop(0)
#gotindex.update({"name" == dictgot["name"]})
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


