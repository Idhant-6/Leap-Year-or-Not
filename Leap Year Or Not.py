import time
user_plays = True
while user_plays:
    year = int(input("Which year do you want to check? "))
    if year % 4 == 0:
      if year % 100 == 0:
        if year % 400 == 0:
          print("Leap year.")
        else:
          print("Not a leap year.")
      else:
        print("Leap year.")
    else:
      print("Not a leap year.")
    user_choice = input("Do You Want To Calculate Years Again?? [Y/N]: ").lower()
    if user_choice == "y":
        user_plays = True
    elif user_choice == "n":
        user_choice = False
        print("Good Byee")
        break
    else:
      print("Invalid Command, Please Try Again")
      time.sleep(5)