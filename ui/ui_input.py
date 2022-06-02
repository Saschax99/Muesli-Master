# keyboard https://www.bitforestinfo.com/blog/03/19/how-to-create-virtual-keyboard-using.html
import customtkinter
from tkinter import Label, Frame, CENTER, LEFT, Toplevel, END, LabelFrame, Button
from config.config import *
from ui.ui_functions import UiFunc
import sys

# all keys needed
keys =[ 
    [
        [
            ("Character_Keys"),
            ({'side':'top','expand':'yes','fill':'both'}),
            [
                ('q','w','e','r','t','z','u','i','o','p'),
                ('a','s','d','f','g','h','j','k','l'),
                ('y','x','c','v','b','n','m', '.', '<'),
                ('Space',)
            ]
        ]
    ],
    [

        [
        ("Numeric_Keys"),
        ({'side':'top','expand':'yes','fill':'both'}),
        [
            ("7","8","9"),
            ("4","5","6"),
            ("1","2","3"),
            ("0")
        ]
        ]

    ]
]

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
        self.entry_count = 0
        self.top = Toplevel()

        #region MAIN SETTINGS AND BACKGROUND
        self.top.title("Einstellungen")
        self.top.geometry(f"{width}x{height}") #Define the size of the tkinter frame
        if not "win" in sys.platform: # if execute on rpi get fullscreen
            self.top.attributes("-fullscreen", True)
        else:
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

        InputLevel.loadKeyboard(self)

    def loadTopBar(self):
        '''load all elements on top area'''
        
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
        '''load all elements from containers'''
        
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
                                      width=29, 
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
        self.container_name.place(x=20, y=41) 

        self.entry_name = customtkinter.CTkEntry(master=self.container_input, # ENTRY NAME
                                                placeholder_text="Container Name..", 
                                                text_font=(TEXT_FONT, STANDARD_FONTSIZE),
                                                placeholder_text_color="white",
                                                text_color="white",
                                                bg_color="white",
                                                fg_color=TEXT_BORDER_COLOR,
                                                corner_radius=8,
                                                width=300)
        self.entry_name.bind("<FocusIn>", lambda event: InputLevel.changeInputFocus(self, 1))
        self.entry_name.place(x=20, y=62)


        self.container_kcal = Label(self.container_input, # NAME OF ENTRY
                                      text="Kcal/100g",
                                      bg="white", 
                                      width=10, 
                                      justify=LEFT,
                                      anchor="w",
                                      font=(TEXT_FONT, SMALL_FONTSIZE)) 
        self.container_kcal.place(x=380, y=41) 

        self.entry_kcal = customtkinter.CTkEntry(master=self.container_input, # ENTRY KCAL
                                                placeholder_text="Kcal..", 
                                                text_font=(TEXT_FONT, STANDARD_FONTSIZE),
                                                placeholder_text_color="white",
                                                text_color="white",
                                                bg_color="white",
                                                fg_color=TEXT_BORDER_COLOR,
                                                corner_radius=8,
                                                width=300)
        self.entry_kcal.bind("<FocusIn>", lambda event: InputLevel.changeInputFocus(self, 2))
        self.entry_kcal.place(x=380, y=62)

        customtkinter.CTkFrame(master=self.container_input, # BORDER 2
                               width=self.container_input.winfo_reqwidth(),
                               height=2,
                               corner_radius=10,
                               fg_color=ACCENTS_BG_COLOR).place(x=0, y=102)


        self.container_fat = Label(self.container_input, # NAME OF ENTRY
                                      text="Fett/100g",
                                      bg="white", 
                                      width=10, 
                                      justify=LEFT,
                                      anchor="w",
                                      font=(TEXT_FONT, SMALL_FONTSIZE)) 
        self.container_fat.place(x=20, y=108) 

        self.entry_fat = customtkinter.CTkEntry(master=self.container_input, # ENTRY FAT
                                                placeholder_text="Fett..", 
                                                text_font=(TEXT_FONT, STANDARD_FONTSIZE),
                                                placeholder_text_color="white",
                                                text_color="white",
                                                bg_color="white",
                                                fg_color=TEXT_BORDER_COLOR,
                                                corner_radius=8,
                                                width=300)
        self.entry_fat.bind("<FocusIn>", lambda event: InputLevel.changeInputFocus(self, 3))                                        
        self.entry_fat.place(x=20, y=129)


        self.container_sugar = Label(self.container_input, # NAME OF ENTRY
                                      text="Zucker/100g",
                                      bg="white", 
                                      width=10, 
                                      justify=LEFT,
                                      anchor="w",
                                      font=(TEXT_FONT, SMALL_FONTSIZE)) 
        self.container_sugar.place(x=380, y=108) 

        self.entry_sugar = customtkinter.CTkEntry(master=self.container_input, # ENTRY SUGAR
                                                placeholder_text="Zucker..", 
                                                text_font=(TEXT_FONT, STANDARD_FONTSIZE),
                                                placeholder_text_color="white",
                                                text_color="white",
                                                bg_color="white",
                                                fg_color=TEXT_BORDER_COLOR,
                                                corner_radius=8,
                                                width=300)
        self.entry_sugar.bind("<FocusIn>", lambda event: InputLevel.changeInputFocus(self, 4))                                                  
        self.entry_sugar.place(x=380, y=129)

        customtkinter.CTkFrame(master=self.container_input, # BORDER 3
                               width=self.container_input.winfo_reqwidth(),
                               height=2,
                               corner_radius=10,
                               fg_color=ACCENTS_BG_COLOR).place(x=0, y=174)




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
        self.button_save.place(x=400, y=433, anchor=CENTER)

    def loadBottomBar(self):
        '''load all elements on bottom area'''
        
        Frame(self.top, 
              height=25, 
              width=800, 
              bg=BOTTOM_BORDER_BG_COLOR).place(x=BORDER_BOT_X,y=BORDER_BOT_Y)
        Frame(self.top,
            height=3,
            width=800,
            bg=BORDER_ACCENTS_BG_COLOR).place(x=0, y=452)

    def button_command(self, event):
        '''button functions when spacing or using backspace'''
        
        try:
            entry_instance = InputLevel.inputFocus(self, self.entry_count)
            if event == "<": # delete last character if backspace
                entry_instance.delete(len(entry_instance.get())-1, END)
            elif event == "Space":
                entry_instance.insert(END, " ")
            else: 
                entry_instance.insert(END, event)

        except AttributeError:
            return

    def create_frames_and_buttons(self):
        '''create main frame for keyboard'''
        
        for key_section in keys:
            store_section = Frame(self.top)
            if keys[0][0][0] ==  key_section[0][0]: # if 
                store_section.place(x=59, y=220)
            elif keys[1][0][0] ==  key_section[0][0]:
                store_section.place(x=581, y=220)

            for layer_name, layer_properties, layer_keys in key_section:
                store_layer = LabelFrame(store_section)#, text=layer_name)
                store_layer.pack(layer_properties)
                for key_bunch in layer_keys:
                    store_key_frame = Frame(store_layer)
                    store_key_frame.pack(side='top',expand='yes',fill='both')
                    for k in key_bunch:
                        if len(k)<=3:
                            if not "win" in sys.platform: 
                                store_button = Button(store_key_frame, text=k, width=3, height=2)
                            else:
                                store_button = Button(store_key_frame, text=k, width=6, height=2)

                        else:
                            store_button = Button(store_key_frame, text=k.center(5,' '), height=2)

                        store_button['relief']="sunken"
                        store_button['bg']="#2f49cf"
                        store_button['fg']="white"
                        store_button['command']=lambda q=k: InputLevel.button_command(self, event=q)
                        store_button.pack(side='left',fill='both',expand='yes')

    def create_container_shadow(master, width, height, color, posx, posy):
        '''create shadow effect of container/buttons'''
        
        customtkinter.CTkFrame(master=master,
                               width=width + 1,
                               height=height + 1,
                               corner_radius = 3,
                               fg_color = color).place(x=posx - 2, y=posy - 2)     

    def isFloat(list):
        '''check if tuple list are float values or not'''
        
        try:
            for element in list:
                float(element)
            return True
        except ValueError:
            return False

    def maxLength(element):
        '''check if element reached max size of 10'''
        
        if len(element) >= 10:
            return False
        return True

    def Save(self):
        '''save all inputs into config'''
        
        listentries = (self.entry_kcal.get(),self.entry_fat.get(),self.entry_sugar.get())
        if not InputLevel.isFloat(listentries): # if not float value return
            return

        if not InputLevel.maxLength(str(self.entry_name.get())):
            return

        UiFunc.writeConfigFile("c"+ str(self.c_count), "name", str(self.entry_name.get()).capitalize())
        UiFunc.writeConfigFile("c"+ str(self.c_count), "kcal", str(self.entry_kcal.get()))
        UiFunc.writeConfigFile("c"+ str(self.c_count), "fat", str(self.entry_fat.get()))
        UiFunc.writeConfigFile("c"+ str(self.c_count), "sugar", str(self.entry_sugar.get()))
        
        if self.c_count == 1:
            self.instance.container_1_settings.configure(text=str(self.entry_name.get()).capitalize())
        if self.c_count == 2:
            self.instance.container_2_settings.configure(text=str(self.entry_name.get()).capitalize())
        if self.c_count == 3:
            self.instance.container_3_settings.configure(text=str(self.entry_name.get()).capitalize())
            
        UiFunc.closeTopLevel(self)

    def loadContainerValues(self):
        '''load container values when opening window'''
        
        config = UiFunc.readConfigFile()
        self.entry_name.insert(END, config.get("c"+ str(self.c_count), "name"))
        self.entry_kcal.insert(END, config.get("c"+ str(self.c_count), "kcal"))
        self.entry_fat.insert(END, config.get("c"+ str(self.c_count), "fat"))
        self.entry_sugar.insert(END, config.get("c"+ str(self.c_count), "sugar"))

    def loadKeyboard(self):
        '''load keyboard into self instance'''
        
        InputLevel.create_frames_and_buttons(self)

    def changeInputFocus(self, entry):
        '''get focus of textfields - knowing which textfield needs to be changed with keyboard'''

        self.entry_count = entry
        print(self.entry_count)

    def inputFocus(self, entry):
        '''translate focus of textfield into label'''
        
        print("input")
        if entry == 1:
            return self.entry_name
        elif entry == 2:
            return self.entry_kcal
        elif entry == 3:
            return self.entry_fat
        elif entry == 4:
            return self.entry_sugar
        else:
            return None
