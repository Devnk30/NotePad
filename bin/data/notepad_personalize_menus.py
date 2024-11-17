import os
from tkinter import PhotoImage
from data.notepad_font_menu import Font_menu
from data.notepad_colorbook_menu import Colorbook_menu


class Personalize_menu(Font_menu, Colorbook_menu):
    def __init__(self):
        super().__init__()
        # colorbook_personalizemenu.png
        self._colorbook_personalizemenu_image = PhotoImage(
            file=os.path.join(self._xpath_images, "colorbook_personalizemenu.png")
        )
        self._font_personalizemenu_image = PhotoImage(
            file=os.path.join(self._xpath_images, "font_personalizemenu.png")
        )

    def _add_personalize_menu(self):
        self._menubar.add_cascade(
            label="  Personalize  ",
            menu=self._personlize_menu,
            font=(
                "Ubuntu Sans",
                "10",
                "bold italic",
            ),
        )
        self._personlize_menu.config(
            background=self._color3,
            activebackground=self._color1,
            foreground=self._color1,
            font=(
                "Ubuntu Sans",
                "10",
                "bold italic",
            ),
            relief="flat",
        )
        self._personlize_menu.add_command(
            image=self._font_personalizemenu_image,
            label=f"   Font...{25 * " "}",
            compound="left",
            command=self._add_font_menu,
        )
        self._personlize_menu.add_command(
            image=self._colorbook_personalizemenu_image,
            label="   Colorbook...",
            compound="left",
            command=self._add_colorbook_menu,
        )
