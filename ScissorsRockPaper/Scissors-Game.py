import random

# Function to Prompt User to enter value
def promptUser():
    print("Welcome to our Rock, Scissors and Paper Game")
    print("Pick an option between R, S and P")
    print("Where R = Rock, S = Scissors and P = Paper")
    user_option = input("Enter your Chioce: ")
    user_option_capitalized = user_option.upper()

    return user_option_capitalized


def starter():
    user_option_key = promptUser()
    possible_options = [{"R": "Rock"}, {"S": "Scissors"}, {"P": "Paper"}]
    # getting the first key from the list'R'
    item_1 = possible_options[0]
    item_key_1 = list(item_1)
    Key_one = item_key_1[0]

    # getting the second key from the list'S'
    item_2 = possible_options[1]
    item_key_2 = list(item_2)
    Key_two = item_key_2[0]

    # getting the second key from the list'P'
    item_3 = possible_options[2]
    item_key_3 = list(item_3)
    Key_three = item_key_3[0]

    if user_option_key == Key_one:
        computer_choice = random.choice(possible_options)
        for key, value in computer_choice.items():
            computer_choice_key = key

            if computer_choice_key == user_option_key:
                print("Its a tie, lets try again")
                starter()
            else:
                if computer_choice_key == Key_two:
                    print("Computer Choice: ", computer_choice_key)
                    print("You Won (Rock Wins)")

                elif computer_choice_key == Key_three:
                    print("Computer Choice: ", computer_choice_key)
                    print("You Lose (Paper Wins)")

    elif user_option_key == Key_two:
        computer_choice = random.choice(possible_options)
        for key, value in computer_choice.items():
            computer_choice_key = key
            if computer_choice_key == user_option_key:
                print("Its a tie, lets try again")
                starter()
            else:
                if computer_choice_key == Key_one:
                    print("Computer Choice: ", computer_choice_key)
                    print("You Lose (Rock Wins)")

                elif computer_choice_key == Key_three:
                    print("Computer Choice: ", computer_choice_key)
                    print("You Win (Scissors Wins)")
    elif user_option_key == Key_three:
        computer_choice = random.choice(possible_options)
        for key, value in computer_choice.items():
            computer_choice_key = key
            if computer_choice_key == user_option_key:
                print("Its a tie, lets try again")
                starter()
            else:
                if computer_choice_key == Key_one:
                    print("Computer Choice: ", computer_choice_key)
                    print("You Win (Paper Wins)")

                elif computer_choice_key == Key_two:
                    print("Computer Choice: ", computer_choice_key)
                    print("You Lose (Scissors Wins)")
    else:
        print("Incorrect Entry, Please input correctly.")
        starter()


starter()
