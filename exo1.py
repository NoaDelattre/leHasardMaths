from random import* # from random import randint ou from random import choice 

# Exemples de random(), de randint, et de choice
print(random())
print(randint(1,6))
liste=['a','b','c','d']
print(choice(liste))

# Exercice 1 : 100 lancers de dés
t = 0

for i in range(100):
    t = t + 1
    print("Le lancer n°",t," est : ",randint(1,6))