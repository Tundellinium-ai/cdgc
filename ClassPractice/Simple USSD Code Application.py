print("    _____You are Wecome to Element Network USSD Application_____")

codes = ["*310#", "*312#", "*321#"]

print('''
      *310# - Aritime balance check 
      *312# - Buy data 
      *321# - Share data
''')

ussd = input(f"    Enter USSD: ")
if ussd in codes and ussd ==  "*310#":
    print('''    
      SmartTALK Main Bal:N2941.3 .Dial *310*1# for bonus balance
      Select
      1) 6GB @ N2500 (7days)
      2) 100mins @ N1000 (14days)
      3) Cancel
''')
    choice1 = int(input("    Enter your choice (1-3): "))
    if choice1 == 1:
        print("    You have successfully subscribed for 6GB")
    elif choice1 == 2:
        print("    You have successfully subscribed for 100mins")
    elif choice1 == 3:
        print("    Request cancelled")
    else:
        print("    Wrong input, try again")
elif ussd in codes and ussd == "*312#":
    print('''
      1 My Area
      2 Data Plans
      3 10GB @N3000
      4 5GB @N1500
      5 3GB @N750
      6 1.5GB @N500
      7 2GB @N600
      8 6GB @N2500
      9 Voice Plans
      * Next
''')
    choice2 = input("   ")
    if choice2 == "1":
        print("    You have successfully migrated to My Area")
    elif choice2 == "2":
        print("    You will see data plans shortly...")
    elif choice2 == "3":
        print("    You have successfully subscribed for 10GB")
    elif choice2 == "4":
        print("    You have successfully subscribed for 5GB")
    elif choice2 == "5":
        print("    You have successfully subscribed for 3GB")
    elif choice2 == "6":
        print("    You have successfully subscribed for 1.5GB")
    elif choice2 == "7":
        print("    You have successfully subscribed for 2GB")
    elif choice2 == "8":
        print("    You have successfully subscribed for 6GB")
    elif choice2 == "9":
        print("    You will see voice plans shortly...")
    elif choice2 == "*":
        print("    You will be shown the next options soon...")
    else:
      print("    Wrong input, try again")
else:
  print("    Wrong USSD, try again")
