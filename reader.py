"""Parses the JSON-database."""
# **********************
# * JSON-reader v. 0.2 *
# **********************
import json
from pprint import pprint

with open('database.json') as data_file:
    data = json.load(data_file)

"""pprint(data)
pprint(data["acts"][0]["materials"][0]["title"])"""

print (30 * '-')
print ("   M A I N - M E N U")
print (30 * '-')
print ("1. Print all acts")
print ("2. Print specific act*")
print ("3. List all occurences of actor*")
print ("4. Delete act*")
print ("5. Quit")
print (30 * '-')
number_of_acts = len(data["acts"][0]["materials"])
while True:
    selection = input("Please Select:")
    if selection == '1':
        for x in range(0, number_of_acts):
            pprint(data["acts"][0]["materials"][x-1])
    elif selection == '2':
        print("Not yet implemented")
    elif selection == '3':
        print("Please enter the name of the actor:")
        name = input()
        count = 0
        for x in range(0, number_of_acts):
            number_of_roles = len(data["acts"][0]["materials"][x-1]["roles"])
            for y in range(0, number_of_roles):
                result = (data["acts"][0]["materials"][x-1]
                         ["roles"][y-1]["actor"])
                if result.lower() == name.lower():
                    print("\n", name, " appears in act ", x-1, ", \"",
                    (data["acts"][0]["materials"][x-1]["title"]), "\"", sep='')
                    count = count + 1
        if count == 0:
            print("\n", name, " does not appear in any acts.\n", sep='')
    elif selection == '4':
                print("Not yet implemented")
    elif selection == '5':
        break
    else:
        print("Unknown Option Selected!")
