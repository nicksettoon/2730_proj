import pandas as pd

class MenuBase():
    #base class for menus 
    def __init__(self, string_in):
        self.prompt = string_in

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



class Menu(MenuBase):
    #base class for basic menu creation and printing
    def __init__(self, prompt_in, menu_dict):
        #sets up prompt string and creates the menu dataframe
        self.prompt = prompt_in+">"
        self.menudict = menu_dict 
        self.menutype = ""
        self.menu = pd.DataFrame(self.menudict)
        self.menu.index += 1

    def printMenu(self):
        #prints the current menu
        self.printList(self.optionlist)

    def printLoop(self, orig_end, print_menu=True):
        #input validation loop making sure the user's input is an integer or "list", "back", "quit"
        selected = None
        endstring = orig_end + "\nType 'list' to print the list again."

        while(selected == None):
            if print_menu:
                # print("\n")
                self.printMenu()
                print_menu = False

            print(endstring)
            selected = input(self.prompt)

            if selected == "list":
                print_menu = True
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

    def getValidSelection(self, string_in, print_menu=True):
        #input validation loop making sure a given integer selection is in the list of options for the menu instance
        #runs until user picks an option, then returnthreshold
        selection = None
        endstring = string_in + "\nPlease enter a number from the list."
        while(selection == None):
            selection = self.printLoop(endstring, print_menu)
            if selection == "quit" or selection == "back":
                print("hit valid selection block")
                break
            try:
                item = self.getItem(selection)
                selection = item
            except:
                endstring = f"\n{selection} is not an option. Please pick a valid option."
                print_menu = False
                selection = None
        return selection

    def getItem(self, selection):
        #virtual function indended to be overwritten by inheriting functions
        return self.menu[self.menutype][selection]

    def promptLoop(self, string_in, print_menu=True):
        #runs getValidSelection until user selects, backs out, or quits program
        selection = None
        while(selection == None):
            selection = self.getValidSelection(string_in, print_menu)
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

    def startPrompt(self, string_in, print_menu=True):
        #runs prompt for functions until back is returned
        exitcode = False
        while(exitcode != True):
            exitcode = self.promptLoop(string_in, print_menu) #find function to execute and try to execute it
            if exitcode == "back": #if recieved "back" in the promptLoop
                exitcode = False
                break #just break out of this loop and end startPrompt call
            else:
                break
        # print(f"exitcode: {exitcode}")
        return exitcode

class FunctionMenu(Menu):
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

    def startPrompt(self, string_in, print_menu=True):
        #runs prompt for functions until back is returned
        exitcode = False
        while(exitcode != True):
            try:
                exitcode = self.promptLoop(string_in, print_menu) #find function to execute and try to execute it
                exitcode = exitcode()
            except: #if hit this, that means we recieved "quit", or "back"
                if exitcode == "back": #if recieved "back" in the promptLoop
                    exitcode = False
                    break #just break out of this loop and end startPrompt call
        # print(f"exitcode: {exitcode}")
        return exitcode