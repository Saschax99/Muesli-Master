#Import all the necessary libraries
# https://www.raspberrypi-spy.co.uk/2017/11/how-to-rotate-the-raspberry-pi-display-output/#prettyPhoto
from matplotlib import container
import customtkinter
from tkinter import Label, Frame, CENTER, LEFT, RIGHT
from PIL import Image, ImageTk
from config import *
from ui_functions import UiFunc
from functions import openTopLevel

class InitializeMainTkWindow:
    def __init__(self, master):
        #region MAIN SETTINGS AND BACKGROUND
        master.title("Müsli-Master")
        master.geometry("800x480") #Define the size of the tkinter frame
        master.attributes("-fullscreen", False)
        #master.attributes('-alpha',0.85) # transparent
        self.bg = Label(master, bg = BACKGROUND_COLOR, width = 800, height = 480) # background color
        self.bg.place(x=0, y =0)
        #endregion
 
        #region LOADING IN
        InitializeMainTkWindow.loadTopBar(self, master)

        InitializeMainTkWindow.loadContainerLeft(self, master)

        InitializeMainTkWindow.loadContainerMiddle(self, master)

        InitializeMainTkWindow.loadContainerRight(self, master)

        InitializeMainTkWindow.loadPortionSize(self, master)

        InitializeMainTkWindow.loadNutritionalValues(self, master)

        InitializeMainTkWindow.loadBottomBar(self, master)        

        UiFunc.updateContainerValues(self)

        UiFunc.portionButtonStartup(self)
        UiFunc.CheckboxStartup(self)
        #UiFunc.writeConfigFile("c1", "kcal", "12341")

        #endregion LOADING IN

    def loadTopBar(self, master):
        self.top_frame = Frame(master, 
                               height=40, 
                               width=800, 
                               bg=BACKGROUND_TOP_COLOR_BORDERS)
        self.top_frame.place(x=BORDER_TOP_X,y=BORDER_TOP_Y)

        Frame(master,
              height=3,
              width=800,
              bg=BACKGROUND_BORDER_COLOR).place(x=0, y=40)

        # title name
        # self.top_name = Label(self.top_frame, 
        #                       text="Müsli-Master",
        #                       bg=BACKGROUND_COLOR_BORDERS, 
        #                       fg="white",
        #                       width=12, 
        #                       font=(TEXT_FONT, TITLE_FONTSIZE)) 
        # self.top_name.place(x=30, y=5)

        image = Image.open('pictures/logo.PNG')
        zoom = .19
        #multiple image size by zoom
        pixels_x, pixels_y = tuple([int(zoom * x)  for x in image.size])
        img = ImageTk.PhotoImage(image.resize((pixels_x, pixels_y))) 
        label = Label(self.top_frame, image=img, bg=BACKGROUND_TOP_COLOR_BORDERS)
        label.image = img
        label.place(x=0, y=-15)



        self.button_port_settings = customtkinter.CTkButton(master=self.top_frame, 
                                           text="Portionseinstellungen", 
                                           text_color="white", 
                                           bg_color=BACKGROUND_TOP_COLOR_BORDERS,
                                           fg_color=BACKGROUND_COLOR_BUTTON,
                                           hover_color=BUTTON_HOVER_COLOR_BORDERS,
                                           command=lambda: openTopLevel(self))
        self.button_port_settings.place(x=706, y=20, anchor=CENTER)

    def loadContainerLeft(self, master):
        # InitializeMainTkWindow.create_container_shadow(master, 
        #                                                 width = CONTAINER_WIDTH, 
        #                                                 height = CONTAINER_HEIGHT, 
        #                                                 color = CONTAINER_SHADOW_COLOR,
        #                                                 posx = CONTAINER_1_X, 
        #                                                 posy = CONTAINER_1_Y)

        # val = UiFunc.readConfigFile()
        # if int(val.get("portionsettings", "main_supply_container")) != 1:
        #     self.activated_container_border_1.place_forget()
        # else:
        #     self.activated_container_border_1.place(x=CONTAINER_1_X - 6, y=CONTAINER_1_Y - 6) 


        self.container_1 = customtkinter.CTkFrame(master=master,
                                                  width=CONTAINER_WIDTH,
                                                  height=CONTAINER_HEIGHT,
                                                  corner_radius=4,
                                                  fg_color="white")
        self.container_1.place(x=CONTAINER_1_X, y=CONTAINER_1_Y)

        self.border_container_1_1 = customtkinter.CTkFrame(master=self.container_1,
                                                           width=self.container_1.winfo_reqwidth(),
                                                           height=2,
                                                           corner_radius=10,
                                                           fg_color=MATERIALS_STANDARD_BORDER)
        self.border_container_1_1.place(x=30, y=40)

        self.container_1_name = Label(self.container_1,
                                      bg="white", 
                                      width=10, 
                                      font=(TEXT_FONT, TITLE_FONTSIZE),
                                      justify=LEFT,
                                      anchor="w")
        self.container_1_name.place(x=35 + 6, y=6) 


        self.container_1_checkbox = customtkinter.CTkButton(self.container_1,
                                                            width=25,
                                                            height=25,
                                                            fg_color=CHECKBOX_COLOR,
                                                            bg_color=CHECKBOX_COLOR,
                                                            hover_color=None,
                                                            border_color=CHECKBOX_COLOR,
                                                            corner_radius=7,
                                                            text="")
        self.container_1_checkbox.place(x=118 + 30, y=8)
        self.container_1_checkbox.configure(command = lambda: UiFunc.switchCheckboxState(self.container_1_checkbox, 1))


        self.container_1_kcal = Label(self.container_1, 
                                      text="xxx Kcal/100g",
                                      bg=self.container_1.fg_color, 
                                      width=14, 
                                      font=(TEXT_FONT, STANDARD_FONTSIZE)) 
        self.container_1_kcal.place(x=30 + 9, y=49) 

        self.border_container_1_2 = customtkinter.CTkFrame(master=self.container_1,
                                                           width=self.container_1.winfo_reqwidth(),
                                                           height=2,
                                                           corner_radius=10,
                                                           fg_color=MATERIALS_LIGHT_BORDER)
        self.border_container_1_2.place(x=30, y=79)

        self.container_1_fat = Label(self.container_1, 
                                     text="xx Fett/100g",
                                     bg=self.container_1.fg_color, 
                                     width=14, 
                                     font=(TEXT_FONT, STANDARD_FONTSIZE)) 
        self.container_1_fat.place(x=30 + 9, y=90) 

        self.border_container_1_3 = customtkinter.CTkFrame(master=self.container_1,
                                                           width=self.container_1.winfo_reqwidth(),
                                                           height=2,
                                                           corner_radius=10,
                                                           fg_color=MATERIALS_LIGHT_BORDER)
        self.border_container_1_3.place(x=30, y=118)

        self.container_1_sugar = Label(self.container_1, 
                                       text="xx Zucker/100g",
                                       bg=self.container_1.fg_color, 
                                       width=14, 
                                       font=(TEXT_FONT, STANDARD_FONTSIZE))
        self.container_1_sugar.place(x=30 + 9, y=127) 

        self.border_container_1_4 = customtkinter.CTkFrame(master=self.container_1,
                                                           width=self.container_1.winfo_reqwidth(),
                                                           height=2,
                                                           corner_radius=10,
                                                           fg_color=MATERIALS_STANDARD_BORDER)
        self.border_container_1_4.place(x=30, y=157)

        self.container_1_portion_amount = Label(self.container_1, 
                                               text="3/6",
                                               bg=self.container_1.fg_color, 
                                               width=12, 
                                               font=(TEXT_FONT, TITLE_FONTSIZE)) 
        self.container_1_portion_amount.place(x=30 + 6, y=165) 



        self.container_1_percents_bar = customtkinter.CTkProgressBar(self.container_1,
                                                                     width=150,
                                                                     height=5)
        self.container_1_percents_bar.place(x=30 + 5, y=195)
        self.container_1_percents_bar.set(0.65)

        self.button_container_1_dec = customtkinter.CTkButton(master=self.container_1, 
                                           text="-", 
                                           text_color="white", 
                                           height=200,
                                           width=30,
                                           text_font=(TEXT_FONT, TITLE_FONTSIZE + 1),
                                           bg_color=BACKGROUND_COLOR_BUTTON,
                                           fg_color=BACKGROUND_COLOR_BUTTON,
                                           hover_color=BUTTON_HOVER_COLOR_BORDERS)
        self.button_container_1_dec.place(x=0, y=0)


        self.button_container_1_inc = customtkinter.CTkButton(master=self.container_1, 
                                           text="+", 
                                           text_color="white", 
                                           height=200,
                                           width=27,
                                           text_font=(TEXT_FONT, TITLE_FONTSIZE + 1),
                                           bg_color=BACKGROUND_COLOR_BUTTON,
                                           fg_color=BACKGROUND_COLOR_BUTTON,
                                           hover_color=BUTTON_HOVER_COLOR_BORDERS)
        self.button_container_1_inc.place(x=185, y=0)

    def loadContainerMiddle(self, master):
        '''loading middle container'''
        self.container_2 = customtkinter.CTkFrame(master=master,
                                                  width=CONTAINER_WIDTH,
                                                  height=CONTAINER_HEIGHT,
                                                  corner_radius=4,
                                                  fg_color="white")
        self.container_2.place(x=CONTAINER_2_X, y=CONTAINER_2_Y)

        self.border_container_2_1 = customtkinter.CTkFrame(master=self.container_2,
                                                           width=self.container_2.winfo_reqwidth(),
                                                           height=2,
                                                           corner_radius=10,
                                                           fg_color=MATERIALS_STANDARD_BORDER)
        self.border_container_2_1.place(x=30, y=40)

        self.container_2_name = Label(self.container_2,
                                      bg="white", 
                                      width=10, 
                                      font=(TEXT_FONT, TITLE_FONTSIZE),
                                      justify=LEFT,
                                      anchor="w")
        self.container_2_name.place(x=35 + 6, y=6) 


        self.container_2_checkbox = customtkinter.CTkButton(self.container_2,
                                                            width=25,
                                                            height=25,
                                                            fg_color=CHECKBOX_COLOR,
                                                            bg_color=CHECKBOX_COLOR,
                                                            hover_color=None,
                                                            border_color=CHECKBOX_COLOR,
                                                            corner_radius=7,
                                                            text="")
        self.container_2_checkbox.place(x=118 + 30, y=8)
        self.container_2_checkbox.configure(command = lambda: UiFunc.switchCheckboxState(self.container_2_checkbox, 2))


        self.container_2_kcal = Label(self.container_2, 
                                      text="xxx Kcal/100g",
                                      bg=self.container_2.fg_color, 
                                      width=14, 
                                      font=(TEXT_FONT, STANDARD_FONTSIZE)) 
        self.container_2_kcal.place(x=30 + 9, y=49) 

        self.border_container_2_2 = customtkinter.CTkFrame(master=self.container_2,
                                                           width=self.container_2.winfo_reqwidth(),
                                                           height=2,
                                                           corner_radius=10,
                                                           fg_color=MATERIALS_LIGHT_BORDER)
        self.border_container_2_2.place(x=30, y=79)

        self.container_2_fat = Label(self.container_2, 
                                     text="xx Fett/100g",
                                     bg=self.container_2.fg_color, 
                                     width=14, 
                                     font=(TEXT_FONT, STANDARD_FONTSIZE)) 
        self.container_2_fat.place(x=30 + 9, y=90) 

        self.border_container_2_3 = customtkinter.CTkFrame(master=self.container_2,
                                                           width=self.container_2.winfo_reqwidth(),
                                                           height=2,
                                                           corner_radius=10,
                                                           fg_color=MATERIALS_LIGHT_BORDER)
        self.border_container_2_3.place(x=30, y=118)

        self.container_2_sugar = Label(self.container_2, 
                                       text="xx Zucker/100g",
                                       bg=self.container_2.fg_color, 
                                       width=14, 
                                       font=(TEXT_FONT, STANDARD_FONTSIZE))
        self.container_2_sugar.place(x=30 + 9, y=127) 

        self.border_container_2_4 = customtkinter.CTkFrame(master=self.container_2,
                                                           width=self.container_2.winfo_reqwidth(),
                                                           height=2,
                                                           corner_radius=10,
                                                           fg_color=MATERIALS_STANDARD_BORDER)
        self.border_container_2_4.place(x=30, y=157)

        self.container_2_portion_amount = Label(self.container_2, 
                                               text="2/6",
                                               bg=self.container_2.fg_color, 
                                               width=12, 
                                               font=(TEXT_FONT, TITLE_FONTSIZE)) 
        self.container_2_portion_amount.place(x=30 + 6, y=165) 



        self.container_2_percents_bar = customtkinter.CTkProgressBar(self.container_2,
                                                                     width=150,
                                                                     height=5)
        self.container_2_percents_bar.place(x=30 + 5, y=195)
        self.container_2_percents_bar.set(0.25)

        self.button_container_2_dec = customtkinter.CTkButton(master=self.container_2, 
                                           text="-", 
                                           text_color="white", 
                                           height=200,
                                           width=30,
                                           text_font=(TEXT_FONT, TITLE_FONTSIZE + 1),
                                           bg_color=BACKGROUND_COLOR_BUTTON,
                                           fg_color=BACKGROUND_COLOR_BUTTON,
                                           hover_color=BUTTON_HOVER_COLOR_BORDERS)
        self.button_container_2_dec.place(x=0, y=0)


        self.button_container_2_inc = customtkinter.CTkButton(master=self.container_2, 
                                           text="+", 
                                           text_color="white", 
                                           height=200,
                                           width=27,
                                           text_font=(TEXT_FONT, TITLE_FONTSIZE + 1),
                                           bg_color=BACKGROUND_COLOR_BUTTON,
                                           fg_color=BACKGROUND_COLOR_BUTTON,
                                           hover_color=BUTTON_HOVER_COLOR_BORDERS)
        self.button_container_2_inc.place(x=185, y=0)


    def loadContainerRight(self, master):
        self.container_3 = customtkinter.CTkFrame(master=master,
                                                  width=CONTAINER_WIDTH,
                                                  height=CONTAINER_HEIGHT,
                                                  corner_radius=4,
                                                  fg_color="white")
        self.container_3.place(x=CONTAINER_3_X, y=CONTAINER_3_Y)

        self.border_container_3_1 = customtkinter.CTkFrame(master=self.container_3,
                                                           width=self.container_3.winfo_reqwidth(),
                                                           height=2,
                                                           corner_radius=10,
                                                           fg_color=MATERIALS_STANDARD_BORDER)
        self.border_container_3_1.place(x=30, y=40)

        self.container_3_name = Label(self.container_3,
                                      bg="white", 
                                      width=10, 
                                      font=(TEXT_FONT, TITLE_FONTSIZE),
                                      justify=LEFT,
                                      anchor="w")
        self.container_3_name.place(x=35 + 6, y=6) 


        self.container_3_checkbox = customtkinter.CTkButton(self.container_3,
                                                            width=25,
                                                            height=25,
                                                            fg_color=CHECKBOX_COLOR,
                                                            bg_color=CHECKBOX_COLOR,
                                                            hover_color=None,
                                                            border_color=CHECKBOX_COLOR,
                                                            corner_radius=7,
                                                            text="")
        self.container_3_checkbox.place(x=118 + 30, y=8)
        self.container_3_checkbox.configure(command = lambda: UiFunc.switchCheckboxState(self.container_3_checkbox, 3))


        self.container_3_kcal = Label(self.container_3, 
                                      text="xxx Kcal/100g",
                                      bg=self.container_3.fg_color, 
                                      width=14, 
                                      font=(TEXT_FONT, STANDARD_FONTSIZE)) 
        self.container_3_kcal.place(x=30 + 9, y=49) 

        self.border_container_3_2 = customtkinter.CTkFrame(master=self.container_3,
                                                           width=self.container_3.winfo_reqwidth(),
                                                           height=2,
                                                           corner_radius=10,
                                                           fg_color=MATERIALS_LIGHT_BORDER)
        self.border_container_3_2.place(x=30, y=79)

        self.container_3_fat = Label(self.container_3, 
                                     text="xx Fett/100g",
                                     bg=self.container_3.fg_color, 
                                     width=14, 
                                     font=(TEXT_FONT, STANDARD_FONTSIZE)) 
        self.container_3_fat.place(x=30 + 9, y=90) 

        self.border_container_3_3 = customtkinter.CTkFrame(master=self.container_3,
                                                           width=self.container_3.winfo_reqwidth(),
                                                           height=2,
                                                           corner_radius=10,
                                                           fg_color=MATERIALS_LIGHT_BORDER)
        self.border_container_3_3.place(x=30, y=118)

        self.container_3_sugar = Label(self.container_3, 
                                       text="xx Zucker/100g",
                                       bg=self.container_3.fg_color, 
                                       width=14, 
                                       font=(TEXT_FONT, STANDARD_FONTSIZE))
        self.container_3_sugar.place(x=30 + 9, y=127) 

        self.border_container_3_4 = customtkinter.CTkFrame(master=self.container_3,
                                                           width=self.container_3.winfo_reqwidth(),
                                                           height=2,
                                                           corner_radius=10,
                                                           fg_color=MATERIALS_STANDARD_BORDER)
        self.border_container_3_4.place(x=30, y=157)

        self.container_3_portion_amount = Label(self.container_3, 
                                               text="2/6",
                                               bg=self.container_3.fg_color, 
                                               width=12, 
                                               font=(TEXT_FONT, TITLE_FONTSIZE)) 
        self.container_3_portion_amount.place(x=30 + 6, y=165) 



        self.container_3_percents_bar = customtkinter.CTkProgressBar(self.container_3,
                                                                     width=150,
                                                                     height=5)
        self.container_3_percents_bar.place(x=30 + 5, y=195)
        self.container_3_percents_bar.set(0.25)

        self.button_container_3_dec = customtkinter.CTkButton(master=self.container_3, 
                                           text="-", 
                                           text_color="white", 
                                           height=200,
                                           width=30,
                                           text_font=(TEXT_FONT, TITLE_FONTSIZE + 1),
                                           bg_color=BACKGROUND_COLOR_BUTTON,
                                           fg_color=BACKGROUND_COLOR_BUTTON,
                                           hover_color=BUTTON_HOVER_COLOR_BORDERS)
        self.button_container_3_dec.place(x=0, y=0)


        self.button_container_3_inc = customtkinter.CTkButton(master=self.container_3, 
                                           text="+", 
                                           text_color="white", 
                                           height=200,
                                           width=27,
                                           text_font=(TEXT_FONT, TITLE_FONTSIZE + 1),
                                           bg_color=BACKGROUND_COLOR_BUTTON,
                                           fg_color=BACKGROUND_COLOR_BUTTON,
                                           hover_color=BUTTON_HOVER_COLOR_BORDERS)
        self.button_container_3_inc.place(x=185, y=0)


    def loadPortionSize(self, master):
        InitializeMainTkWindow.create_container_shadow(master, 
                                                       width = LARGE_CONTAINER_WIDTH, 
                                                       height = LARGE_CONTAINER_HEIGHT, 
                                                       color = CONTAINER_SHADOW_COLOR,
                                                       posx = CONTAINER_PORTION_X, 
                                                       posy = CONTAINER_PORTION_Y)


        self.container_portion = customtkinter.CTkFrame(master=master,
                                             width=LARGE_CONTAINER_WIDTH,
                                             height=LARGE_CONTAINER_HEIGHT,
                                             corner_radius=4)
        self.container_portion.place(x=CONTAINER_PORTION_X, y=CONTAINER_PORTION_Y)


        self.border_1_container_portion_horizontal = customtkinter.CTkFrame(master=self.container_portion,
                                                           width=self.container_portion.winfo_reqwidth(),
                                                           height=2,
                                                           corner_radius=10,
                                                           fg_color=MATERIALS_STANDARD_BORDER)
        self.border_1_container_portion_horizontal.place(x=0, y=40)

        self.container_portion_name = Label(self.container_portion, 
                                      text="Portionsgröße",
                                      bg="white", 
                                      width=30, 
                                      font=(TEXT_FONT, TITLE_FONTSIZE)) 
        self.container_portion_name.place(x=0 + 6, y=6) 


        self.button_portion_1 = customtkinter.CTkButton(master=self.container_portion, 
                                                        text="6 Schaufeln", 
                                                        width=75,
                                                        fg_color=BACKGROUND_LIGHT_COLOR_BUTTON,
                                                        text_color="white",
                                                        text_font=(TEXT_FONT, SMALL_FONTSIZE + 1),
                                                        hover_color=BUTTON_HOVER_COLOR_BORDERS,
                                                        command=lambda: UiFunc.portionButtonSwitch(self, self.button_portion_1, 1))
        self.button_portion_1.place(x=3, y=46)

        self.border_2_container_portion_vertical = customtkinter.CTkFrame(master=self.container_portion,
                                                                 width=2,
                                                                 height=self.container_portion.winfo_reqheight() - 42,
                                                                 corner_radius=10,
                                                                 fg_color=MATERIALS_LIGHT_BORDER)
        self.border_2_container_portion_vertical.place(x=110, y=42)

        self.button_portion_2 = customtkinter.CTkButton(master=self.container_portion, 
                                                        text="9 Schaufeln", 
                                                        width=75,
                                                        fg_color=BACKGROUND_LIGHT_COLOR_BUTTON,
                                                        text_color="white",
                                                        text_font=(TEXT_FONT, SMALL_FONTSIZE + 1),
                                                        hover_color=BUTTON_HOVER_COLOR_BORDERS,
                                                        command=lambda: UiFunc.portionButtonSwitch(self, self.button_portion_2, 2))
        self.button_portion_2.place(x=118, y=46)

      
        self.border_3_container_portion_vertical = customtkinter.CTkFrame(master=self.container_portion,
                                                                 width=2,
                                                                 height=self.container_portion.winfo_reqheight() - 42,
                                                                 corner_radius=10,
                                                                 fg_color=MATERIALS_LIGHT_BORDER)
        self.border_3_container_portion_vertical.place(x=229, y=42)

        
        self.button_portion_3 = customtkinter.CTkButton(master=self.container_portion, 
                                                        text="12 Schaufeln", 
                                                        width=75,
                                                        fg_color=BACKGROUND_LIGHT_COLOR_BUTTON,
                                                        text_color="white",
                                                        text_font=(TEXT_FONT, SMALL_FONTSIZE + 1),
                                                        hover_color=BUTTON_HOVER_COLOR_BORDERS,
                                                        command= lambda: UiFunc.portionButtonSwitch(self, self.button_portion_3, 3))
        self.button_portion_3.place(x=234, y=46)


    def loadNutritionalValues(self, master):
        InitializeMainTkWindow.create_container_shadow(master, 
                                                       width = LARGE_CONTAINER_WIDTH, 
                                                       height = LARGE_CONTAINER_HEIGHT, 
                                                       color = CONTAINER_SHADOW_COLOR,
                                                       posx = CONTAINER_PORTION_NUTRITIONAL_VALUES_X, 
                                                       posy = CONTAINER_PORTION_NUTRITIONAL_VALUES_Y)


        self.container_portion_nutritional_values = customtkinter.CTkFrame(master=master,
                                             width=LARGE_CONTAINER_WIDTH,
                                             height=LARGE_CONTAINER_HEIGHT,
                                             corner_radius=4)
        self.container_portion_nutritional_values.place(x=CONTAINER_PORTION_NUTRITIONAL_VALUES_X, y=CONTAINER_PORTION_NUTRITIONAL_VALUES_Y)

        self.border_1_container_portion_nutritional_values_horizontal = customtkinter.CTkFrame(master=self.container_portion_nutritional_values,
                                                           width=self.container_portion.winfo_reqwidth(),
                                                           height=2,
                                                           corner_radius=10,
                                                           fg_color=MATERIALS_STANDARD_BORDER)
        self.border_1_container_portion_nutritional_values_horizontal.place(x=0, y=40)


        self.container_portion_nutritional_values_name = Label(self.container_portion_nutritional_values, 
                                      text="Nährwerte",
                                      bg="white", 
                                      width=30, 
                                      font=(TEXT_FONT, TITLE_FONTSIZE)) 
        self.container_portion_nutritional_values_name.place(x=0 + 6, y=6) 
        
        
        self.label_portion_nutritional_values_kcal = Label(master=self.container_portion_nutritional_values, 
                                                        text="333 Kcal", 
                                                        width=10,
                                                        font=(TEXT_FONT, STANDARD_FONTSIZE), 
                                                        bg="white")
        self.label_portion_nutritional_values_kcal.place(x=7, y=50)
        
        
        self.border_2_container_portion_nutritional_values_vertical = customtkinter.CTkFrame(master=self.container_portion_nutritional_values,
                                                                 width=2,
                                                                 height=self.container_portion_nutritional_values.winfo_reqheight(),
                                                                 corner_radius=10,
                                                                 fg_color=MATERIALS_LIGHT_BORDER)
        self.border_2_container_portion_nutritional_values_vertical.place(x=110, y=42)
        

        self.label_portion_nutritional_values_fat = Label(master=self.container_portion_nutritional_values, 
                                                        text="xx Fett", 
                                                        width=10,
                                                        font=(TEXT_FONT, STANDARD_FONTSIZE), 
                                                        bg="white")
        self.label_portion_nutritional_values_fat.place(x=122, y=50)
        

        self.border_3_container_portion_nutritional_values_vertical = customtkinter.CTkFrame(master=self.container_portion_nutritional_values,
                                                                 width=2,
                                                                 height=self.container_portion_nutritional_values.winfo_reqheight(),
                                                                 corner_radius=10,
                                                                 fg_color=MATERIALS_LIGHT_BORDER)
        self.border_3_container_portion_nutritional_values_vertical.place(x=229, y=42)


        self.label_portion_nutritional_values_sugar = Label(master=self.container_portion_nutritional_values, 
                                                        text="xx Zucker", 
                                                        width=10,
                                                        font=(TEXT_FONT, STANDARD_FONTSIZE), 
                                                        bg="white")
        self.label_portion_nutritional_values_sugar.place(x=242, y=50)

    def loadBottomBar(self, master):
        self.button_start = customtkinter.CTkButton(master=master, 
                                           text="Servieren", 
                                           width=200, 
                                           height=35,
                                           text_color="white", 
                                           fg_color=BACKGROUND_COLOR_BUTTON,
                                           bg_color=BACKGROUND_COLOR,
                                           hover_color=BUTTON_HOVER_COLOR_BORDERS,
                                           text_font=(TEXT_FONT, TITLE_FONTSIZE), 
                                           command=lambda: InitializeMainTkWindow.test(self))
        self.button_start.place(x=400, y=412, anchor=CENTER)

        self.bot_frame = Frame(master, 
                               height=25, 
                               width=800, 
                               bg=BACKGROUND_BOTTOM_COLOR_BORDERS)
        self.bot_frame.place(x=BORDER_BOT_X,y=BORDER_BOT_Y)

        Frame(master,
            height=3,
            width=800,
            bg=BACKGROUND_BORDER_COLOR).place(x=0, y=452)


        self.bot_date = Label(self.bot_frame, 
                              text="12:20 | 15.02.2022",
                              bg=BACKGROUND_BOTTOM_COLOR_BORDERS,  
                              fg=TEXT_BORDER_COLOR,
                              justify=LEFT,
                              anchor="w",
                              width=16, 
                              font=(TEXT_FONT, SMALL_FONTSIZE),) 
        self.bot_date.place(x=0,y=2)

        UiFunc.startClock(self)

        self.bot_footer = Label(self.bot_frame, 
                              text="S. Dolgow | M. Nicolaisen © 2022",
                              bg=BACKGROUND_BOTTOM_COLOR_BORDERS,  
                              fg=TEXT_BORDER_COLOR,
                            justify=RIGHT,
                              anchor="e",
                              width=25, 
                              font=(TEXT_FONT, SMALL_FONTSIZE),) 
        self.bot_footer.place(x=594,y=2)

    def create_container_shadow(master, width, height, color, posx, posy):
        customtkinter.CTkFrame(master=master,
                               width=width + 1,
                               height=height + 1,
                               corner_radius = 3,
                               fg_color = color).place(x=posx - 2, y=posy - 2)     



    def test(self):
        print("Asdasd")

        # config = UiFunc.readConfigFile()
        # main_supply = int(config.get("portionsettings", "main_supply_container"))



    # def portionButtonSwitch(self, instance):
    #     if self.button_portion_1.fg_color == BACKGROUND_COLOR_BUTTON:
    #         self.button_portion_1.configure(fg_color = BACKGROUND_LIGHT_COLOR_BUTTON)
    #     if self.button_portion_2.fg_color == BACKGROUND_COLOR_BUTTON:
    #         self.button_portion_2.configure(fg_color = BACKGROUND_LIGHT_COLOR_BUTTON)
    #     if self.button_portion_3.fg_color == BACKGROUND_COLOR_BUTTON:
    #         self.button_portion_3.configure(fg_color = BACKGROUND_LIGHT_COLOR_BUTTON)
    #     if self.button_portion_4.fg_color == BACKGROUND_COLOR_BUTTON:
    #         self.button_portion_4.configure(fg_color = BACKGROUND_LIGHT_COLOR_BUTTON)

    #     instance.configure(fg_color= BACKGROUND_COLOR_BUTTON)