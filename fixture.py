from datetime import datetime

class Fixture:
    id = 0
    kickoff = datetime.now()
    venue = ""
    goals_home = 0
    goals_away = 0

    def __init__(self, id, timestamp, venue, goals = {}):
        self.id = id
        self.kickoff = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S%z")
        self.venue = venue
        self.goals_home = int(goals["home"]) if goals else 0
        self.goals_away = int(goals["away"]) if goals else 0