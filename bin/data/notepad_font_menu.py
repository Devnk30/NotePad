import os, json
from tkinter import *
from tkinter import font
from tkinter.ttk import Scrollbar
from data.notepad_root import Notepad


class Font_menu(Notepad):
    """
    This class creates the font configuration interface (type, style, and size) for the text editor.
    It inherits from the Notepad class to access its settings and functionality.
    """

    def __init__(self):
        # Base class initialization and initial font setup
        super().__init__()
        self._sample_font = self._font  # Default selected font
        self._sample_fontstyle = self._fontstyle  # Default selected font style
        self._sample_fontsize = (
            self._fontsize
        )  # Tamaño de la fuente seleccionada por defecto

    def __font_menu(self):
        """
        Creates the main window for font configuration, including controls for selecting the font type, style, and size, as well as a preview of the selected font.
        """

        # Creating a Toplevel window for the font configuration menu
        self.__font_toplevel = Toplevel(padx=20, pady=20, bg=self._color2)

        # Basic window settings
        self.__font_toplevel.title("Font")
        self.__font_toplevel.pack_propagate(
            False
        )  # Prevents the window from automatically resizing
        self.__font_toplevel.resizable(0, 0)  # Prevent resizing

        self.__font_toplevel.transient(
            self._root
        )  # Sets the window as a child of the main window
        self.__font_toplevel.protocol(
            "WM_DELETE_WINDOW",
            self.__font_toplevel.destroy,
        )  # Acción al cerrar la ventana
        self.__font_toplevel.grab_set()  # Captura todos los eventos de la ventana

        # -------------------------- Widgets Settings ----------------------- #

        ## Label to select the font
        Label(
            self.__font_toplevel,
            text="Font:",
            bg=self._color2,
            fg=self._color1,
            font=("Ubuntu Sans", "11", "italic"),
        ).grid(row=1, column=1, sticky="w")

        ## Input to display the selected font type
        self.__font_entry = Entry(
            self.__font_toplevel,
            readonlybackground=self._color12,
            foreground=self._color1,
            relief="flat",
            highlightthickness=0,
            highlightbackground=self._color1,
            highlightcolor=self._color1,
            insertbackground=self._color1,
            width=18,
            state="readonly",
            font=("Ubuntu Sans", "12", "italic"),
        )
        self.__font_entry.grid(row=2, column=1, columnspan=2, sticky="nswe", ipady=2)

        ## Listbox to display available fonts
        self.__font_listbox = Listbox(
            self.__font_toplevel,
            width=19,
            height=9,
            bg=self._color12,
            fg=self._color1,
            relief="flat",
            highlightthickness=0,
            highlightbackground=self._color1,
            highlightcolor=self._color1,
            font=("Ubuntu Sans", "11", "italic"),
            exportselection=False,
        )
        self.__font_listbox.grid(row=3, column=1, sticky="w")
        self.__scrollbar_font_listbox = Scrollbar(
            self.__font_toplevel, command=self.__font_listbox.yview
        )
        self.__scrollbar_font_listbox.grid(row=3, column=2, sticky="nswe")
        self.__font_listbox.config(yscrollcommand=self.__scrollbar_font_listbox.set)

        ## Label to select the font style
        Label(
            self.__font_toplevel,
            text="Font Style:",
            bg=self._color2,
            fg=self._color1,
            font=("Ubuntu Sans", "11", "italic"),
        ).grid(row=1, column=3, sticky="w", padx=25)

        ## Input to display the selected font style
        self.__style_entry = Entry(
            self.__font_toplevel,
            readonlybackground=self._color12,
            foreground=self._color1,
            relief="flat",
            highlightthickness=0,
            highlightbackground=self._color1,
            highlightcolor=self._color1,
            insertbackground=self._color1,
            width=13,
            state="readonly",
            font=("Ubuntu Sans", "12", "italic"),
        )
        self.__style_entry.grid(
            row=2, column=3, columnspan=2, sticky="nswe", padx=25, ipady=2
        )

        ## Input to display the selected font style
        self.__style_listbox = Listbox(
            self.__font_toplevel,
            width=13,
            height=9,
            bg=self._color12,
            fg=self._color1,
            relief="flat",
            highlightthickness=0,
            highlightbackground=self._color1,
            highlightcolor=self._color1,
            font=("Ubuntu Sans", "11", "italic"),
            exportselection=False,
        )
        self.__style_listbox.grid(row=3, column=3, sticky="w", padx=(25, 0))

        self.__scrollbar_style_listbox = Scrollbar(
            self.__font_toplevel, command=self.__style_listbox.yview
        )
        self.__scrollbar_style_listbox.grid(
            row=3,
            column=4,
            sticky="nswe",
            padx=(0, 25),
        )
        self.__style_listbox.config(yscrollcommand=self.__scrollbar_style_listbox.set)

        ## Label to select the font size
        Label(
            self.__font_toplevel,
            text="Size:",
            bg=self._color2,
            fg=self._color1,
            font=("Ubuntu Sans", "11", "italic"),
        ).grid(row=1, column=5, sticky="w")

        ## Input to display the selected font size
        self.__size_entry = Entry(
            self.__font_toplevel,
            readonlybackground=self._color12,
            foreground=self._color1,
            relief="flat",
            highlightthickness=0,
            highlightbackground=self._color1,
            highlightcolor=self._color1,
            insertbackground=self._color1,
            width=7,
            state="readonly",
            font=("Ubuntu Sans", "12", "italic"),
        )
        self.__size_entry.grid(row=2, column=5, columnspan=6, sticky="nswe", ipady=2)

        ## Listbox to display available font sizes
        self.__size_listbox = Listbox(
            self.__font_toplevel,
            width=7,
            height=9,
            bg=self._color12,
            fg=self._color1,
            relief="flat",
            highlightthickness=0,
            highlightbackground=self._color1,
            highlightcolor=self._color1,
            font=("Ubuntu Sans", "11", "italic"),
            exportselection=0,
        )
        self.__size_listbox.grid(row=3, column=5, sticky="w")

        self.__scrollbar_size_listbox = Scrollbar(
            self.__font_toplevel, command=self.__size_listbox.yview
        )
        self.__scrollbar_size_listbox.grid(row=3, column=6, sticky="nswe")
        self.__size_listbox.config(yscrollcommand=self.__scrollbar_size_listbox.set)

        ## Frame & Label Sample Config
        self._frame_sample = Frame(
            self.__font_toplevel,
            width=410,
            height=100,
        )

        self.__label_sample = Label(
            self._frame_sample,
            # width=410,
            height=100,
            text="AaBb YyZz",
            justify="center",
            bg=self._color2,
            fg=self._color1,
            font=("Ubuntu Sans", "12", "normal italic"),
            relief="flat",
        )

        self._frame_sample.grid(row=4, column=1, columnspan=7, pady=20, sticky="nswe")
        self._frame_sample.pack_propagate(
            0
        )  # Does not allow the frame to fit the content

        self.__label_sample.pack(fill="both")
        self.__label_sample.focus()

        ## Button to accept changes
        Button(
            self.__font_toplevel,
            text="Accept",
            bg=self._color12,
            activebackground=self._color1,
            fg=self._color1,
            activeforeground=self._color12,
            relief="flat",
            highlightthickness=0,
            highlightcolor=self._color1,
            width=10,
            font=("Ubuntu Sans", "10", "italic"),
            command=self.__accept,
        ).grid(row=5, column=1, columnspan=6, padx=(0, 125), pady=(0, 5), sticky="e")

        ## Button to cancel changes
        Button(
            self.__font_toplevel,
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
            command=self.__font_toplevel.destroy,
        ).grid(row=5, column=1, columnspan=6, pady=(0, 10), sticky="e")

        # --------------------- Adding Fonts, Style, Size ------------------- #

        ## Load available fonts
        self._font_list = []

        for myfont in font.families():
            self._font_list.append(myfont)
            self.__font_listbox.insert("end", myfont)

        for font_num in range(len(self._font_list)):
            self.__font_listbox.itemconfig(
                font_num,
                selectbackground=self._color1,
                selectforeground=self._color2,
            )

        ## Load available styles
        self._style_list = (
            "normal",
            "bold",
            "italic",
            "normal bold",
            "normal italic",
            "bold italic",
        )
        for style in self._style_list:
            self.__style_listbox.insert("end", style)

        for style_num in range(len(self._style_list)):
            self.__style_listbox.itemconfig(
                style_num,
                selectbackground=self._color1,
                selectforeground=self._color2,
            )

        ## Load available sizes
        self._size_list = (
            "8",
            "9",
            "10",
            "11",
            "12",
            "14",
            "16",
            "18",
            "20",
            "22",
            "24",
            "26",
            "28",
            "36",
            "48",
            "72",
        )
        for size in self._size_list:
            self.__size_listbox.insert("end", size)

        for size_num in range(len(self._size_list)):
            self.__size_listbox.itemconfig(
                size_num,
                selectbackground=self._color1,
                selectforeground=self._color2,
            )

        # ------------------- Show selection in the Entrys ------------------ #

        self.__font_entry.config(state="normal")
        self.__font_entry.insert("0", self._font)
        self.__font_listbox.selection_set(
            self._font_list.index(self.__font_entry.get()),
        )
        self.__font_entry.config(state="readonly")

        self.__style_entry.config(state="normal")
        self.__style_entry.insert("0", self._fontstyle)
        self.__style_listbox.selection_set(
            self._style_list.index(self.__style_entry.get()),
        )
        self.__style_entry.config(state="readonly")

        self.__size_entry.config(state="normal")
        self.__size_entry.insert("0", self._fontsize)
        self.__size_listbox.selection_set(
            self._size_list.index(self.__size_entry.get()),
        )

        self.__size_entry.config(state="readonly")

    def __accept(self):
        """
        Saves the selected font settings and applies them to the text editor.
        """

        self._sample_font = self._font
        self._fontstyle = self._sample_fontstyle
        self._fontsize = self._sample_fontsize

        # Update the font in the main interface
        self._get_select_text().configure(
            font=(
                self._font,
                self._fontsize,
                self._fontstyle,
            )
        )
        self._label_lines.config(
            font=(
                self._font,
                "10",
                self._fontstyle,
            )
        )

        # Save the configuration to a JSON file
        with open(
            os.path.join(self._xpath_configfile, "config.json"),
            "r",
        ) as f:
            self.json_file = json.load(f)
            self.json_file["font"]["fontname"] = self._font
            self.json_file["font"]["fontsize"] = self._fontsize
            self.json_file["font"]["fontstyle"] = self._fontstyle

        with open(
            os.path.join(self._xpath_configfile, "config.json"),
            "w",
        ) as f:
            json.dump(self.json_file, f, indent=2)

    def __select_font(self):
        """
        Updates the sample font when a font is selected from the list.
        """

        for myfont in range(len(self._font_list)):
            self.__check_font = self.__font_listbox.selection_includes(myfont)

            if self.__check_font:
                self.__font_entry.config(state="normal")

                self.__font_listbox.config(exportselection=True)
                self._sample_font = self.__font_listbox.selection_get()
                self.__font_listbox.config(exportselection=False)
                self.__font_entry.delete("0", END)
                self.__font_entry.insert("0", self._sample_font)  # Update source input
                self.__font_entry.config(state="readonly")
                break

        self.__font_toplevel.after(200, self.__select_font)

    def __scroll_font(self):
        # Displays the currently selected font
        self.__font_listbox.see(self._font_list.index(self._sample_font))

    def __select_style(self):
        """
        Updates the font style in the sample when a style is selected.
        """

        for mystyle in range(len(self._style_list)):
            self.__check_style = self.__style_listbox.selection_includes(mystyle)

            if self.__check_style:
                self.__style_entry.config(state="normal")

                self.__style_listbox.config(exportselection=True)
                self._sample_fontstyle = self.__style_listbox.selection_get()
                self.__style_listbox.config(exportselection=False)
                self.__style_entry.delete("0", END)
                self.__style_entry.insert(
                    "0", self._sample_fontstyle
                )  # Update style entry
                self.__style_entry.config(state="readonly")
                break

        self.__font_toplevel.after(200, self.__select_style)

    def __sroll_style(self):
        # Displays the currently selected style
        self.__style_listbox.see(self._style_list.index(self._sample_fontstyle))

    def __select_size(self):
        """
        Updates the font size in the sample when a size is selected.
        """

        for mysize in range(len(self._size_list)):
            self.__check_size = self.__size_listbox.selection_includes(mysize)

            if self.__check_size:
                self.__size_entry.config(state="normal")

                self.__size_listbox.config(exportselection=True)
                self._sample_fontsize = self.__size_listbox.selection_get()
                self.__size_listbox.config(exportselection=False)
                self.__size_entry.delete("0", END)
                self.__size_entry.insert(
                    "0", self._sample_fontsize
                )  # Update size entry
                self.__size_entry.config(state="readonly")
                break

        self.__font_toplevel.after(200, self.__select_size)

    def __scroll_size(self):
        # Displays the currently selected size
        self.__size_listbox.see(self._size_list.index(self._sample_fontsize))

    def __selection_sample(self):
        # Displays the font, style, and size currently selected in the sample label
        self.__label_sample.config(
            font=(
                self._sample_font,
                self._sample_fontsize,
                self._sample_fontstyle,
            )
        )

        self.__label_sample.grid_propagate(0)

        self.__font_toplevel.after(200, self.__selection_sample)

    def _bind_event_fontmenu_return(self, event):
        self.__accept()
        return "break"

    def _add_font_menu(self):
        self.__font_menu()
        self.__font_toplevel.after(200, self.__select_font)
        self.__font_toplevel.after(200, self.__scroll_font)
        self.__font_toplevel.after(200, self.__select_style)
        self.__font_toplevel.after(200, self.__sroll_style)
        self.__font_toplevel.after(200, self.__select_size)
        self.__font_toplevel.after(200, self.__scroll_size)
        self.__font_toplevel.after(200, self.__selection_sample)
        self.__font_toplevel.bind("<Return>", self._bind_event_fontmenu_return)
