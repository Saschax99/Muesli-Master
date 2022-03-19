#Import all the necessary libraries
import customtkinter
from tkinter import Label, Frame, CENTER, LEFT, Toplevel, END
from config.config import *
import configparser


class InputSensorLevel:
    def __init__(self,
                main_instance,
                c_count):

        height = WINDOW_HEIGHT
        width = WINDOW_WIDTH
        self.c_count = c_count
        self.instance = main_instance
        self.config = InputSensorLevel.readConfigFile()
        self.c_name = self.config.get("c"+str(self.c_count), "name")

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

        InputSensorLevel.loadTopBar(self)

        InputSensorLevel.container(self)

        InputSensorLevel.loadBottomBar(self)

        InputSensorLevel.loadContainerValues(self)

    def readConfigFile():
        '''reading config for containers'''

        try:
            parser_file = configparser.ConfigParser(allow_no_value=True, comment_prefixes='///')
            parser_file.read(CONFIG_PATH, encoding='utf-8')
            return parser_file
        except Exception as e:
            print(e)

    def writeConfigFile(self, section, option, value):
        '''writing config for containers'''

        self.config.set(section, option, value)

        with open(CONFIG_PATH, 'w', encoding="utf-8") as configfile: # save
            self.config.write(configfile)

    def updateContainerValues(self, instance):
        '''update values of containers'''

        for i in range(1, 4): # roll container 1 to 3
            # setup all container details
            exec('instance.container_'
                + str(i)
                + '_name.configure(text=self.config.get("c" + str(i), "name"))')

            exec('instance.container_'
                 + str(i) 
                 + '_kcal.configure(text=self.config.get("c" + str(i), "kcal") + " Kcal/100g")')

            exec('instance.container_' 
                 + str(i)
                 + '_fat.configure(text=self.config.get("c" + str(i), "fat")  + "g Fett/100g")')
            exec('instance.container_' 
                 + str(i) 
                 + '_sugar.configure(text=self.config.get("c" + str(i), "sugar") + "g Zucker/100g")')

            exec('instance.container_' 
                 + str(i) 
                 + '_percents_bar.set(float(self.config.get("c" + str(i), "fill_state")))')
            # /setup all container details


    def updatePortionShovels(self, instance, var1, var2, var3):
        cur_size = int(var1) + int(var2) + int(var3)
        instance.container_portion_value.configure(text=str(cur_size) + "/" + str(MAX_PORTION_SIZE) + " Schaufeln" + " | " + str(cur_size * GRAMM_PER_PORTION) + " Gramm")

    def updateResultSize(self, instance):
        '''update result size of portion'''

        var_amount_1 = self.config.get(CONFIG_PORTIONS_NAME, "c1_amount")
        instance.container_1_portion_amount.configure(text=str(var_amount_1))

        var_amount_2 = self.config.get(CONFIG_PORTIONS_NAME, "c2_amount")
        instance.container_2_portion_amount.configure(text=str(var_amount_2))

        var_amount_3 = self.config.get(CONFIG_PORTIONS_NAME, "c3_amount")
        instance.container_3_portion_amount.configure(text=str(var_amount_3))

        InputSensorLevel.updatePortionShovels(self, instance, var_amount_1, var_amount_2, var_amount_3)

    def updateResult(self, instance, kcal, fat, sugar):
        '''updating result portion'''

        instance.label_portion_nutritional_values_kcal.configure(text=str(kcal) + " Kcal")
        instance.label_portion_nutritional_values_fat.configure(text=str(fat) + " Fett")
        instance.label_portion_nutritional_values_sugar.configure(text=str(sugar) + " Zucker")

    def calculateResultValues(self, instance):
        '''calculate result values for portion'''

        c1_count = float(self.config.get("portionsettings", "c1_amount"))
        c2_count = float(self.config.get("portionsettings", "c2_amount"))
        c3_count = float(self.config.get("portionsettings", "c3_amount"))

        c1_kcal = float(self.config.get("c1", "kcal"))
        c1_fat = float(self.config.get("c1", "fat"))
        c1_sugar = float(self.config.get("c1", "sugar"))

        c2_kcal = float(self.config.get("c2", "kcal"))
        c2_fat = float(self.config.get("c2", "fat"))
        c2_sugar = float(self.config.get("c2", "sugar"))

        c3_kcal = float(self.config.get("c3", "kcal"))
        c3_fat = float(self.config.get("c3", "fat"))
        c3_sugar = float(self.config.get("c3", "sugar"))

        kcal_result = round(((c1_count * (c1_kcal))
                            + (c2_count * (c2_kcal))
                            + (c3_count * (c3_kcal)))
                            / CALCULATION_RATIO, 1)

        fat_result = round(((c1_count * (c1_fat))
                            + (c2_count * (c2_fat))
                            + (c3_count * (c3_fat)))
                            / CALCULATION_RATIO, 1)

        sugar_result = round(((c1_count * (c1_sugar))
                            + (c2_count * (c2_sugar))
                            + (c3_count * (c3_sugar))) 
                            / CALCULATION_RATIO, 1)

        InputSensorLevel.writeConfigFile(self, "portionsettings", "kcal", str(kcal_result))
        InputSensorLevel.writeConfigFile(self, "portionsettings", "fat", str(fat_result))
        InputSensorLevel.writeConfigFile(self, "portionsettings", "sugar", str(sugar_result))

        InputSensorLevel.updateResult(self, instance, kcal_result, fat_result, sugar_result)

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
                              text="Behälter Zuweisung",
                              bg=TOP_BORDER_BG_COLOR, 
                              fg="white",
                              width=17, 
                              font=(TEXT_FONT, TITLE_FONTSIZE)) 
        self.top_name.place(x=30, y=5)

    def container(self):
        InputSensorLevel.create_container_shadow(self.top, # SHADOW
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
                                      text="Kcal/100g",
                                      bg="white", 
                                      width=10, 
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
                                      text="Fett/100g",
                                      bg="white", 
                                      width=10, 
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
                                      text="Zucker/100g",
                                      bg="white", 
                                      width=10, 
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
                                           command=lambda: InputSensorLevel.Save(self))
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

    def writeConfigFile(self, section, option, value):
        '''writing config for containers'''

        self.config.set(section, option, value)

        with open(CONFIG_PATH, 'w', encoding="utf-8") as configfile: # save
            self.config.write(configfile)

    def closeTopLevel(self, instance):
    
        InputSensorLevel.updateContainerValues(self, instance)
        InputSensorLevel.updateResultSize(self, instance)
        InputSensorLevel.calculateResultValues(self, instance)
        self.top.destroy()

    def Save(self):
        print("saving")
        InputSensorLevel.writeConfigFile(self, "c"+ str(self.c_count), "name", str(self.entry_name.get()))
        InputSensorLevel.writeConfigFile(self, "c"+ str(self.c_count), "kcal", str(self.entry_kcal.get()))
        InputSensorLevel.writeConfigFile(self, "c"+ str(self.c_count), "fat", str(self.entry_fat.get()))
        InputSensorLevel.writeConfigFile(self, "c"+ str(self.c_count), "sugar", str(self.entry_sugar.get()))
            
        InputSensorLevel.closeTopLevel(self, self.instance)


    def loadContainerValues(self):
        config = InputSensorLevel.readConfigFile()
        self.entry_name.insert(END, config.get("c"+ str(self.c_count), "name"))
        self.entry_kcal.insert(END, config.get("c"+ str(self.c_count), "kcal"))
        self.entry_fat.insert(END, config.get("c"+ str(self.c_count), "fat"))
        self.entry_sugar.insert(END, config.get("c"+ str(self.c_count), "sugar"))