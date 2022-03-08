from tkinter import Toplevel
from ui_toplevel import InitializeTopLevelTkWindow

def openTopLevel(self):
        '''execute toplevel and open'''
        try:
            if not Toplevel.winfo_exists(self.toplevel): # if not exist create one
                self.toplevel = Toplevel()
                InitializeTopLevelTkWindow(self.toplevel)
                self.toplevel.mainloop()

        except AttributeError: # except if self.toplevel didnt created | if variable does not exists
            self.toplevel = Toplevel()
            InitializeTopLevelTkWindow(self.toplevel)
            self.toplevel.mainloop()