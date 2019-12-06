#EXTERNAL IMPORTS#
import pandas as pd
import numpy as np
import os
from tabulate import tabulate
#CUSTOM IMPORTS#

class BaseMenu():
    #base class for menus 
    def __init__(self, string_in):
        self.prompt = string_in + ">"
        # self.strflag = False #decendant class will set this to true if its indexes are strings

    def clearTerm(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print2DList(self, list_in):
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
    def __init__(self):
        #sets up prompt string and creates the menu dataframe
        super().__init__(self.prompt)
        # self.prompt = self.prompt+">" #sets prompt for this menu
        self.printmenu = True #instance variable to toggle printing of the menu options
        #create menu data frame
        mindex = self.menudict.pop("index", None)
        if mindex == []:
            self.menuframe = pd.DataFrame(self.menudict)
        else:
            self.menuframe = pd.DataFrame(self.menudict, index=mindex)
        if not self.strflag:
            self.menuframe.index += 1
            # print(self.menuframe.index.values)

        #clear terminal
        self.clearTerm()

    def printMenu(self):
        # prints the current menu
        if len(self.menuframe.index.values) < 10:
            print(tabulate(self.menuframe[['options']], showindex=True, tablefmt="psql"))
            return
        heads = self.menuframe.index.values # list of all options
        sz = len(heads) #get length of all options
        i = 1
        divsize = sz
        while(divsize > 10):
            #keep dividing the lenth of options by a bigger number until you get below 10
            divsize = sz//i 
            i += 1 
        heads = np.array_split(heads, i) #split heads into i groups which should yeild a size <=10
        # options = [
        #     "grid",
        #     "fancy_grid",
        #     "rst",
        # ]
        # for style in options:
        #     print(f"\n{style}\n")
        for arr in heads: #print the transpose of the list with the elements in the arr grouping 
            print(tabulate(self.menuframe[['options']].T[arr], headers=arr, tablefmt=self.style, showindex=False))
        return

    def getValidMenuOption(self, string_in):
        #input validation loop making sure a given output is in the list of options for the menu instance
        #runs until user picks an option, then return
        output = None
        helpmenu = "\nlist\tprints menu\nback\tgoes back one menu\nquit\tquits program\nclear\tclears screen\nhelp\tprints this list" 
        endstring = string_in + "\nType help for a list of commands."

        while(output == None):
            if self.printmenu:
                self.printMenu()
                self.printmenu = False
            print(endstring)
            endstring = string_in
            inpt = input(self.prompt)
            
            if inpt == "list":
                self.printmenu = True
                endstring = string_in 
                output = None
            elif inpt == "help":
                endstring = helpmenu
                output = None
            elif inpt == "clear":
                self.clearTerm()
                endstring = string_in
                output = None
            elif inpt == "quit":
                output = True
                break
            elif inpt == "back":
                output = False
                break
            else:
                # print(type(self.menuframe))
                # print(self.menuframe)
                try:
                    index = int(inpt)
                    output = self.menuframe[self.menutype][index]
                    # output = output.loc[self.menutype]
                    # print(type(output))
                except ValueError:
                    try:
                        index = inpt
                        output = self.menuframe.loc[index, self.menutype]
                    except KeyError:
                        if self.strflag:
                            endstring = f"\n{output} is not an valid option.\n{string_in}\nType help for commands."
                            self.printmenu = False
                            output = None
                        else:
                            endstring = f"{output} is not an integer.\n{string_in}\nType help for commands."
                            self.printmenu = False
                            output = None
                except KeyError:
                    intstring = f"\n{output} is not an valid option.\n{string_in}\nType help for commands."
                    self.printmenu = False
                    output = None

        return output

class ListMenu(Menu):
    #class for selecting from a list of items
    def __init__(self):
        self.menutype = "options" 
        # build dataframe dictionary
        self.style = "rst"
        self.menudict = {#build new dict in it's shoes
            "index":self.optionslist.pop(-1),
            "options":self.optionslist,
        }

        #call super i.e Menu() class to actually make self.menuframe
        super().__init__()

    def startPrompt(self, end_string):
        #runs prompt for functions until back is returned
        exitcode = False
        while(exitcode != True):
            exitcode = self.getValidMenuOption(end_string) #find function to execute and try to execute it
            if not exitcode: #if not False 
                break #break out with exitcode == False so will just drop out of this prompt
            else:
                break

        return exitcode

class FuncMenu(Menu):
    #class for selecting from a list of functions
    """MENUDICT TEMPLATE"""
    # self.menudict = {
    #     "option1":self.func1,
    #     "option2":self.func2,
    #     "option3":self.func3,
    #     "option4":self.func4,
    #     "index":np.array(),
    # }
    def __init__(self):
        self.menutype = "functions" 
        self.optionslist = []
        self.functionslist = []
        self.style = "github"
        # build dataframe dictionary
        for key, value in self.menudict.items():
            #cycle through all items in dict that decendant set up
            if key == "index": #once end of self.menudict has been reached
                self.menudict = {#build new dict in it's shoes
                    "options":self.optionslist,
                    "functions":self.functionslist,
                    "index":value,}
                break
            self.optionslist.append(key)
            self.functionslist.append(value)
        #call super i.e Menu() class to actually make self.menuframe
        super().__init__()
    
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
                exitcode = self.getValidMenuOption(string_in) #find function to execute and try to execute it
                exitcode = exitcode()
                self.returnFunc()
            except: #if hit this, that means we recieved "quit", or "back"
                if not exitcode: #if not False we will back out instead of quitting
                    break #break out with exitcode == False so will just drop out of this prompt

        self.exitFunc()
        return exitcode
