import random

def get_user_choice():
    while True:
        try:
            print("Enter your Choice:")
            print("1. Rock")
            print("2. Paper")
            print("3. Scissors\n")
            choice = int(input("Enter Your Choice: "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Invalid choice. Please choose 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_choice_name(choice):
    if choice == 1:
        return 'Rock'
    elif choice == 2:
        return 'Paper'
    else:
        return 'Scissors'

def winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return 'draw'
    elif(user_choice == 'Rock' and comp_choice=='Paper'):
        return  'lose'
    elif(user_choice == 'Rock' and comp_choice=='Scissors'):
        return  'Win'
    elif(user_choice == 'Paper' and comp_choice=='Rock'):
        return  'Win'
    elif(user_choice == 'Paper' and comp_choice=='Scissors'):
        return  'lose'
    elif(user_choice == 'Scissors' and comp_choice=='Rock'):
        return  'lose'
    elif(user_choice == 'Scissors' and comp_choice=='Paper'):
        return  'Win'

def main():
    while True:
        user_choice = get_user_choice()
        user_choice_name = get_choice_name(user_choice)
        print(f'User choice is {user_choice_name}\n')
        
        print("Now it's Computer's Turn....")
        comp_choice = random.randint(1, 3)
        comp_choice_name = get_choice_name(comp_choice)
        print(f'Computer choice is {comp_choice_name}\n')
        
        print(f'{user_choice_name} VS {comp_choice_name}')
        
        result = winner(user_choice, comp_choice)
        
        if result == 'draw':
            print("It's a tie")
        elif result == 'lose':
            print("Computer Wins")
        else:
            print("User Wins")
        
        print('\nDo you want to play again? (Y/N)')
        ch = input().strip().upper()
        if ch == 'N':
            break
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
