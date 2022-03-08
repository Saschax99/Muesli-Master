#Import all the necessary libraries
import customtkinter
from tkinter import Label, Frame, CENTER, LEFT, RIGHT
from config import *
import math
from ui_functions import UiFunc

class InitializeTopLevelTkWindow:
    def __init__(self, master):
        self.master = master

        #region MAIN SETTINGS AND BACKGROUND
        master.title("Einstellungen")
        master.geometry("800x480") #Define the size of the tkinter frame
        master.attributes("-fullscreen", False)
        #master.attributes('-alpha',0.85) # transparent
        self.bg = Label(master, bg = BACKGROUND_COLOR, width = 800, height = 480) # background color
        self.bg.place(x=0, y =0)
        #endregion

        InitializeTopLevelTkWindow.loadTopBar(self, master)

        InitializeTopLevelTkWindow.container(self, master)

        InitializeTopLevelTkWindow.loadBottomBar(self, master)

        UiFunc.CheckboxStartup(self)

    def loadTopBar(self, master):
        self.top_frame = Frame(master, 
                               height=40, 
                               width=800, 
                               bg=BACKGROUND_COLOR_BORDERS)
        self.top_frame.place(x=BORDER_TOP_X,y=BORDER_TOP_Y)


        Frame(master,
              height=3,
              width=800,
              bg="#725eba").place(x=0, y=40)
        # title name
        self.top_name = Label(self.top_frame, 
                              text="Einstellungen",
                              bg=BACKGROUND_COLOR_BORDERS, 
                              fg="white",
                              width=12, 
                              font=(TEXT_FONT, TITLE_FONTSIZE)) 
        self.top_name.place(x=30, y=5)

        self.button_back = customtkinter.CTkButton(master=self.top_frame, 
                                                   text="Zurück", 
                                                   compound="right", 
                                                   text_font=(TEXT_FONT, STANDARD_FONTSIZE), 
                                                   text_color="white", 
                                                   bg_color=BACKGROUND_COLOR_BORDERS,
                                                   fg_color=BUTTON_COLOR_BORDERS,
                                                   hover_color=BUTTON_HOVER_COLOR_BORDERS,
                                                   command=lambda: InitializeTopLevelTkWindow.closeTopLevel(self))
        self.button_back.place(x=722, y=20, anchor=CENTER)


    def container(self, master):
        InitializeTopLevelTkWindow.create_container_shadow(master, 
                                                           width = CONTAINER_SLIDER_WIDTH, 
                                                           height = CONTAINER_SLIDER_HEIGHT, 
                                                           color = CONTAINER_SHADOW_COLOR,
                                                           posx = CONTAINER_SLIDER_POSITION_X, 
                                                           posy = CONTAINER_SLIDER_POSITION_Y)

        self.container_sliders = customtkinter.CTkFrame(master=master,
                                                        width=CONTAINER_SLIDER_WIDTH,
                                                        height=CONTAINER_SLIDER_HEIGHT,
                                                        corner_radius=5,
                                                        fg_color="white")
        self.container_sliders.place(x=CONTAINER_SLIDER_POSITION_X, y=CONTAINER_SLIDER_POSITION_Y)

        config = UiFunc.readConfigFile()
        #region container 1
        self.container_1_checkbox = customtkinter.CTkButton(self.container_sliders,
                                                            width=32,
                                                            height=32,
                                                            fg_color=BACKGROUND_COLOR_BUTTON,
                                                            bg_color="black",
                                                            hover_color=None,
                                                            border_color="black",
                                                            corner_radius=7,
                                                            text="")
        self.container_1_checkbox.place(x=25, y=25)
        self.container_1_checkbox.configure(command = lambda: UiFunc.switchCheckboxState(self.container_1_checkbox, 1))    


        self.slider_container_1_name = Label(self.container_sliders, 
                                      text=config.get("c1", "name"),
                                      bg="white", 
                                      width=16, 
                                      font=(TEXT_FONT, TITLE_FONTSIZE)) 
        self.slider_container_1_name.place(x=0 + 145, y=6) 
        self.container_title_kcal_ref_coords = self.slider_container_1_name.place_info()

        customtkinter.CTkFrame(master=self.container_sliders,
                               width=self.slider_container_1_name.winfo_reqwidth(),
                               height=2,
                               corner_radius=10,
                               fg_color=MATERIALS_LIGHT_BORDER).place(x=int(self.container_title_kcal_ref_coords.get("x")), y=int(self.container_title_kcal_ref_coords.get("y")) + 28)

        self.slider_kcal = customtkinter.CTkSlider(master=self.container_sliders,
                                                   width=200,
                                                   height=25,
                                                   border_width=5,
                                                   from_=0,
                                                   to=100,
                                                   number_of_steps=100,
                                                   bg_color="white",
                                                   progress_color = CONTAINER_SHADOW_COLOR,
                                                   command = self.refreshKcalSlider) # no need for arg to  work
        self.slider_kcal.place(x=int(self.container_title_kcal_ref_coords.get("x")) - 9, y=int(self.container_title_kcal_ref_coords.get("y")) + 40)

        self.slider_kcal_max = Label(self.container_sliders, 
                                      text="0%",
                                      bg="white", 
                                      width=4, 
                                      justify=RIGHT,
                                      anchor="e",
                                      font=(TEXT_FONT, 8)) 
        self.slider_kcal_max.place(x=int(self.container_title_kcal_ref_coords.get("x")) - 39, y=int(self.container_title_kcal_ref_coords.get("y")) + 43) 

        self.slider_kcal_min = Label(self.container_sliders, 
                                      text="100%",
                                      bg="white", 
                                      width=5, 
                                      justify=LEFT,
                                      anchor="w",
                                      font=(TEXT_FONT, 8)) 
        self.slider_kcal_min.place(x=int(self.container_title_kcal_ref_coords.get("x")) + 191, y=int(self.container_title_kcal_ref_coords.get("y")) + 43) 
        #endregion container 1

        customtkinter.CTkFrame(master=self.container_sliders,
                               width=self.container_sliders.winfo_reqwidth(),
                               height=2,
                               corner_radius=10,
                               fg_color=MATERIALS_STANDARD_BORDER).place(x=0, y=82)

        #region container 2
        self.container_2_checkbox = customtkinter.CTkButton(self.container_sliders,
                                                            width=32,
                                                            height=32,
                                                            fg_color=BACKGROUND_COLOR_BUTTON,
                                                            bg_color="black",
                                                            hover_color=None,
                                                            border_color="black",
                                                            corner_radius=7,
                                                            text="")
        self.container_2_checkbox.place(x=25, y=25 + 82)
        self.container_2_checkbox.configure(command = lambda: UiFunc.switchCheckboxState(self.container_2_checkbox, 2))    

        self.slider_fat_name = Label(self.container_sliders, 
                                      text=config.get("c2", "name"),
                                      bg="white", 
                                      width=16, 
                                      font=(TEXT_FONT, TITLE_FONTSIZE)) 
        self.slider_fat_name.place(x=0 + 145, y=90) 
        self.container_title_fat_ref_coords = self.slider_fat_name.place_info()

        customtkinter.CTkFrame(master=self.container_sliders,
                               width=self.slider_fat_name.winfo_reqwidth(),
                               height=2,
                               corner_radius=10,
                               fg_color=MATERIALS_LIGHT_BORDER).place(x=int(self.container_title_fat_ref_coords.get("x")), y=int(self.container_title_fat_ref_coords.get("y")) + 28)


        self.slider_fat = customtkinter.CTkSlider(master=self.container_sliders,
                                                   width=200,
                                                   height=25,
                                                   border_width=5,
                                                   from_=0,
                                                   to=100,
                                                   number_of_steps=100,
                                                   bg_color="white",
                                                   progress_color = CONTAINER_SHADOW_COLOR,
                                                   command = self.refreshFatSlider) # no need for arg to  work
        self.slider_fat.place(x=int(self.container_title_fat_ref_coords.get("x")) - 9, y=int(self.container_title_fat_ref_coords.get("y")) + 40)

        self.slider_fat_max = Label(self.container_sliders, 
                                      text="0%",
                                      bg="white", 
                                      width=4, 
                                      justify=RIGHT,
                                      anchor="e",
                                      font=(TEXT_FONT, 8)) 
        self.slider_fat_max.place(x=int(self.container_title_fat_ref_coords.get("x")) - 39, y=int(self.container_title_fat_ref_coords.get("y")) + 43) 

        self.slider_fat_min = Label(self.container_sliders, 
                                      text="100%",
                                      bg="white", 
                                      width=5, 
                                      justify=LEFT,
                                      anchor="w",
                                      font=(TEXT_FONT, 8)) 
        self.slider_fat_min.place(x=int(self.container_title_fat_ref_coords.get("x")) + 191, y=int(self.container_title_fat_ref_coords.get("y")) + 43) 
        #endregion container 2



        customtkinter.CTkFrame(master=self.container_sliders,
                               width=self.container_sliders.winfo_reqwidth(),
                               height=2,
                               corner_radius=10,
                               fg_color=MATERIALS_STANDARD_BORDER).place(x=0, y=166)

        #region container 3
        self.container_3_checkbox = customtkinter.CTkButton(self.container_sliders,
                                                            width=32,
                                                            height=32,
                                                            fg_color=BACKGROUND_COLOR_BUTTON,
                                                            bg_color="black",
                                                            hover_color=None,
                                                            border_color="black",
                                                            corner_radius=7,
                                                            text="")
        self.container_3_checkbox.place(x=25, y=25 + 166)
        self.container_3_checkbox.configure(command = lambda: UiFunc.switchCheckboxState(self.container_3_checkbox, 3))    

        self.slider_sugar_name = Label(self.container_sliders, 
                                      text=config.get("c3", "name"),
                                      bg="white", 
                                      width=16, 
                                      font=(TEXT_FONT, TITLE_FONTSIZE)) 
        self.slider_sugar_name.place(x=0 + 145, y=174) 
        self.container_title_sugar_ref_coords = self.slider_sugar_name.place_info()

        customtkinter.CTkFrame(master=self.container_sliders,
                               width=self.slider_sugar_name.winfo_reqwidth(),
                               height=2,
                               corner_radius=10,
                               fg_color=MATERIALS_LIGHT_BORDER).place(x=int(self.container_title_sugar_ref_coords.get("x")), y=int(self.container_title_sugar_ref_coords.get("y")) + 28)

        self.slider_sugar = customtkinter.CTkSlider(master=self.container_sliders,
                                                   width=200,
                                                   height=25,
                                                   border_width=5,
                                                   from_=0,
                                                   to=100,
                                                   number_of_steps=100,
                                                   bg_color="white",
                                                   progress_color = CONTAINER_SHADOW_COLOR,
                                                   command = self.refreshSugarSlider) # no need for arg to  work
        self.slider_sugar.place(x=int(self.container_title_sugar_ref_coords.get("x")) - 9, y=int(self.container_title_sugar_ref_coords.get("y")) + 40)

        self.slider_sugar_max = Label(self.container_sliders, 
                                      text="0%",
                                      bg="white", 
                                      width=4, 
                                      justify=RIGHT,
                                      anchor="e",
                                      font=(TEXT_FONT, 8)) 
        self.slider_sugar_max.place(x=int(self.container_title_sugar_ref_coords.get("x")) - 39, y=int(self.container_title_sugar_ref_coords.get("y")) + 43) 

        self.slider_sugar_min = Label(self.container_sliders, 
                                      text="100%",
                                      bg="white", 
                                      width=5, 
                                      justify=LEFT,
                                      anchor="w",
                                      font=(TEXT_FONT, 8)) 
        self.slider_sugar_min.place(x=int(self.container_title_sugar_ref_coords.get("x")) + 191, y=int(self.container_title_sugar_ref_coords.get("y")) + 43) 
        #endregion container 3


        

        # config = UiFunc.readConfigFile()
        # config.get("c1", "name")


    def loadBottomBar(self, master):
        Frame(master, 
              height=25, 
              width=800, 
              bg=BACKGROUND_COLOR_BORDERS).place(x=BORDER_BOT_X,y=BORDER_BOT_Y)
        Frame(master,
            height=3,
            width=800,
            bg="#725eba").place(x=0, y=452)


    def create_container_shadow(master, width, height, color, posx, posy):
        customtkinter.CTkFrame(master=master,
                               width=width + 1,
                               height=height + 1,
                               corner_radius = 3,
                               fg_color = color).place(x=posx - 2, y=posy - 2)   


    def calculateSliderValues(self):
        config = UiFunc.readConfigFile()
        main_supply = int(config.get("portionsettings", "main_supply_container"))
        if main_supply == 1: # container 1
            kcal = int(config.get("c1", "kcal"))
            fat = int(config.get("c1", "fat"))
            sugar = int(config.get("c1", "sugar"))

        elif main_supply == 2: # container 2
            kcal = int(config.get("c2", "kcal"))
            fat = int(config.get("c2", "fat"))
            sugar = int(config.get("c2", "sugar"))

        refill_kcal = int(config.get("c3", "kcal")) # container 3
        refill_fat = int(config.get("c3", "fat"))
        refill_sugar = int(config.get("c3", "sugar"))


        slider_kcal = self.slider_kcal.value
        slider_fat = self.slider_fat.value
        slider_sugar = self.slider_sugar.value
        # define min and max at beginning of toplevel load !!!!!!!!!!!!!!!!!!!
        result_kcal = round((slider_kcal * kcal) + (refill_kcal * (1 - slider_kcal)), 1)
        result_fat = round((slider_fat * fat) + (refill_fat * (1 - slider_fat)), 1)
        result_sugar = round((slider_sugar * sugar) + (refill_sugar * (1 - slider_sugar)), 1)

        self.slider_container_1_name.configure(text= str(result_kcal) + " Kcal auf 100g")
        self.slider_fat_name.configure(text= str(result_fat) + " Fett auf 100g")
        self.slider_sugar_name.configure(text= str(result_sugar) + " Zucker auf 100g")
        #0,2 * 25 + 5 * (1- 0,2)

    def refreshKcalSlider(self, value):
        InitializeTopLevelTkWindow.calculateSliderValues(self)

    def refreshFatSlider(self, value):
        InitializeTopLevelTkWindow.calculateSliderValues(self)

    def refreshSugarSlider(self, value):
        InitializeTopLevelTkWindow.calculateSliderValues(self)

    def closeTopLevel(self):
        #UiFunc.CheckboxStartup(self) ##################### DAS HIER SOLLTE NICHT UI TOPLEVEL AKTUALISIEREN SONDER UI MAIN
        self.master.destroy()