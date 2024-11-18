import configparser
import requests
import json

from fixture import Fixture
 
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
    fixture = Fixture(item["fixture"]["id"], item)

    ko_time = fixture.kickoff.strftime("%a %d/%m/%Y - Kick Off: %H%M")
    print("[" + str(fixture.id) + "] - " + ko_time + " - Venue: " + fixture.venue)

# Prompt for fixture id
fixture_id = input("Which match would you like further details about: ")

endpoint = "fixtures?id=" + format(fixture_id)
url = config["api"]["url"] + endpoint
response = requests.request("GET", url, headers=headers)

data = json.loads(response.text)
match = data["response"][0]

fixture = Fixture(match["fixture"]["id"], match)

score = fixture.retrieve_event_counts("Goal")
print("The score in this game: " + str(score["home"]) + "-" + str(score["away"]))

ycards = fixture.retrieve_event_counts("Yellow Card")
rcards = fixture.retrieve_event_counts("Red Card")
totalcards = ycards["home"] + ycards["away"] + rcards["home"] + rcards["away"]
print("The total number of cards in this game: " + str(totalcards))
