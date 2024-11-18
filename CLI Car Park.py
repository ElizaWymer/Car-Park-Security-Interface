SavedGeneralRegNumbers = ["VI03 BAW", "FQ63 LNZ", "AN36 BOI", "NB45 VWE", "MO87 HJU", "AN07 NOI", "BR63 CBA", "LK97 OFA", "EW04 MNI", "LI37 NQG", "OI32 BAT", "LP14 NIU"]
SavedVIPRegNumbers = ["GF21 WSN", "HU55 BQY", "PZ65 PWO", "BD51 SMR", "NU34 REG", "AI69 PRO", "IL21 NQI"]

CurrentGeneralRegNumbers = []
CurrentVIPRegNumbers = []

def SearchExistingReg(list, RegNumber):
    for i in range(len(list)):
        if list[i] == RegNumber:
            return True
    return False

def EnterNewReg():
    NewReg = input("\nPlease enter the new registration number: ")
    if SearchExistingReg(SavedGeneralRegNumbers, NewReg) == True and SearchExistingReg(CurrentGeneralRegNumbers, NewReg) == False and len(CurrentGeneralRegNumbers) != 10 and len(NewReg) > 0 and len(NewReg) < 9:
        CurrentGeneralRegNumbers.append(NewReg)
        input("The registration number has been added.")
    elif SearchExistingReg(SavedVIPRegNumbers, NewReg) == True and SearchExistingReg(CurrentGeneralRegNumbers, NewReg) == False and  SearchExistingReg(CurrentVIPRegNumbers, NewReg) == False and len(CurrentVIPRegNumbers) != 5 and len(NewReg) > 0 and len(NewReg) < 9:
        CurrentVIPRegNumbers.append(NewReg)
        input("The registration number has been added.")
    elif SearchExistingReg(SavedVIPRegNumbers, NewReg) == True and SearchExistingReg(CurrentGeneralRegNumbers, NewReg) == False and SearchExistingReg(CurrentVIPRegNumbers, NewReg) == False and len(CurrentGeneralRegNumbers) != 10 and len(NewReg) > 0 and len(NewReg) < 9:
        CurrentGeneralRegNumbers.append(NewReg)
        input("The registration number has been added.")
    else:
        input("The registration number could not be saved either because the entered reg number is invalid or because the car park is full.")

def RemoveReg():
    RegRemoval = input("\nPlease enter the registration number you would like to remove: ")
    if SearchExistingReg(CurrentGeneralRegNumbers, RegRemoval) == True and len(RegRemoval) > 0 and len(RegRemoval) < 9:
        CurrentGeneralRegNumbers.remove(RegRemoval)
        input("The registration number has been removed.")
    elif SearchExistingReg(CurrentVIPRegNumbers, RegRemoval) == True and len(RegRemoval) > 0 and len(RegRemoval) < 9:
        CurrentVIPRegNumbers.remove(RegRemoval)
        input("The registration number has been removed.")
    else:
        input("The registration number could not be found.")

def DisplayCurrentReg():
    print("\nGeneral Space Reg Numbers:")
    for x in CurrentGeneralRegNumbers:
        print(x)
    print("\nVIP Space Reg Numbers:")
    for x in CurrentVIPRegNumbers:
        print(x)
    input()

def SearchCurrentReg():
    RegInput = input("\nPlease enter the registration number you would like to search for: ")
    if SearchExistingReg(CurrentGeneralRegNumbers, RegInput) == True:
        input("The registration number has been found in a general parking space.")
    elif SearchExistingReg(CurrentVIPRegNumbers, RegInput) == True:
        input("The registration number has been found in a VIP parking space.")
    else:
        input("The registration number could not been found.")

User = None
while True:
  print(" _____________________________________________")
  print("|                                             |")
  print("| >'Enter' a registration number              |")
  print("| >'Remove' a registraton number              |")
  print("| >'Display' the stored registration numbers  |")
  print("| >'Search' for a registration number         |")
  print("| >'Close' the program                        |")
  print("|_____________________________________________|")
  User = input("\nPlease enter one of the keywords above: ")
  if User == "Enter":
      EnterNewReg()
  elif User == "Remove":
      RemoveReg()
  elif User == "Display":
      DisplayCurrentReg()
  elif User == "Search":
      SearchCurrentReg()
  elif User == "Close":
      quit()
