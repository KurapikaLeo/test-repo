import random

user_wins = 0
computer_wins = 0

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
while True:
    try:
        options = [rock, paper, scissors, quit]
        user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors or 3 to quit .\n"))
        print(options[user_choice])

        computer_choice = random.randint(0, 2)
        print("Computer chose:", computer_choice)
        print(options[computer_choice])

        if user_choice == 3:
            break

        if user_choice == 0 and computer_choice == 2:
            print("You win!")
            user_wins += 1

        elif user_choice == 1 and computer_choice == 0:
            print("You win!")
            user_wins += 1

        elif user_choice == 2 and computer_choice == 1:
            print("You win!")
            user_wins += 1

        elif user_choice == computer_choice:
            print("Draw!")
            
        else:
            print("You lose")
            computer_wins += 1

        print("You won", user_wins, "times")
        print("Computer won", computer_wins, "times")

    except IndexError:
        print("The option you chose is out of range")
      
      # accepts the index error 