import configparser
import requests
import json
 
config = configparser.ConfigParser()
config.read("config.ini")

def print_fixture(fixture):
    print(fixture["date"] + " " + item["fixture"]["venue"]["name"])

team1 = input("Please enter one of the teams: ")
team2 = input("Please enter the other team: ")

endpoint = "fixtures/headtohead?h2h=" + format(team1) + "-" + format(team2)
url = config["api"]["url"] + endpoint

headers = {
    'x-apisports-key': config["api"]["key"]
    }

response = requests.request("GET", url, headers=headers)

data = json.loads(response.text) 

for item in data["response"]: 
    print_fixture(item["fixture"])
