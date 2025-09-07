# ------------------TASK 1  (Dictionary)-------------
# Create a dictionary named character_profile to store Alistair's basic information.
character_profile = {
    'name': 'Alistair the Brave',
    'level': 1,
    'health': 100,
    'mana': 50,
    'gold': 50.75,
    'is_alive': True
}

# Print the character's name and level in a formatted string.
print(f'Charcater "{character_profile['name']}" is on level {character_profile['level']}')

# Update the character's health to 85.
character_profile['health'] = 85

# Add a new key-value pair for 'experience' with a value of 0.
character_profile['experience'] = 0

# Print the final character_profile dictionary to the console.
print(character_profile)

# ------------------TASK 2  (Lists)-------------
#Initialize the list with a few items, for example: ['sword', 'shield', 'health potion'].
inventory = ['sword', 'shield', 'health potion']

# Add a new item to the inventory (e.g., 'mana potion').
inventory.append('mana potion')

# Remove an existing item from the inventory (e.g., 'shield').
inventory.remove('shield')

# Use a for loop to iterate through the inventory list and print each item.
for item in inventory:
    print(item)

# ------------------TASK 3 (Tuples)-------------
# Create a tuple named base_stats to store Alistair's base attributes.
strength = 9
dexterity = 6
intelligence = 8
base_stats = (strength, dexterity, intelligence)

# Print a statement explaining why a tuple is a good choice for base stats (because they are immutable and won't change).
print("Tuple is a good choice for base stats becuase the value won't change once the charracter is created.")

# Access and print the value of intelligence from the base_stats tuple.
print(base_stats[2])

# Try to change one of the values in the tuple. Observe and explain the error you receive.
# base_stats[1] = 20
print(base_stats)
#  We received TypeError: 'tuple' object does not support item assignment since tuple values cannot be changed once assigned or created.

# ------------------TASK 4 (Sets)-------------
# Initialize the set with a few quests
quest_log = {'Defeat the Goblin King', 'Find the Lost Amulet', 'Get Rich'}

# Add a new quest to the log
quest_log.add('Deliver the Old Scroll and sell it')

# Add a quest that is already in the set.
quest_log.add('Defeat the Goblin King')
print(quest_log)
# {'Get Rich', 'Find the Lost Amulet', 'Deliver the Old Scroll and sell it', 'Defeat the Goblin King'}

# Remove a completed quest from the log
quest_log.remove('Get Rich')

print(quest_log)
# {'Defeat the Goblin King', 'Find the Lost Amulet', 'Deliver the Old Scroll and sell it'}

# ------------------TASK 5 (Putting it all together)-------------
# Create a dictionary named character_sheet.
character_sheet = {
    'profile': character_profile,
    'inventory': inventory,
    'stats': base_stats,
    'quests': quest_log
}

# Print the entire character_sheet to demonstrate how different data structures can be nested within each other.
print(character_sheet)