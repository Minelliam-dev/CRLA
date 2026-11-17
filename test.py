from ai import *

options = ["-2", "-1", "0", "1", "2"]
rewards = [-2, -1, 0, 1, 2]

ai = AI(options, rewards)

for i in range(5):
    print(ai.chances[i])

for i in range(1000000):
    ai.pickOption()
    
print("after")    

for i in range(5):
    print(ai.chances[i])