import random

choices = int(input(
    "What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors: "))
choices_computer = random.randint(1, 3)

if choices == 0 :
    print("""
          
    Your Choise:
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    
elif choices == 1:
    print("""

    Your Choise:
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

elif choices == 2:
    print("""
          
    Your Choise:
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

else:
    print("\nError\n")
   


if choices_computer == 0 :
    print("""

    Computer Chose:      
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    
elif choices_computer == 1:
    print("""
          
    Computer Chose:
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

elif choices_computer == 2:
    print("""
          
    Computer Chose:
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

else:
    print("\nError\n")



if choices_computer == 0 and choices == 1 and choices == 2 > choices_computer == 1 and choices == 0 > choices_computer == 2:
    print("You Win\n")
elif choices_computer == choices:
    print("Tie\n")
else:
    print("You Lose\n")

