import sys, os, json
from tkinter import *
from tkinter.ttk import Notebook, Style, Scrollbar


class Notepad:
    def __init__(self):
        """Initialize the Notepad application with main UI components and basic configurations."""

        # Main root window and styles
        self._root = Tk()
        self.style = Style()
        self._notebook = Notebook(self._root, cursor="hand2")
        self._menubar = Menu(self._root)
        self._label_lines = Label(self._root)

        # Menus for file, edit, customization, and help
        self._file_menu = Menu(self._menubar, tearoff=0)
        self._edition_menu = Menu(self._menubar, tearoff=0)
        self._personlize_menu = Menu(self._menubar, tearoff=0)
        self._help_menu = Menu(self._menubar, tearoff=0)

        # Context menu
        self._context_menu = Menu(
            self._root,
            relief="flat",
            tearoff=0,
        )

        # Paths for images and configuration files
        self._xpath_images = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "images"
        )
        self._xpath_configfile = os.path.dirname(os.path.dirname(__file__))
        # self._xpath = os.path.join(os.getcwd(), "bin")

        # Placeholder for active tab close button
        self._tab_button_active = None

        # Font Settings
        self._font = "Ubuntu Sans"
        self._fontsize = "12"
        self._fontstyle = "normal italic"

        # Palette Color
        self._color1 = "#ff9700"  # foreground color Text
        self._color2 = "#414141"  # background color Text
        self._color3 = "#2b2b2b"  # background color menu
        self._color4 = "#2b2b2b"  # background color shortcut menu and shortcut buttons
        self._color5 = "#353535"  # background root, notebook
        self._color6 = "#414141"  # foreground tabs
        self._color7 = "#ff9700"  # background tabs
        self._color8 = "#353535"  # label lines
        self._color9 = "#353535"  # scrollbar trough color
        self._color10 = "#2b2b2b"  # activebackground scrollbar
        self._color11 = "#1F1F1F"  # background scrollbar
        self._color12 = "#1F1F1F"  # entry and button background
        self._color13 = "#414141"  # foreground search tags
        self._color14 = "#ff9700"  # background search tags
        self._color15 = "#ff9700"  # next and previous foreground search tag
        self._color16 = "#000000"  # next and previous background search tag
        self._color17 = "#fffb00"  # foreground replace tags
        self._color18 = "#000000"  # background replace tags

        # Jsonfile Config
        self._selected_theme = StringVar()
        self.json_file = {}  # Placeholder for theme JSON configuration
        self._saved_themes = []  # List of saved themes

        # Index of the insert bar to show its position in the label lines
        self.__idx_line = ""
        self.__idx_column = ""

        # Initial configurations for app title and file management
        self.file = sys.argv[1] if len(sys.argv) > 1 else None
        self._file_path_list = []
        self._filename = ""
        self._title_filename = ""

        # Screen dimensions for app positioning
        self._screenwidth = self._root.winfo_screenwidth()
        self._screenheight = self._root.winfo_screenheight()

    def _root_config(self):
        """Configure the main root window properties, like title, icon, and window size."""

        self._root.title("NotePad")
        self.__icon = PhotoImage(file=os.path.join(self._xpath_images, "NotePad.gif"))
        self._root.config(menu=self._menubar, background=self._color5)

        # Configure the main menu's appearance
        self._menubar.config(
            background=self._color3,
            activebackground=self._color1,
            foreground=self._color1,
            font=(
                self._font,
                "10",
                self._fontstyle,
            ),
            relief="flat",
        )

        # Set window icon
        self._root.iconphoto(True, self.__icon)

        # Center the app window on screen
        self.__width = round(
            (self._screenwidth / 2) - (1366 / 2)
        )  # Calculate horizontal position
        self.__height = round(
            (self._screenheight / 2) - (850 / 2)
        )  # Calculate vertical position
        self._root.geometry(f"{1366}x{800}+{self.__width}+{self.__height}")

        # Enable auto-resizing
        self._root.grid_rowconfigure(1, weight=1)
        self._root.grid_columnconfigure(0, weight=1)

        # Handle opening files through command-line arguments
        if len(sys.argv) > 1:
            self.__file_path = sys.argv[1]
            self._filename = os.path.basename(self.__file_path)
            self._title_filename = os.path.splitext(self._filename)[0]
            self._file_path_list.append(self.__file_path)

        else:
            self._file_path_list.append(os.path.join(os.getcwd(), "Notepad.txt"))

    def _notebook_config(self):
        """Configure notebook layout and style, including custom close buttons for each tab."""

        # Images for the close button
        self._close_images = (
            PhotoImage(  # Default image
                "img_close_default",
                data="""
                iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAbUlEQVR4nI2Qyw3CQAwFZ7aDrSHiwCUFohzSAaKyFYmUXnIiArF8goXWpyd7/Hvwjkwc+aXUs1qA7pNQR3UB+kcipXQCVnUGjrvcFTh8dT8LRb1Uvd9SJw93ALj9TPoDTiHYtDo6PHqw3Z4WwzfsLiDCz7Z4VwAAAABJRU5ErkJggg== 
            """,
            ),
            PhotoImage(  # Active image
                "img_close_active",
                data="""
                iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAhklEQVR4nGNggAJ+fgZBBiyAH1m8qFy0f95S2fOOjnzKyIryi4Ub5q+QuebhK6AHFsgrEql68Fr958oNcpftXHg0kcXWbpG/6OLNq4qi++Fr9Z+rNsqdT8sWnghjo9sCBln5IjUgU97/0vq/ahOaSbgUrt4kfwmrQqKsxuZwbB4kPniICXAAUkNhGeysSRsAAAAASUVORK5CYII=
            """,
            ),
            PhotoImage(  # Pressed image
                "img_close_pressed",
                data="""
                iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAfklEQVR4nGNggAJ+BgZBBiyAH1m8XFS0f6ms7HlHPj5lZEXFwsINK2RkrvkKCOiBBYpERKpeq6v/3CAnd9mFh0cTWWyLvPxFb15eVRTdIImNcnLns4WFJ8LY6LaAQb6ISA1IwS8trf+b0E3Co/ASVoVEWY3N4dg8SHzwEBPgAEScSTT8cRAgAAAAAElFTkSuQmCC
            """,
            ),
        )

        # Define close button layout and style in tabs
        self.style.element_create(
            "button_close",
            "image",
            "img_close_default",
            ("active", "pressed", "!disabled", "img_close_pressed"),
            ("active", "!disabled", "img_close_active"),
            border=8,
            sticky="ne",
            padding=10,
        )

        self.style.layout(
            "TNotebook.Tab",
            [
                (
                    "TNotebook.tab",
                    {
                        "sticky": "nswe",
                        "children": [
                            (
                                "TNotebook.padding",
                                {
                                    "side": "top",
                                    "sticky": "nswe",
                                    "children": [
                                        (
                                            "TNotebook.focus",
                                            {
                                                "side": "top",
                                                "sticky": "nswe",
                                                "children": [
                                                    (
                                                        "TNotebook.label",
                                                        {"side": "left", "sticky": ""},
                                                    ),
                                                    (
                                                        "TNotebook.button_close",
                                                        {"side": "left", "sticky": ""},
                                                    ),
                                                ],
                                            },
                                        )
                                    ],
                                },
                            )
                        ],
                    },
                )
            ],
        )

        # Configure the notebook's appearance
        self.style.configure(
            "TNotebook",
            background=self._color5,
            highlightbackground=self._color2,
            borderwidth=0,
            relief="flat",
        )
        self.style.map("TNotebook", relief=[("active", "flat")])
        self.style.configure(
            "TNotebook.Tab",
            background=self._color7,
            foreground=self._color6,
            font=(
                self._font,
                "10",
                self._fontstyle,
            ),
            padding=(4, 6, 4, 6),
        )
        self.style.map(
            "TNotebook.Tab",
            background=[("selected", self._color7)],
            foreground=[("selected", self._color6)],
        )

        self._notebook.grid(row=1, column=0, sticky="nswe")

    def _notepad_text_config(self):
        """Configure the main text area for the notepad, including font, color, and focus settings."""

        self.__notepad_text = Text(
            self._notebook,
            bg=self._color2,
            fg=self._color1,
            font=(
                self._font,
                self._fontsize,
                self._fontstyle,
            ),
            relief="flat",
            undo=True,
            insertbackground=self._color1,
            selectbackground=self._color1,
            selectforeground=self._color2,
            highlightbackground=self._color2,
        )
        self.__notepad_text.grid(sticky="nswe")

        # Add the text area to the notebook and set initial focus
        self._notebook.add(
            self.__notepad_text,
            text=f"{self._title_filename if self._title_filename != "" else 'Notepad'}",
        )
        self.__notepad_text.focus()

        return self.__notepad_text

    def _scrollbar_config(self):
        """Configure the scrollbar for the main text area, with custom style and color mapping."""

        self.style.configure(
            "Vertical.TScrollbar",
            background=self._color11,
            troughcolor=self._color9,
            arrowcolor=self._color1,
            relief="flat",
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
            relief=[("active", "flat")],
        )
        self._scrollbar = Scrollbar(
            self._root,
            orient="vertical",
            style="Vertical.TScrollbar",
        )

        self._scrollbar.grid(row=1, column=1, pady=(34, 0), sticky="nswe")

    def _label_lines_config(self):
        """Config a label to display the cursor index in the label line."""

        self._label_lines.config(
            width=1366,
            font=(self._font, "11", self._fontstyle),
            bg=self._color8,
            fg=self._color1,
        )
        self._label_lines.grid(row=2, column=0, columnspan=2, sticky="nwe")

    def _custom_checkbox_config(self):
        """Set up a custom-styled checkbox"""

        # Define checked and unchecked images
        self._checked_image = PhotoImage(
            file=os.path.join(self._xpath_images, "checkbox.png")
        )
        self._unchecked_image = PhotoImage(width=12, height=12)
        self._unchecked_image.put(("white"), to=(0, 0, 12, 12))
        self.style.element_create(
            "custom.check.indicator",
            "image",
            self._unchecked_image,
            ("selected", self._checked_image),
            sticky="w",
            padding=12,
        )

        self.style.layout(
            "TCheckbutton",
            [
                (
                    "Checkbutton.padding",
                    {
                        "children": [
                            (
                                "custom.check.indicator",
                                {"side": "left"},
                            ),
                            ("Checkbutton.label", {"side": "left"}),
                        ],
                        "sticky": "nswe",
                    },
                )
            ],
        )

        # Configure checkbox layout and color mappings
        self.style.configure(
            "TCheckbutton",
            background=self._color2,
            foreground=self._color1,
            font=("Ubuntu Sans", "10", "italic"),
        )
        self.style.map(
            "TCheckbutton",
            background=[("active", self._color2)],
        )

    def _get_select_text(self):
        """Retrieve the selected text from the currently active tab."""
        self.__mytext = self._notebook.winfo_children()[self._notebook.index("current")]

        return self.__mytext

    def _show_cursor_idx(self):
        """Show cursor index in the label line."""

        self.__idx_line, self.__idx_column = self.__notepad_text.index("insert").split(
            "."
        )
        self._label_lines.configure(
            text=f"Line: {self.__idx_line}  Column: {self.__idx_column}"
        )

        self._root.after(200, self._show_cursor_idx)

    def _show_file_content(self):
        """
        Reads the content of the currently opened file and displays it in the text widget.
        Clears any existing content in the text widget before inserting the file content.
        Moves the cursor to the last line of the text widget after inserting the content.
        """

        if self.file:
            # reading file content
            with open(self.file, "r") as f:
                self.texto = f.read()

                # delete existing content if any
                self.__notepad_text.delete("1.0", END)

                # insert content at beginning
                self.__notepad_text.insert("1.0", self.texto)

                # Move the insertion bar to the las line
                self.__notepad_text.see(END)

            self.__notepad_text.edit_reset()
            self.__notepad_text.edit_modified(False)

    def _themes_config_file(self):
        """
        Loads theme and font configuration from a JSON file. If the file doesn't exist or is corrupted,
        creates a new file with default configuration.
        """

        try:
            with open(
                os.path.join(self._xpath_configfile, "config.json"),
                "r",
            ) as f:
                self.json_file = json.load(f)
                self._selected_theme.set(self.json_file["select_theme"])
                self._font = self.json_file["font"]["fontname"]
                self._fontsize = self.json_file["font"]["fontsize"]
                self._fontstyle = self.json_file["font"]["fontstyle"]
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

                for theme in self.json_file["themes"]:
                    self._saved_themes.append(theme)

        except (FileNotFoundError, KeyError, json.decoder.JSONDecodeError):
            with open(
                os.path.join(self._xpath_configfile, "config.json"),
                "w",
            ) as f:
                self.json_file = {
                    "font": {
                        "fontname": "Ubuntu Sans",
                        "fontsize": "12",
                        "fontstyle": "normal italic",
                    },
                    "select_theme": "default",
                    "themes": {
                        "default": {
                            "color1": "#ff9700",  # foreground color
                            "color2": "#414141",  # background color text
                            "color3": "#2b2b2b",  # background color menu
                            "color4": "#2b2b2b",  # background color shortcut menu and shortcut buttons
                            "color5": "#353535",  # background root, notebook
                            "color6": "#414141",  # foreground tabs
                            "color7": "#ff9700",  # background tabs
                            "color8": "#353535",  # label lines
                            "color9": "#353535",  # scrollbar trough color
                            "color10": "#2b2b2b",  # activebackground scrollbar
                            "color11": "#1F1F1F",  # background scrollbar
                            "color12": "#1F1F1F",  # entry and listbox background
                            "color13": "#414141",  # foreground search tags
                            "color14": "#ff9700",  # background search tags
                            "color15": "#ff9700",  # next and previous foreground search tag
                            "color16": "#000000",  # next and previous background search tag
                            "color17": "#fffb00",  # foreground replace tags
                            "color18": "#000000",  # background replace tags
                        }
                    },
                }

                self._selected_theme.set(self.json_file["select_theme"])
                self._font = "Ubuntu Sans"
                self._fontsize = "12"
                self._fontstyle = "normal italic"
                self._color1 = "#ff9700"  # foreground color Text
                self._color2 = "#414141"  # background color Text
                self._color3 = "#2b2b2b"  # background color menu
                self._color4 = (
                    "#2b2b2b"  # background color shortcut menu and shortcut buttons
                )
                self._color5 = "#353535"  # background root, notebook
                self._color6 = "#414141"  # foreground tabs
                self._color7 = "#ff9700"  # background tabs
                self._color8 = "#353535"  # label lines
                self._color9 = "#353535"  # scrollbar trough color
                self._color10 = "#2b2b2b"  # activebackground scrollbar
                self._color11 = "#1F1F1F"  # background scrollbar
                self._color12 = "#1F1F1F"  # entry and button background
                self._color13 = "#414141"  # foreground search tags
                self._color14 = "#ff9700"  # background search tags
                self._color15 = "#ff9700"  # next and previous foreground search tag
                self._color16 = "#000000"  # next and previous background search tag
                self._color17 = "#fffb00"  # foreground replace tags
                self._color18 = "#000000"  # background replace tags

                for theme in self.json_file["themes"]:
                    self._saved_themes.append(theme)

                json.dump(self.json_file, f, indent=2)

        self.json_file = {}

    def _focustext_on_tab_selected(self, event):
        """
        Handles the event when a tab is selected in the notebook. It updates the scrollbar and focuses
        the corresponding text widget. It also updates the window title to reflect the selected file.
        """

        self.__selected_tab = event.widget.select()
        self.__tab_index = event.widget.index(self.__selected_tab)

        self._scrollbar.config(
            command=self._notebook.winfo_children()[self.__tab_index].yview
        )
        self._notebook.winfo_children()[self.__tab_index].config(
            yscrollcommand=self._scrollbar.set
        )
        self._notebook.winfo_children()[self.__tab_index].focus()

        try:
            self._root.title(self._file_path_list[self.__tab_index])

        except IndexError:
            print("IndexError")

        return "break"

    def tab_button_close_press(self, event):
        """
        Detects when the close button on a tab is pressed. It determines which tab's close button was clicked
        and marks the tab as "pressed".
        """

        self._tab_element = self._notebook.identify(event.x, event.y)

        if "button_close" in self._tab_element:
            # self.index: the numeric index of the tab specified by tab_id
            self.index = self._notebook.index(
                "@%d,%d" % (event.x, event.y),
            )
            self._notebook.state(["pressed"])
            self._tab_button_active = self.index
            return "break"

    def tab_button_close_release(self, event):
        """
        Handles the event when the close button on a tab is released. If the tab is the last one open,
        it will close the application. Otherwise, it will close the tab and remove it from the notebook.
        """

        if not self._notebook.instate(["pressed"]):
            return

        self._tab_element = self._notebook.identify(event.x, event.y)

        if "button_close" not in self._tab_element:
            return

        self.index = self._notebook.index(
            "@%d,%d" % (event.x, event.y),
        )

        if self._notebook.index("end") == 1:
            self._root.destroy()

        else:
            self._notebook.forget(self.index)  # Delete Tab
            self._file_path_list.pop(self.index)  # Delete Path

            self._notebook.state(["!pressed"])
        self._tab_button_active = None
