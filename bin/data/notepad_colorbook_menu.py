import os, json, re
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from data.notepad_shortcut_menu import Shortcut_menu


class Colorbook_menu(Shortcut_menu):
    """
    Class to manage a color theme menu in the application.
    Allows you to create, delete, and select color themes, as well as update colors in real time.
    Inherits from Shortcut_menu.

    Attributes:
    _create_themeicon: Image for the theme creation button.
    _delete_themeicon: Image for the theme deletion button.
    """

    def __init__(self):
        """Initializes the color theme menu and loads the necessary images."""
        super().__init__()
        # Load icon images from the defined path
        self._create_themeicon = PhotoImage(
            file=os.path.join(self._xpath_images, "create_theme.png")
        )
        self._delete_themeicon = PhotoImage(
            file=os.path.join(self._xpath_images, "delete_theme.png")
        )

    def __colorbook_menu(self):
        """
        Create and configure the color theme management window.
        Includes inputs for theme name, buttons for creating/deleting themes,
        and items for selecting custom colors.
        """

        # Create a secondary window (Toplevel) for the theme menu
        self.__colorbook_toplevel = Toplevel(
            padx=30,
            pady=20,
            bg=self._color2,  # Window background color
        )
        self.__colorbook_toplevel.title("Color Book")
        self.__colorbook_toplevel.pack_propagate(False)  # Disable auto resize
        self.__colorbook_toplevel.resizable(0, 0)  # Disable manual resizing

        self.__colorbook_toplevel.transient(
            self._root
        )  # Attach the window to the main root
        self.__colorbook_toplevel.grab_set()  # Block interaction with other windows
        self.__colorbook_toplevel.protocol(
            "WM_DELETE_WINDOW", self.__colorbook_toplevel.destroy
        )  # Handle window closing

        # Section: Input for theme name and action buttons
        self._frame_sel_theme = Frame(
            self.__colorbook_toplevel, bg=self._color2, height=50
        )
        self._frame_sel_theme.grid(row=0, column=0, sticky="we")

        # Label for the theme name
        Label(
            self._frame_sel_theme,
            font=(self._font, "10", self._fontstyle),
            text="Name theme:",
            bg=self._color2,
            fg=self._color1,
        ).grid(row=0, column=0, padx=10, pady=10, sticky="nswe")

        # Input field for the theme name
        self._themes_entry = Entry(
            self._frame_sel_theme,
            bg=self._color12,  # Field background
            fg=self._color1,  # Text color
            justify="center",  # Center alignment
            relief="flat",  # No border
            highlightthickness=1,  # Focus border thickness
            highlightbackground=self._color1,  # Border color in normal state
            highlightcolor=self._color1,  # Border color on focus
            insertbackground=self._color1,  # Insertbar color
            selectbackground=self._color1,  # Background when selecting text
            selectforeground=self._color2,  # Text color when selecting text
            font=("Ubuntu Sans", "10", "italic"),
        )
        self._themes_entry.grid(row=0, column=1, padx=20, pady=10, sticky="nswe")

        # Button to create a new theme
        self.__create_theme_button = Button(
            self._frame_sel_theme,
            image=self._create_themeicon,  # Button icon
            bg=self._color2,
            activebackground=self._color1,
            width=34,
            relief="flat",
            highlightthickness=0,
            highlightcolor=self._color1,
            borderwidth=0,
            command=self.__create_theme,
        )
        self.__create_theme_button.grid(row=0, column=2, pady=10)

        # Button to delete an existing theme
        self.__delete_theme_button = Button(
            self._frame_sel_theme,
            image=self._delete_themeicon,
            bg=self._color2,
            activebackground=self._color1,
            width=34,
            relief="flat",
            highlightthickness=0,
            highlightcolor=self._color1,
            borderwidth=0,
            command=self.__delete_theme,
        )
        self.__delete_theme_button.grid(row=0, column=3, padx=10, pady=10)

        Label(
            self._frame_sel_theme,
            font=(self._font, "10", self._fontstyle),
            text="Themes:",
            bg=self._color2,
            fg=self._color1,
        ).grid(row=1, column=0, padx=10, pady=10, sticky="nswe")

        # Sets the visual style of Comboboxes of type TCombobox
        self.style.configure(
            "TCombobox",
            foreground=self._color1,
            borderwidth=0.3,
            selectbackground=self._color1,
            selectforeground=self._color12,
            padding=(0, 3, 0, 3),
            relief="flat",
        )
        self.style.map(
            "TCombobox",
            background=[
                ("active", self._color10),
                ("readonly", self._color11),
            ],
            fieldbackground=[("readonly", self._color12)],
            arrowcolor=[
                ("active", self._color1),
                ("readonly", self._color1),
            ],
        )

        # Creates a frame that serves as a border for the Combobox, with a background color (bg) and a thin border (bd=0.5).
        self._bordercolor_combobox = Frame(
            self._frame_sel_theme, bg=self._color1, bd=0.5
        )
        self._bordercolor_combobox.grid(row=1, column=1, padx=20, pady=10)

        # Create a Combobox to select themes
        # Use values ​​as the available options (self._saved_themes).
        # Store the selected option in a variable (self._selected_theme).
        # Apply the TCombobox style.
        # Set the state to readonly to avoid manual input.
        self._combobox_themes = ttk.Combobox(
            self._bordercolor_combobox,
            values=self._saved_themes,
            textvariable=self._selected_theme,
            justify="center",
            cursor="hand2",
            font=(
                self._font,
                "10",
                self._fontstyle,
            ),
            state="readonly",
            style="TCombobox",
        )

        # Customize the Combobox dropdown list
        # Set colors for the background, text, and selection.
        # Apply a custom font.
        self._root.option_add("*TCombobox*Listbox.background", self._color12)
        self._root.option_add(
            "*TCombobox*Listbox.font", (self._font, "10", self._fontstyle)
        )
        self._root.option_add("*TCombobox*Listbox.foreground", self._color1)
        self._root.option_add("*TCombobox*Listbox.selectBackground", self._color1)
        self._root.option_add("*TCombobox*Listbox.selectForeground", self._color12)

        self._combobox_themes.grid(sticky="nswe")

        # Button frame that allows you to select text and background colors.
        self._frame_background_and_text = Frame(
            self.__colorbook_toplevel, bg=self._color2, height=50
        )
        self._frame_background_and_text.grid(row=1, column=0, pady=5, sticky="we")

        # Defines two buttons that allow you to change the text color (self._color_text) and the background color (self._color_background).
        Label(
            self._frame_background_and_text,
            font=(self._font, "10", self._fontstyle),
            text="Text:",
            bg=self._color2,
            fg=self._color1,
        ).grid(row=0, column=0, padx=(155, 10), pady=(0, 5), sticky="nswe")

        self._color_text = Button(
            self._frame_background_and_text,
            bg=self._color1,
            width=0,
            activebackground=self._color1,
            highlightthickness=0,
            highlightcolor=self._color1,
            relief="solid",
            cursor="hand2",
            font=(
                self._font,
                "2",
                self._fontstyle,
            ),
            command=lambda: self.__update_color(self._color1, "color1"),
        )
        self._color_text.grid(row=1, column=0, padx=(155, 10), pady=(0, 3))

        Label(
            self._frame_background_and_text,
            font=(self._font, "10", self._fontstyle),
            text="Background:",
            bg=self._color2,
            fg=self._color1,
        ).grid(row=0, column=1, padx=(5, 0), pady=(0, 5), sticky="nswe")

        self._color_background = Button(
            self._frame_background_and_text,
            bg=self._color2,
            width=0,
            activebackground=self._color2,
            highlightthickness=0,
            highlightcolor=self._color2,
            relief="solid",
            cursor="hand2",
            font=(
                self._font,
                "2",
                self._fontstyle,
            ),
            command=lambda: self.__update_color(self._color2, "color2"),
        )
        self._color_background.grid(row=1, column=1, pady=(0, 3))

        # Sets the visual style of Labelframe of type TLabelframe and TLabelframe.Label
        self.style.configure("TLabelframe", background=self._color2)
        self.style.configure(
            "TLabelframe.Label",
            background=self._color2,
            foreground=self._color1,
            font=(self._font, "10", self._fontstyle),
        )

        # shows a sample of how the text and background color looks
        self.__labelframe_sample = ttk.Labelframe(
            self.__colorbook_toplevel,
            text=" Sample Label ",
            style="TLabelframe",
            relief="solid",
            border=1,
        )
        self.__labelframe_sample.grid(row=2, column=0, sticky="nswe")

        self.__label_sample = Label(
            self.__labelframe_sample,
            height=5,
            text="AaBb YyZz",
            bg=self._color2,
            fg=self._color1,
            justify="center",
            font=("Ubuntu Sans", "12", "normal italic"),
        )
        self.__label_sample.pack(fill="both", padx=10, pady=(0, 10))

        # This frame contains a series of buttons that act as a color palette.
        self._frame_palette_color = Frame(self.__colorbook_toplevel, bg=self._color2)
        self._frame_palette_color.grid(row=3, column=0, pady=20, sticky="we")

        Label(
            self._frame_palette_color,
            font=(self._font, "10", self._fontstyle),
            text="Palette color:",
            justify="center",
            bg=self._color2,
            fg=self._color1,
        ).grid(row=0, column=0, rowspan=2, padx=10, pady=10, sticky="nswe")

        self._button_color1 = Button(
            self._frame_palette_color,
            bg=self._color1,
            width=0,
            activebackground=self._color1,
            highlightthickness=0,
            highlightcolor=self._color1,
            relief="solid",
            cursor="hand2",
            font=(
                self._font,
                "2",
                self._fontstyle,
            ),
            command=lambda: self.__update_color(self._color1, "color1"),
        )
        self._button_color1.grid(row=0, column=1)

        self._button_color2 = Button(
            self._frame_palette_color,
            bg=self._color2,
            width=0,
            activebackground=self._color2,
            highlightthickness=0,
            highlightcolor=self._color2,
            relief="solid",
            cursor="hand2",
            font=(
                self._font,
                "2",
                self._fontstyle,
            ),
            command=lambda: self.__update_color(self._color2, "color2"),
        )
        self._button_color2.grid(row=0, column=2, padx=5)

        self._button_color3 = Button(
            self._frame_palette_color,
            bg=self._color3,
            width=0,
            activebackground=self._color3,
            highlightthickness=0,
            highlightcolor=self._color3,
            relief="solid",
            cursor="hand2",
            font=(
                self._font,
                "2",
                self._fontstyle,
            ),
            command=lambda: self.__update_color(self._color3, "color3"),
        )
        self._button_color3.grid(row=0, column=3)

        self._button_color4 = Button(
            self._frame_palette_color,
            bg=self._color4,
            width=0,
            activebackground=self._color4,
            highlightthickness=0,
            highlightcolor=self._color4,
            relief="solid",
            cursor="hand2",
            font=(
                self._font,
                "2",
                self._fontstyle,
            ),
            command=lambda: self.__update_color(self._color4, "color4"),
        )
        self._button_color4.grid(row=0, column=4, padx=5)

        self._button_color5 = Button(
            self._frame_palette_color,
            bg=self._color5,
            width=0,
            activebackground=self._color5,
            highlightthickness=0,
            highlightcolor=self._color5,
            relief="solid",
            cursor="hand2",
            font=(
                self._font,
                "2",
                self._fontstyle,
            ),
            command=lambda: self.__update_color(self._color5, "color5"),
        )
        self._button_color5.grid(row=0, column=5)

        self._button_color6 = Button(
            self._frame_palette_color,
            bg=self._color6,
            width=0,
            activebackground=self._color6,
            highlightthickness=0,
            highlightcolor=self._color6,
            relief="solid",
            cursor="hand2",
            font=(
                self._font,
                "2",
                self._fontstyle,
            ),
            command=lambda: self.__update_color(self._color6, "color6"),
        )
        self._button_color6.grid(row=0, column=6, padx=5)

        self._button_color7 = Button(
            self._frame_palette_color,
            bg=self._color7,
            width=0,
            activebackground=self._color7,
            highlightthickness=0,
            highlightcolor=self._color7,
            relief="solid",
            cursor="hand2",
            font=(
                self._font,
                "2",
                self._fontstyle,
            ),
            command=lambda: self.__update_color(self._color7, "color7"),
        )
        self._button_color7.grid(row=0, column=7)

        self._button_color8 = Button(
            self._frame_palette_color,
            bg=self._color8,
            width=0,
            activebackground=self._color8,
            highlightthickness=0,
            highlightcolor=self._color8,
            relief="solid",
            cursor="hand2",
            font=(
                self._font,
                "2",
                self._fontstyle,
            ),
            command=lambda: self.__update_color(self._color8, "color8"),
        )
        self._button_color8.grid(row=0, column=8, padx=5)

        self._button_color9 = Button(
            self._frame_palette_color,
            bg=self._color9,
            width=0,
            activebackground=self._color9,
            highlightthickness=0,
            highlightcolor=self._color9,
            relief="solid",
            cursor="hand2",
            font=(
                self._font,
                "2",
                self._fontstyle,
            ),
            command=lambda: self.__update_color(self._color9, "color9"),
        )
        self._button_color9.grid(row=0, column=9)

        self._button_color10 = Button(
            self._frame_palette_color,
            bg=self._color10,
            width=0,
            activebackground=self._color10,
            highlightthickness=0,
            highlightcolor=self._color10,
            relief="solid",
            cursor="hand2",
            font=(
                self._font,
                "2",
                self._fontstyle,
            ),
            command=lambda: self.__update_color(self._color10, "color10"),
        )
        self._button_color10.grid(row=1, column=1)

        self._button_color11 = Button(
            self._frame_palette_color,
            bg=self._color11,
            width=0,
            activebackground=self._color11,
            highlightthickness=0,
            highlightcolor=self._color11,
            relief="solid",
            cursor="hand2",
            font=(
                self._font,
                "2",
                self._fontstyle,
            ),
            command=lambda: self.__update_color(self._color11, "color11"),
        )
        self._button_color11.grid(row=1, column=2, padx=5)

        self._button_color12 = Button(
            self._frame_palette_color,
            bg=self._color12,
            width=0,
            activebackground=self._color12,
            highlightthickness=0,
            highlightcolor=self._color12,
            relief="solid",
            cursor="hand2",
            font=(
                self._font,
                "2",
                self._fontstyle,
            ),
            command=lambda: self.__update_color(self._color12, "color12"),
        )
        self._button_color12.grid(row=1, column=3)

        self._button_color13 = Button(
            self._frame_palette_color,
            bg=self._color13,
            width=0,
            activebackground=self._color13,
            highlightthickness=0,
            highlightcolor=self._color13,
            relief="solid",
            cursor="hand2",
            font=(
                self._font,
                "2",
                self._fontstyle,
            ),
            command=lambda: self.__update_color(self._color13, "color13"),
        )
        self._button_color13.grid(row=1, column=4, padx=5)

        self._button_color14 = Button(
            self._frame_palette_color,
            bg=self._color14,
            width=0,
            activebackground=self._color14,
            highlightthickness=0,
            highlightcolor=self._color14,
            relief="solid",
            cursor="hand2",
            font=(
                self._font,
                "2",
                self._fontstyle,
            ),
            command=lambda: self.__update_color(self._color14, "color14"),
        )
        self._button_color14.grid(row=1, column=5)

        self._button_color15 = Button(
            self._frame_palette_color,
            bg=self._color15,
            width=0,
            activebackground=self._color15,
            highlightthickness=0,
            highlightcolor=self._color15,
            relief="solid",
            cursor="hand2",
            font=(
                self._font,
                "2",
                self._fontstyle,
            ),
            command=lambda: self.__update_color(self._color15, "color15"),
        )
        self._button_color15.grid(row=1, column=6, padx=5)

        self._button_color16 = Button(
            self._frame_palette_color,
            bg=self._color16,
            width=0,
            activebackground=self._color16,
            highlightthickness=0,
            highlightcolor=self._color16,
            relief="solid",
            cursor="hand2",
            font=(
                self._font,
                "2",
                self._fontstyle,
            ),
            command=lambda: self.__update_color(self._color16, "color16"),
        )
        self._button_color16.grid(row=1, column=7)

        self._button_color17 = Button(
            self._frame_palette_color,
            bg=self._color17,
            width=0,
            activebackground=self._color17,
            highlightthickness=0,
            highlightcolor=self._color17,
            relief="solid",
            cursor="hand2",
            font=(
                self._font,
                "2",
                self._fontstyle,
            ),
            command=lambda: self.__update_color(self._color17, "color17"),
        )
        self._button_color17.grid(row=1, column=8, padx=5)

        self._button_color18 = Button(
            self._frame_palette_color,
            bg=self._color18,
            width=0,
            activebackground=self._color18,
            highlightthickness=0,
            highlightcolor=self._color18,
            relief="solid",
            cursor="hand2",
            font=(
                self._font,
                "2",
                self._fontstyle,
            ),
            command=lambda: self.__update_color(self._color18, "color18"),
        )
        self._button_color18.grid(row=1, column=9)

        Button(
            self.__colorbook_toplevel,
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
            command=self.__colorbook_toplevel.destroy,
        ).grid(row=4, column=0, pady=10, sticky="e")

    def __create_theme(self):

        # Check if the theme name input field is not empty
        if re.search(r"^[a-z]{3}[0-9a-z]*$", self._themes_entry.get()):
            # Open the configuration file and load the JSON content
            with open(
                os.path.join(self._xpath_configfile, "config.json"),
                "r",
            ) as f:
                self.json_file = json.load(f)

                # Check if the theme name already exists in the saved themes
                if self._themes_entry.get() in self._saved_themes:
                    messagebox.showwarning(
                        "Warning", "There is already a theme created with that name."
                    )
                    return

            # If the name is valid and does not exist, proceed to save the new theme
            with open(
                os.path.join(self._xpath_configfile, "config.json"),
                "w",
            ) as f:

                # Add the new theme with its colors to the JSON file
                self.json_file["themes"][self._themes_entry.get()] = {
                    "color1": self._color1,
                    "color2": self._color2,
                    "color3": self._color3,
                    "color4": self._color4,
                    "color5": self._color5,
                    "color6": self._color6,
                    "color7": self._color7,
                    "color8": self._color8,
                    "color9": self._color9,
                    "color10": self._color10,
                    "color11": self._color11,
                    "color12": self._color12,
                    "color13": self._color13,
                    "color14": self._color14,
                    "color15": self._color15,
                    "color16": self._color16,
                    "color17": self._color17,
                    "color18": self._color18,
                }

                # Save changes to JSON file
                json.dump(self.json_file, f, indent=2)

                # Update the list of saved themes
                self._saved_themes.clear()
                for theme in self.json_file["themes"]:
                    self._saved_themes.append(theme)

                # Configure the combobox with the updated themes
                self._combobox_themes.config(values=self._saved_themes)

            # Show success message when creating theme
            messagebox.showinfo("Info", "Theme created.")

        else:
            # Show warning if theme name is invalid
            messagebox.showwarning(
                "Warning", "Give a valid name to the theme you want to create."
            )
        self.json_file = {}

    def __delete_theme(self):

        try:
            # Check if theme name is 'default' and prevent deletion
            if self._themes_entry.get() == "default":
                messagebox.showwarning(
                    "Warning", '"default" is the default theme so it cannot be deleted.'
                )
                return

            # Open the configuration file and load the JSON content
            with open(
                os.path.join(self._xpath_configfile, "config.json"),
                "r",
            ) as f:
                self.json_file = json.load(f)
                # Remove the specified theme from the JSON file
                del self.json_file["themes"][self._themes_entry.get()]

            # Save changes to JSON file after deletion
            with open(
                os.path.join(self._xpath_configfile, "config.json"),
                "w",
            ) as f:
                json.dump(self.json_file, f, indent=2)

                # Update the list of saved themes
                self._saved_themes.clear()
                for theme in self.json_file["themes"]:
                    self._saved_themes.append(theme)

                # Configure the combobox with the updated themes
                self._combobox_themes.config(values=self._saved_themes)

                # Show success message when deleting theme
                messagebox.showinfo("Info", "Theme deleted.")

        except KeyError:
            # Show warning if theme name is invalid
            messagebox.showwarning(
                "Warning", "Give a valid name to the theme you want to delete."
            )

        self.json_file = {}

    def __update_color(self, color, colorname):

        # Release the capture of the main window (to prevent it from being in capture mode)
        self.__colorbook_toplevel.grab_release()

        # Create a new child window to update the color
        self.__updatecolor_toplevel = Toplevel(
            padx=20,
            pady=20,
            bg=self._color2,
        )
        self.__updatecolor_toplevel.title(f"Update Color")
        self.__updatecolor_toplevel.pack_propagate(False)
        self.__updatecolor_toplevel.resizable(0, 0)
        self.__updatecolor_toplevel.transient(self.__colorbook_toplevel)
        self.__updatecolor_toplevel.grab_set()

        # Create a label to display the current color
        self._updatecolor_label = Label(
            self.__updatecolor_toplevel,
            font=(self._font, "10", self._fontstyle),
            width=10,
            bg=color,
            relief="solid",
        )
        self._updatecolor_label.grid(row=0, column=0, padx=20, pady=10, sticky="nswe")

        # Create an input field where you can view and edit the hexadecimal value of the color
        self._updatecolor_entry = Entry(
            self.__updatecolor_toplevel,
            bg=self._color12,
            fg=self._color1,
            relief="flat",
            justify="center",
            highlightthickness=1,
            highlightbackground=self._color1,
            highlightcolor=self._color1,
            insertbackground=self._color1,
            selectbackground=self._color1,
            selectforeground=self._color2,
            font=("Ubuntu Sans", "10", "italic"),
        )
        self._updatecolor_entry.grid(row=0, column=1, padx=20, pady=10, sticky="nswe")

        # Create a slider to adjust the value of the red color (R)
        self.__red_silder = Scale(
            self.__updatecolor_toplevel,
            from_=0,
            to=255,
            bg=self._color2,
            fg=self._color1,
            troughcolor="#f01d1d",
            sliderrelief="flat",
            relief="flat",
            orient="horizontal",
            highlightthickness=0,
            activebackground=self._color10,
            cursor="hand2",
            font=(
                self._font,
                "10",
                self._fontstyle,
            ),
            command=lambda _: self.__update_color_slider(),
        )
        self.__red_silder.grid(row=1, column=0, columnspan=2, padx=20, sticky="nswe")

        # Create a slider to adjust the value of the green color (G)
        self.__green_slider = Scale(
            self.__updatecolor_toplevel,
            from_=0,
            to=255,
            bg=self._color2,
            fg=self._color1,
            troughcolor="#4cf01d",
            sliderrelief="flat",
            relief="flat",
            orient="horizontal",
            highlightthickness=0,
            activebackground=self._color10,
            cursor="hand2",
            font=(
                self._font,
                "10",
                self._fontstyle,
            ),
            command=lambda _: self.__update_color_slider(),
        )
        self.__green_slider.grid(
            row=2, column=0, columnspan=2, padx=20, pady=5, sticky="nswe"
        )

        # Create a slider to adjust the value of the blue color (B)
        self.__blue_slider = Scale(
            self.__updatecolor_toplevel,
            from_=0,
            to=255,
            bg=self._color2,
            fg=self._color1,
            troughcolor="#1d40f0",
            sliderrelief="flat",
            relief="flat",
            orient="horizontal",
            highlightthickness=0,
            activebackground=self._color10,
            cursor="hand2",
            font=(
                self._font,
                "10",
                self._fontstyle,
            ),
            command=lambda _: self.__update_color_slider(),
        )
        self.__blue_slider.grid(row=3, column=0, padx=20, columnspan=2, sticky="nswe")

        self.frameee = Frame(self.__updatecolor_toplevel, bg=self._color2)
        self.frameee.grid(
            row=4, column=0, columnspan=2, padx=20, pady=(30, 20), sticky="nswe"
        )

        # Create an "Update" button to confirm the color update
        Button(
            self.frameee,
            text="Update",
            bg=self._color12,
            activebackground=self._color1,
            fg=self._color1,
            activeforeground=self._color12,
            relief="flat",
            highlightthickness=0,
            highlightcolor=self._color1,
            width=10,
            font=("Ubuntu Sans", "10", "italic"),
            command=lambda: self._button_update(colorname),
        ).grid(row=0, column=0, padx=(25, 0), sticky="e")

        # Create a "Cancel" button to close the window without making changes
        Button(
            self.frameee,
            text="Cancel",
            bg=self._color12,
            activebackground=self._color1,
            fg=self._color1,
            activeforeground=self._color12,
            relief="flat",
            highlightthickness=0,
            highlightcolor=self._color1,
            width=10,
            font=("Ubuntu Sans", "10", "italic"),
            command=self.__updatecolor_toplevel.destroy,
        ).grid(row=0, column=1, padx=(25, 0), sticky="w")

    def __update_color_slider(self):
        # Get the values ​​of the sliders for the colors red, green and blue
        self._r = self.__red_silder.get()
        self._g = self.__green_slider.get()
        self._b = self.__blue_slider.get()

        # Create hexadecimal color from RGB values
        self._samplecolor = f"#{self._r:02x}{self._g:02x}{self._b:02x}"

        # Update the color label with the new color
        self._updatecolor_label.config(bg=self._samplecolor)

        # Update the input field with the new hexadecimal value
        self._updatecolor_entry.delete("0", END)
        self._updatecolor_entry.insert("0", self._samplecolor)

    def _button_update(self, colorname):

        # Updates the selected color and thus the widget that uses it

        match colorname:
            case "color1":
                self._color1 = self._updatecolor_entry.get()
                self._menubar.config(
                    activebackground=self._color1, foreground=self._color1
                )
                self._file_menu.config(
                    activebackground=self._color1, foreground=self._color1
                )
                self._edition_menu.config(
                    activebackground=self._color1, foreground=self._color1
                )
                self._personlize_menu.config(
                    activebackground=self._color1, foreground=self._color1
                )
                self._help_menu.config(
                    activebackground=self._color1, foreground=self._color1
                )
                self.style.map(
                    "Shortcut.TButton",
                    background=[("active", self._color1)],
                )
                self._get_select_text().config(
                    foreground=self._color1,
                    insertbackground=self._color1,
                    selectbackground=self._color1,
                )
                self.style.configure("Vertical.TScrollbar", arrowcolor=self._color1)
                self.style.map(
                    "Vertical.TScrollbar",
                    arrowcolor=[
                        ("active", self._color1),
                        ("disabled", self._color1),
                        ("pressed", self._color1),
                    ],
                )
                self._label_lines.config(foreground=self._color1)
                self.style.configure("TCheckbutton", foreground=self._color1)

                with open(
                    os.path.join(self._xpath_configfile, "config.json"),
                    "r",
                ) as f:
                    self.json_file = json.load(f)

                with open(
                    os.path.join(self._xpath_configfile, "config.json"),
                    "w",
                ) as f:

                    self.json_file["themes"][self._selected_theme.get()][
                        "color1"
                    ] = self._color1

                    json.dump(self.json_file, f, indent=2)

                self.__updatecolor_toplevel.destroy()
                self.__colorbook_toplevel.destroy()
                self._add_colorbook_menu()

            case "color2":
                self._color2 = self._updatecolor_entry.get()

                self._get_select_text().config(
                    background=self._color2,
                    selectforeground=self._color2,
                    highlightbackground=self._color2,
                )
                self.style.configure(
                    "TNotebook",
                    highlightbackground=self._color2,
                )
                self.style.map(
                    "Vertical.TScrollbar",
                    background=[
                        ("disabled", self._color2),
                    ],
                )
                self.style.configure(
                    "TCheckbutton",
                    background=self._color2,
                )
                self.style.map(
                    "TCheckbutton",
                    background=[("active", self._color2)],
                )

                with open(
                    os.path.join(self._xpath_configfile, "config.json"),
                    "r",
                ) as f:
                    self.json_file = json.load(f)

                with open(
                    os.path.join(self._xpath_configfile, "config.json"),
                    "w",
                ) as f:

                    self.json_file["themes"][self._selected_theme.get()][
                        "color2"
                    ] = self._color2

                    json.dump(self.json_file, f, indent=2)

                self.__updatecolor_toplevel.destroy()
                self.__colorbook_toplevel.destroy()
                self._add_colorbook_menu()

            case "color3":
                self._color3 = self._updatecolor_entry.get()
                self._file_menu.config(background=self._color3)
                self._edition_menu.config(background=self._color3)
                self._personlize_menu.config(background=self._color3)
                self._help_menu.config(background=self._color3)
                self._menubar.config(background=self._color3)

                with open(
                    os.path.join(self._xpath_configfile, "config.json"),
                    "r",
                ) as f:
                    self.json_file = json.load(f)

                with open(
                    os.path.join(self._xpath_configfile, "config.json"),
                    "w",
                ) as f:

                    self.json_file["themes"][self._selected_theme.get()][
                        "color3"
                    ] = self._color3

                    json.dump(self.json_file, f, indent=2)

                self.__updatecolor_toplevel.destroy()
                self.__colorbook_toplevel.destroy()
                self._add_colorbook_menu()

            case "color4":
                self._color4 = self._updatecolor_entry.get()
                self._shortcut_bar.config(background=self._color4)

                self.style.configure("Shortcut.TButton", background=self._color4)
                self.style.map(
                    "Shortcut.TButton",
                    background=[("disabled", self._color4)],
                )

                with open(
                    os.path.join(self._xpath_configfile, "config.json"),
                    "r",
                ) as f:
                    self.json_file = json.load(f)

                with open(
                    os.path.join(self._xpath_configfile, "config.json"),
                    "w",
                ) as f:

                    self.json_file["themes"][self._selected_theme.get()][
                        "color4"
                    ] = self._color4

                    json.dump(self.json_file, f, indent=2)

                self.__updatecolor_toplevel.destroy()
                self.__colorbook_toplevel.destroy()
                self._add_colorbook_menu()

            case "color5":
                self._color5 = self._updatecolor_entry.get()
                self._root.config(background=self._color5)
                self.style.configure("TNotebook", background=self._color5)

                with open(
                    os.path.join(self._xpath_configfile, "config.json"),
                    "r",
                ) as f:
                    self.json_file = json.load(f)

                with open(
                    os.path.join(self._xpath_configfile, "config.json"),
                    "w",
                ) as f:

                    self.json_file["themes"][self._selected_theme.get()][
                        "color5"
                    ] = self._color5

                    json.dump(self.json_file, f, indent=2)

                self.__updatecolor_toplevel.destroy()
                self.__colorbook_toplevel.destroy()
                self._add_colorbook_menu()

            case "color6":
                self._color6 = self._updatecolor_entry.get()
                self.style.configure("TNotebook.Tab", foreground=self._color6)
                self.style.map("TNotebook.Tab", foreground=[("selected", self._color6)])

                with open(
                    os.path.join(self._xpath_configfile, "config.json"),
                    "r",
                ) as f:
                    self.json_file = json.load(f)

                with open(
                    os.path.join(self._xpath_configfile, "config.json"),
                    "w",
                ) as f:

                    self.json_file["themes"][self._selected_theme.get()][
                        "color6"
                    ] = self._color6

                    json.dump(self.json_file, f, indent=2)

                self.__updatecolor_toplevel.destroy()
                self.__colorbook_toplevel.destroy()
                self._add_colorbook_menu()

            case "color7":
                self._color7 = self._updatecolor_entry.get()
                self.style.configure("TNotebook.Tab", background=self._color7)
                self.style.map("TNotebook.Tab", background=[("selected", self._color7)])

                with open(
                    os.path.join(self._xpath_configfile, "config.json"),
                    "r",
                ) as f:
                    self.json_file = json.load(f)

                with open(
                    os.path.join(self._xpath_configfile, "config.json"),
                    "w",
                ) as f:

                    self.json_file["themes"][self._selected_theme.get()][
                        "color7"
                    ] = self._color7

                    json.dump(self.json_file, f, indent=2)

                self.__updatecolor_toplevel.destroy()
                self.__colorbook_toplevel.destroy()
                self._add_colorbook_menu()

            case "color8":
                self._color8 = self._updatecolor_entry.get()
                self._label_lines.config(background=self._color8)

                with open(
                    os.path.join(self._xpath_configfile, "config.json"),
                    "r",
                ) as f:
                    self.json_file = json.load(f)

                with open(
                    os.path.join(self._xpath_configfile, "config.json"),
                    "w",
                ) as f:

                    self.json_file["themes"][self._selected_theme.get()][
                        "color8"
                    ] = self._color8

                    json.dump(self.json_file, f, indent=2)

                self.__updatecolor_toplevel.destroy()
                self.__colorbook_toplevel.destroy()
                self._add_colorbook_menu()

            case "color9":
                self._color9 = self._updatecolor_entry.get()
                self.style.configure("Vertical.TScrollbar", troughcolor=self._color9)

                with open(
                    os.path.join(self._xpath_configfile, "config.json"),
                    "r",
                ) as f:
                    self.json_file = json.load(f)

                with open(
                    os.path.join(self._xpath_configfile, "config.json"),
                    "w",
                ) as f:

                    self.json_file["themes"][self._selected_theme.get()][
                        "color9"
                    ] = self._color9

                    json.dump(self.json_file, f, indent=2)

                self.__updatecolor_toplevel.destroy()
                self.__colorbook_toplevel.destroy()
                self._add_colorbook_menu()

            case "color10":
                self._color10 = self._updatecolor_entry.get()
                self.style.map(
                    "Vertical.TScrollbar",
                    background=[
                        ("active", self._color10),
                        ("pressed", self._color10),
                    ],
                )

                with open(
                    os.path.join(self._xpath_configfile, "config.json"),
                    "r",
                ) as f:
                    self.json_file = json.load(f)

                with open(
                    os.path.join(self._xpath_configfile, "config.json"),
                    "w",
                ) as f:

                    self.json_file["themes"][self._selected_theme.get()][
                        "color10"
                    ] = self._color10

                    json.dump(self.json_file, f, indent=2)

                self.__updatecolor_toplevel.destroy()
                self.__colorbook_toplevel.destroy()
                self._add_colorbook_menu()

            case "color11":
                self._color11 = self._updatecolor_entry.get()
                self.style.configure("Vertical.TScrollbar", background=self._color11)
                with open(
                    os.path.join(self._xpath_configfile, "config.json"),
                    "r",
                ) as f:
                    self.json_file = json.load(f)

                with open(
                    os.path.join(self._xpath_configfile, "config.json"),
                    "w",
                ) as f:

                    self.json_file["themes"][self._selected_theme.get()][
                        "color11"
                    ] = self._color11

                    json.dump(self.json_file, f, indent=2)

                self.__updatecolor_toplevel.destroy()
                self.__colorbook_toplevel.destroy()
                self._add_colorbook_menu()

            case "color12":
                self._color12 = self._updatecolor_entry.get()
                with open(
                    os.path.join(self._xpath_configfile, "config.json"),
                    "r",
                ) as f:
                    self.json_file = json.load(f)

                with open(
                    os.path.join(self._xpath_configfile, "config.json"),
                    "w",
                ) as f:

                    self.json_file["themes"][self._selected_theme.get()][
                        "color12"
                    ] = self._color12

                    json.dump(self.json_file, f, indent=2)

                self.__updatecolor_toplevel.destroy()
                self.__colorbook_toplevel.destroy()
                self._add_colorbook_menu()

            case "color13":
                self._color13 = self._updatecolor_entry.get()
                with open(
                    os.path.join(self._xpath_configfile, "config.json"),
                    "r",
                ) as f:
                    self.json_file = json.load(f)

                with open(
                    os.path.join(self._xpath_configfile, "config.json"),
                    "w",
                ) as f:

                    self.json_file["themes"][self._selected_theme.get()][
                        "color13"
                    ] = self._color13

                    json.dump(self.json_file, f, indent=2)

                self.__updatecolor_toplevel.destroy()
                self.__colorbook_toplevel.destroy()
                self._add_colorbook_menu()

            case "color14":
                self._color14 = self._updatecolor_entry.get()
                with open(
                    os.path.join(self._xpath_configfile, "config.json"),
                    "r",
                ) as f:
                    self.json_file = json.load(f)

                with open(
                    os.path.join(self._xpath_configfile, "config.json"),
                    "w",
                ) as f:

                    self.json_file["themes"][self._selected_theme.get()][
                        "color14"
                    ] = self._color14

                    json.dump(self.json_file, f, indent=2)

                self.__updatecolor_toplevel.destroy()
                self.__colorbook_toplevel.destroy()
                self._add_colorbook_menu()

            case "color15":
                self._color15 = self._updatecolor_entry.get()
                with open(
                    os.path.join(self._xpath_configfile, "config.json"),
                    "r",
                ) as f:
                    self.json_file = json.load(f)

                with open(
                    os.path.join(self._xpath_configfile, "config.json"),
                    "w",
                ) as f:

                    self.json_file["themes"][self._selected_theme.get()][
                        "color15"
                    ] = self._color15

                    json.dump(self.json_file, f, indent=2)

                self.__updatecolor_toplevel.destroy()
                self.__colorbook_toplevel.destroy()
                self._add_colorbook_menu()

            case "color16":
                self._color16 = self._updatecolor_entry.get()
                with open(
                    os.path.join(self._xpath_configfile, "config.json"),
                    "r",
                ) as f:
                    self.json_file = json.load(f)

                with open(
                    os.path.join(self._xpath_configfile, "config.json"),
                    "w",
                ) as f:

                    self.json_file["themes"][self._selected_theme.get()][
                        "color16"
                    ] = self._color16

                    json.dump(self.json_file, f, indent=2)

                self.__updatecolor_toplevel.destroy()
                self.__colorbook_toplevel.destroy()
                self._add_colorbook_menu()

            case "color17":
                self._color17 = self._updatecolor_entry.get()
                with open(
                    os.path.join(self._xpath_configfile, "config.json"),
                    "r",
                ) as f:
                    self.json_file = json.load(f)

                with open(
                    os.path.join(self._xpath_configfile, "config.json"),
                    "w",
                ) as f:

                    self.json_file["themes"][self._selected_theme.get()][
                        "color17"
                    ] = self._color17

                    json.dump(self.json_file, f, indent=2)

                self.__updatecolor_toplevel.destroy()
                self.__colorbook_toplevel.destroy()
                self._add_colorbook_menu()

            case "color18":
                self._color18 = self._updatecolor_entry.get()
                with open(
                    os.path.join(self._xpath_configfile, "config.json"),
                    "r",
                ) as f:
                    self.json_file = json.load(f)

                with open(
                    os.path.join(self._xpath_configfile, "config.json"),
                    "w",
                ) as f:

                    self.json_file["themes"][self._selected_theme.get()][
                        "color18"
                    ] = self._color18

                    json.dump(self.json_file, f, indent=2)

                self.__updatecolor_toplevel.destroy()
                self.__colorbook_toplevel.destroy()
                self._add_colorbook_menu()

    def _combobox_selected_theme(self, event):
        # Displays the selected theme with its own color palette

        with open(
            os.path.join(self._xpath_configfile, "config.json"),
            "r",
        ) as f:
            self.json_file = json.load(f)
            self.json_file["select_theme"] = self._selected_theme.get()
            self._color1 = self.json_file["themes"][self._selected_theme.get()][
                "color1"
            ]
            self._color2 = self.json_file["themes"][self._selected_theme.get()][
                "color2"
            ]
            self._color3 = self.json_file["themes"][self._selected_theme.get()][
                "color3"
            ]
            self._color4 = self.json_file["themes"][self._selected_theme.get()][
                "color4"
            ]
            self._color5 = self.json_file["themes"][self._selected_theme.get()][
                "color5"
            ]
            self._color6 = self.json_file["themes"][self._selected_theme.get()][
                "color6"
            ]
            self._color7 = self.json_file["themes"][self._selected_theme.get()][
                "color7"
            ]
            self._color8 = self.json_file["themes"][self._selected_theme.get()][
                "color8"
            ]
            self._color9 = self.json_file["themes"][self._selected_theme.get()][
                "color9"
            ]
            self._color10 = self.json_file["themes"][self._selected_theme.get()][
                "color10"
            ]
            self._color11 = self.json_file["themes"][self._selected_theme.get()][
                "color11"
            ]
            self._color12 = self.json_file["themes"][self._selected_theme.get()][
                "color12"
            ]
            self._color13 = self.json_file["themes"][self._selected_theme.get()][
                "color13"
            ]
            self._color14 = self.json_file["themes"][self._selected_theme.get()][
                "color14"
            ]
            self._color15 = self.json_file["themes"][self._selected_theme.get()][
                "color15"
            ]
            self._color16 = self.json_file["themes"][self._selected_theme.get()][
                "color16"
            ]
            self._color17 = self.json_file["themes"][self._selected_theme.get()][
                "color17"
            ]
            self._color18 = self.json_file["themes"][self._selected_theme.get()][
                "color18"
            ]
            self._menubar.config(
                activebackground=self._color1,
                foreground=self._color1,
                background=self._color3,
            )
            self._file_menu.config(
                activebackground=self._color1,
                foreground=self._color1,
                background=self._color3,
            )
            self._edition_menu.config(
                activebackground=self._color1,
                foreground=self._color1,
                background=self._color3,
            )
            self._personlize_menu.config(
                activebackground=self._color1,
                foreground=self._color1,
                background=self._color3,
            )
            self._help_menu.config(
                activebackground=self._color1,
                foreground=self._color1,
                background=self._color3,
            )
            self._shortcut_bar.config(background=self._color4)
            self.style.configure("Shortcut.TButton", background=self._color4)
            self.style.map(
                "Shortcut.TButton",
                background=[
                    ("active", self._color1),
                    ("disabled", self._color4),
                ],
            )
            self._get_select_text().config(
                foreground=self._color1,
                insertbackground=self._color1,
                selectbackground=self._color1,
                background=self._color2,
                selectforeground=self._color2,
                highlightbackground=self._color2,
            )
            self._label_lines.config(
                foreground=self._color1,
                background=self._color8,
            )
            self.style.configure(
                "Vertical.TScrollbar",
                arrowcolor=self._color1,
                troughcolor=self._color9,
                background=self._color11,
            )
            self.style.map(
                "Vertical.TScrollbar",
                background=[
                    ("active", self._color10),
                    ("disabled", self._color2),
                    ("pressed", self._color10),
                ],
                arrowcolor=[
                    ("active", self._color1),
                    ("disabled", self._color1),
                    ("pressed", self._color1),
                ],
            )
            self.style.configure(
                "TCheckbutton",
                foreground=self._color1,
                background=self._color2,
            )
            self.style.map(
                "TCheckbutton",
                background=[("active", self._color2)],
            )
            self._root.config(background=self._color5)
            self.style.configure(
                "TNotebook",
                highlightbackground=self._color2,
                background=self._color5,
            )
            self.style.configure(
                "TNotebook.Tab",
                foreground=self._color6,
                background=self._color7,
            )
            self.style.map(
                "TNotebook.Tab",
                background=[("selected", self._color7)],
                foreground=[("selected", self._color6)],
            )

        with open(
            os.path.join(self._xpath_configfile, "config.json"),
            "w",
        ) as f:
            json.dump(self.json_file, f, indent=2)

        self.json_file = {}

        self.__colorbook_toplevel.destroy()
        self._add_colorbook_menu()

    def _add_colorbook_menu(self):
        self.__colorbook_menu()
        self._combobox_themes.bind(
            "<<ComboboxSelected>>", self._combobox_selected_theme
        )
