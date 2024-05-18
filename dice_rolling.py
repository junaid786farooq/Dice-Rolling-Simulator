import random

def dice_roll():

    # dice_drawing is a dictionary where each key represents a number on the dice (from 1 to 6), and the corresponding value is a tuple containing ASCII art representations of the dice faces with that number of pips.
    dice_drawing = {
        1:(" _________",
          "|    1    |",
          "|    ●    |",
          "|         |",
          "|_________|"
            ),

        2:(" _________",
          "| ●       |",
          "|    2    |",
          "|       ● |",
          "|_________|"
            ),

        3:(" _________",
          "| ●  3    |",
          "|    ●    |",
          "|       ● |",
          "|_________|"
            ),

        4:(" _________",
          "| ●     ● |",
          "|    4    |",
          "| ●     ● |",
          "|_________|"
            ),

        5:(" _________",
          "| ●     ● |",
          "|    ●    |",
          "| ●  5  ● |",
          "|_________|"
            ),

        6:(" _________",
          "|  ●   ●  |",
          "|  ● 6 ●  |",
          "|  ●   ●  |",
          "|_________|"
            )
         
        }

    roll = input("Roll the dice? (yes/no): ")
    
    # generates random numbers for two dice
    while roll.lower() == "yes":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print("Dice rolled: {} and {}".format(dice1, dice2))
        
        # The ASCII art representation of the dice faces corresponding to the rolled numbers is obtained
        # The "\n".join() method is used to join the lines of the ASCII art representation and print them in a readable format.
        print("\n".join(dice_drawing[dice1]))
        print("\n".join(dice_drawing[dice2]))

        roll = input("Roll again? (yes/no): ")

# Call the function
dice_roll()