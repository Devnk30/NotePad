from data.notepad_root import Notepad
from tkinter import *
from tkinter.ttk import Checkbutton


class Search_menus(Notepad):
    """
    Class that extends Notepad functionality to include a search menu.
    Provides functionality such as searching, case-sensitive searching,
    and navigation between matches.
    """

    def __init__(self):
        super().__init__()

        # Initialization of attributes required for search functionality
        self._label_warning = None  # Label for warning messages (e.g. "No match found")
        self._label_search = None  # Label for search field
        self._search_entry = None  # Input field for search text
        self._checkbutton = None  # Checkbutton for "Case Sensitive" option
        self._button_previous = None  # Button to go to previous match
        self._button_next = None  # Button to go to next match
        self._button_cancel = None  # Button to close search window
        self._checkvalue = BooleanVar()  # Boolean variable bound to Checkbutton
        self._replacement_label = None  # Label for replacement field
        self._replacement_entry = None  # Input field for replacement text
        self._button_replace = None  # Button to replace one match
        self._button_replace_all = None  # Button to replace all matches
        self._boolreplace = BooleanVar()  # Flag for replacement operations
        self._searchtext = ""  # Current text to search for
        self._savetext_search_entry = ""  # Last text searched
        self._fst_matching_idx = "1.0"  # Index of first match
        self._last_matching_idx = ""  # Index of last match
        self._list_index = []  # List of indexes of all matches

    def _menu_search(self):
        """
        Configures and initializes the graphical interface for searching.
        """

        # Create secondary window for search
        self.__search_toplevel = Toplevel(padx=10, pady=10, bg=self._color2)

        # Window settings
        self.__search_toplevel.title("Search")
        self.__search_toplevel.pack_propagate(
            False
        )  # Prevents resizing based on widget content.
        self.__search_toplevel.resizable(0, 0)  # Disables resizing the window.

        # Center window on screen
        self._width = round((self._screenwidth / 2) - (625 / 2))
        self._height = round((self._screenheight / 2) - (192 / 2))
        self.__search_toplevel.geometry(f"{625}x{192}+{self._width}+{self._height}")

        # Configure behavior when closing the window
        self.__search_toplevel.transient(self._root)
        self.__search_toplevel.protocol(
            "WM_DELETE_WINDOW",
            self.__search_toplevel.destroy,
        )
        self.__search_toplevel.grab_set()  # Prevents interacting with other windows until closed.

        # ------------------------- Widgets Settings ------------------------ #
        ## Label for warnings
        self._label_warning = Label(
            self.__search_toplevel,
            bg=self._color2,
            fg=self._color1,
            font=("Ubuntu Sans", "8", "italic"),
        )
        self._label_warning.grid(
            row=0,
            column=2,
            sticky="nswe",
            padx=(18, 5),
        )

        ## Label for search text
        self._label_search = Label(
            self.__search_toplevel,
            text="Search: ",
            bg=self._color2,
            fg=self._color1,
            font=("Ubuntu Sans", "10", "italic"),
        )
        self._label_search.grid(
            row=1,
            column=1,
            sticky="w",
            padx=(22, 0),
            pady=(5, 0),
        )

        ## Input field for search text
        self._search_entry = Entry(
            self.__search_toplevel,
            bg=self._color12,
            fg=self._color1,
            relief="flat",
            highlightthickness=1,
            highlightbackground=self._color1,
            highlightcolor=self._color1,
            insertbackground=self._color1,
            selectbackground=self._color1,
            selectforeground=self._color2,
            font=("Ubuntu Sans", "10", "italic"),
        )
        self._search_entry.grid(
            row=1,
            column=2,
            padx=(18, 5),
            ipadx=140,
            ipady=1,
            pady=(5, 0),
        )
        self._search_entry.focus()

        ## Checkbutton for case sensitive search
        self._checkbutton = Checkbutton(
            self.__search_toplevel,
            text="Case Sensitive",
            style="TCheckbutton",
            variable=self._checkvalue,
        )
        self._checkbutton.grid(
            row=2,
            column=2,
            padx=(16, 0),
            sticky="ns",
            pady=10,
        )

        ## Previous match button
        self._button_previous = Button(
            self.__search_toplevel,
            text="Previous",
            bg=self._color12,
            activebackground=self._color1,
            fg=self._color1,
            activeforeground=self._color12,
            relief="flat",
            width=17,
            highlightthickness=0,
            highlightcolor=self._color1,
            font=("Ubuntu Sans", "9", "italic"),
            command=self._previous_search,
        )
        self._button_previous.grid(
            row=3,
            column=2,
            sticky="w",
            padx=(18, 0),
            pady=5,
        )

        ## Next match button
        self._button_next = Button(
            self.__search_toplevel,
            text="Next",
            bg=self._color12,
            activebackground=self._color1,
            fg=self._color1,
            activeforeground=self._color12,
            relief="flat",
            width=17,
            highlightthickness=0,
            highlightcolor=self._color1,
            font=("Ubuntu Sans", "9", "italic"),
            command=self._next_search,
        )
        self._button_next.grid(
            row=3,
            column=2,
            sticky="e",
            padx=(0, 5),
        )

        ## Cancel button (close window)
        self._button_cancel = Button(
            self.__search_toplevel,
            text="Cancel",
            bg=self._color12,
            activebackground=self._color1,
            fg=self._color1,
            activeforeground=self._color12,
            relief="flat",
            highlightthickness=0,
            highlightcolor=self._color1,
            font=("Ubuntu Sans", "9", "italic"),
            command=self.__search_toplevel.destroy,
        )
        self._button_cancel.grid(
            row=4,
            column=2,
            sticky="nswe",
            padx=(18, 5),
        )

        # Insert previous text into the search input
        self._search_entry.insert("0", self._savetext_search_entry)

    def _previous_search(self, event=None):
        """
        Finds and highlights the previous occurrence of the search term in the text widget.
        """

        try:
            # Remove current highlight
            self._get_select_text().tag_remove(
                "Next_Previous_Search",  # Name of the tag to remove
                f"{self._last_matching_idx}-{len(self._searchtext)}c",  # Starting index of the range to clear
                self._last_matching_idx,  # Ending index of the range to clear
            )
            # If not in replacement mode, add a "Search" tag
            if not self._boolreplace.get():

                self._get_select_text().tag_add(
                    "Search",  # Name of the tag to add
                    f"{self._last_matching_idx}-{len(self._searchtext)}c",  # Initial index
                    self._last_matching_idx,  # Final index
                )

            # Check if the search is case sensitive
            if self._checkvalue.get() == True:

                # Backward search (case-sensitive)
                self._fst_matching_idx = (
                    f"{self._fst_matching_idx}-{len(self._searchtext)}c"
                )
                self._fst_matching_idx = self._get_select_text().search(
                    self._searchtext,
                    self._fst_matching_idx,  # Index from which to search
                    nocase=0,  # Do not ignore case
                    stopindex="1.0",  # Final index (upper limit)
                    backwards=True,  # Search backwards
                    regexp=False,  # Do not use regular expressions
                )

            else:
                self._fst_matching_idx = (
                    f"{self._fst_matching_idx}-{len(self._searchtext)}c"
                )
                # Backward lookup (case-insensitive)
                self._fst_matching_idx = self._get_select_text().search(
                    self._searchtext,
                    self._fst_matching_idx,
                    nocase=1,  # Ignore case
                    stopindex="1.0",
                    backwards=True,
                    regexp=False,
                )

            # If there are no matches, set the index to `END`
            if not self._fst_matching_idx:
                self._fst_matching_idx = END

            else:
                # Update last match index
                self._last_matching_idx = (
                    f"{self._fst_matching_idx}+{len(self._searchtext)}c"
                )
                # Remove previous highlight
                self._get_select_text().tag_remove(
                    "Search",
                    self._fst_matching_idx,
                    self._last_matching_idx,
                )
                # Highlight the new match
                self._get_select_text().tag_add(
                    "Next_Previous_Search",
                    self._fst_matching_idx,
                    self._last_matching_idx,
                )
                self._fst_matching_idx = self._last_matching_idx
                # Apply colors to the highlight
                self._get_select_text().tag_config(
                    "Next_Previous_Search",
                    background=self._color16,
                    foreground=self._color15,
                )

            self._boolreplace.set(False)

            # Make sure the match is visible
            self._get_select_text().see(self._fst_matching_idx)

        except TclError:
            print("TclError")

    def _next_search(self, event=None):
        """
        Finds and highlights the next occurrence of the search term in the text widget.
        """

        try:
            # Remove current highlight
            self._get_select_text().tag_remove(
                "Next_Previous_Search",
                f"{self._last_matching_idx}-{len(self._searchtext)}c",
                self._last_matching_idx,
            )

            # If not in replacement mode, add the "Search" tag
            if not self._boolreplace.get():
                self._get_select_text().tag_add(
                    "Search",
                    f"{self._last_matching_idx}-{len(self._searchtext)}c",
                    self._last_matching_idx,
                )
            # Check case sensitivity
            if self._checkvalue.get() == True:
                # Look forward (case-sensitive)
                self._fst_matching_idx = self._get_select_text().search(
                    self._searchtext,
                    self._fst_matching_idx,
                    nocase=0,
                    stopindex=END,
                    regexp=False,
                )

            else:
                # Look forward (case-insensitive)
                self._fst_matching_idx = self._get_select_text().search(
                    self._searchtext,
                    self._fst_matching_idx,
                    nocase=1,
                    stopindex=END,
                    regexp=False,
                )

            # If there are no matches, return to the beginning
            if not self._fst_matching_idx:
                self._fst_matching_idx = "1.0"

            else:
                # Update last match index
                self._last_matching_idx = (
                    f"{self._fst_matching_idx}+{len(self._searchtext)}c"
                )
                # Remove previous highlighting
                self._get_select_text().tag_remove(
                    "Search",
                    self._fst_matching_idx,
                    self._last_matching_idx,
                )
                # Highlight the new match
                self._get_select_text().tag_add(
                    "Next_Previous_Search",
                    self._fst_matching_idx,
                    self._last_matching_idx,
                )
                self._fst_matching_idx = self._last_matching_idx
                # Apply colors to the highlight
                self._get_select_text().tag_config(
                    "Next_Previous_Search",
                    background=self._color16,
                    foreground=self._color15,
                )
            self._boolreplace.set(False)

            # Make sure the match is visible
            self._get_select_text().see(self._fst_matching_idx)

        except TclError:
            pass

    def _search(self, interface_replace):
        """
        Highlights all matches of the search term in the text widget.
        """

        # Check if the text entered in the search field is new
        if (
            self._savetext_search_entry != self._search_entry.get()
            and self._search_entry.get() != ""
        ):
            # Clear previous highlights
            self._get_select_text().tag_remove("Search", "1.0", END)
            self._get_select_text().tag_remove("Next_Previous_Search", "1.0", END)
            self._get_select_text().tag_remove("Replace", "1.0", END)

            # Initialize variables
            self._fst_matching_idx = "1.0"
            self._list_index.clear()  # Clear index list
            self._searchtext = self._search_entry.get()

            # Find matches in the entire text
            while True:
                if self._checkvalue.get() == True:
                    self._fst_matching_idx = self._get_select_text().search(
                        self._searchtext,
                        self._fst_matching_idx,
                        nocase=0,
                        stopindex=END,
                        regexp=False,
                    )

                else:
                    self._fst_matching_idx = self._get_select_text().search(
                        self._searchtext,
                        self._fst_matching_idx,
                        nocase=1,
                        stopindex=END,
                        regexp=False,
                    )

                # If there are no matches, stop the search
                if not self._fst_matching_idx:
                    self._fst_matching_idx = "1.0"
                    if self._list_index == []:
                        self._label_warning.config(text="No match found!!!")

                    break

                else:
                    # Highlight matches and store them
                    self._last_matching_idx = (
                        f"{self._fst_matching_idx}+{len(self._searchtext)}c"
                    )

                    self._get_select_text().tag_add(
                        "Search",
                        self._fst_matching_idx,
                        self._last_matching_idx,
                    )
                    self._list_index.append(self._fst_matching_idx)
                    self._fst_matching_idx = self._last_matching_idx
                    # Configurar colores para el resaltado
                    self._get_select_text().tag_config(
                        "Search",
                        background=self._color14,
                        foreground=self._color13,
                    )
                    self._label_warning.config(text="")
            self._savetext_search_entry = self._searchtext

        elif self._search_entry.get() == "":
            self._get_select_text().tag_remove("Search", "1.0", END)
            self._get_select_text().tag_remove("Next_Previous_Search", "1.0", END)
            self._get_select_text().tag_remove("Replace", "1.0", END)

        if interface_replace == "":
            self.__search_toplevel.after(200, lambda: self._search(""))
        else:
            interface_replace.after(
                200,
                lambda: self._search(interface_replace),
            )

    def _bind_event_search_ctrl_backspace(self, event):
        if self._search_entry.select_present() == True:
            self._search_entry.delete(
                self._search_entry.index(SEL_FIRST),
                self._search_entry.index(SEL_LAST),
            )

        else:
            self._search_entry.delete("0", END)

        return "break"

    def _bind_event_focus_in(self, event):
        self._search_entry.focus()

    def _add_searchmenu(self, event=None):
        self._menu_search()
        self.__search_toplevel.after(200, lambda: self._search(""))
        self._search_entry.bind(
            "<Control-BackSpace>", self._bind_event_search_ctrl_backspace
        )
        self._checkbutton.bind("<FocusIn>", self._bind_event_focus_in)
