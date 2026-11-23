from random import*
from numpy import random 

t = 1

for i in range(100):
    liste = random.choice([1, 2, 3, 4, 5, 6], p=[0.1, 0.15, 0.15, 0.15, 0.15, 0.3])
    print("Le lancer n°",t, "est : ",liste)
    t = t+1