# Tarot Reader!

# Baka has helped me scrape some tables for the cards, I will clean up the tables, export the csv from the google doc, and then add in as a dictionary here.
# turn the csv into an appropriate dictionary
# create a class that is "Tarot Deck" which includes keys from tarot dictionary - nevermind, simpler solution implemented
# create object/iteration method - nevermind, simpler to create dictionary on each program run and modify the dictionary when drawing cards
# create method for 3 card draw: past, present, future - pull keys, list key names and return values from above dictionary
# optional - potential room for improvement here - ask user what type of spread they would like (provide multiple choices, ensure any input that isnt one of the choices returns "that wasn't a valid choice, please input valid choice")
# random module needs to be imported in order to randomize cards that are drawn from deck. randomization should be included in deck object instatiation in order to ensure each reading iteration is entirely unique.
# in the future will add initial option of choosing whether or not to use cp77 deck, will have to have full separate branch of code for that since no up/down values for that.

import random
import csv
tarot_deck = {}
nr_tarot_deck = {}
tarot_orientation = {0: "Right-Side-Up", 1: "Up-Side-Down"}
filename = 'simpletarot.csv'
nrfilename = 'cyberpunktarot.csv'

with open(filename, 'r') as data:
    templist = csv.reader(data)
    for line in templist:
        tarot_deck[line[0]] = line[-2:]

with open(nrfilename, 'r') as data:
    templist = csv.reader(data)
    for line in templist:
        nr_tarot_deck[line[0]] = line[1]

# print(tarot_deck)
# print(nr_tarot_deck)

print("Welcome to Oku-Jo's very simple tarot reader!")
print("Would you like to have a reading without reversals?")
imp1 = input("If yes, please type 'y', if no, please type 'n': ")
if imp1 == "y":
    print("Currently this program is capable of providing either a single card read for simpler questions (think magic 8-ball), or a three card spread which represents the past, present and future. Before making your choice please hold the question you are seeking advice on in the forefront of your mind, and then indicate which spread you would like generated for you.")
    imp2 = input("Please input your spread choice (either '1' or '3'): ")
    if imp2 == "1":
        tarot = random.choice(list(nr_tarot_deck))

        print("You have drawn: '" + tarot + "' which should be read thusly: " + nr_tarot_deck[tarot])
    elif imp2 == "3":
        tarotpast = random.choice(list(nr_tarot_deck))
        print("'" + tarotpast + "'" + " represents your past. It should be read thusly: " + nr_tarot_deck[tarotpast])
        nr_tarot_deck.pop(tarotpast)

        tarotpresent = random.choice(list(nr_tarot_deck))
        print("'" + tarotpresent + "'" + " represents your present. It should be read thusly: " + nr_tarot_deck[tarotpresent])
        nr_tarot_deck.pop(tarotpresent)

        tarotfuture = random.choice(list(nr_tarot_deck))
        print("'" + tarotfuture + "'" + " represents your future. It should be read thusly: " + nr_tarot_deck[tarotfuture])
        nr_tarot_deck.pop(tarotfuture)
    else:
        print("I do not have the functionality right now to provide readings for other spreads, please input either '1' or '3'.")
 
elif imp1 == "n":
    print("Currently this program is capable of providing either a single card read for simpler questions (think magic 8-ball), or a three card spread which represents the past, present and future. Before making your choice please hold the question you are seeking advice on in the forefront of your mind, and then indicate which spread you would like generated for you.")
    imp2 = input("Please input your spread choice (either '1' or '3'): ")
    if imp2 == "1":
        tarot = random.choice(list(tarot_deck))
        orientation = random.choice(list(tarot_orientation))

        print("You have drawn: " + tarot + " and it is " + tarot_orientation[orientation] + "." + "\nIn this orientation it should be read: " + tarot_deck[tarot][orientation])
    elif imp2 == "3":
        tarotpast = random.choice(list(tarot_deck))
        orientationpast = random.choice(list(tarot_orientation))
        print(tarotpast + " represents your past. It is " + tarot_orientation[orientationpast] + " so it should be read thusly: " + tarot_deck[tarotpast][orientationpast])
        tarot_deck.pop(tarotpast)

        tarotpresent = random.choice(list(tarot_deck))
        orientationpresent = random.choice(list(tarot_orientation))
        print(tarotpresent + " represents your present. It is " + tarot_orientation[orientationpresent] + " so it should be read thusly: " + tarot_deck[tarotpresent][orientationpresent])
        tarot_deck.pop(tarotpresent)

        tarotfuture = random.choice(list(tarot_deck))
        orientationfuture = random.choice(list(tarot_orientation))
        print(tarotfuture + " represents your future. It is " + tarot_orientation[orientationfuture] + " so it should be read thusly: " + tarot_deck[tarotfuture][orientationfuture])
        tarot_deck.pop(tarotfuture)
    else:
        print("I do not have the functionality right now to provide readings for other spreads, please input either '1' or '3'.")
else:
    print("I can only accept a 'y' or 'n' input. Maybe in the future I will be able to take other inputs for a yes/no question.")
        
        
        
        
        
        
        # print(tarot)
        # # print(orientation)
        # print(tarot_deck[tarot][orientation])
        # print(tarot)
        # # print(orientation)
        # print(tarot_deck[tarot][orientation])