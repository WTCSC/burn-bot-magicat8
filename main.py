name = input("What is your name? ")
age = input("What is your age? ")
food = input("What is your favorite food? ")
maiden_name = input("What is your mother's maiden name? ")

while True:
    try:
        level = int(input("On a scale of 1 to 10 how rude should I be? "))
        if 1 <= level <= 10:
            break
        else:
            print("Please enter a number between 1 and 10.")
    except ValueError:
        print("Scale should be a number.")

def be_rude(level):
    if level < 5:
        print(f"Really {food} is your favorite food, sooooooo basic.")
        print(f"Like really, a {age}-year-old likes {food}? You can't become much more basic.")
    else:
        print(f"Wow {name}, your taste is tragic. {food}! Really? Out of all the foods in the world?")
        print(f"At least your mom’s maiden name ({maiden_name}) is more interesting than your food choice.")

be_rude(level)
