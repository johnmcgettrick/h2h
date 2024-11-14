from datetime import datetime

class Fixture:
    id = 0
    kickoff = datetime.now()
    venue = ""
    goals = {"home": 0, "away": 0}
    cards = {"home": 0, "away": 0}

    def __init__(self, id, timestamp, data):
        self.id = id
        self.kickoff = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S%z")
        self.venue = data["fixture"]["venue"]["name"]
        
        self.process_events(data)

    def process_events(self, data):
        self.goals = {
            "home": int(data["goals"]["home"]) if data["goals"]["home"] else 0, 
            "away": int(data["goals"]["away"]) if data["goals"]["away"] else 0
        }