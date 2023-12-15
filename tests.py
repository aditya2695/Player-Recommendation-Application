## Importing unittest

import unittest
from app_home import PlayerRecommendationSystem as PRS 

## TestSuite is going to be a subclass of unittest.TestCase!

class app_test_suite(unittest.TestCase):
    """Our different test cases"""
    
    

    def test_male_player_details(self):

        app = PRS()

        # Robert Lewandoski player_id=188545
        ans = {'face': 'https://cdn.sofifa.net/players/188/545/22_120.png', 'positions': 'ST', 'traits': 'Solid Player, Finesse Shot, Outside Foot Shot, Chip Shot (AI)', 'club': 'https://cdn.sofifa.net/teams/21/60.png', 'value': 119500000.0, 'salary': 270000.0}
        self.assertEqual(app.get_player_details(player_id=188545), ans)

    def test_female_player_details(self):

        app = PRS(gender='Female')

        # Lieke Martens player_id=233748
        ans = {'face': 'https://cdn.sofifa.com/players/233/748/22_120.png', 'positions': 'LW, CAM', 'traits': 'Flair, Playmaker (AI), Outside Foot Shot, Technical Dribbler (AI)'}
        self.assertEqual(app.get_player_details(player_id=233748), ans)


        

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)