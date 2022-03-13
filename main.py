
if __name__ == "__main__":
    from tkinter import Tk
    from ui_main import InitializeMainTkWindow
    from ui_functions import UiFunc

    root = Tk()
    
    my_gui = InitializeMainTkWindow(root) # load gui
    UiFunc.logging() # create file when not exists
    root.mainloop()