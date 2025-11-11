# Write a rock, paper, scissors game
# import random module
import random
#define main function that handles all the logic
def main():
    # define choices
    choices = ['rock', 'paper', 'scissors']
    
    # get user input
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    
    # validate user input
    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return
    
    # get computer choice
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    
    # determine winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
    else:
        print("You lose!")

if __name__ == "__main__":
    main()      
    