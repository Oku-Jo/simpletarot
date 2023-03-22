#Goblin Slayer!
import random

class Goblin_Slayer:
    def __init__(self, name, strength = 3, level = 2):
      self.name = name
      self.level = level
      self.health = level * 5
      self.max_health = level * 5
      self.damage = strength * self.level

    def __repr__(self):
      return "{name} is a goblin slayer, they are able to dish out {strength} damage per attack, and they have made it to level {level}. They enjoy long walks on the beach and killing goblins.".format(name = self.name, strength = self.damage, level = self.level)

    def attack(self, goblin):
      if self.health == 0:
        print("You are dead. Your lifeless body cannot attack.")
      else:
        print("{name} attacked {goblin} for {damage} points of damage!".format(name = self.name, goblin = goblin.gobname, damage = self.damage))
        goblin.gob_lose_health(self.damage)
        if goblin.gobhealth <= 0:
          self.level += 1
          print("You've killed the goblin! You have gained a level!")
        else:
          print("It is now the goblin's turn!")
    
    def lose_health(self, amount):
      self.health -= amount
      if self.health <= 0:
        self.health = 0
        print("{name} has died, GAME OVER.".format(name = self.name))  
      else:
        print("{name} has {health} health remaining. It is now your turn!".format(name = self.name, health = self.health))
    
    def use_health_potion(self, amount = 10):
      if self.health == 0:
        print("You are dead. Your lifeless body cannot attack.")
      else:
        print("{name} consumes a health potion!".format(name = self.name))
        self.health += amount
        if self.health >= self.max_health:
          self.health = self.max_health
        print("{name} now has {health} health. It is now the goblin's turn!".format(name = self.name, health = self.health))




class Goblin:
    def __init__(self, name, strength = random.randint(1,5), health = random.randint(1, 10)):
      self.gobname = name
      self.gobstrength = strength
      self.gobhealth = health
      self.maxgobhealth = health

    def __repr__(self):
      return "{name} is a goblin, they enjoy eating sand and have a terrible sense of fashion. {name} has a measly {gobhealth} hitpoints, and it is no surprise they can only deal {gobstrength} damage per attack.".format(name = self.gobname, gobhealth = self.gobhealth, gobstrength = self.gobstrength)

    def gobattack(self, goblinslayer):
      if self.gobhealth == 0:
        print("Thanks to being dead, {name} cannot take any actions!".format(name = self.gobname))
      else:
        print("{name} attacks {goblinslayer} for {strength} points of damage!".format(name = self.gobname, goblinslayer = goblinslayer.name, strength = self.gobstrength))
        goblinslayer.lose_health(self.gobstrength)
  
    def gob_lose_health(self, amount):
      self.gobhealth -= amount
      if self.gobhealth <= 0:
        self.gobhealth = 0
      else:
        print("{name} has {health} health remaining.".format(name = self.gobname, health = self.gobhealth))
  
    def pocket_meat(self):
      if self.gobhealth == 0:
        print("Thanks to being dead, {name} cannot take any actions!".format(name = self.gobname))
      else:
        self.amount = random.randint(1, 5)
        self.gobhealth += self.amount
        if self.gobhealth >= self.maxgobhealth:
          self.gobhealth = self.maxgobhealth
        print("{name} has regained {healing}, and has {gobhealth} health remaining.".format(name = self.gobname, healing = self.amount, gobhealth = self.gobhealth))

    def cower_in_fear(self):
      if self.gobhealth == 0:
        print("Thanks to being dead, {name} cannot take any actions!".format(name = self.gobname))
      else:
        print("{name} cowers in fear, they are too terrified to do anything this turn!".format(name = self.gobname))

# slayer1name = input("Hello, please name your first Goblin Slayer! ")
# slayer2name = input("Hello, please name your second Goblin Slayer! ")

# goblin1name = input("Hello, please name your first goblin! ")
# goblin2name = input("Hello, please name your second goblin! ")

slayer1 = Goblin_Slayer("Robert")
slayer2 = Goblin_Slayer("Bob")
goblin1 = Goblin("Roblin")
goblin2 = Goblin("Boblin")

##########################################################
goblin1.gobattack(slayer2)
goblin2.gobattack(slayer1)


slayer1.attack(goblin1)
goblin1.gobattack(slayer1)
slayer1.attack(goblin2)
goblin2.gobattack(slayer1)