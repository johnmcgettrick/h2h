from datetime import datetime

def print_fixture(fixture):
    fixture_date = datetime.strptime(fixture["date"], "%Y-%m-%dT%H:%M:%S%z")
    ko_time = fixture_date.strftime("%a %d/%m/%Y - Kick Off: %H%M")
    print(ko_time + " - Venue: " + fixture["venue"]["name"])