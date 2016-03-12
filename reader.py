"""This parses the RAD.js file."""
import json

"""Bind the RAD.py file to the variable data"""
with open('database.js') as data_file:
    data = json.load(data_file)


def reader(index, item):
    """Take two inputs and return a list of strings from the RAD.js file."""
    if item in ["title", "author", "length", "status", "version",
                "revuename", "revueyear", "loaction", "type", "order"]:
        return [str(data["acts"][0]["materials"][index][item])]

    elif item in ["roles"]:
        return [x['title'] for x in (data["acts"][0]["materials"][index]
                ["roles"]) if 'title' in x]

    elif item in ["actor"]:
        return [x['actor'] for x in (data["acts"][0]["materials"][index]
                ["roles"])]

    elif item in ["abbr"]:
        return [x['abbr'] for x in (data["acts"][0]["materials"][index]
                ["roles"])]

    elif item in ["propname"]:
        return [x['name'] for x in (data["acts"][0]["materials"][index]
                ["props"])]

    elif item in ["propresponsible"]:
        return [x['responsible'] for x in (data["acts"][0]["materials"][index]
                ["props"])]

    elif item in ["propdescription"]:
        return [x['description'] for x in (data["acts"][0]["materials"][index]
                ["props"])]

    else:
        return ["Invalid input"]


'''forfattere, rollefordeling,  rekvisitter.
["title", "author", "length", "status", "version",
"revuename", "revueyear", "loaction", "type", "order"]'''
