
if __name__ == "__main__":
    from tkinter import Tk
    from ui_main import InitializeMainTkWindow

    root = Tk()
    
    my_gui = InitializeMainTkWindow(root) # load gui
    root.mainloop()