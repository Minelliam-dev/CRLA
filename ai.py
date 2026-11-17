import random

class AI:
    def __init__(self, options, rewards):
        self.options = options
        self.rewards = rewards
        self.chances = [50 for _ in options]
        
        self.drift = 2
    
    def pickOption(self):
        choice = random.randint(0, len(self.options)-1)

        chance = random.randint(0, 100)
        
        if chance <= 50:
            self.chances[choice] += (self.rewards[choice] + random.randint(-self.drift, self.drift))
        
        return self.options[choice]
    
    def pickOptionFromChances(self, chances):
            choice = random.randint(0, len(self.options)-1)
    
            chance = random.randint(0, 100)
            
            if chance <= 50:
                self.chances[choice] += (self.rewards[choice] + random.randint(-self.drift, self.drift))
            
            return self.options[choice]