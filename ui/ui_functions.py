import configparser
from config.config import *
from datetime import datetime
import time
import threading
import sys
from loggingsystem import writeLog
from main_sensors import sens

class UiFunc:
    '''All User Interface functions'''
    
    #region portions size
    def updateResultSize(self):
        '''update result size of portion'''

        var_amount_1 = config.get(CONFIG_PORTIONS_NAME, "c1_amount")
        self.container_1_portion_amount.configure(text=str(var_amount_1))

        var_amount_2 = config.get(CONFIG_PORTIONS_NAME, "c2_amount")
        self.container_2_portion_amount.configure(text=str(var_amount_2))

        var_amount_3 = config.get(CONFIG_PORTIONS_NAME, "c3_amount")
        self.container_3_portion_amount.configure(text=str(var_amount_3))

        UiFunc.updatePortionShovels(self, var_amount_1, var_amount_2, var_amount_3)

    def updatePortionShovels(self, var1, var2, var3):
        '''updating portions label'''
        cur_size = int(var1) + int(var2) + int(var3)
        self.container_portion_value.configure(text=str(cur_size) + "/" + str(config.get(CONFIG_PORTIONS_NAME, "max_portion_size")) + " Schaufeln" + " | " + str(cur_size * GRAMM_PER_PORTION) + " Gramm")

    def resetResultValues(self, count = 0):
        '''reset result values of containers - after resizing amount'''
        
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
        
        c1_amount = int(config.get(CONFIG_PORTIONS_NAME, "c1_amount"))
        c2_amount = int(config.get(CONFIG_PORTIONS_NAME, "c2_amount"))
        c3_amount = int(config.get(CONFIG_PORTIONS_NAME, "c3_amount"))
        c_all_amount = c1_amount + c2_amount + c3_amount

        if int(c_all_amount) == int(config.get(CONFIG_PORTIONS_NAME, "max_portion_size")): # if max reached return
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
        '''disabling button'''
        
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
        '''enabling button'''
        
        if count == 1:
            self.button_container_1_inc.configure(state= "normal", fg_color=BUTTON_BG_COLOR)
            self.button_container_1_dec.configure(state= "normal", fg_color=BUTTON_BG_COLOR)

        if count == 2:
            self.button_container_2_inc.configure(state= "normal", fg_color=BUTTON_BG_COLOR)  
            self.button_container_2_dec.configure(state= "normal", fg_color=BUTTON_BG_COLOR)      

        if count == 3:
            self.button_container_3_inc.configure(state= "normal", fg_color=BUTTON_BG_COLOR)
            self.button_container_3_dec.configure(state= "normal", fg_color=BUTTON_BG_COLOR)


    def portionMaximumDecrease(self):
        '''decrease the value of maximum portion size in settings'''

        current_val = int(config.get(CONFIG_PORTIONS_NAME, "max_portion_size"))
        if current_val <= 0:
            return
        else: # if current value is not below 0
            for i in range(1, 4): # reset all active values
                UiFunc.writeConfigFile(CONFIG_PORTIONS_NAME, "c" + str(i) + "_amount", str(0))

            UiFunc.writeConfigFile(CONFIG_PORTIONS_NAME, "max_portion_size", str(current_val - 1))
            self.port_value.configure(text = str(current_val - 1))

    def portionMaximumIncrease(self):
        '''increase the value of maximum portion size in settings'''

        current_val = int(config.get(CONFIG_PORTIONS_NAME, "max_portion_size"))
        UiFunc.writeConfigFile(CONFIG_PORTIONS_NAME, "max_portion_size", str(current_val + 1))
        self.port_value.configure(text = str(current_val + 1))
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

    #region result calculation
    def calculateResultValues(self):
        '''calculate result values for portion'''

        c1_count = float(config.get(CONFIG_PORTIONS_NAME, "c1_amount"))
        c2_count = float(config.get(CONFIG_PORTIONS_NAME, "c2_amount"))
        c3_count = float(config.get(CONFIG_PORTIONS_NAME, "c3_amount"))

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

        UiFunc.writeConfigFile(CONFIG_PORTIONS_NAME, "kcal", str(kcal_result))
        UiFunc.writeConfigFile(CONFIG_PORTIONS_NAME, "fat", str(fat_result))
        UiFunc.writeConfigFile(CONFIG_PORTIONS_NAME, "sugar", str(sugar_result))

        UiFunc.updateResult(self, kcal_result, fat_result, sugar_result)

    def updateResult(self, kcal, fat, sugar):
        '''updating result portion'''

        self.label_portion_nutritional_values_kcal.configure(text=str(kcal) + " Kcal")
        self.label_portion_nutritional_values_fat.configure(text=str(fat) + " Fett")
        self.label_portion_nutritional_values_sugar.configure(text=str(sugar) + " Zucker")

    def serve():
        '''serving portion with motors and logging into csv'''
        
        if DEBUG: print("Serving...")

        c1_amount = int(config.get(CONFIG_PORTIONS_NAME, "c1_amount"))
        c2_amount = int(config.get(CONFIG_PORTIONS_NAME, "c2_amount"))
        c3_amount = int(config.get(CONFIG_PORTIONS_NAME, "c3_amount"))

        sens.motorCalculation(c1_amount, c2_amount, c3_amount)

        #region csv file
        amount = (c1_amount
                + c2_amount
                + c3_amount)

        if amount <= 0: # if 0 quit
            print("no amount set")
            return
            
        kcal = config.get(CONFIG_PORTIONS_NAME, "kcal")
        fat = config.get(CONFIG_PORTIONS_NAME, "fat")
        sugar = config.get(CONFIG_PORTIONS_NAME, "sugar")

        with open(LOGSYSTEM_PATH, 'r') as csv: # get number of entries
            lines = csv.readlines()

        now = datetime.now()
        t_string = now.strftime("%H:%M:%S")
        dt_string = now.strftime("%d.%m.%Y")
        writeLog(len(lines), amount, kcal, fat, sugar, t_string, dt_string)
        #endregion /csv file

    #endregion result calculation


    def closeTopLevel(self, instance = None):
        '''close toplevel after beeing in settings - modular as instance'''

        if not instance == None: # if instance | from ui settings to main transition
            UiFunc.updateContainerValues(instance)
            UiFunc.updateResultSize(instance)
            UiFunc.calculateResultValues(instance)
            #UiFunc.updateCheckboxValues(instance)

        self.top.destroy()
        
    #endregion TOPLEVEL

    #region SENSORS
    def startReedSensorThread(main_instance):
        '''starting new thread for reed sensor'''

        thread = threading.Thread(target=sens.fetchReedSensorValues, args=(main_instance, ))
        thread.setDaemon(True)
        thread.start()
        
    def startDistanceSensorThread(main_instance):
        '''starting new thread for reed sensor'''
        
        print("idas")
        thread2 = threading.Thread(target=sens.fetchDistanceSensorValues, args=(main_instance, ))
        thread2.setDaemon(True)
        thread2.start()
    #endregion /SENSORS


config = UiFunc.readConfigFile()        
