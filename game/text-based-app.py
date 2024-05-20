import time

# Define rooms and their connections
rooms = {
    'Hall': {'north': 'Kitchen', 'east': 'Living Room'},
    'Kitchen': {'south': 'Hall'},
    'Living Room': {'west': 'Hall'}
}

# Define items in rooms
items = {
    'Hall': ['key'],
    'Kitchen': ['knife'],
    'Living Room': ['potion']
}

# Define actions
actions = {
    'Hall': 'You are in the hall. There is a key here.',
    'Kitchen': 'You are in the kitchen. There is a knife here.',
    'Living Room': 'You are in the living room. There is a potion here.'
}

def main():
    current_room = 'Hall'
    inventory = []

    print("Welcome to the Text Adventure Game!\n")
    print("You find yourself in a mysterious house. Your goal is to find the treasure.\n")
    print("Commands: 'go [direction]', 'take [item]', 'inventory', 'quit'\n")

    while True:
        print(actions[current_room])
        command = input("> ").lower().split()

        if len(command) == 2:
            verb, obj = command
        elif len(command) == 1:
            verb = command[0]
        else:
            print("Invalid command!")
            continue

        if verb == 'quit':
            print("Thanks for playing!")
            break
        elif verb == 'go':
            direction = obj
            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
                print(f"You go {direction}.")
            else:
                print("You can't go that way!")
        elif verb == 'take':
            item = obj
            if item in items[current_room]:
                items[current_room].remove(item)
                inventory.append(item)
                print(f"You take the {item}.")
            else:
                print("There is no such item here!")
        elif verb == 'inventory':
            print("Inventory:", inventory)
        else:
            print("Invalid command!")

if __name__ == "__main__":
    main()
