try:
    name = input("type your name : ")
    if name == "":
        name = "human"
    else:
        name = name

    computer_point = 0
    human_point = 0

    roundn = 0
    while roundn < 10:
        roundn = roundn + 1

        import random

        list2 = ["snake", "water", "gun"]
        computer_choice = random.choice(list2)

        print("\n snake , water , gun")
        human_choice = input("choose one of this : ")  # user input

        # --------------------------------- if else statement start here--------------------------------
        if computer_choice == "snake" and human_choice == "water":
            print("computer choice", computer_choice)
            print("computer won this round")
            computer_point += 1

        elif computer_choice == "water" and human_choice == "snake":
            print("computer choice", computer_choice)
            print("you won this round")
            human_point += 1

        elif computer_choice == "gun" and human_choice == "water":
            print("computer choice", computer_choice)
            print("you won this round")
            human_point += 1

        elif computer_choice == "water" and human_choice == "gun":
            print("computer choice", computer_choice)
            print("computer won this round")
            computer_point += 1

        elif computer_choice == "gun" and human_choice == "snake":
            print("computer choice", computer_choice)
            print("computer won this round")
            computer_point += 1

        elif computer_choice == "snake" and human_choice == "gun":
            print("computer choice", computer_choice)
            print("you won this round")
            human_point += 1

        elif computer_choice == "snake" and human_choice == "snake":
            print("computer choice", computer_choice)
            print("both are winners this round")
            computer_point += 1
            human_point += 1

        elif computer_choice == "gun" and human_choice == "gun":
            print("computer choice", computer_choice)
            print("both are winners this round")
            computer_point += 1
            human_point += 1

        elif computer_choice == "water" and human_choice == "water":
            print("computer choice", computer_choice)
            print("both are winners this round")
            computer_point += 1
            human_point += 1

        else:
            print("your input maybe wrong ! please try again")
        # ---------------------------finished main if else code----------------------------------

        print("you have finished", roundn, "round , and you have", 10 - roundn, "left")

        if roundn == 10 and human_point < computer_point:
            print("\nGame is over")
            print(f"{name} point = {human_point} and compuer point = {computer_point}")
            print(f"Computer is the winner of this game and {name} is the runner-up")

        elif roundn == 10 and human_point > computer_point:
            print("\nGame is over")
            print(f"{name} point = {human_point} and compuer point = {computer_point}")
            print(f"{name} is the winner of this game and computer is runner-up")

        elif roundn == 10 and human_point == computer_point:
            print("\nGame is over")
            print(f"{name} point = {human_point} and compuer point = {computer_point}")
            print("Both are the winner of this game")

except Exception as k:
    print(k)
