# CS1030 - Adventure Game
# Byers, Chance - WSU 2025
# Version 1.0
# Description: This program starts the adventure game

# Index / Introduction
print("\nWelcome to the Adventure Game!")
print("Your journey begins here...")

# Player Name / String Concat
playerName = input("\nAdventurer, what is your name? ")
print(f"Your journey begins now, {playerName}!")


# Starting Area
startingArea = """
You find yourself in a dark forest.
The sound of rustling leaves fills the air.
A faint path lies ahead, leading deeper into the unknown...
"""
print(startingArea)

# Players Decision #1
dOne = input("Do you wish to take the path? [y/n | yes/no]: ").lower()

# Decision #1 Response
if dOne == "y" or dOne == "yes":
    print(f"Honor awaits you {playerName}, feeling brave you venture forward onto the path that lies ahead.") #f String
elif dOne == "n" or dOne == "no":
    print("It appears you've yet to find the courage, may it come to you soon, " + playerName) # Concat
else:
    print("Frozen in fear, gut wrenching, unsure of what steps to take.") # Response was not y/n  or yes/no