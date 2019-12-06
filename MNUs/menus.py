#EXTERNAL IMPORTS#
import pandas as pd
import numpy as np
import os
from tabulate import tabulate
#CUSTOM IMPORTS#

class BaseMenu():
    #base class for initial menu setup
    def __init__(self, string_in):
        self.prompt = string_in + ">" #set prompt
        #decide if quick codes should be used or not based on terminal height
        #set up help menu helpmenu
        self.helpmenu = {
            "list":['Reprints menu.','list','ll','ls','l'],
            "back":['Go to prev menu.','back','bk','b'],
            "quit":['Saves progress and closes program.','quit','exit','qt', 'q'],
            "clear":['Clears screen.','clear','cl','c'],
            "help":['Prints this list.','help','?','man','h'],
        }
    
    def printHelp(self):
        #prints help menu information
        print("\nCommands available at and prompt:\n")
        for cmd, alias in self.helpmenu.items():
            print(f"{cmd}\t{alias[0]}")

        print("You can use the following commands:\n")
        for cmd, alias in self.helpmenu.items():
            print(f"{cmd}: {alias[1:]}")

    def getTermSize(self):
        #gets size of terminal for __init__()
        if os.name == 'nt':
            from ctypes import windll, create_string_buffer
            # stdin handle is -10
            # stdout handle is -11
            # stderr handle is -12

            h = windll.kernel32.GetStdHandle(-12)
            csbi = create_string_buffer(22)
            res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)

            if res:
                import struct
                (bufx, bufy, curx, cury, wattr,
                left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
                sizex = right - left + 1
                sizey = bottom - top + 1
            else:
                sizex, sizey = 80, 25 # can't determine actual size - return default values

            return [sizex, sizey]
        else:
            try:
                rows, columns = os.get_terminal_size(0)
            except OSError:
                rows, columns = os.get_terminal_size(1)
            return [rows, columns]

    def genQuickCodes(self):
        #gets a numpy array of short prefixes of the menu's options to use as index
        quickcodes = []
        taglist = []
        for char in self.optionslist:
            newchar = char.replace("_","")
            newchar = newchar.replace("-","")
            newchar = newchar.replace(" ","")
            tag = newchar[:4].lower()
            i=1
            while(tag in taglist):
                tag = newchar[:4+i].lower()
                i += 1
            taglist.append(tag)

        quickcodes = np.array(taglist)
        return quickcodes

    def clearTerm(self):
        #clears terminal
        os.system('cls' if os.name == 'nt' else 'clear')

    def basicIntLoop(self):
        #basic loop for ensuring user input is an integer.
        #for use outside of the complicated getValidMenuOption()
        usrinput = None
        while(usrinput == None):
            try:
                usrinput = int(input(self.prompt))
            except:
                print("Invalid input.")
                usrinput = None
        return usrinput

class Menu(BaseMenu):
    #base class for menuframe creation and printing
    def __init__(self):
        #sets up prompt string and creates the menu dataframe
        super().__init__(self.prompt)
        self.printmenu = True #instance variable to toggle printing of the menu options
        self.termshape = self.getTermSize()
        if len(self.optionslist) > self.termshape[1]//5: #if so
            self.menudict["index"] = self.genQuickCodes()
            self.strflag = True
            self.style = "grid"
        else:
            self.menudict["index"] = []
            self.strflag = False
            self.style = "fancy_grid"
        #create menu data frame
        mindex = self.menudict.pop("index", None)
        if mindex == []:
            self.menuframe = pd.DataFrame(self.menudict)
            self.menuframe.index += 1
        else:
            self.menuframe = pd.DataFrame(self.menudict, index=mindex)

        #clear terminal
        # self.clearTerm()

    def printMenu(self):
        self.printAnything(self.menuframe)
        pass

    def printAnything(self, orig_dataframe):
        # prints the current menu
        if not self.strflag:
            print(tabulate(orig_dataframe[['options']], showindex=True, tablefmt=self.style))
            return

        df = orig_dataframe[['options']].T
        orig_cols = np.array(df.columns).tolist()
        cols = orig_cols #make copy for calculations

        maxlen = 0
        for item in cols:
            frame = df[[item]]
            if len(frame.iat[0,0]) > maxlen:
                maxlen = len(frame.iat[0,0])
        # for index in cols:
        dictarray = []
        index = 0
        while(index < len(orig_cols)):
            workspace = self.termshape[0]
            printdict = {} #set printdict
            while(workspace > maxlen):
                try:
                    frame = df[[cols[index]]]
                    index += 1
                    printdict[frame.columns[0]] = [frame.iat[0,0]]
                    workspace -= (len(frame.iat[0,0])+3)
                except:
                    break
            dictarray.append(printdict)

        for dictionary in dictarray:
            print(tabulate(dictionary, headers="keys", tablefmt=self.style))

    def getValidMenuOption(self, string_in):
        #input validation loop making sure a given output is in the list of options for the menu instance
        #runs until user picks an option, then return
        output = None
        endstring = string_in + "\nType help for a list of commands."

        while(output == None):
            if self.printmenu:
                self.printMenu()
                self.printmenu = False
            print(endstring)
            endstring = string_in
            inpt = input(self.prompt)

            if inpt in self.helpmenu["list"][1:]:
                self.printmenu = True
                endstring = string_in 
                output = None
            elif inpt in self.helpmenu["help"][1:]:
                self.printHelp()
                output = None
            elif inpt in self.helpmenu["clear"][1:]:
                self.clearTerm()
                endstring = string_in
                output = None
            elif inpt in self.helpmenu["quit"][1:]:
                output = True
                break
            elif inpt in self.helpmenu["back"][1:]:
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
        self.menudict = {#build new dict in it's shoes
            "options":self.optionslist,
            "index":[],
        }

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
