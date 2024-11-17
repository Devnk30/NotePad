import os
from tkinter import *
from data.notepad_root import Notepad


class Help_menus(Notepad):
    """
    A class to create and manage the "Help" menu for the Notepad application.
    It includes options for "About" and a "Personalization Guide."
    """

    def __init__(self):
        """
        Initialize the Help_menus class by loading required images for the Help menu.
        """
        super().__init__()

        # Load images used in the help menu.
        self._about_helpmenu = PhotoImage(
            file=os.path.join(self._xpath_images, "about_helpmenu.png")
        )
        self._image_notepad = PhotoImage(
            file=os.path.join(self._xpath_images, "NotePad_helpmenu.png")
        )
        self._guide_font_image1 = PhotoImage(
            file=os.path.join(self._xpath_images, "notepad_font_menu_image_guide1.png")
        )
        self._guide_font_image2 = PhotoImage(
            file=os.path.join(self._xpath_images, "notepad_font_menu_image_guide2.png")
        )
        self._guide_font_image3 = PhotoImage(
            file=os.path.join(self._xpath_images, "notepad_font_menu_image_guide3.png")
        )
        self._guide_colorbook_image1 = PhotoImage(
            file=os.path.join(
                self._xpath_images, "notepad_colorbook_menu_image_guide1.png"
            )
        )

    def _add_help_menus(self):
        """
        Add the "Help" menu to the main menu bar and configure its options.
        """

        # Add the "Help" menu to the menu bar.
        self._menubar.add_cascade(
            label="  Help  ",
            menu=self._help_menu,
            font=(
                "Ubuntu Sans",
                "10",
                "bold italic",
            ),
        )
        # Configure the appearance of the "Help" menu.
        self._help_menu.config(
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
        # Add "About" and "Personalization Guide" commands to the Help menu.
        self._help_menu.add_command(
            image=self._about_helpmenu,
            label=f"   About...{25 * " "}",
            compound="left",
            command=self._about,
        )
        self._help_menu.add_command(
            label=f"Personalization guide...",
            command=self._personalization_guide,
        )

    def _about(self):
        """
        Display the "About" dialog with information about the application.
        """

        self.__help_toplevel = Toplevel(
            width=450, height=380, bg=self._color2, padx=30, pady=30
        )
        self.__help_toplevel.title("About Notepad")
        self.__help_toplevel.transient(
            self._root
        )  # Keeps the dialog on top of the main window.
        self.__help_toplevel.grid_propagate(
            0
        )  # Prevents resizing based on widget content.
        self.__help_toplevel.resizable(0, 0)  # Disables resizing the dialog window.
        self.__help_toplevel.grab_set()  # Prevents interacting with other windows until closed.

        # Add labels for application information and an image.
        Label(
            self.__help_toplevel,
            image=self._image_notepad,
            bg=self._color2,
            relief="flat",
        ).grid(row=0, column=0, padx=84, sticky="nswe")

        Label(
            self.__help_toplevel,
            text="Notepad",
            bg=self._color2,
            fg=self._color1,
            font=(self._font, "10", self._fontstyle),
            relief="flat",
        ).grid(row=1, column=0, padx=84, pady=(10, 0), sticky="nswe")

        # Additional details about the application.
        Label(
            self.__help_toplevel,
            text="1.0.0",
            bg=self._color2,
            fg=self._color1,
            font=(self._font, "10", self._fontstyle),
            relief="flat",
        ).grid(row=2, column=0, padx=84, sticky="nswe")

        Label(
            self.__help_toplevel,
            text="Developed by: Devnk30",
            bg=self._color2,
            fg=self._color1,
            font=("Ubuntu Sans", "10", "italic"),
            relief="flat",
        ).grid(row=3, column=0, padx=84, sticky="nswe")

        Label(
            self.__help_toplevel,
            text="Release date: 30/10/2024",
            bg=self._color2,
            fg=self._color1,
            font=(self._font, "10", self._fontstyle),
            relief="flat",
        ).grid(row=4, column=0, padx=84, pady=5, sticky="nswe")

        Label(
            self.__help_toplevel,
            text="A simple and customizable notepad.",
            bg=self._color2,
            fg=self._color1,
            font=(self._font, "10", self._fontstyle),
            relief="flat",
        ).grid(row=5, column=0, padx=84, sticky="nswe")

        Label(
            self.__help_toplevel,
            text="GitHub",
            bg=self._color2,
            fg=self._color1,
            font=(self._font, "10", self._fontstyle),
            relief="flat",
        ).grid(row=6, column=0, padx=84, pady=5, sticky="nswe")

        # Add a "Close" button to dismiss the dialog.
        Button(
            self.__help_toplevel,
            text="Close",
            bg=self._color12,
            activebackground=self._color1,
            fg=self._color1,
            activeforeground=self._color12,
            relief="flat",
            highlightthickness=0,
            highlightcolor=self._color1,
            width=10,
            font=(self._font, "10", self._fontstyle),
            command=self.__help_toplevel.destroy,
        ).place(x=275, y=290)

    def _personalization_guide(self):
        """
        Display the "Personalization Guide" dialog with instructions on customizing the application.
        """

        self.__guide_toplevel = Toplevel(
            width=620, height=970, bg=self._color2, padx=30, pady=30
        )
        self.__guide_toplevel.title("Personalization Guide")
        self.__guide_toplevel.transient(
            self._root
        )  # Keeps the dialog on top of the main window.
        self.__guide_toplevel.grid_propagate(
            0
        )  # Prevents resizing based on widget content.
        self.__guide_toplevel.resizable(0, 0)  # Disables resizing the dialog window.
        self.__guide_toplevel.grab_set()  # Prevents interacting with other windows until closed.

        # Add instructions and images for the guide.
        Label(
            self.__guide_toplevel,
            text="Font options:",
            bg=self._color2,
            fg=self._color1,
            justify="left",
            font=(self._font, "10", "underline"),
            relief="flat",
        ).grid(row=0, column=0, sticky="w")

        Label(
            self.__guide_toplevel,
            text="    The entry above the options shows the currently selected option, and the label below\n    with the letters (AaBb YyZz) shows an example of what those changes would look like.\n    Simply select the option you want and then apply the changes by pressing the accept button.",
            bg=self._color2,
            fg=self._color1,
            justify="left",
            font=(self._font, "10", self._fontstyle),
            relief="flat",
        ).grid(row=1, column=0, columnspan=3, sticky="w")

        # Example images for font customization.
        Label(
            self.__guide_toplevel,
            image=self._guide_font_image1,
            bg=self._color2,
            relief="solid",
        ).grid(row=2, column=0, pady=10, sticky="w")

        Label(
            self.__guide_toplevel,
            image=self._guide_font_image3,
            bg=self._color2,
        ).grid(row=2, column=1, padx=10, pady=10, sticky="nswe")

        Label(
            self.__guide_toplevel,
            image=self._guide_font_image2,
            bg=self._color2,
            relief="solid",
        ).grid(row=2, column=2, pady=10, sticky="w")

        # More instructions for color themes and palette customization.
        Label(
            self.__guide_toplevel,
            text="Color book options:",
            bg=self._color2,
            fg=self._color1,
            justify="left",
            font=(self._font, "10", "underline"),
            relief="flat",
        ).grid(row=3, column=0, sticky="w")

        Label(
            self.__guide_toplevel,
            text="    Color Book is a tool for creating and managing color themes.\n\n    Name theme --> Enter the name of the topic you want to create or delete.\n    Add button (+) --> Adds a new theme based on the current colors and settings with\n    the name given in Name theme.\n    Delete button (trash icon) --> Deletes the theme with the name given in Name theme.\n    Themes --> A drop-down menu showing the available themes. The theme shown is the\n    theme currently being used.\n    Text --> Select the color of the text.\n    Background --> Select the color of the background.\n    Sample Label --> Displays an example of the text with the selected colors for the text and\n    background.",
            bg=self._color2,
            fg=self._color1,
            justify="left",
            font=(self._font, "10", self._fontstyle),
            relief="flat",
        ).grid(row=4, column=0, columnspan=3, sticky="w")

        Label(
            self.__guide_toplevel,
            text="    Palette color: {\n        color1: text color,\n        color2: background color,\n        color3: menu background color,\n        color4: shortcut menu background color\n        color5: root, notebook background color,\n        color6: tabs text color,\n        color7: tabs background color,\n        color8: label lines background color\n        color9: scrollbar trough color\n        color10: scrollbar activebackground color,\n        color11: scrollbar background color,\n        color12: entry and button background color,\n        color13: search tags text color,\n        color14: search tags background color,\n        color15: search tags next and previous text color,\n        color16: search tags next and previous background color,\n        color17: replace tags text color,\n        color18:  replace tags background color,\n    }",
            bg=self._color2,
            fg=self._color1,
            justify="left",
            compound="left",
            font=(self._font, "10", self._fontstyle),
            relief="flat",
        ).grid(row=5, column=0, columnspan=3, sticky="w")

        # Add a "Close" button to dismiss the guide.
        Button(
            self.__guide_toplevel,
            text="Close",
            bg=self._color12,
            activebackground=self._color1,
            fg=self._color1,
            activeforeground=self._color12,
            relief="flat",
            highlightthickness=0,
            highlightcolor=self._color1,
            width=10,
            font=("Ubuntu Sans", "10", "italic"),
            command=self.__guide_toplevel.destroy,
        ).grid(row=6, column=2, pady=(5, 0), sticky="e")
