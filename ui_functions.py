import configparser

from config import BACKGROUND_COLOR_BUTTON, BUTTON_HOVER_COLOR_BORDERS, CONFIG_PATH, CHECKBOX_COLOR
from datetime import datetime
import time
import threading
import sys

#from ui import new
class UiFunc:
    '''All User Interface functions'''
    
    def portionButtonSwitch(self, instance, count):
        '''setup portion size with switches'''
        if self.button_portion_1.fg_color == BUTTON_HOVER_COLOR_BORDERS:
            self.button_portion_1.configure(fg_color = BACKGROUND_COLOR_BUTTON)

        if self.button_portion_2.fg_color == BUTTON_HOVER_COLOR_BORDERS:
            self.button_portion_2.configure(fg_color = BACKGROUND_COLOR_BUTTON)

        if self.button_portion_3.fg_color == BUTTON_HOVER_COLOR_BORDERS:
            self.button_portion_3.configure(fg_color = BACKGROUND_COLOR_BUTTON)

        instance.configure(fg_color= BUTTON_HOVER_COLOR_BORDERS)
        UiFunc.writeConfigFile("portionsettings", "size", str(count)) # get last letter of var - convert to int divide 1 and convert to str......

    def portionButtonStartup(self):
        '''setup portion size on startup'''
        value = int(config.get("portionsettings", "size"))
        if value == 1:
            self.button_portion_1.configure(fg_color = BUTTON_HOVER_COLOR_BORDERS)

        if value == 2:
            self.button_portion_2.configure(fg_color = BUTTON_HOVER_COLOR_BORDERS)

        if value == 3:
            self.button_portion_3.configure(fg_color = BUTTON_HOVER_COLOR_BORDERS)

    # def openTopLevel(self):
    #     '''execute toplevel and open'''
    #     try:
    #         if not Toplevel.winfo_exists(self.toplevel): # if not exist create one
    #             self.toplevel = Toplevel()
    #             InitializeTopLevelTkWindow(self.toplevel)
    #             self.toplevel.mainloop()
    #     except AttributeError: # except if self.toplevel didnt created | if variable does not exists
    #         self.toplevel = Toplevel()
    #         InitializeTopLevelTkWindow(self.toplevel)
    #         self.toplevel.mainloop()
            
    def refreshDateTime(self):
        '''refreshing datetime as thread'''
        while True:
            try:
                now = datetime.now()
                dt_string = now.strftime("%H:%M:%S | %d.%m.%Y")
                self.bot_date.configure(text=dt_string)
                time.sleep(1)
            except KeyboardInterrupt:
                sys.exit()
    def startClock(self):
        '''starting clock for bottom left as thread'''
        thread = threading.Thread(target=UiFunc.refreshDateTime, args=(self, ))
        thread.setDaemon(True)
        thread.start()
        
    def readConfigFile():
        '''reading config for containers'''
        try:
            parser_file = configparser.ConfigParser()
            parser_file.read(CONFIG_PATH, encoding='utf-8')
            return parser_file
        except Exception as e:
            print(e)

    def writeConfigFile(section, option, value):
        '''writing config for containers'''
        config.set(section, option, value)

        with open(CONFIG_PATH, 'w', encoding="utf-8") as configfile: # save
            config.write(configfile)

    def updateContainerValues(self):
        '''update values of containers'''
        for i in range(1, 4): # roll container 1 to 3
            # setup all container details
            exec('self.container_' + str(i) + '_name.configure(text=config.get("c" + str(i), "name"))')
            exec('self.container_' + str(i) + '_kcal.configure(text=config.get("c" + str(i), "kcal") + " Kcal/100g")')
            exec('self.container_' + str(i) + '_fat.configure(text=config.get("c" + str(i), "fat")  + "g Fett/100g")')
            exec('self.container_' + str(i) + '_sugar.configure(text=config.get("c" + str(i), "sugar") + "g Zucker/100g")')
            exec('self.container_' + str(i) + '_percents_bar.set(float(config.get("c" + str(i), "fill_state")))')
            # /setup all container details

            #exec('self.checkbox_' + str(i) + '_var.set(config.get("c" + str(i), "supply_active"))') # setup supply actived

    

    def switchCheckboxState(self, count):
        '''updating checkboxes for supply'''
        if config.get("c" + str(count), "supply_active") == str(True):
            self.configure(fg_color="white")
            UiFunc.writeConfigFile("c" + str(count), "supply_active", str(False))
        else:
            self.configure(fg_color=CHECKBOX_COLOR)
            UiFunc.writeConfigFile("c" + str(count), "supply_active", str(True))


    def CheckboxStartup(self):
        for i in range(1, 4):
            if config.get("c" + str(i), "supply_active") == str(True):
                exec('self.container_' + str(i) + '_checkbox.configure(fg_color=CHECKBOX_COLOR)')
            else:
                exec('self.container_' + str(i) + '_checkbox.configure(fg_color="white")')


    def resizeSlider(self):
        if config.get("c1", "supply_active") == str(False):
            self.slider_container_1.value = 0
            config.set("portionsettings", "c1_percentage", str(self.slider_container_1.value))

        if config.get("c2", "supply_active") == str(False):
            self.slider_container_2.value = 0
            config.set("portionsettings", "c2_percentage", str(self.slider_container_2.value))
            
        if config.get("c3", "supply_active") == str(False):
            self.slider_container_3.value = 0
            config.set("portionsettings", "c3_percentage", str(self.slider_container_3.value))


    #region TOPLEVEL
    def calculateSliderValues(self, priority):
        '''calculating values of sliders on toplevel'''
        con_1_value = 0
        con_2_value = 0
        con_3_value = 0

        config = UiFunc.readConfigFile()
        activated_supply = []
        for i in range(1, 4):
            activated_supply.append(config.get("c"+ str(i), "supply_active"))
        print(activated_supply)

        if activated_supply[0] == str(True):
            con_1_value = self.slider_container_1.value
            config.set("portionsettings", "c1_percentage", str(con_1_value))
            print(con_1_value)
        else: # if slider is deactivated -> set to 0 and refresh slider
            self.slider_container_1.value = 0
            self.slider_container_1.draw()
        

        if activated_supply[1] == str(True):
            con_2_value = self.slider_container_2.value
            config.set("portionsettings", "c2_percentage", str(con_2_value))
            print(con_2_value)
        else:
            self.slider_container_2.value = 0
            self.slider_container_2.draw()


        if activated_supply[2] == str(True):
            con_3_value = self.slider_container_3.value
            config.set("portionsettings", "c3_percentage", str(con_3_value))
            print(con_3_value)
        else:
            self.slider_container_3.value = 0
            self.slider_container_3.draw()

        if priority == 1:
            print("container 1 is moving")
            # if con_1_value + con_2_value + con_3_value < 1:
            #     if con_2_value 
        if priority == 2:
            print("container 2 is moving")        
        if priority == 3:
            print("container 3 is moving")
            

        calc_kcal = (int(config.get("c1", "kcal")) * con_1_value) + (int(config.get("c2", "kcal")) * con_2_value) + (int(config.get("c3", "kcal")) * con_3_value)
        calc_fat = (int(config.get("c1", "fat")) * con_1_value) + (int(config.get("c2", "fat")) * con_2_value) + (int(config.get("c3", "fat")) * con_3_value)
        calc_sugar = (int(config.get("c1", "sugar")) * con_1_value) + (int(config.get("c2", "sugar")) * con_2_value) + (int(config.get("c3", "sugar")) * con_3_value)
        
        self.calculated_kcal.configure(text=str(round(calc_kcal, 1)) + " Kcal")
        self.calculated_fat.configure(text=str(round(calc_fat, 1)) + " Fett")
        self.calculated_sugar.configure(text=str(round(calc_sugar, 1)) + " Zucker")
        


        # main_supply = int(config.get("portionsettings", "main_supply_container"))
        # if main_supply == 1: # container 1
        #     kcal = int(config.get("c1", "kcal"))
        #     fat = int(config.get("c1", "fat"))
        #     sugar = int(config.get("c1", "sugar"))

        # elif main_supply == 2: # container 2
        #     kcal = int(config.get("c2", "kcal"))
        #     fat = int(config.get("c2", "fat"))
        #     sugar = int(config.get("c2", "sugar"))

        # refill_kcal = int(config.get("c3", "kcal")) # container 3
        # refill_fat = int(config.get("c3", "fat"))
        # refill_sugar = int(config.get("c3", "sugar"))


        # slider_kcal = self.slider_kcal.value
        # slider_fat = self.slider_fat.value
        # slider_sugar = self.slider_sugar.value
        # # define min and max at beginning of toplevel load !!!!!!!!!!!!!!!!!!!
        # result_kcal = round((slider_kcal * kcal) + (refill_kcal * (1 - slider_kcal)), 1)
        # result_fat = round((slider_fat * fat) + (refill_fat * (1 - slider_fat)), 1)
        # result_sugar = round((slider_sugar * sugar) + (refill_sugar * (1 - slider_sugar)), 1)

        # self.slider_container_1_name.configure(text= str(result_kcal) + " Kcal auf 100g")
        # self.slider_fat_name.configure(text= str(result_fat) + " Fett auf 100g")
        # self.slider_sugar_name.configure(text= str(result_sugar) + " Zucker auf 100g")

        #0,2 * 25 + 5 * (1- 0,2)



    def closeTopLevel(self):
        #UiFunc.CheckboxStartup(self)
        self.master.destroy()
        
    #endregion TOPLEVEL


config = UiFunc.readConfigFile()        