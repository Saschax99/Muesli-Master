import configparser
from config.config import *
from datetime import datetime
import time
import threading
import sys
from loggingsystem import writeLog

class UiFunc:
    '''All User Interface functions'''
    
    #region portions size
    def portionButtonSwitch(self, instance, count):
        '''setup portion size with switches on main window'''

        if self.button_portion_1.fg_color == BUTTON_HOVER_BG_COLOR:
            self.button_portion_1.configure(fg_color = BUTTON_BG_COLOR)

        if self.button_portion_2.fg_color == BUTTON_HOVER_BG_COLOR:
            self.button_portion_2.configure(fg_color = BUTTON_BG_COLOR)

        if self.button_portion_3.fg_color == BUTTON_HOVER_BG_COLOR:
            self.button_portion_3.configure(fg_color = BUTTON_BG_COLOR)

        instance.configure(fg_color= BUTTON_HOVER_BG_COLOR)
        UiFunc.writeConfigFile(CONFIG_PORTIONS_NAME, "size_var", str(count))
        UiFunc.resetResultValues(self) # reset values when switching
        UiFunc.updateResultSize(self) # update result sizes
        UiFunc.calculateResultValues(self) # update result labels and calc

    def updatePortionValues(self):
        '''update portion size button on startup'''

        value = int(config.get(CONFIG_PORTIONS_NAME, "size_var"))
        if value == 0:
            self.button_portion_1.configure(fg_color = BUTTON_HOVER_BG_COLOR)

        if value == 1:
            self.button_portion_2.configure(fg_color = BUTTON_HOVER_BG_COLOR)

        if value == 2:
            self.button_portion_3.configure(fg_color = BUTTON_HOVER_BG_COLOR)

    def updatePortionSizesValues(self):
        '''update portion size text on startup'''

        p1 = config.get(CONFIG_PORTIONS_NAME, "portion_size[0]")
        self.button_portion_1.configure(text=str(p1) +" Schaufeln")   
        
        p2 = config.get(CONFIG_PORTIONS_NAME, "portion_size[1]")
        self.button_portion_2.configure(text=str(p2) +" Schaufeln")     
        
        p3 = config.get(CONFIG_PORTIONS_NAME, "portion_size[2]")
        self.button_portion_3.configure(text=str(p3) +" Schaufeln")

    def updateResultSize(self):
        '''update result size of portion'''

        var_amount_1 = config.get(CONFIG_PORTIONS_NAME, "c1_amount")
        var_1 = config.get(CONFIG_PORTIONS_NAME, "size_var")
        por_size_1 = config.get(CONFIG_PORTIONS_NAME, "portion_size[" + var_1 +"]")
        self.container_1_portion_amount.configure(text=str(var_amount_1) + "/" + str(por_size_1))

        var_amount_2 = config.get(CONFIG_PORTIONS_NAME, "c2_amount")
        var_2 = config.get(CONFIG_PORTIONS_NAME, "size_var")
        por_size_2 = config.get(CONFIG_PORTIONS_NAME, "portion_size[" + var_2 +"]")
        self.container_2_portion_amount.configure(text=str(var_amount_2) + "/" + str(por_size_2))

        var_amount_3 = config.get(CONFIG_PORTIONS_NAME, "c3_amount")
        var_3 = config.get(CONFIG_PORTIONS_NAME, "size_var")
        por_size_3 = config.get(CONFIG_PORTIONS_NAME, "portion_size[" + var_3 +"]")
        self.container_3_portion_amount.configure(text=str(var_amount_3) + "/" + str(por_size_3))

    def resetResultValues(self, count = 0):
        if count == 0: # reset all
            UiFunc.writeConfigFile(CONFIG_PORTIONS_NAME, "c1_amount", "0")
            UiFunc.writeConfigFile(CONFIG_PORTIONS_NAME, "c2_amount", "0")
            UiFunc.writeConfigFile(CONFIG_PORTIONS_NAME, "c3_amount", "0")

        elif count == 1:
            UiFunc.writeConfigFile(CONFIG_PORTIONS_NAME, "c1_amount", "0")        
        elif count == 2:
            UiFunc.writeConfigFile(CONFIG_PORTIONS_NAME, "c2_amount", "0")        
        elif count == 3:
            UiFunc.writeConfigFile(CONFIG_PORTIONS_NAME, "c3_amount", "0")


    def increasePortionAmount(self, con):
        '''increase amount of containers portion size'''

        var = config.get(CONFIG_PORTIONS_NAME, "size_var")
        por_size = config.get(CONFIG_PORTIONS_NAME, "portion_size[" + var +"]")

        c1_amount = int(config.get(CONFIG_PORTIONS_NAME, "c1_amount"))
        c2_amount = int(config.get(CONFIG_PORTIONS_NAME, "c2_amount"))
        c3_amount = int(config.get(CONFIG_PORTIONS_NAME, "c3_amount"))
        c_all_amount = c1_amount + c2_amount + c3_amount

        if int(c_all_amount) == int(por_size): # if max reached return
            return

        if con == 1:
            UiFunc.writeConfigFile(CONFIG_PORTIONS_NAME, "c1_amount", str(c1_amount + 1))

        elif con == 2:
            UiFunc.writeConfigFile(CONFIG_PORTIONS_NAME, "c2_amount", str(c2_amount + 1))

        elif con == 3:
            UiFunc.writeConfigFile(CONFIG_PORTIONS_NAME, "c3_amount", str(c3_amount + 1))

        UiFunc.updateResultSize(self)
        UiFunc.calculateResultValues(self)

    def decreasePortionAmount(self, con):
        '''decrease amount of containers portion size'''

        c1_amount = int(config.get(CONFIG_PORTIONS_NAME, "c1_amount"))
        c2_amount = int(config.get(CONFIG_PORTIONS_NAME, "c2_amount"))
        c3_amount = int(config.get(CONFIG_PORTIONS_NAME, "c3_amount"))
        c_all_amount = c1_amount + c2_amount + c3_amount

        if int(c_all_amount) == 0: # if min reached return
            return

        if con == 1:
            if c1_amount == 0: # return before reaching negative numbers
                return
            UiFunc.writeConfigFile(CONFIG_PORTIONS_NAME, "c1_amount", str(c1_amount - 1))

        elif con == 2:
            if c2_amount == 0:
                return
            UiFunc.writeConfigFile(CONFIG_PORTIONS_NAME, "c2_amount", str(c2_amount - 1))

        elif con == 3:
            if c3_amount == 0:
                return
            UiFunc.writeConfigFile(CONFIG_PORTIONS_NAME, "c3_amount", str(c3_amount - 1))

        UiFunc.updateResultSize(self)
        UiFunc.calculateResultValues(self)

    def disableButton(self, count):
        if count == 1:
            self.button_container_1_inc.configure(state= "disabled", fg_color=BUTTON_DISABLED_BG_COLOR)
            self.button_container_1_dec.configure(state= "disabled", fg_color=BUTTON_DISABLED_BG_COLOR)

        if count == 2:
            self.button_container_2_inc.configure(state= "disabled", fg_color=BUTTON_DISABLED_BG_COLOR)        
            self.button_container_2_dec.configure(state= "disabled", fg_color=BUTTON_DISABLED_BG_COLOR)

        if count == 3:
            self.button_container_3_inc.configure(state= "disabled", fg_color=BUTTON_DISABLED_BG_COLOR)
            self.button_container_3_dec.configure(state= "disabled", fg_color=BUTTON_DISABLED_BG_COLOR)

    def enableButton(self, count):
        if count == 1:
            self.button_container_1_inc.configure(state= "normal", fg_color=BUTTON_BG_COLOR)
            self.button_container_1_dec.configure(state= "normal", fg_color=BUTTON_BG_COLOR)

        if count == 2:
            self.button_container_2_inc.configure(state= "normal", fg_color=BUTTON_BG_COLOR)  
            self.button_container_2_dec.configure(state= "normal", fg_color=BUTTON_BG_COLOR)      

        if count == 3:
            self.button_container_3_inc.configure(state= "normal", fg_color=BUTTON_BG_COLOR)
            self.button_container_3_dec.configure(state= "normal", fg_color=BUTTON_BG_COLOR)
    #endregion portions size   
 
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
            parser_file = configparser.ConfigParser(allow_no_value=True, comment_prefixes='///')
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
            exec('self.container_'
                + str(i)
                + '_name.configure(text=config.get("c" + str(i), "name"))')

            exec('self.container_'
                 + str(i) 
                 + '_kcal.configure(text=config.get("c" + str(i), "kcal") + " Kcal/100g")')

            exec('self.container_' 
                 + str(i)
                 + '_fat.configure(text=config.get("c" + str(i), "fat")  + "g Fett/100g")')
            exec('self.container_' 
                 + str(i) 
                 + '_sugar.configure(text=config.get("c" + str(i), "sugar") + "g Zucker/100g")')

            exec('self.container_' 
                 + str(i) 
                 + '_percents_bar.set(float(config.get("c" + str(i), "fill_state")))')
            # /setup all container details

    #region checkboxes
    def switchCheckboxState(self, instance, count):
        '''updating checkboxes for supply'''

        if config.get("c" + str(count), "supply_active") == str(True):
            instance.configure(fg_color="white")
            UiFunc.writeConfigFile("c" + str(count), "supply_active", str(False))
            UiFunc.resetResultValues(self, count)
            UiFunc.updateResultSize(self)
            UiFunc.updatePortionValues(self)
            UiFunc.disableButton(self, count)
            UiFunc.calculateResultValues(self)

        else:
            instance.configure(fg_color=CHECKBOX_BG_COLOR)
            UiFunc.writeConfigFile("c" + str(count), "supply_active", str(True))
            UiFunc.enableButton(self, count)

    def updateCheckboxValues(self):
        '''update checkboxes at startup'''

        for i in range(1, 4):
            if config.get("c" + str(i), "supply_active") == str(True):
                exec('self.container_' + str(i) + '_checkbox.configure(fg_color=CHECKBOX_BG_COLOR)')
            else:
                exec('self.container_' + str(i) + '_checkbox.configure(fg_color="white")')
            
            if config.get("c" + str(i), "supply_active") == str(False): # at startup disable buttons if supply is deactivated
                UiFunc.resetResultValues(self, i) # not necessary
                UiFunc.disableButton(self, i)      
    #endregion checkboxes

    #region result calculation
    def calculateResultValues(self):
        '''calculate result values for portion'''

        c1_count = float(config.get("portionsettings", "c1_amount"))
        c2_count = float(config.get("portionsettings", "c2_amount"))
        c3_count = float(config.get("portionsettings", "c3_amount"))

        c1_kcal = float(config.get("c1", "kcal"))
        c1_fat = float(config.get("c1", "fat"))
        c1_sugar = float(config.get("c1", "sugar"))

        c2_kcal = float(config.get("c2", "kcal"))
        c2_fat = float(config.get("c2", "fat"))
        c2_sugar = float(config.get("c2", "sugar"))

        c3_kcal = float(config.get("c3", "kcal"))
        c3_fat = float(config.get("c3", "fat"))
        c3_sugar = float(config.get("c3", "sugar"))

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

        UiFunc.writeConfigFile("portionsettings", "kcal", str(kcal_result))
        UiFunc.writeConfigFile("portionsettings", "fat", str(fat_result))
        UiFunc.writeConfigFile("portionsettings", "sugar", str(sugar_result))

        UiFunc.updateResult(self, kcal_result, fat_result, sugar_result)

    def updateResult(self, kcal, fat, sugar):
        '''updating result portion'''

        self.label_portion_nutritional_values_kcal.configure(text=str(kcal) + " Kcal")
        self.label_portion_nutritional_values_fat.configure(text=str(fat) + " Fett")
        self.label_portion_nutritional_values_sugar.configure(text=str(sugar) + " Zucker")

    def serve():
        if DEBUG: print("Serving...")

        amount = (int(config.get("portionsettings", "c1_amount"))
                + int(config.get("portionsettings", "c2_amount"))
                + int(config.get("portionsettings", "c3_amount")))

        if amount <= 0: # if 0 quit
            print("no amount set")
            return
            
        kcal = config.get("portionsettings", "kcal")
        fat = config.get("portionsettings", "fat")
        sugar = config.get("portionsettings", "sugar")

        with open(LOGSYSTEM_PATH, 'r') as csv: # get number of entries
            lines = csv.readlines()

        now = datetime.now()
        dt_string = now.strftime("%H:%M:%S | %d.%m.%Y")
        writeLog(len(lines), amount, kcal, fat, sugar, dt_string)

    #endregion result calculation


    def closeTopLevel(self, instance = None):
        #UiFunc.CheckboxStartup(self)
        if not instance == None: # if instance | from ui settings to main transition
            UiFunc.updateContainerValues(instance)
            UiFunc.updatePortionValues(instance)
            UiFunc.updatePortionSizesValues(instance)
            UiFunc.updateResultSize(instance)
            UiFunc.calculateResultValues(instance)
            #UiFunc.updateCheckboxValues(instance)

        self.top.destroy()
        
    #endregion TOPLEVEL



config = UiFunc.readConfigFile()        