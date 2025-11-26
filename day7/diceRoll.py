import random

dice_faces = {
    1: (
        "┌───────┐",
        "│       │",
        "│   ●   │",
        "│       │",
        "└───────┘"
    ),
    2: (
        "┌───────┐",
        "│ ●     │",
        "│       │",
        "│     ● │",
        "└───────┘"
    ),
    3: (
        "┌───────┐",
        "│ ●     │",
        "│   ●   │",
        "│     ● │",
        "└───────┘"
    ),
    4: (
        "┌───────┐",
        "│ ●   ● │",
        "│       │",
        "│ ●   ● │",
        "└───────┘"
    ),
    5: (
        "┌───────┐",
        "│ ●   ● │",
        "│   ●   │",
        "│ ●   ● │",
        "└───────┘"
    ),
    6: (
        "┌───────┐",
        "│ ●   ● │",
        "│ ●   ● │",
        "│ ●   ● │",
        "└───────┘"
    )
}

def roll_dice():
    return random.randint(1,6)

print("Welcome to the Digital Dice Roller!")
# print("Press Enter to roll the dice or type 'q' nto quit.\n")

while True:
    user_input = input("Press Enter to roll the dice (or type 'q' to quit):").lower()
    if user_input == 'q':
        print("Goodbye!")
        break
    else:
        result = roll_dice()

        print("You rolled",roll_dice())
        for line in dice_faces[result]:
            print(line)
        print()