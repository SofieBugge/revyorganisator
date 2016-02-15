"""This is responsible for parsing the JSON-database."""
import json
from pprint import pprint

with open('database.json') as data_file:
    data = json.load(data_file)

"""pprint(data)"""
pprint(data["acts"])
