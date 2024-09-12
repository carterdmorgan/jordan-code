# Implement a number guessing game, such that when initialized with a set of 
# valid four-digit numbers and a target number, the user can enter guesses, 
# and the system provides feedback on whether each individual digit is too 
# high or too low.

# The set of valid numbers is all possible four-digit numbers 
# (i.e., 0000 through 9999).
# The target number is randomly selected from the set.
# The user has up to 7 guesses to find the correct number. After each guess, 
# the system provides feedback based on whether each digit of the guess is too 
# high or too low compared to the corresponding digit in the target number.
# Each guess must be a valid four-digit number. If the user enters an invalid
# number (e.g., not four digits or containing non-numeric characters), 
# it is rejected and does not count toward the guess limit.
# A hint is provided after each valid guess with the following structure:
# H means the guessed digit is too high.
# L means the guessed digit is too low.
# = means the guessed digit is correct.

import random

# check if user's selected number contains only digits
def validate_input_digits(user_input: str):
    try: 
        user_input = int(user_input)
        return True
    except:
        return False
    
# check if user's selected number contains four characters
def validate_input_length(user_input: str):
    if len(user_input) != 4:
        return False
    else:
        return True

# format generated solution int into four character string
def format_solution(solution: str):
    return solution.zfill(4)

# format solution string into list
def convert_to_list(formatted_solution: str):
    solution_list = list(formatted_solution)
    return solution_list

# create a solution for the game
def generate_solution(solution = None):
    if solution is None:
        solution = str(random.randint(0, 9999))
    formatted_solution = format_solution(solution)
    solution_list = convert_to_list(formatted_solution)
    return solution_list

# compare user's number to solution and return hints
def compare_lists(user_list: list, solution_list: list):
    hint_list = []
    for i in range(len(user_list)):
        if user_list[i] > solution_list[i]:
            hint_list.append('H')
        elif user_list[i] < solution_list[i]:
            hint_list.append('L')
        else:
            hint_list.append('=')
    return hint_list


def main():
    solution_list = generate_solution()

    #guess counter
    guesses = 0

    while guesses < 7:
        user_input = input('Enter a four-digit number\n')
        if validate_input_digits(user_input) is False or validate_input_length(user_input) is False:
            print('Invalid number')
        else:
            user_input_formatted = format_solution(user_input)
            user_list = convert_to_list(user_input_formatted)
            hint_list = compare_lists(user_list, solution_list)
            if hint_list == ['=', '=', '=', '=']:
                print('Congratulations!')
                break
            else:
                print(hint_list)
                guesses += 1
                print(f'You have {7 - guesses} guesses remaining')


if __name__ == "__main__":
    main()




    