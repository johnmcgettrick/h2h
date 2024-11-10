import configparser
import requests
import json

import fixture
 
config = configparser.ConfigParser()
config.read("config.ini")

team1 = input("Please enter one of the teams: ")
team2 = input("Please enter the other team: ")

endpoint = "fixtures/headtohead?h2h=" + format(team1) + "-" + format(team2)
url = config["api"]["url"] + endpoint

headers = {
    'x-apisports-key': config["api"]["key"]
    }

response = requests.request("GET", url, headers=headers)

data = json.loads(response.text) 

print("There have been " + str(len(data["response"])) + " matches between these two teams since 2010")

for item in data["response"]: 
    fixture.print_fixture(item["fixture"])

# Prompt for fixture id
fixture_id = input("Which match would you like further details about: ")

endpoint = "fixtures?id=" + format(fixture_id)
url = config["api"]["url"] + endpoint
response = requests.request("GET", url, headers=headers)

data = json.loads(response.text)
match = data["response"][0]

print("The score that day was: " + 
        str(match["goals"]["home"]) + "-" +
        str(match["goals"]["away"]))