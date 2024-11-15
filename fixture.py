from datetime import datetime

from team import Team

class Fixture:
    id = 0
    teams = {}
    kickoff = datetime.now()
    venue = ""
    goals = {}
    cards = {}

    def __init__(self, id, data):
        self.id = id
        self.kickoff = datetime.strptime(data["fixture"]["date"], "%Y-%m-%dT%H:%M:%S+00:00")
        self.venue = data["fixture"]["venue"]["name"] if data["fixture"]["venue"] else ""
        
        self.teams["home"] = Team(data["teams"]["home"]["id"], data["teams"]["home"]["name"])
        self.teams["away"] = Team(data["teams"]["away"]["id"], data["teams"]["away"]["name"])

        self.cards = {"home": 0, "away": 0}

        self.process_events(data)

    def process_events(self, data):
        self.goals = {
            "home": int(data["goals"]["home"]) if data["goals"]["home"] else 0, 
            "away": int(data["goals"]["away"]) if data["goals"]["away"] else 0
        }
        for ev in data["events"]:
            if ev["type"] == "card":
                team = "home" if ev["team"]["id"] == self.teams["home"].id else "away"
                self.cards[team] += 1

    def retrieve_score(self):
        # TODO: Add status and break goals down into stages/halves
        return self.goals