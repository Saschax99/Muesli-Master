
if __name__ == "__main__":
    from tkinter import Tk
    from ui.ui_main import InitializeMainTkWindow
    from ui.ui_functions import UiFunc
    from loggingsystem import logging

    root = Tk()
    
    my_gui = InitializeMainTkWindow(root) # load gui
    logging() # create file when not exists
    root.mainloop()