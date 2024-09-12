# Implement a number guessing game, such that when initialized with a set of valid four-digit numbers and a target number, 
# the user can enter guesses, and the system provides feedback on whether each individual digit is too high or too low.

# The set of valid numbers is all possible four-digit numbers (i.e., 0000 through 9999).
# The target number is randomly selected from the set.
# The user has up to 7 guesses to find the correct number. After each guess, the system provides feedback based on 
# whether each digit of the guess is too high or too low compared to the corresponding digit in the target number.
# Each guess must be a valid four-digit number. If the user enters an invalid number (e.g., not four digits or 
# containing non-numeric characters), it is rejected and does not count toward the guess limit.
# A hint is provided after each valid guess with the following structure:
# H means the guessed digit is too high.
# L means the guessed digit is too low.
# = means the guessed digit is correct.

import random

# list 2 need to be solution
def compare_lists(player_guess, solution):
    differences = []
    for i in range(min(len(player_guess), len(solution))):
        if player_guess[i] > solution[i]:
            differences.append('H')
        elif player_guess[i] < solution[i]:
            differences.append('L')
        elif player_guess[i] == solution[i]:
            differences.append('=')
    return differences


def main():
    solution = random.randint(0, 9999)
    formatted_solution = f"{solution:04}"
    solution_list = list(formatted_solution)
    guesses = 0
    
    while guesses < 7:
        while True:
            player_guess = input('Please enter a number between 0 and 9999\n')
            if len(player_guess) != 4:
                print('invalid number')
            else:
                break
        player_guess_list = list(player_guess)
        print(formatted_solution)
        print(compare_lists(player_guess_list, solution_list))
        attempted_solution = compare_lists(player_guess_list, solution_list)
        if attempted_solution == ['=', '=', '=', '=']:
            print('congrats, grad! Youre engaged!')
            break   
        else:
            guesses += 1
            guesses_remaining = 7-guesses
            print(f'You have {guesses_remaining} guesses remaining')
main()