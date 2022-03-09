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

        UiFunc.resizeSlider(self)

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
                                                   command=lambda: UiFunc.closeTopLevel(self))
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
        self.container_title_container_1_ref_coords = self.slider_container_1_name.place_info()

        customtkinter.CTkFrame(master=self.container_sliders,
                               width=self.slider_container_1_name.winfo_reqwidth(),
                               height=2,
                               corner_radius=10,
                               fg_color=MATERIALS_LIGHT_BORDER).place(x=int(self.container_title_container_1_ref_coords.get("x")), y=int(self.container_title_container_1_ref_coords.get("y")) + 28)

        self.slider_container_1 = customtkinter.CTkSlider(master=self.container_sliders,
                                                   width=200,
                                                   height=25,
                                                   border_width=5,
                                                   from_=0,
                                                   to=100,
                                                   number_of_steps=100,
                                                   bg_color="white",
                                                   progress_color = CONTAINER_SHADOW_COLOR,
                                                   command = self.refreshContainer1Slider) # no need for arg to  work
        self.slider_container_1.place(x=int(self.container_title_container_1_ref_coords.get("x")) - 9, y=int(self.container_title_container_1_ref_coords.get("y")) + 40)

        self.slider_container_1_max = Label(self.container_sliders, 
                                      text="0%",
                                      bg="white", 
                                      width=4, 
                                      justify=RIGHT,
                                      anchor="e",
                                      font=(TEXT_FONT, 8)) 
        self.slider_container_1_max.place(x=int(self.container_title_container_1_ref_coords.get("x")) - 39, y=int(self.container_title_container_1_ref_coords.get("y")) + 43) 

        self.slider_container_1_min = Label(self.container_sliders, 
                                      text="100%",
                                      bg="white", 
                                      width=5, 
                                      justify=LEFT,
                                      anchor="w",
                                      font=(TEXT_FONT, 8)) 
        self.slider_container_1_min.place(x=int(self.container_title_container_1_ref_coords.get("x")) + 191, y=int(self.container_title_container_1_ref_coords.get("y")) + 43) 
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

        self.slider_container_2_name = Label(self.container_sliders, 
                                      text=config.get("c2", "name"),
                                      bg="white", 
                                      width=16, 
                                      font=(TEXT_FONT, TITLE_FONTSIZE)) 
        self.slider_container_2_name.place(x=0 + 145, y=90) 
        self.container_title_container_2_ref_coords = self.slider_container_2_name.place_info()

        customtkinter.CTkFrame(master=self.container_sliders,
                               width=self.slider_container_2_name.winfo_reqwidth(),
                               height=2,
                               corner_radius=10,
                               fg_color=MATERIALS_LIGHT_BORDER).place(x=int(self.container_title_container_2_ref_coords.get("x")), y=int(self.container_title_container_2_ref_coords.get("y")) + 28)


        self.slider_container_2 = customtkinter.CTkSlider(master=self.container_sliders,
                                                   width=200,
                                                   height=25,
                                                   border_width=5,
                                                   from_=0,
                                                   to=100,
                                                   number_of_steps=100,
                                                   bg_color="white",
                                                   progress_color = CONTAINER_SHADOW_COLOR,
                                                   command = self.refreshContainer2Slider) # no need for arg to  work
        self.slider_container_2.place(x=int(self.container_title_container_2_ref_coords.get("x")) - 9, y=int(self.container_title_container_2_ref_coords.get("y")) + 40)

        self.slider_container_2_max = Label(self.container_sliders, 
                                      text="0%",
                                      bg="white", 
                                      width=4, 
                                      justify=RIGHT,
                                      anchor="e",
                                      font=(TEXT_FONT, 8)) 
        self.slider_container_2_max.place(x=int(self.container_title_container_2_ref_coords.get("x")) - 39, y=int(self.container_title_container_2_ref_coords.get("y")) + 43) 

        self.slider_container_2_min = Label(self.container_sliders, 
                                      text="100%",
                                      bg="white", 
                                      width=5, 
                                      justify=LEFT,
                                      anchor="w",
                                      font=(TEXT_FONT, 8)) 
        self.slider_container_2_min.place(x=int(self.container_title_container_2_ref_coords.get("x")) + 191, y=int(self.container_title_container_2_ref_coords.get("y")) + 43) 
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

        self.slider_container_3_name = Label(self.container_sliders, 
                                      text=config.get("c3", "name"),
                                      bg="white", 
                                      width=16, 
                                      font=(TEXT_FONT, TITLE_FONTSIZE)) 
        self.slider_container_3_name.place(x=0 + 145, y=174) 
        self.container_title_container_3_ref_coords = self.slider_container_3_name.place_info()

        customtkinter.CTkFrame(master=self.container_sliders,
                               width=self.slider_container_3_name.winfo_reqwidth(),
                               height=2,
                               corner_radius=10,
                               fg_color=MATERIALS_LIGHT_BORDER).place(x=int(self.container_title_container_3_ref_coords.get("x")), y=int(self.container_title_container_3_ref_coords.get("y")) + 28)

        self.slider_container_3 = customtkinter.CTkSlider(master=self.container_sliders,
                                                   width=200,
                                                   height=25,
                                                   border_width=5,
                                                   from_=0,
                                                   to=100,
                                                   number_of_steps=100,
                                                   bg_color="white",
                                                   progress_color = CONTAINER_SHADOW_COLOR,
                                                   command = self.refreshContainer3Slider) # no need for arg to  work
        self.slider_container_3.place(x=int(self.container_title_container_3_ref_coords.get("x")) - 9, y=int(self.container_title_container_3_ref_coords.get("y")) + 40)

        self.slider_container_3_max = Label(self.container_sliders, 
                                      text="0%",
                                      bg="white", 
                                      width=4, 
                                      justify=RIGHT,
                                      anchor="e",
                                      font=(TEXT_FONT, 8)) 
        self.slider_container_3_max.place(x=int(self.container_title_container_3_ref_coords.get("x")) - 39, y=int(self.container_title_container_3_ref_coords.get("y")) + 43) 

        self.slider_container_3_min = Label(self.container_sliders, 
                                      text="100%",
                                      bg="white", 
                                      width=5, 
                                      justify=LEFT,
                                      anchor="w",
                                      font=(TEXT_FONT, 8)) 
        self.slider_container_3_min.place(x=int(self.container_title_container_3_ref_coords.get("x")) + 191, y=int(self.container_title_container_3_ref_coords.get("y")) + 43) 
        #endregion container 3


        
    def refreshContainer1Slider(self, value):
        UiFunc.calculateSliderValues(self)

    def refreshContainer2Slider(self, value):
        UiFunc.calculateSliderValues(self)

    def refreshContainer3Slider(self, value):
        UiFunc.calculateSliderValues(self)
        
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
