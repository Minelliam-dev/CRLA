import random

class AI:
    def __init__(self, options, rewards):
        self.options = options
        self.rewards = rewards
        self.chances = [50 for _ in options]
    
    def pickOption(self):
        choice = random.randint(0, len(self.options)-1)

        chance = random.randint(0, 100)
        
        if chance <= 50:
            self.chances[choice] += (self.rewards[choice] + random.randint(-2, 2))
        
        return self.options[choice]