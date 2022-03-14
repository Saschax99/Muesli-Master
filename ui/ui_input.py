#Import all the necessary libraries
import customtkinter
from tkinter import Label, Frame, CENTER, LEFT, Toplevel, END
from config.config import *
from ui.ui_functions import UiFunc

class InputLevel:
    def __init__(self,
                c_name,
                c_count,
                instance):

        height = WINDOW_HEIGHT
        width = WINDOW_WIDTH
        self.c_name = c_name
        self.c_count = c_count
        self.instance = instance
        self.top = Toplevel()

        #region MAIN SETTINGS AND BACKGROUND
        self.top.title("Einstellungen")
        self.top.geometry(f"{width}x{height}") #Define the size of the tkinter frame
        self.top.attributes("-fullscreen", False)
        #master.attributes('-alpha',0.85) # transparent
        self.bg = Label(self.top, bg = WINDOW_BG_COLOR, width = WINDOW_WIDTH, height = WINDOW_HEIGHT) # background color
        self.bg.place(x=0, y =0)

        self.top.resizable(False, False)
        self.top.lift()
        self.top.focus_force()
        self.top.grab_set()


        #endregion

        InputLevel.loadTopBar(self)

        InputLevel.container(self)

        InputLevel.loadBottomBar(self)

        InputLevel.loadContainerValues(self)

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
                                                   command=lambda: UiFunc.closeTopLevel(self))
        self.button_back.place(x=722, y=20, anchor=CENTER)


    def container(self):
        InputLevel.create_container_shadow(self.top, # SHADOW
                                        width = CONTAINER_UI_INPUT_WIDTH, 
                                        height = CONTAINER_UI_INPUT_HEIGHT, 
                                        color = CONTAINER_SHADOW_COLOR,
                                        posx = CONTAINER_UI_INPUT_POSITION_X, 
                                        posy = CONTAINER_UI_INPUT_POSITION_Y)

        self.container_input = customtkinter.CTkFrame(master=self.top, # CONTAINER
                                                        width=CONTAINER_UI_INPUT_WIDTH,
                                                        height=CONTAINER_UI_INPUT_HEIGHT,
                                                        corner_radius=5,
                                                        fg_color="white")
        self.container_input.place(x=CONTAINER_UI_INPUT_POSITION_X, y=CONTAINER_UI_INPUT_POSITION_Y)


        self.container_input_name = Label(self.container_input, # NAME OF CONTAINER
                                      text=self.c_name,
                                      bg="white", 
                                      width=16, 
                                      font=(TEXT_FONT, TITLE_FONTSIZE)) 
        self.container_input_name.place(x=(self.container_input.winfo_reqwidth() / 4) + 10, y=5) 

        customtkinter.CTkFrame(master=self.container_input, # BORDER
                               width=self.container_input.winfo_reqwidth() / 2,
                               height=2,
                               corner_radius=10,
                               fg_color=ACCENTS_BG_COLOR).place(x=self.container_input.winfo_reqwidth() / 4, y=35)

        self.container_name = Label(self.container_input, # NAME OF ENTRY
                                      text="Name",
                                      bg="white", 
                                      width=5, 
                                      justify=LEFT,
                                      anchor="w",
                                      font=(TEXT_FONT, SMALL_FONTSIZE)) 
        self.container_name.place(x=40, y=46) 

        self.entry_name = customtkinter.CTkEntry(master=self.container_input, # ENTRY NAME
                                                placeholder_text="Container Name..", 
                                                text_font=(TEXT_FONT, STANDARD_FONTSIZE),
                                                placeholder_text_color="white",
                                                text_color="white",
                                                bg_color="white",
                                                fg_color=TEXT_BORDER_COLOR,
                                                corner_radius=8,
                                                width=300)
        self.entry_name.place(x=40, y=67)

        customtkinter.CTkFrame(master=self.container_input, # BORDER 2
                               width=self.container_input.winfo_reqwidth(),
                               height=2,
                               corner_radius=10,
                               fg_color=ACCENTS_BG_COLOR).place(x=0, y=112)


        self.container_kcal = Label(self.container_input, # NAME OF ENTRY
                                      text="Kcal",
                                      bg="white", 
                                      width=5, 
                                      justify=LEFT,
                                      anchor="w",
                                      font=(TEXT_FONT, SMALL_FONTSIZE)) 
        self.container_kcal.place(x=40, y=123) 

        self.entry_kcal = customtkinter.CTkEntry(master=self.container_input, # ENTRY KCAL
                                                placeholder_text="Kcal..", 
                                                text_font=(TEXT_FONT, STANDARD_FONTSIZE),
                                                placeholder_text_color="white",
                                                text_color="white",
                                                bg_color="white",
                                                fg_color=TEXT_BORDER_COLOR,
                                                corner_radius=8,
                                                width=300)
        self.entry_kcal.place(x=40, y=144)

        customtkinter.CTkFrame(master=self.container_input, # BORDER 3
                               width=self.container_input.winfo_reqwidth(),
                               height=2,
                               corner_radius=10,
                               fg_color=ACCENTS_BG_COLOR).place(x=0, y=189)


        self.container_fat = Label(self.container_input, # NAME OF ENTRY
                                      text="Fett",
                                      bg="white", 
                                      width=5, 
                                      justify=LEFT,
                                      anchor="w",
                                      font=(TEXT_FONT, SMALL_FONTSIZE)) 
        self.container_fat.place(x=40, y=200) 

        self.entry_fat = customtkinter.CTkEntry(master=self.container_input, # ENTRY FAT
                                                placeholder_text="Fett..", 
                                                text_font=(TEXT_FONT, STANDARD_FONTSIZE),
                                                placeholder_text_color="white",
                                                text_color="white",
                                                bg_color="white",
                                                fg_color=TEXT_BORDER_COLOR,
                                                corner_radius=8,
                                                width=300)
        self.entry_fat.place(x=40, y=221)

        customtkinter.CTkFrame(master=self.container_input, # BORDER 4
                               width=self.container_input.winfo_reqwidth(),
                               height=2,
                               corner_radius=10,
                               fg_color=ACCENTS_BG_COLOR).place(x=0, y=266)



        self.container_sugar = Label(self.container_input, # NAME OF ENTRY
                                      text="Zucker",
                                      bg="white", 
                                      width=5, 
                                      justify=LEFT,
                                      anchor="w",
                                      font=(TEXT_FONT, SMALL_FONTSIZE)) 
        self.container_sugar.place(x=40, y=277) 

        self.entry_sugar = customtkinter.CTkEntry(master=self.container_input, # ENTRY SUGAR
                                                placeholder_text="Zucker..", 
                                                text_font=(TEXT_FONT, STANDARD_FONTSIZE),
                                                placeholder_text_color="white",
                                                text_color="white",
                                                bg_color="white",
                                                fg_color=TEXT_BORDER_COLOR,
                                                corner_radius=8,
                                                width=300)
        self.entry_sugar.place(x=40, y=297)


        self.button_save = customtkinter.CTkButton(master=self.top, 
                                           text="Speichern", 
                                           width=200, 
                                           height=35,
                                           text_color="white", 
                                           fg_color=BUTTON_BG_COLOR,
                                           bg_color=WINDOW_BG_COLOR,
                                           hover_color=BUTTON_HOVER_BG_COLOR,
                                           text_font=(TEXT_FONT, TITLE_FONTSIZE), 
                                           command=lambda: InputLevel.Save(self))
        self.button_save.place(x=400, y=427, anchor=CENTER)

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

    
    def Save(self):
        UiFunc.writeConfigFile("c"+ str(self.c_count), "name", str(self.entry_name.get()))
        UiFunc.writeConfigFile("c"+ str(self.c_count), "kcal", str(self.entry_kcal.get()))
        UiFunc.writeConfigFile("c"+ str(self.c_count), "fat", str(self.entry_fat.get()))
        UiFunc.writeConfigFile("c"+ str(self.c_count), "sugar", str(self.entry_sugar.get()))

        if self.c_count == 1:
            self.instance.container_1_settings.configure(text=str(self.entry_name.get()))
        if self.c_count == 2:
            self.instance.container_2_settings.configure(text=str(self.entry_name.get()))
        if self.c_count == 3:
            self.instance.container_3_settings.configure(text=str(self.entry_name.get()))
            
        UiFunc.closeTopLevel(self)


    def loadContainerValues(self):
        config = UiFunc.readConfigFile()
        self.entry_name.insert(END, config.get("c"+ str(self.c_count), "name"))
        self.entry_kcal.insert(END, config.get("c"+ str(self.c_count), "kcal"))
        self.entry_fat.insert(END, config.get("c"+ str(self.c_count), "fat"))
        self.entry_sugar.insert(END, config.get("c"+ str(self.c_count), "sugar"))