import customtkinter
from tkinter import Label, Frame, CENTER, Toplevel
from config.config import *
from ui.ui_functions import UiFunc
from ui.ui_input import InputLevel

class TLevel:
    def __init__(self,
                instance):

        self.instance = instance

        height = WINDOW_HEIGHT
        width = WINDOW_WIDTH
        self.top = Toplevel()
        #region MAIN SETTINGS AND BACKGROUND
        self.top.title("Einstellungen")
        self.top.geometry(f"{width}x{height}") #Define the size of the tkinter frame
        self.top.attributes("-fullscreen", False)
        #master.attributes('-alpha',0.85) # transparent
        self.bg = Label(self.top, bg = WINDOW_BG_COLOR, width = WINDOW_WIDTH, height = WINDOW_HEIGHT) # background color
        self.bg.place(x=0, y =0)

        self.top.resizable(False, False)
        # self.top.lift()
        # self.top.focus_force()
        # self.top.grab_set() # maybe add later


        #endregion

        TLevel.loadTopBar(self)

        TLevel.container(self)

        TLevel.loadBottomBar(self)

        TLevel.updateContainerNames(self)

    def loadTopBar(self):
        self.top_frame = Frame(self.top, 
                               height=40, 
                               width=800, 
                               bg=TOP_BORDER_BG_COLOR)
        self.top_frame.place(x=BORDER_TOP_X,y=BORDER_TOP_Y)


        Frame(self.top,
              height=3,
              width=800,
              bg=BORDER_ACCENTS_BG_COLOR).place(x=0, y=40)
        # title name
        self.top_name = Label(self.top_frame, 
                              text="Einstellungen",
                              bg=TOP_BORDER_BG_COLOR, 
                              fg="white",
                              width=12, 
                              font=(TEXT_FONT, TITLE_FONTSIZE)) 
        self.top_name.place(x=30, y=5)

        self.button_back = customtkinter.CTkButton(master=self.top_frame, 
                                                   text="Zurück", 
                                                   compound="right", 
                                                   text_font=(TEXT_FONT, STANDARD_FONTSIZE), 
                                                   text_color="white", 
                                                   bg_color=TOP_BORDER_BG_COLOR,
                                                   fg_color=BUTTON_BG_COLOR,
                                                   hover_color=BUTTON_HOVER_BG_COLOR,
                                                   command=lambda: UiFunc.closeTopLevel(self, self.instance))
        self.button_back.place(x=722, y=20, anchor=CENTER)

    def container(self):        
        TLevel.create_container_shadow(self.top, 
                                        width = CONTAINER_UI_SETTINGS_WIDTH, 
                                        height = CONTAINER_UI_SETTINGS_HEIGHT, 
                                        color = CONTAINER_SHADOW_COLOR,
                                        posx = 276, 
                                        posy = 114)

        self.container_1 = customtkinter.CTkFrame(master=self.top,
                                                        width=CONTAINER_UI_SETTINGS_WIDTH,
                                                        height=CONTAINER_UI_SETTINGS_HEIGHT,
                                                        corner_radius=5,
                                                        fg_color="white")
        self.container_1.place(x=276, y=114)

        #region container 1

        self.container_1_settings = customtkinter.CTkButton(master=self.container_1, # BUTTON 1 CONTAINER
                                                        text="x", 
                                                        width=217,
                                                        height=50,
                                                        fg_color=BUTTON_BG_COLOR,
                                                        text_color="white",
                                                        text_font=(TEXT_FONT, TITLE_FONTSIZE),
                                                        hover_color=BUTTON_HOVER_BG_COLOR,
                                                        command=lambda: TLevel.openEditor(self, 1))
        self.container_1_settings.place(x=16, y=16) 
        #endregion container 1

        customtkinter.CTkFrame(master=self.container_1,
                               width=self.container_1.winfo_reqwidth(),
                               height=2,
                               corner_radius=10,
                               fg_color=ACCENTS_BG_COLOR).place(x=0, y=82)

        #region container 2
        self.container_2_settings = customtkinter.CTkButton(master=self.container_1, 
                                                        text="x", 
                                                        width=217,
                                                        height=50,
                                                        fg_color=BUTTON_BG_COLOR,
                                                        text_color="white",
                                                        text_font=(TEXT_FONT, TITLE_FONTSIZE),
                                                        hover_color=BUTTON_HOVER_BG_COLOR,
                                                        command=lambda: TLevel.openEditor(self, 2))
        self.container_2_settings.place(x=16, y=100) 
        #endregion container 2



        customtkinter.CTkFrame(master=self.container_1,
                               width=self.container_1.winfo_reqwidth(),
                               height=2,
                               corner_radius=10,
                               fg_color=ACCENTS_BG_COLOR).place(x=0, y=166)

        #region container 3
        self.container_3_settings = customtkinter.CTkButton(master=self.container_1, 
                                                        text="x", 
                                                        width=217,
                                                        height=50,
                                                        fg_color=BUTTON_BG_COLOR,
                                                        text_color="white",
                                                        text_font=(TEXT_FONT, TITLE_FONTSIZE),
                                                        hover_color=BUTTON_HOVER_BG_COLOR,
                                                        command=lambda: TLevel.openEditor(self, 3))
        self.container_3_settings.place(x=16, y=184)         
        #endregion container 3

    def loadBottomBar(self):
        Frame(self.top, 
              height=25, 
              width=800, 
              bg=BOTTOM_BORDER_BG_COLOR).place(x=BORDER_BOT_X,y=BORDER_BOT_Y)
        Frame(self.top,
            height=3,
            width=800,
            bg=BORDER_ACCENTS_BG_COLOR).place(x=0, y=452)


    def create_container_shadow(master, width, height, color, posx, posy):
        customtkinter.CTkFrame(master=master,
                               width=width + 1,
                               height=height + 1,
                               corner_radius = 3,
                               fg_color = color).place(x=posx - 2, y=posy - 2)     


    def openEditor(self, container_count):
        config = UiFunc.readConfigFile()
        InputLevel(c_name=config.get("c"+str(container_count), "name"), c_count=container_count, instance=self) #parse instance to refresh textboxes

    def updateContainerNames(self):
        config = UiFunc.readConfigFile()
        self.container_1_settings.configure(text=config.get("c1", "name"))
        self.container_2_settings.configure(text=config.get("c2", "name"))
        self.container_3_settings.configure(text=config.get("c3", "name"))
