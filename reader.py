"""Parses the JSON-database."""
# **********************
# * JSON-reader v. 0.21 *
# **********************
import json
from pprint import pprint

with open('database.json') as data_file:
    data = json.load(data_file)

"""The menu. It let's you do stuff. Mostly justhere to play around with, and
   is unlikely to actually be used for anything. The logic it uses should be
   reimplemented in the final version though."""
while True:
    print (30 * '-')
    print ("   M A I N - M E N U")
    print (30 * '-')
    print ("1. Print all acts")
    print ("2. Print specific act")
    print ("3. List all occurences of actor")
    print ("4. Delete act*")
    print ("5. Quit")
    print (30 * '-')
    number_of_acts = len(data["acts"][0]["materials"])
    selection = input("Please Select:")
    if selection == '1':
        for x in range(0, number_of_acts):
            pprint(data["acts"][0]["materials"][x-1])
    elif selection == '2':
        while True:
            print("Do you wish to seach by ID or title?")
            print("1. ID\n2. Title:\n")
            subselection = input()
            if subselection == "1":
                id = int(input("Please enter the ID of the act: "))
                # Makes sure the ID entered actually exists, then info about
                # the act.
                if id <= (number_of_acts - 1) & id > 0:
                    print("\n")
                    pprint(data["acts"][0]["materials"][id])
                    print("\n")
                    break
                else:
                    print("Unknown ID. Returning to main menu.")
                    break
            if subselection == "2":
                name = input("\nPlease enter the title: ")
                count = 0
                # Converts the title entered by the user to lowercase,
                # then checks it against every title of every act in the
                # database.
                for x in range(0, number_of_acts):
                    title = (data["acts"][0]["materials"][x-1]["title"])
                    if title.lower() == name.lower():
                        pprint(data["acts"][0]["materials"][x-1])
                        count = count + 1
            else:
                print("\nUnknown option selected. Returning to main menu.")
                break
            if count == 0:
                print("\nUnknown title. Returning to main menu.")
                break
            elif count > 1:
                print("\nMore than one act has the title", title,
                      ". All of them have been printed above, ordered by ID.")
            else:
                print("\n")
                break
    elif selection == '3':
        # Searches through the database, and finds all acts where a particular
        # actor is involved. They are then presented to the user.
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
                          (data["acts"][0]["materials"][x-1]["title"]),
                          "\"", sep='')
                    count = count + 1
        if count == 0:
            print("\n", name, " does not appear in any acts.\n", sep='')
    elif selection == '4':
                print("Not yet implemented")
    elif selection == '5':
        break
    else:
        print("Unknown Option Selected!")
