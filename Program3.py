'''
*********
PROGRAM 3
*********
The addtobag(bag, itemstoadd) function below is part of a RPG game where loot is added to a player's bag after they have defeated an opponent. 
The bag parameter is an already existing dictionary with the user's already existing items, and itemstoadd is a list of new items that the player received. 
The function should return an updated dictionary where the keys are the unique items in the bag, and the values are how many of each item are in the bag.

EXAMPLE OF HOW PROGRAM MIGHT WORK:
mybag = {"Potion": 3, "Water Stone": 2, "Nugget": 5} #what the user already had
newloot = ["Potion", "Potion", "Hyper Potion", "Bicycle", "Hyper Potion"] #what the user received from defeating an opponent

addtobag(mybag, newloot)
--> returns {'Potion': 5, 'Water Stone': 2, 'Nugget': 5, 'Hyper Potion': 2, 'Bicycle': 1}

'''
def addtobag(bag, itemstoadd):
  d = {}
  types_of_objects = []
  for i in bag:
    if i in types_of_objects:
      d[1] = d[1] + 1
    else:
      d[1] = 1
  for i in itemstoadd:
    if i in types_of_objects:
      d[1] = d[1] + 1
    else: d[1] = 1
