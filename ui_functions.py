import configparser

from numpy import true_divide
from config import BACKGROUND_COLOR_BUTTON, BACKGROUND_LIGHT_COLOR_BUTTON, CONFIG_PATH
from datetime import datetime
import time
import threading
import sys
import math

#from ui import new
class UiFunc:
    #region TOPLEVEL


    #endregion TOPLEVEL


    def portionButtonSwitch(self, instance, count):
        '''setup portion size with switches'''
        if self.button_portion_1.fg_color == BACKGROUND_COLOR_BUTTON:
            self.button_portion_1.configure(fg_color = BACKGROUND_LIGHT_COLOR_BUTTON)

        if self.button_portion_2.fg_color == BACKGROUND_COLOR_BUTTON:
            self.button_portion_2.configure(fg_color = BACKGROUND_LIGHT_COLOR_BUTTON)

        if self.button_portion_3.fg_color == BACKGROUND_COLOR_BUTTON:
            self.button_portion_3.configure(fg_color = BACKGROUND_LIGHT_COLOR_BUTTON)

        if self.button_portion_4.fg_color == BACKGROUND_COLOR_BUTTON:
            self.button_portion_4.configure(fg_color = BACKGROUND_LIGHT_COLOR_BUTTON)

        instance.configure(fg_color= BACKGROUND_COLOR_BUTTON)
        UiFunc.writeConfigFile("portionsettings", "size", str(count)) # get last letter of var - convert to int divide 1 and convert to str......

    def portionButtonStartup(self):
        '''setup portion size on startup'''
        value = int(config.get("portionsettings", "size"))
        if value == 1:
            self.button_portion_1.configure(fg_color = BACKGROUND_COLOR_BUTTON)

        if value == 2:
            self.button_portion_2.configure(fg_color = BACKGROUND_COLOR_BUTTON)

        if value == 3:
            self.button_portion_3.configure(fg_color = BACKGROUND_COLOR_BUTTON)

        if value == 4:
            self.button_portion_4.configure(fg_color = BACKGROUND_COLOR_BUTTON)

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
            exec('self.container_' + str(i) + '_percents_name.configure(text=str(round(float(config.get("c" + str(i), "fill_State")) * 100)) + "%")')
            exec('self.container_' + str(i) + '_percents_bar.set(float(config.get("c" + str(i), "fill_state")))')
            # /setup all container details

            #exec('self.checkbox_' + str(i) + '_var.set(config.get("c" + str(i), "supply_active"))') # setup supply actived

    

    def switchCheckboxState(self, count):
        '''updating checkboxes for supply'''
        if config.get("c" + str(count), "supply_active") == str(True):
            self.configure(fg_color="white")
            UiFunc.writeConfigFile("c" + str(count), "supply_active", str(False))
        else:
            self.configure(fg_color=BACKGROUND_COLOR_BUTTON)
            UiFunc.writeConfigFile("c" + str(count), "supply_active", str(True))


    def CheckboxStartup(self):
        for i in range(1, 4):
            if config.get("c" + str(i), "supply_active") == str(True):
                exec('self.container_' + str(i) + '_checkbox.configure(fg_color=BACKGROUND_COLOR_BUTTON)')
            else:
                exec('self.container_' + str(i) + '_checkbox.configure(fg_color="white")')



config = UiFunc.readConfigFile()        
    # TOPLEVEL
    
    # def calculateSliderValues(self):
        
    #     self.slider_kcal.value


    #     self.slider_fat.value

    #     self.slider_sugar.value
    #     pass

    # def refreshKcalSlider(self, value):
    #     slider_value = math.trunc(self.slider_kcal.value * 100)
    #     UiFunc.calculateSliderValues()
    #     self.slider_kcal_name.configure(text= str(slider_value) + " Kcal auf 100g")




    # def refreshFatSlider(self, value):

    #     slider_value = math.trunc(self.slider_fat.value * 100)

    #     self.slider_fat_name.configure(text= str(slider_value) + " Fett auf 100g")

    # def refreshSugarSlider(self, value):
    #     slider_value = math.trunc(self.slider_sugar.value * 100)

    #     self.slider_sugar_name.configure(text= str(slider_value) + " Zucker auf 100g")
