#EXTERNAL IMPORTS#
import pandas as pd
import os
from tabulate import tabulate
#CUSTOM IMPORTS#

class BaseMenu():
    #base class for menus 
    def __init__(self, string_in):
        self.prompt = string_in

    def clearTerm(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def printList(self, list_in):
        print("\t")
        for i, option in enumerate(list_in):
            print(f"{i+1}. {option}")

    def basicIntLoop(self):
        usrinput = None
        while(usrinput == None):
            try:
                usrinput = int(input(self.prompt))
            except:
                print("Invalid input.")
                usrinput = None
        return usrinput

class Menu(BaseMenu):
    #base class for basic menu creation and printing
    def __init__(self, prompt_in, menu_dict):
        #sets up prompt string and creates the menu dataframe
        self.prompt = prompt_in+">"
        self.menudict = menu_dict 
        self.menutype = ""
        self.printmenu = True
        self.menu = pd.DataFrame(self.menudict)
        self.menu.index += 1
        self.clearTerm()

    def printMenu(self):
        #prints the current menu
        # listsize = len(self.optionlist)
        # if len 
        df = pd.DataFrame(self.optionlist)
        df.index += 1
        # # print(df)
        # options = ["plain",
        #         "simple",
        #         "github",
        #         "grid",
        #         "fancy_grid",
        #         "pipe",
        #         "orgtbl",
        #         "jira",
        #         "presto",
        #         "psql",
        #         "rst",
        #         "mediawiki",
        #         "moinmoin",
        #         "youtrack",
        #         "html",
        #         "latex",
        #         "latex_raw",
        #         "latex_booktabs",
        #         "textile",
        # ]
        # for style in options:
        #     print(style + "\n")
        print(tabulate(df, tablefmt="psql"))
        # self.printList(self.optionlist)

    def printLoop(self, orig_end):
        #input validation loop making sure the user's input is an integer or "list", "back", "quit"
        selected = None
        endstring = orig_end + "\nType 'list' to print the list again."

        while(selected == None):
            if self.printmenu:
                # print("\n")
                self.printMenu()
                self.printmenu = False

            print(endstring)
            selected = input(self.prompt)

            if selected == "list":
                self.printmenu = True
                endstring = "Type 'list' to print the list again."
                endstring = endstring + "Type 'quit' to quit."
                selected = None
            elif selected == "quit":
                break
            elif selected == "back":
                break
            else:
                try:
                    selected = int(selected)
                except ValueError:
                    endstring = "Invalid input. Please input a number or type 'list' to print the options again."
                    selected = None
        return selected

    def getValidSelection(self, string_in):
        #input validation loop making sure a given integer selection is in the list of options for the menu instance
        #runs until user picks an option, then returnthreshold
        selection = None
        endstring = string_in + "\nPlease enter a number from the list."
        while(selection == None):
            selection = self.printLoop(endstring)
            if selection == "quit" or selection == "back":
                # print("hit valid selection block")
                break
            try:
                item = self.getItem(selection)
                selection = item
            except:
                endstring = f"\n{selection} is not an option. Please pick a valid option."
                self.printmenu = False
                selection = None
        return selection

    def getItem(self, selection):
        #virtual function indended to be overwritten by inheriting functions
        return self.menu[self.menutype][selection]

    def promptLoop(self, string_in):
        #runs getValidSelection until user selects, backs out, or quits program
        selection = None
        while(selection == None):
            selection = self.getValidSelection(string_in)
            if selection == "quit": #if user wants to quit, return True to fall through all parent while loops
                selection = True
        return selection

class ListMenu(Menu):
    #class for selecting from a list of items
    def __init__(self, prompt_in):
        # print("made it to listmenu creation")
        menudict = {
            "options":self.optionlist
        }
        super().__init__(prompt_in, menudict)
        self.menutype = "options"

    def startPrompt(self, string_in):
        #runs prompt for functions until back is returned
        exitcode = False
        while(exitcode != True):
            exitcode = self.promptLoop(string_in) #find function to execute and try to execute it
            if exitcode == "back": #if recieved "back" in the promptLoop
                exitcode = False
                break #just break out of this loop and end startPrompt call
            else:
                break
        # print(f"exitcode: {exitcode}")
        return exitcode

class FuncMenu(Menu):
    #class for selecting from a list of functions
    # def __init__(self, prompt_in, option_list, function_list):
    def __init__(self, prompt_in):
        # self.optionlist = option_list
        # self.functionlist = function_list
        menudict = {
            "options":self.optionlist,
            "functions":self.functionlist
        }
        super().__init__(prompt_in, menudict)
        self.menutype = "functions" 
    
    def exitFunc(self):
        #function that runs as the quit command is cascading down the prompt stack
        #virtual function meant to be over ridden by descendant class
        pass

    def returnFunc(self):
        #function that runs every time the prompt returns to the current menu
        #virtual function meant to be over ridden by descendant class
        pass

    def startPrompt(self, string_in):
        #runs prompt for functions until back is returned
        exitcode = False
        while(exitcode != True):
            try:
                exitcode = self.promptLoop(string_in) #find function to execute and try to execute it
                # exitcode = True
                exitcode = exitcode()
                self.returnFunc()
            except: #if hit this, that means we recieved "quit", or "back"
                if exitcode == "back": #if recieved "back" in the promptLoop
                    exitcode = False
                    self.printmenu = True
                    break #just break out of this loop and end startPrompt call
        # print(f"exitcode: {exitcode}")
        self.exitFunc()
        return exitcode