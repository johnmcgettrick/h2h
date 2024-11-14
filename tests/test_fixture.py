import unittest
from datetime import datetime

from fixture import Fixture

class TestFixture(unittest.TestCase):

    def setUp(self):
        self.fixture1 = Fixture(1, datetime.now().strftime("%Y-%m-%dT%H:%M:%S%z"), {"fixture": { "venue": { "name": "The Park" } }, "goals":{"home": 3, "away": 1}})
        self.fixture2 = Fixture(1, datetime.now().strftime("%Y-%m-%dT%H:%M:%S%z"), {"fixture": { "venue": { "name": "El Stadio" } }, "goals":{"home": 2, "away": 0}})

    def test_process_events(self):
        self.assertEqual(self.fixture1.goals["home"], 3, "Home team goals for fixture 1 are set correctly")
        self.assertEqual(self.fixture1.goals["away"], 1, "Away team goals for fixture 1 are set correctly")
        self.assertEqual(self.fixture2.goals["home"], 2, "Home team goals for fixture 2 are set correctly")
        self.assertEqual(self.fixture2.goals["away"], 0, "Away team goals for fixture 2 are set correctly")


if __name__ == '__main__':
    unittest.main()