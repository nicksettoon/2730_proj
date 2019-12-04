import pandas as pd

class Menu():
    def __init__(self, prompt_string, option_list, function_list):
        self.prompt = prompt_string 
        self.optionlist = option_list
        self.functionlist = function_list
        self.makeMenu()
    
    def makeMenu(self):
        options = pd.Series(self.optionlist)
        functions = pd.Series(self.functionlist)
        menudict = {
            "options":options,
            "functions":functions
        }
        self.menu = pd.DataFrame(menudict)
        self.menu.index += 1

    def printMenu(self):
        for i, option in enumerate(self.menu.iloc[0:, 0]):
            print(f"{i+1}. {option}")

    def getMethod(self, argument):
        try:
            method = self.menu['functions'][argument]
            return method
        except:
            print(f"{argument} is not a valid option. Please pick a valid option.")
            return None

    def promptLoop(self):
        method = None
        while(method == None):
            self.printMenu()
            inpt = input(self.prompt)
            try:
                method = self.getMethod(int(inpt))
            except ValueError:
                print("Invalid input. Please input a number.")
                method = None
        return method