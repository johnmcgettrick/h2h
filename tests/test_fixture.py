import unittest
import json
import pathlib

from datetime import datetime

from fixture import Fixture

class TestFixture(unittest.TestCase):

    def setUp(self):
        file = pathlib.Path("tests/data/fixture1.json")  
        with open(file) as f:  
            data_fixture1 = json.load(f)

        self.fixture1 = Fixture(1, data_fixture1)

        file = pathlib.Path("tests/data/fixture2.json")  
        with open(file) as f:  
            data_fixture2 = json.load(f)
        
        self.fixture2 = Fixture(2, data_fixture2)

    def test_process_events(self):
        self.assertEqual(len(self.fixture1.events), 3, "Fixture 1 event count is correct")
        self.assertEqual(len(self.fixture2.events), 0, "Fixture 2 event count is correct")

        self.assertEqual(self.fixture1.events[0].type, "Yellow Card", "Fixture 1 first event is correct")

    def test_retrieve_event_counts(self):
        yellow_cards = self.fixture1.retrieve_event_counts("Yellow Card")
        self.assertEqual(yellow_cards["home"], 1, "Home team cards for fixture 1 are set correctly")
        self.assertEqual(yellow_cards["away"], 2, "Away team cards for fixture 1 are set correctly")

        yellow_cards = self.fixture2.retrieve_event_counts("Yellow Card")
        self.assertEqual(yellow_cards["home"], 0, "Home team cards for fixture 2 are set correctly")
        self.assertEqual(yellow_cards["away"], 0, "Away team cards for fixture 2 are set correctly")

if __name__ == '__main__':
    unittest.main()