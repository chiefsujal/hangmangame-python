import random

word_list = [
    "Lion", "Elephant", "Tiger", "Giraffe", "Monkey", "Penguin", "Dolphin", "Koala", "Kangaroo", "Cheetah",
    "Panda", "Zebra", "Bear", "Fox", "Rabbit", "Owl", "Gorilla", "Rhinoceros", "Camel", "Wolf",
    "Horse", "Alligator", "Peacock", "Chimpanzee", "Hippopotamus", "Ostrich", "Sloth",

    "Apple", "Banana", "Orange", "Mango", "Strawberry", "Pineapple", "Watermelon", "Grapes", "Kiwi", "Blueberry",
    "Raspberry", "Peach", "Plum", "Cherry", "Lemon", "Lime", "Grapefruit", "Papaya", "Pear", "Avocado",
    "Apricot", "Pomegranate", "Fig", "Cranberry", "Blackberry", "Coconut", "Guava", "Passionfruit", "Melon",
    "Nectarine",

    "United States", "Canada", "Brazil", "Australia", "Japan", "India", "Germany", "France", "Italy", "South Africa",
    "Egypt", "Mexico", "Argentina", "China", "Russia", "Spain", "Turkey", "Thailand", "Kenya", "United Kingdom",
    "Peru", "Greece", "Saudi Arabia", "South Korea", "Sweden", "Nigeria", "Malaysia", "New Zealand", "Switzerland",

    "Car", "Bus", "Motorcycle", "Bicycle", "Truck", "Boat", "Plane", "Train", "Scooter", "Helicopter",
    "Submarine", "Jet", "Tram", "Bulldozer", "Ambulance", "Taxi", "Hovercraft", "Segway", "Yacht", "Canoe",
    "Skateboard", "Hot Air Balloon", "Segway", "Golf Cart", "Snowmobile", "Rickshaw", "Fire Truck", "RV", "Cruise Ship",
    "Ambulance",

    "Run", "Jump", "Swim", "Sing", "Dance", "Write", "Read", "Cook", "Eat", "Sleep",
    "Speak", "Listen", "Play", "Study", "Work", "Travel", "Explore", "Laugh", "Cry", "Create",
    "Imagine", "Teach", "Learn", "Build", "Design", "Drive", "Fly", "Sail", "Climb", "Hike"
]

word = random.choice(word_list)
word_display = "_" * len(word)
stages = [
    '''
       ------
       |    |
       |
       |
       |
       |
    ---
    '''
    ,
    '''
       ------
       |    |
       |    O
       |
       |
       |
    ---
    '''
    ,
    '''
       ------
       |    |
       |    O
       |    |
       |
       |
    ---
    '''
    ,
    '''
       ------
       |    |
       |    O
       |   /|
       |
       |
    ---
    '''
    ,
    '''
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    ---
    '''
    ,
    '''
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    ---
    '''
    ,
    '''
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    ---
    '''
]

count = 0
guessed_letters = set()

while True:
    print("Word:", " ".join([char if char in guessed_letters else "_" for char in word]))

    user_letter = input("Guess a letter: ").lower()

    if user_letter.isalpha() and len(user_letter) == 1:
        if user_letter in guessed_letters:
            print("You've already guessed that letter. Try again.")
        elif user_letter in word:
            guessed_letters.add(user_letter)
            print("Good guess!")
        else:
            count += 1
            print(stages[count])
            print(f"Oops, wrong guess! You have {6 - count} tries remaining.")
    else:
        print("Invalid input. Please enter a single letter.")

    if set(guessed_letters) == set(word):
        print("Congratulations! You guessed the word:", word)
        break

    if count == 6:
        print("Sorry, you ran out of attempts. The correct word was:", word)
        break
