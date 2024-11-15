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

    def test_process_events_score(self):
        self.assertEqual(self.fixture1.goals["home"], 3, "Home team goals for fixture 1 are set correctly")
        self.assertEqual(self.fixture1.goals["away"], 1, "Away team goals for fixture 1 are set correctly")
        self.assertEqual(self.fixture2.goals["home"], 2, "Home team goals for fixture 2 are set correctly")
        self.assertEqual(self.fixture2.goals["away"], 0, "Away team goals for fixture 2 are set correctly")

    def test_process_events_cards(self):
        self.assertEqual(self.fixture1.cards["home"], 1, "Home team cards for fixture 1 are set correctly")
        self.assertEqual(self.fixture1.cards["away"], 2, "Away team cards for fixture 1 are set correctly")
        self.assertEqual(self.fixture2.cards["home"], 0, "Home team cards for fixture 2 are set correctly")
        self.assertEqual(self.fixture2.cards["away"], 0, "Away team cards for fixture 2 are set correctly")


if __name__ == '__main__':
    unittest.main()