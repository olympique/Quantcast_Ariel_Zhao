import unittest
from most_active_cookie import parse_file, most_active_cookie

class Tests(unittest.TestCase):

    def test_most_active_cookie(self):
        cookieCountsByDate = {'2018-12-07': {'4sMM2LxV07bPJzwf': 1}, '2018-12-08': {'4sMM2LxV07bPJzwf': 1, 'fbcn5UAVanZf6UtG': 1, 'SAZuXPGUrfbcn5UA': 1}, 
        '2018-12-09': {'5UAVanZf6UtGyKVS': 1, 'SAZuXPGUrfbcn5UA': 1, 'AtY0laUfhglK3lC7': 2}}

        self.assertEqual(most_active_cookie(cookieCountsByDate, '2018-12-09'), ['AtY0laUfhglK3lC7'])
        self.assertEqual(most_active_cookie(cookieCountsByDate, '2018-12-08'), ['4sMM2LxV07bPJzwf', 'fbcn5UAVanZf6UtG', 'SAZuXPGUrfbcn5UA'])
        self.assertEqual(most_active_cookie(cookieCountsByDate, '2018-12-07'), ['4sMM2LxV07bPJzwf'])
        self.assertEqual(most_active_cookie(cookieCountsByDate, '2018-12-06'), [])

    def test_parse_file(self):
        cookieCountsByDate = {'2018-12-07': {'4sMM2LxV07bPJzwf': 1}, '2018-12-08': {'4sMM2LxV07bPJzwf': 1, 'fbcn5UAVanZf6UtG': 1, 'SAZuXPGUrfbcn5UA': 1}, 
        '2018-12-09': {'5UAVanZf6UtGyKVS': 1, 'SAZuXPGUrfbcn5UA': 1, 'AtY0laUfhglK3lC7': 2}}
        
        self.assertEqual(parse_file('cookie_log.csv'), cookieCountsByDate)


if __name__=="__main__":
    unittest.main()
