import tkinter
from customtkinter.customtkinter_label import CTkLabel
from customtkinter.customtkinter_button import CTkButton
from customtkinter.customtkinter_color_manager import CTkColorManager

from config.config import BUTTON_HOVER_BG_COLOR, BUTTON_BG_COLOR, TEXT_FONT, STANDARD_FONTSIZE, WINDOW_BG_COLOR
from ui.ui_functions import UiFunc

class CTkDialog:
    def __init__(self,
                 master=None,
                 title="Warnung",
                 text="CTkDialog",
                 declinebutton_text="Nein",
                 acceptbutton_text="Ja",
                 fg_color=BUTTON_BG_COLOR,
                 hover_color=BUTTON_HOVER_BG_COLOR):
        self.master = master

        self.user_input = None

        self.height = 125
        self.width = 280

        self.fg_color = CTkColorManager.MAIN if fg_color == "CTkColorManager" else fg_color
        self.hover_color = CTkColorManager.MAIN_HOVER if hover_color == "CTkColorManager" else hover_color

        self.top = tkinter.Toplevel()
        self.top.geometry(f"{self.width}x{self.height}")
        self.top.resizable(False, False)
        self.top.title(title)
        self.top.lift()
        self.top.focus_force()
        self.top.grab_set()


        self.button_frame = tkinter.Frame(master=self.top,
                                                    width=self.width,
                                                    background=WINDOW_BG_COLOR,
                                                    height=125)
        self.button_frame.place(x=0, y=0)

        self.myLabel = CTkLabel(master=self.button_frame, # text question frame
                                text=text,
                                width=self.width,
                                text_font=(TEXT_FONT, STANDARD_FONTSIZE),
                                height=45)
        self.myLabel.place(x=0, y=0)


        self.ok_button = CTkButton(master=self.button_frame,
                                   text=acceptbutton_text,
                                   width=100,
                                   command=self.ok_event,
                                   fg_color=self.fg_color,
                                   bg_color=WINDOW_BG_COLOR,
                                   text_color="white",
                                   hover_color=self.hover_color)
        self.ok_button.place(relx=0.28, rely=0.75, anchor=tkinter.CENTER)

        self.cancel_button = CTkButton(master=self.button_frame,
                                       text=declinebutton_text,
                                       width=100,
                                       command=self.cancel_event,
                                       fg_color=self.fg_color,
                                       bg_color=WINDOW_BG_COLOR,
                                       text_color="white",
                                       hover_color=self.hover_color)
        self.cancel_button.place(relx=0.72, rely=0.75, anchor=tkinter.CENTER)

    def ok_event(self):
        UiFunc.serve()
        self.top.destroy()

    def cancel_event(self):
        self.top.destroy()
