import random
words = [
    "book", "tree", "chair", "bread", "planet", 
    "camera", "picture", "blanket", "elephant", "computer", 
    "house", "apple", "school", "family", "rainbow", 
    "diamond", "cylinder", "mountain", "snake", "heart", 
    "window", "garden", "spindle", "building", "guitar", 
    "keyboard", "pyramid", "ocean", "butterfly", "monkey", 
    "forest", "river", "castle", "sunflower", "jungle", 
    "rocket", "python", "umbrella", "waterfall", "zebra", 
    "tiger", "penguin", "balloon", "chimney", "galaxy", 
    "laptop", "backpack", "triangle", "octopus", "volcano", 
    "banana", "waffle", "pickle", "pancake", "jellybean", 
    "donut", "pillow", "bubble", "sock", "toothpaste", 
    "taco", "cactus", "cheeseburger", "popcorn", "pineapple", 
    "marshmallow", "hotdog", "cupcake", "avocado", "kitten", 
    "puppy", "spider", "koala", "sloth", "goose", 
    "hedgehog", "llama", "potato", "carrot", "onion", 
    "meatball", "pizza", "cabbage", "shrimp", "mustard", 
    "ketchup", "spaghetti", "noodle", "pogo", "glove", 
    "trombone", "trumpet", "bucket", "clown", "pirate", 
    "wizard", "unicorn", "goblin", "hamster", "squirrel", 
    "walnut", "otter", "dolphin", "sneeze", "pudding", 
    "wiggle", "bubbles", "squishy", "fluffy"
]

print("================================")
print("Welcome to Mystery Word!")
print("================================")
you = input("Enter your Name: ")
print(f"Welcome, {you}!")
print("================================")
while True:
    word=random.choice(words)
    guess=5
    length=len(word)
    display=["_"]*length
    guessed_letters = set()
    print("\nGuess the mystery word:")
    print(" ".join(display))
    print()
    while "_" in display and guess > 0:
        choice = input("Enter your character: ").lower()
        if not choice.isalpha() or len(choice) != 1:
            print("Invalid input. Please enter a single letter.")
            continue

        if choice in guessed_letters:
            print(f"You already guessed '{choice}'. Try a different letter.")
            continue

        guessed_letters.add(choice)
        if choice in word:
            for indx,char in enumerate(word):
                if char==choice:
                    display[indx]=choice
                    print(" ".join(display))
                    print()
        else:
            guess=guess-1
            print(f"Try next time\n{you}, you have {guess} guesses left")
            print(" ".join(display))
            print()
    if "_" in display:
        print("================================")
        print("================================")
        print(f"Better luck next time, {you}! The word was '{word}'.")
        print("================================")
        print("================================")
    else:
        print("================================")
        print("================================")
        print(f"Congratulations, {you}! You guessed the word: '{word}'!")
        print("================================")
        print("================================")
    play= input("Do you want to play again? (yes/no): ").strip().lower()
    if play!="yes":
        print("Thanks for playing! Goodbye!")
        break