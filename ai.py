import random

class AI:
    def __init__(self, options, rewards):
        self.options = options
        self.rewards = rewards
        self.chances = []
        
        for i in range(len(options)):
            self.chances.append(50)
    
    def pickOption(self):
        choice = random.randint(0, len(self.options)-1)
        
        picked = False
        
        chance = random.randint(0, 100)
        
        picked = chance <= 50
        
        if picked:
            self.chances[choice] += (self.rewards[choice] + random.randint(-2, 2))
        
        return self.options[choice]