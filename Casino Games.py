# Algorithm:
# Step 1: Import the random module
# Step 3: Create a variable that holds the random number for each round, to hold the bet, and user winnings
# Step 2: Create conditions for each bet a player could select
#         Prompt the user to select a bet and input a number. When user selects bet, display that the wheel is spinning and the results of their bet:
#          Straight: Checks if the users number is equal to the random number, if it is, the player wins 35 * 5 dollars and display "You win" and the cash amount
#          Split: Checks if the users number is the generated number or the generated number +/- 1, if it is, the player wins 17 * 5 and display "You win" and the cash amount
#          Street: Checks if the users number is the generated number or the number +2, if it is, the player wins 11*5 dollars and display "You win", and the cash amount
#          Top: Checks if the generated number falls within the range of 1-18, if yes the player wins $10, display "You win" and the cash amount
#          Bottom: Checks if the generated number falls within the 19-36 range, if yes, the player wins $10, display "You win" and the cash amount
#          Even/Odd: Player choses to bet that the number is either even or odd, if their choice is correct, the wins $10, display "You win" and the cash amount
# Step 4: Create a key the user can use to quit the game, otherwise the game will continue

import random

rand_num = random.randint(1,36)
bet = 5
user_winnings = 0

while True:
  print("Welcome to Autumns Casino!\nSelect from the bets below to begin your game!")
  bet_selection = input('Straight: The number you enter must equal where the wheel lands.\nSplit: The number you enter must be where the wheel lands or be one greater or one less.\nStreet: The number you enter must be where the wheel lands or within the range of +2\nTop/Bottom: The game will ask you if you want to bet \nTop -- that the number is between 1-18 or \nBottom -- That the number is between 18 and 36\nEven/Odd: The game will ask you if you want to be if the number will be even or odd\nPress 0 to exit the game.\n')

  if bet_selection == "0":
    break
  
  elif bet_selection == "Straight" or bet_selection == "straight":
    user_num = int(input("\n--------Spinning the wheel-------\nEnter the number you would like to bet on: "))
    if user_num == rand_num:
      winnings = bet * 35
      print("Congradulation, you won! Your earning is", str(winnings)+"!")
      user_winnings += winnings
    else:
      print("You lost lol")
      continue

  elif bet_selection == "Street" or bet_selection == "street":
    user_num = int(input("Enter the number you would like to bet on: "))
    if (user_num == rand_num) or (user_num == rand_num + 1) or (user_num == rand_num + 2):
      winnings = bet * 11
      print("Congradulation, you won! Your earning is", str(winnings)+"!")
      user_winnings += winnings
    else:
      print("You lost lol")
      continue

  elif bet_selection == "Split" or bet_selection == "split":
    user_num = int(input("Enter the number you would like to bet on: "))
    if (user_num == rand_num) or (user_num == rand_num - 1) or (user_num == rand_num + 1):
      winnings = bet * 17
      print("Congradulation, you won! Your earning is", str(winnings)+"!")
      user_winnings += winnings
    else:
      print("You lost lol")
      continue
  elif bet_selection == "Top/Bottom":
    user_bet = input("Would you like to bet the top or the bottom? ")
    if user_bet == "top" or user_bet == "Top":
      rand_num = random.randint(1,36)
      if rand_num >= 1 and rand_num <= 18:
        winnings = 10
        print("The number is: " + str(rand_num))
        user_winnings += winnings
        print("You won $" + str(winnings) +"!")
    elif user_bet == "bottom" or user_bet == "Bottom":
      rand_num = random.randint(1,36)
      if rand_num >= 18 and rand_num <= 36:
        winnings = 10
        print("The number is: " + str(rand_num))
        user_winnings += winnings
        print("You won $" + str(winnings) +"!")
        play_again = input("Would you like to play again? ")
      else:
        print("The number is: " + str(rand_num))
  
  elif bet_selection == "Even/Odd" or bet_selection == "even/odd":
    rand_num = random.randint(1,36)
    user_bet = input("Would you like to bet even or odd? ")
    if user_bet == "Even" or user_bet == "even":
      if rand_num % 2 == 0:
        print("The number is: " + str(rand_num))
        winnings = 10
        print("Congratulations, you won! Your earning is $10!")
        user_winnings += winnings
  elif user_bet == "Odd" or user_bet == "odd":
    if rand_num % 2 == 1:
      print("The number is: " + str(rand_num))
      winnings = 10
      print("Congratulations, you won! Your earning is $" + str(winnings) + "!")
      user_winnings += winnings
    else:
      print("The number is: " + str(rand_num))
      play_again = input("You lost lol\nWould you like to play again? ")
      if play_again == "yes":
        continue
      elif play_again == "no":
        print("\n")
        player_choice = False
      else:
        print("Please input a valid option. ", end="")
        continue
  else:
        print("Please input a valid option. ", end="")
        continue