from datetime import datetime

class Fixture:
    id = 0
    kickoff = datetime.now()
    venue = ""

    def __init__(self, id, timestamp, venue):
        self.id = id
        self.kickoff = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S%z")
        self.venue = venue