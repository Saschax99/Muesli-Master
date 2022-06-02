
if __name__ == "__main__":
    from tkinter import Tk
    from ui.ui_main import InitializeMainTkWindow
    from loggingsystem import logging
    from ui.ui_functions import UiFunc
    import sys
    
    # if not "win" in sys.platform:
    #     exec("export DISPLAY=:0.0") # export display for tkinter with 7inch display
        
    root = Tk()
    
    my_gui = InitializeMainTkWindow(root) # load gui
    logging() # create file when not exists
    UiFunc.startReedSensorThread(main_instance=my_gui) # reed sensor
    # UiFunc.startDistanceSensorThread(main_instance=my_gui)
    root.mainloop()