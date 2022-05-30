from random import Random

class Action:
    def __init__(self, points, player):
        self.action_points = points
        self.player = player

    def skill_check(self):
        """Allows player to perform a skill check,
            Returns True if the player succeeds"""
        result = Random.randint(1,6)
        if result < 4: 
            return False
        return True

    def reveal(self):
        if self.action_points < 1: return

    def move(self):
        if self.action_points < 1: return

    def explore(self):
        if self.action_points < 1: return
            
        self.reveal
        self.move

        self.action_points = self.action_points - 1
    
    def run(self):
        if self.action_points < 2: return

    def heal(self):
        if self.action_points < 2: return

    def swim(self):
        if self.action_points < 2: return
    
    def squeeze(self):
        if self.action_points < 2: return

    def dig(self):
        if self.action_points < 2: return
    
    def place_rope(self, player):
        self.player = player
        if self.action_points < 2: return
        if self.skill_check == False: return

    def hide(self):
        if self.action_points < 2: return
        if self.skill_check == False: return
