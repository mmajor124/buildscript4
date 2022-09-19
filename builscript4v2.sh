#!/bin/bash
#Date - 9/15/22 
#Build Script 4
#Description - This script will allow you the ability to learn information about some of Game of Thrones most memorable characters.
#author: Mike Major

echo "Here is the top 10 list of characters in Game of Thrones!"
#Displays a numbered list of pre-set Game of Thrones characters.
cat gotchar.txt
#Requests input from user to select a corresponding Game of Thrones character by utilizing an if statement to authenticate numbered entries are within 1-10.  If entries entered are not within
#1-10, then the user's selection is defaulted to 1, and they are given a warning message.
read -p "Enter a number for a character in the Game of Thrones: " numchar
  if [ $numchar -lt 1 ] || [ $numchar -gt 10 ]; 
 then
   numchar=1 
   echo "Follow the instructions or face the wrath of the Night King!"
   echo "--------------------------------------------------------------"
  fi
    echo $numchar
   #Selecting the Game of Thrones character's name from the list by using the number the user selected and filtering out everything with the exception of the full name. 
    character=$(cat gotchar.txt | head -n $numchar | tail -n 1 | cut -d "." -f 2 | sed 's/^[ \t]*//')
    echo $character
    
   #Pulling Game of Thrones character data from the API and filtering by the character's name.
   gotdata=$(curl -s -X GET https://www.anapioficeandfire.com/api/characters --data-urlencode "name=$character")
    
    #echo "$gotdata"
    #Passes the API data attached to a variable into the python script "main.py".
    python3 main.py "$gotdata"




