# def main():
    start = StartMenu()
    start.startPrompt("Please input a number.")

#     # print(df.shape)
#     print("Closing Main")
#     # training data split
#     # docs_train, docs_test, y_train, y_test = train_test_split(dataset.data, dataset.target, test_size=0.25, random_state=123)

# class StartMenu(mnus.FuncMenu):
#     #Class for start menu options
#     def __init__(self):
#         print("Welcome to the Smash Ultimate Tournament Data Builder!")
#         self.prompt = "SHOW ME YOUR MUs"
#         self.strflag = False
#         self.menudict = {
#             "Open a tournament.":self.startEditTmntMenu,
#             "Make a tournament.":self.startMakeTmntMenu,
#             "Rename tournament.":self.renameTmnt,
#             "Copy tournament.":self.copyTmnt,
#             "Search global matchups.":self.startGlobalMuMenu,
#             # "Edit global matchups.(dummy func)":self.editGlobalMUs,
#             "index":[],
#         }

#         super().__init__()

#     def startEditTmntMenu(self, tmnt_name, META):
#         # #print("hit startEditTmntMenu")
#         if META != None:
#             editTmnt = tmnt.EditTmntMenu(tmnt_name, META) #make menu for tournament
#             return editTmnt.startPrompt("Please input a number.")
#         else:
#             tmntMenu = tmnt.SelTmntMenu(self.prompt) #create tournament selection prompt
#             selection = tmntMenu.startPrompt("Please select a tournament.")# get the user's selection

#             if selection == True:
#                 return True
#             elif selection == False:
#                 return False
#             else:
#                 editTmnt = tmnt.EditTmntMenu(selection, None) #make menu for tournament
#                 return editTmnt.startPrompt("Please input a number.")

#     def startMakeTmntMenu(self):
#         makeTmnt = tmnt.MakeTmntMenu()
#         return makeTmnt.startPrompt("Please input a number.")

#     def renameTmnt(self):
#         selTmnt = tmnt.SelTmntMenu(self.prompt[:-1])
#         choice = selTmnt.startPrompt("Please select a tournament to rename.")
#         os.system(f"rename ./TMNTs/{choice}.tmnt ./TMNTs/{choice}-copy.tmnt" if os.name == 'nt' else f"mv ./TMNTs/{choice}.tmnt ./TMNTs/{choice}-copy.tmnt")
#         selTmnt.printMenu()
#         print(f"{choice} renamed.")

#         return False

#     def copyTmnt(self):
#         selTmnt = tmnt.SelTmntMenu(self.prompt[:-1])
#         choice = selTmnt.startPrompt("Please select a tournament to copy.")
#         os.system(f"copy ./TMNTs/{choice}.tmnt ./TMNTs/{choice}-copy.tmnt" if os.name == 'nt' else f"cp ./TMNTs/{choice}.tmnt ./TMNTs/{choice}-copy.tmnt")
#         selTmnt.printMenu()
#         print(f"{choice} copied.")

#         return False
    
#     def editGlobalMUs(self):
#         #print("hit editGlobalMUs")
#         return True

#     def startGlobalMuMenu(self):
#         #print("hit startGlobalMuMenu")
#         print("Recomputing META.tmnt")
#         meta = tmnt.Tmnt("META")
#         tmnts = meta.loadAllTmnts()
#         meta.sumAllTmnts(tmnts)
#         meta.saveDF()

#         self.startEditTmntMenu("META", meta);
#         return True

#     def exitFunc(self):
#         #print("hit startmenu exitFunc")
#         pass

#     def returnFunc(self):
#         # self.clearTerm()
#         #print("hit startmenu returnFunc")
#         self.printMenu()