# Tarot Reader!

# Baka has helped me scrape some tables for the cards, I will clean up the tables, export the csv from the google doc, and then add in as a dictionary here.
# turn the csv into an appropriate dictionary
# create a class that is "Tarot Deck" which includes keys from tarot dictionary
# create object/iteration method
# create method for 3 card draw: past, present, future - pull keys, list key names and return values from above dictionary
# create a deck object upon user interaction, this has mutable list of dictionary keys, when 'keys' (actually items) from list are pulled they are removed from list, and values from tarot dictionary are called
# optional - potential room for improvement here - ask user what type of spread they would like (provide multiple choices, ensure any input that isnt one of the choices returns "that wasn't a valid choice, please input valid choice")
# random module needs to be imported in order to randomize cards that are drawn from deck. randomization should be included in deck object instatiation in order to ensure each reading iteration is entirely unique.
# if skipping class/object - define function, in function have tarot keys as list, modify list as keys pulled, return keys and corresponding dictionary values with context based on (past/present/future)

import random
import csv
tarot_deck = {}
tarot_orientation = {0: "Right-Side-Up", 1: "Up-Side-Down"}
filename = 'simpletarot.csv'

with open(filename, 'r') as data:
    templist = csv.reader(data)
    for line in templist:
        tarot_deck[line[0]] = line[-2:]

# print(tarot_deck)


print("Welcome to Tarot Reader! Currently this program is capable of providing either a single card read for simpler questions (think magic 8-ball), or a three card spread which represents the past, present and future. Before making your choice please hold the question you are seeking advice on in the forefront of your mind, and then indicate which spread you would like generated for you.")
imp = input("Please input your choice (either '1' or '3'): ")
if imp == "1":
    tarot = random.choice(list(tarot_deck))
    orientation = random.choice(list(tarot_orientation))
    # print(tarot)
    # # print(orientation)
    # print(tarot_deck[tarot][orientation])
    print("You have drawn: " + tarot + " and it is " + tarot_orientation[orientation] + "." + "\nIn this orientation it should be read: " + tarot_deck[tarot][orientation])
elif imp == "3":
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


# at this point i am trying to have the orientation generate an up or down value, which will influence the values returned from the tarot_deck key selection. this may require automated dictionary modification, or duplication of the keys,
# but that is undesireable as it would allow for an individual card to be drawn twice, once in each orientation. ideally each card would be under one key with 2 values assigned, one of which would be shown based on orientation, and then .popped from the dictionary.
# the .pop might have to happen after the information is displayed but before the next card is drawn, fortunately ive got the tarot temp variable as they key that needs to be popped. see you tomorrow. also also also need to finish output text with placeholders for
# correct tarot info based on orientation.