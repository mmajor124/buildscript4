# Build Script 4 

This script is designed to show the following:

Create a script that uses Bash and Python to interact with any API (Some API’s will require authentication):
1. Create a CSV file of the data you choose to store in the file.
2. Only 6 columns are required for this activity (e.g. of the MLB API: Player’s name, number, team, position, height and weight).
3. The script can be interactive or not interactive (You can allow a user to pick a or some parameter).
4. CSV file must be formatted properly.

Welcome to the Game of Thrones

Welcome Game of Thrones fans and newcomers!  You a fan of Game of Thrones?  This interactive script will provide you to know some cool information on some of the most popular characters from the show!

How to Begin

The script starts by asking the user to select which Game of Thrones character you would like to know more about.  The user then selects from a pre-determined list of characters by entering a number between 1-10.  If the user selects a number within 1-10, the corresponding character's information will be generated.  If a value outside of 1-10 is selected, this will generate a prompt to follow the directions and they will be defaulted to the 1.

After selecting a character, the API https://www.anapioficeandfire.com/api/characters will register a get request to pull the specific data related to the character.

