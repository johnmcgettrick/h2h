class Event:

    def __init__(self,  data):
        self.time = data["time"]["elapsed"]
        self.team = data["team"]["id"]
        self.player = data["player"]["id"]

        self.set_event_type(data)

    def set_event_type(self, data):
        match data["type"]:
            case "Card":                
                # Detail will be "Yellow Card" or "Red Card"
                self.type = data["detail"]

            case "subst":
                self.type = "Sub"

            case _:
                self.type = data["type"]
                