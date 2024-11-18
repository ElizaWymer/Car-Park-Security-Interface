import tkinter
import tkinter.messagebox
from tkinter import *
import time

# ________________________________________________________________________________________________________________________________
#|                                                                                                                                |
#| Functions                                                                                                                      |
#|________________________________________________________________________________________________________________________________|

def SearchExistingReg(list, RegNumber):
    for i in range(len(list)):
        if list[i] == RegNumber:
            return True
    return False
    #Searches through a list for the entered reg number.

def Time():
    Window.update()
    time.sleep(2) 
    #Sets a timer for two seconds so that users can read a message before it is removed.
        
def RegEntryFunction():
    NewReg = RegEntryInput.get()
    if len(NewReg) > 0:
        RegEntryInput.config(state = "disable")
        RegRemoveButton.config(state = "disable")
        RegDisplayButton.config(state = "disable")
        RegSearchButton.config(state = "disable")
        CloseButton.config(state = "disable")
        #Doesn't allow for users to click buttons for two seconds after clicking one.
        RegEntryOutput.config(state = "normal")
        RegEntryOutput.delete(1.0, "end")
        if (
              SearchExistingReg(AuthorisedGeneralRegNumbers, NewReg) == True and 
              SearchExistingReg(SavedGeneralRegNumbers, NewReg) == False and 
              len(SavedGeneralRegNumbers) != 10 and len(NewReg) > 0 and len(NewReg) < 9
            ):
            SavedGeneralRegNumbers.append(NewReg)
            Answer = "The reg number has been saved."
        elif (
                SearchExistingReg(AuthorisedVIPRegNumbers, NewReg) == True and
                SearchExistingReg(SavedGeneralRegNumbers, NewReg) == False and
                SearchExistingReg(SavedVIPRegNumbers, NewReg) == False and
                len(SavedVIPRegNumbers) != 5 and len(NewReg) > 0 and len(NewReg) < 9
              ):
            SavedVIPRegNumbers.append(NewReg)
            Answer = "The reg number has been saved."
        elif (
                SearchExistingReg(AuthorisedVIPRegNumbers, NewReg) == True and
                SearchExistingReg(SavedGeneralRegNumbers, NewReg) == False and
                SearchExistingReg(SavedVIPRegNumbers, NewReg) == False and
                len(SavedGeneralRegNumbers) != 10 and len(NewReg) > 0 and len(NewReg) < 9
              ):
            SavedGeneralRegNumbers.append(NewReg)
            Answer = "The reg number has been saved"
        else:
            Answer = "The reg number could not be saved."
        print("\nSaved:\nGeneral Reg Numbers: " + str(SavedGeneralRegNumbers))
        print("VIP Reg Numbers: " + str(SavedVIPRegNumbers))
        #These print statements are used for debugging.
        RegEntryOutput.insert(tkinter.END,Answer)
        RegEntryOutput.config(state = "disable")
        #Gets the value from the input box and compares it to a saved reg number.
        #The appropriate outcome is then executed and an appropriate message is then outputed in the info box.
        Time()
        RegEntryOutput.config(state = "normal")
        RegEntryOutput.delete(1.0, "end")
        RegEntryOutput.config(state = "disable")
        RegEntryInput.config(state = "normal")
        RegEntryInput.delete(0, "end")
        #Removes text from both the input box and the info box.
        if len(SavedGeneralRegNumbers) == 10 and len(SavedVIPRegNumbers) == 5:
            RegEntryOutput.config(state = "normal")
            RegEntryOutput.insert(tkinter.END, "The car park is full.")
            RegEntryInput.config(state = "disable")
            RegEntryButton.config(state = "disable")
            #Doesn't allow users to enter new reg numbers if the car park is full.
        RegEntryOutput.config(state = "disable")
        RegRemoveButton.config(state = "normal")
        RegDisplayButton.config(state = "normal")
        RegSearchButton.config(state = "normal")
        CloseButton.config(state = "normal")
        #Allows users to enter data again.

def RegRemoveFunction():
    NewReg = RegRemoveInput.get()
    if len(NewReg) > 0:
        RegRemoveInput.config(state = "disable")
        RegEntryButton.config(state = "disable")
        RegDisplayButton.config(state = "disable")
        RegSearchButton.config(state = "disable")
        CloseButton.config(state = "disable")
        #Doesn't allow for users to click buttons for two seconds after clicking one.
        RegRemoveOutput.config(state = "normal")
        RegRemoveOutput.delete(1.0, "end")
        if SearchExistingReg(SavedGeneralRegNumbers, NewReg) == True and len(NewReg) > 0 and len(NewReg) < 9:
            SavedGeneralRegNumbers.remove(NewReg)
            Answer = "The reg number has been removed."
        elif SearchExistingReg(SavedVIPRegNumbers, NewReg) == True and len(NewReg) > 0 and len(NewReg) < 9:
            SavedVIPRegNumbers.remove(NewReg)
            Answer = "The reg number has been removed."
        else:
            Answer = "The reg number could not be found."
        print("\nRemoved:\nGeneral Reg Numbers: " + str(SavedGeneralRegNumbers))
        print("VIP Reg Numbers: " + str(SavedVIPRegNumbers))
        #These print statements are used for debugging.
        RegRemoveOutput.insert(tkinter.END,Answer)
        RegRemoveOutput.config(state = "disable")
        #Gets the value from the input box and compares it to a saved reg number.
        #The appropriate outcome is then executed and an appropriate message is then outputed in the info box.
        Time()
        RegRemoveOutput.config(state = "normal")
        RegRemoveOutput.delete(1.0, "end")
        RegRemoveOutput.config(state = "disable")
        RegRemoveInput.config(state = "normal")
        RegRemoveInput.delete(0, "end")
        #Removes text from both the input box and the info box.
        if len(SavedGeneralRegNumbers) < 10 or len(SavedVIPRegNumbers) < 5:
            RegEntryButton.config(state = "normal")
            RegEntryInput.config(state = "normal")
            RegEntryOutput.config(state = "normal")
            RegEntryOutput.delete(1.0, "end")
            RegEntryOutput.config(state = "disable")
           #Allows the user to enter more reg numbers if the car park is not full.
        RegDisplayButton.config(state = "normal")
        RegSearchButton.config(state = "normal")
        CloseButton.config(state = "normal")
        #Allows users to enter data again.

def RegSearchFunction():
    NewReg = RegSearchInput.get()
    if len(NewReg) > 0:
        RegSearchInput.config(state = "disable")
        RegEntryButton.config(state = "disable")
        RegRemoveButton.config(state = "disable")
        RegDisplayButton.config(state = "disable")
        CloseButton.config(state = "disable")
        #Doesn't allow for users to click buttons for two seconds after clicking one.
        RegSearchOutput.config(state = "normal")
        RegSearchOutput.delete(1.0, "end")
        if SearchExistingReg(SavedGeneralRegNumbers, NewReg) == True:
            Answer = "The reg number has been found in a general parking space."
        elif SearchExistingReg(SavedVIPRegNumbers, NewReg) == True:
            Answer = "The reg number has been found in a VIP parking space."
        else:
            Answer = "The reg number could not be found."
        #Gets the value from the input box and compares it to a saved reg number.
        #The appropriate outcome is then executed and an appropriate message is then outputed in the info box.
        RegSearchOutput.insert(tkinter.END,Answer)
        RegSearchOutput.config(state = "disable")
        Time()
        RegSearchOutput.config(state = "normal")
        RegSearchOutput.delete(1.0, "end")
        RegSearchOutput.config(state = "disable")
        RegSearchInput.config(state = "normal")
        RegSearchInput.delete(0, "end")
        #Removes text from both the input box and the info box.
        RegEntryButton.config(state = "normal")
        RegRemoveButton.config(state = "normal")
        RegDisplayButton.config(state = "normal")
        CloseButton.config(state = "normal")
        #Allows users to enter data again.

def RegDisplayFunction():
    RegDisplayOutput.config(state = "normal")
    RegDisplayOutput.delete(1.0, "end")
    RegDisplayOutput.insert(tkinter.END,"General Space Reg Numbers:\n")
    for x in SavedGeneralRegNumbers:
        RegDisplayOutput.insert(tkinter.END,x)
        RegDisplayOutput.insert(tkinter.END,"\n")
    RegDisplayOutput.insert(tkinter.END,"\nVIP Space Reg Numbers:\n")
    for x in SavedVIPRegNumbers:
        RegDisplayOutput.insert(tkinter.END,x)
        RegDisplayOutput.insert(tkinter.END,"\n")
    RegDisplayOutput.config(state = "disable")
    #Outputs all data in CurrentGeneralRegNumbers and CurrentVIPRegNumbers.
    #It also outputs two headings so that the user knows what kind of parking space each car is in.

def ChangeMode():
    global Theme
    if Theme == "Light":
        Theme = "Dark"
        Window.configure(bg = "#2b373d")
        RegEntryLable.configure(bg = "#2b373d", fg = "white")
        RegRemoveLable.configure(bg = "#2b373d", fg = "white")
        RegSearchLable.configure(bg = "#2b373d", fg = "white")
        RegEntryInput.configure(bg = "#38454c", fg = "white")
        RegRemoveInput.configure(bg = "#38454c", fg = "white")
        RegSearchInput.configure(bg = "#38454c", fg = "white")
        RegEntryOutput.configure(bg = "#38454c", fg = "white")
        RegRemoveOutput.configure(bg = "#38454c", fg = "white")
        RegDisplayOutput.configure(bg = "#38454c", fg = "white")
        RegSearchOutput.configure(bg = "#38454c", fg = "white")
        RegEntryButton.configure(bg = "#0784b5", fg = "white")
        RegRemoveButton.configure(bg = "#0784b5", fg = "white")
        RegDisplayButton.configure(bg = "#0784b5", fg = "white")
        RegSearchButton.configure(bg = "#0784b5", fg = "white")
        LightThemeButton.config(state = "normal", bg = "#0784b5", fg = "white")
        DarkThemeButton.config(state = "disable", bg = "#0784b5")
        CloseButton.configure(bg = "#B90103", fg = "white")
    else:
        Theme = "Light"
        LightThemeButton.config(state = "disable", bg = "light blue", fg = "black")
        DarkThemeButton.config(state = "normal", bg = "light blue", fg = "black")
        Window.configure(bg = "white")
        RegEntryLable.configure(bg = "white", fg = "black")
        RegRemoveLable.configure(bg = "white", fg = "black")
        RegSearchLable.configure(bg = "white", fg = "black")
        RegEntryInput.configure(bg = "white", fg = "black")
        RegRemoveInput.configure(bg = "white", fg = "black")
        RegSearchInput.configure(bg = "white", fg = "black")
        RegEntryOutput.configure(bg = "white", fg = "black")
        RegRemoveOutput.configure(bg = "white", fg = "black")
        RegDisplayOutput.configure(bg = "white", fg = "black")
        RegSearchOutput.configure(bg = "white", fg = "black")
        RegEntryButton.configure(bg = "light blue", fg = "black")
        RegRemoveButton.configure(bg = "light blue", fg = "black")
        RegDisplayButton.configure(bg = "light blue", fg = "black")
        RegSearchButton.configure(bg = "light blue", fg = "black")
        CloseButton.configure(bg = "pink", fg = "black")
    #If the light theme is enabled and the button is pressed all of the elements change colour to become darker.
    #If the dark theme is enabled and the button is pressed all of the elements change colour to become lighter.

def CloseApp():
    if tkinter.messagebox.askyesno("Warning", "Are you sure you would like to close the application?", icon = "warning") == True:
        Window.destroy()
    #Ensures that the user intended to press the close button.
    #If the user pressed the button accidentally they can continue using the application by clicking 'no'.
    #If they intentionally pressed the button then they can close the application by clicking 'yes'.
    
# ________________________________________________________________________________________________________________________________
#|                                                                                                                                |
#| Constants and Variables                                                                                                        |
#|________________________________________________________________________________________________________________________________|

AuthorisedGeneralRegNumbers = ["VI03 BAW", "FQ63 LNZ", "AN36 BOI", "NB45 VWE", "MO87 HJU", "AN07 NOI", "BR63 CBA", "AI69 PRO", "EW04 MNI", "LI37 NQG", "OI32 BAT", "LP14 NIU"]
AuthorisedVIPRegNumbers = ["GF21 WSN", "HU55 BQY", "PZ65 PWO", "BD51 SMR", "NU34 REG", "AI69 PRO", "IL21 NQI"]

#Lists of all reg numbers on cars that are allowed to enter the car park.

SavedGeneralRegNumbers = []
SavedVIPRegNumbers = []

#Empty lists of all reg numbers on cars that have entered the car park.
#The user appends, removes and searches through cars from these lists.


Window = tkinter.Tk()
Window.geometry("1090x575")
Window.resizable(width = False, height = False)
Window.title("Car Park Security System")
Theme = "Light"

#Draws and sets the rules of the window.
#Theme is used so the program knows which theme is active.
#It's other state is "Dark".

Banner = tkinter.Label(text = "Car Park Security System", font = "calibri 18 bold", bg = "cornflower blue",width = 84, height = 1)
Banner.grid(columnspan = 5, row = 1, sticky = "nw")

#Creates the banner used in the software.

RegEntryLable = tkinter.Label(text = "Enter a reg number to be added:")
RegEntryLable.grid(column = 1, row = 2, padx = 5, pady = 25, sticky = "nw")
RegEntryInput = tkinter.Entry(width = 35, borderwidth = 2, relief = "ridge")
RegEntryInput.grid(column = 2, row = 2)
RegEntryButton = tkinter.Button(Window, text = "Save reg number       ", command = RegEntryFunction, bg = "light blue")
RegEntryButton.grid(column = 3, row = 2)
RegEntryOutput = tkinter.Text(width = 57, height = 1, borderwidth = 2, relief = "ridge")
RegEntryOutput.grid(column = 4, row = 2, padx = 10)
RegEntryOutput.config(state = "disable")

#Creates the design for the first row of the software which is used for entering reg numbers into the lists.

RegRemoveLable = tkinter.Label(text = "Enter a reg number to be removed: ")
RegRemoveLable.grid(column = 1, row = 3, padx = 4, sticky = "nw")
RegRemoveInput = tkinter.Entry(width = 35, borderwidth = 2, relief = "ridge")
RegRemoveInput.grid(column = 2, row = 3)
RegRemoveButton = tkinter.Button(Window, text = "Remove reg number", command = RegRemoveFunction, bg = "light blue")
RegRemoveButton.grid(column = 3, row = 3)
RegRemoveOutput = tkinter.Text(width = 57, height = 1, borderwidth = 2, relief = "ridge")
RegRemoveOutput.grid(column = 4, row = 3, padx = 10)
RegRemoveOutput.config(state = "disable")

#Creates the design for the second row of the software which is used for removing reg numbers into the lists.

RegSearchLable = tkinter.Label(text = "Search for a reg number: ")
RegSearchLable.grid(column = 1, row = 4, padx = 4, pady = 25, sticky = "nw")
RegSearchInput = tkinter.Entry(width = 35, borderwidth = 2, relief = "ridge")
RegSearchInput.grid(column = 2, row = 4)
RegSearchButton = tkinter.Button(Window, text = "Search reg number   ", command = RegSearchFunction, bg = "light blue")
RegSearchButton.grid(column = 3, row = 4)
RegSearchOutput = tkinter.Text(width = 57, height = 1, borderwidth = 2, relief = "ridge")
RegSearchOutput.grid(column = 4, row = 4, padx = 10)
RegSearchOutput.config(state = "disable")

#Creates the design for the third row of the software which allows for the user to search for a reg number in a list.

RegDisplayButton = tkinter.Button(Window, text = "Display reg numbers ",command = RegDisplayFunction, bg = "light blue")
RegDisplayButton.grid(column = 1, row = 5, padx = 4, pady = 5, sticky = "nw")
RegDisplayOutput = tkinter.Text(width = 26, height = 18, borderwidth = 2, relief = "ridge")
RegDisplayOutput.grid(column = 2, row = 5, padx = 10)
RegDisplayOutput.config(state = "disable")

#Creates the design for the fourth row of the software which is used for displaying the reg numbers in the lists.
#This function could be easily automated whenever a reg number is added or removed.
#Despite this the assignment brief specifies that the function should be tied to a button that the user must click.

LightThemeButton = tkinter.Button(Window, text = "Enable light mode    ", command = ChangeMode, bg = "light blue")
LightThemeButton.grid(column = 1, row = 5, padx = 4, pady = 65, sticky = "nw")
LightThemeButton.config(state = "disable")
DarkThemeButton = tkinter.Button(Window, text = "Enable dark mode    ", command = ChangeMode, bg = "light blue")
DarkThemeButton.grid(column = 1, row = 5, padx = 4, pady = 125, sticky = "nw")

#Creates the designs for the software's light and dark mode buttons.

CloseButton = tkinter.Button(Window, text = "Close the application", command = CloseApp, bg = "pink")
CloseButton.grid(column = 3, row = 6, padx = 25, pady = 30, sticky = "nw")

#Creates the design for the software's close button.
    
Window.mainloop()
quit()
