from datetime import datetime

from team import Team
from event import Event

class Fixture:

    def __init__(self, id, data):
        self.id = id
        self.kickoff = datetime.strptime(data["fixture"]["date"], "%Y-%m-%dT%H:%M:%S+00:00")
        self.venue = data["fixture"]["venue"]["name"] if data["fixture"]["venue"] else ""
        
        self.teams = {
            "home": Team(data["teams"]["home"]["id"], data["teams"]["home"]["name"]),
            "away": Team(data["teams"]["away"]["id"], data["teams"]["away"]["name"])
        }

        self.events = []
        if "events" in data:
            self.process_events(data)

    def process_events(self, data):
        self.goals = {
            "home": int(data["goals"]["home"]) if data["goals"]["home"] else 0, 
            "away": int(data["goals"]["away"]) if data["goals"]["away"] else 0
        }
        
        for ev in data["events"]:
            self.events.append(Event(ev))

    def retrieve_event_counts(self, type):
        data = {"home": 0, "away": 0}
        for ev in self.events:
            team = "home" if ev.team == self.teams["home"].id else "away"
            data[team] += 1 if ev.type == type else 0
        
        return data