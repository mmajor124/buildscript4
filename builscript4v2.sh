#!/bin/bash

#Build Script 4
#author: Mike Major

echo "Here is the top 10 list of characters in Game of Thrones!"
cat gotchar.txt

read -p "Enter a number for a character in the Game of Thrones: " numchar
  if [ $numchar -lt 1 ] || [ $numchar -gt 10 ]; 
 then
   numchar=1 
   echo "Follow the instructions or face the wrath of the Night King!"
   echo "--------------------------------------------------------------"
  fi
    echo $numchar
    
    character=$(cat gotchar.txt | head -n $numchar | tail -n 1 | cut -d "." -f 2 | sed 's/^[ \t]*//')
    echo $character
    

   gotdata=$(curl -s -X GET https://www.anapioficeandfire.com/api/characters --data-urlencode "name=$character")
    
    #echo "$gotdata"
    python3 main.py "$gotdata"





