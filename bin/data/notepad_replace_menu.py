from data.notepad_search_menus import *


class Replace_menu(Search_menus):
    """
    Class to manage the replacement menu in a text editor.
    Inherits from Search_menus and provides an interface to search and replace text.
    """

    def __init__(self):
        # Initializes the Replace_menu class and calls the parent class constructor.
        super().__init__()

    def _menu_replace(self):
        """
        Creates and configures the window for the replacement menu.
        Includes inputs for text to find and replace, case sensitivity options, and action buttons.
        """

        # Create a new window (Toplevel) for the replacement menu
        self.__replacement_toplevel = Toplevel(padx=10, pady=10, bg=self._color2)

        # Window settings
        self.__replacement_toplevel.title("Replace")
        self.__replacement_toplevel.pack_propagate(False)
        self.__replacement_toplevel.resizable(0, 0)

        # Center window on screen
        self._width = round((self._screenwidth / 2) - (625 / 2))
        self._height = round((self._screenheight / 2) - (225 / 2))
        self.__replacement_toplevel.geometry(
            f"{625}x{225}+{self._width}+{self._height}"
        )

        # Configure behavior when closing the window
        self.__replacement_toplevel.transient(self._root)
        self.__replacement_toplevel.protocol(
            "WM_DELETE_WINDOW",
            self.__replacement_toplevel.destroy,
        )
        self.__replacement_toplevel.grab_set()

        # ------------------------- Widgets Settings ------------------------ #

        ## Label for warnings
        self._label_warning = Label(
            self.__replacement_toplevel,
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
            self.__replacement_toplevel,
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
            self.__replacement_toplevel,
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
        self._search_entry.focus()  # Set focus to this field

        ## Label for replacement text
        self._replacement_label = Label(
            self.__replacement_toplevel,
            text="Replace: ",
            bg=self._color2,
            fg=self._color1,
            font=("Ubuntu Sans", "10", "italic"),
        )
        self._replacement_label.grid(
            row=2,
            column=1,
            sticky="w",
            padx=(22, 0),
            pady=(10, 0),
        )

        ## Input field for replacement text
        self._replacement_entry = Entry(
            self.__replacement_toplevel,
            bg=self._color12,
            fg=self._color1,
            relief="flat",
            highlightthickness=1,
            highlightbackground=self._color1,
            highlightcolor=self._color1,
            insertbackground=self._color1,
            font=("Ubuntu Sans", "10", "italic"),
        )
        self._replacement_entry.grid(
            row=2,
            column=2,
            padx=(18, 5),
            ipadx=140,
            ipady=1,
            pady=(10, 0),
        )

        ## Checkbutton for case sensitive search
        self._checkbutton = Checkbutton(
            self.__replacement_toplevel,
            text="Case Sensitive",
            style="TCheckbutton",
            variable=self._checkvalue,
        )
        self._checkbutton.grid(
            row=3,
            column=2,
            padx=(16, 0),
            sticky="w",
            pady=10,
        )

        ## Button to replace the first match
        self._button_replace = Button(
            self.__replacement_toplevel,
            text="Replace",
            bg=self._color12,
            activebackground=self._color1,
            fg=self._color1,
            activeforeground=self._color12,
            relief="flat",
            width=15,
            highlightthickness=0,
            highlightcolor=self._color1,
            font=("Ubuntu Sans", "9", "italic"),
            command=self._replace,
        )
        self._button_replace.grid(
            row=3,
            column=2,
            sticky="e",
            padx=(0, 5),
            pady=(5, 0),
        )

        ## Previous match button
        self._button_previous = Button(
            self.__replacement_toplevel,
            text="Previous",
            bg=self._color12,
            activebackground=self._color1,
            fg=self._color1,
            activeforeground=self._color12,
            relief="flat",
            width=15,
            highlightthickness=0,
            highlightcolor=self._color1,
            font=("Ubuntu Sans", "9", "italic"),
            command=self._previous_search,
        )
        self._button_previous.grid(
            row=4,
            column=2,
            sticky="w",
            padx=(18, 0),
            pady=5,
        )

        ## Next match button
        self._button_next = Button(
            self.__replacement_toplevel,
            text="Next",
            bg=self._color12,
            activebackground=self._color1,
            fg=self._color1,
            activeforeground=self._color12,
            relief="flat",
            width=15,
            highlightthickness=0,
            highlightcolor=self._color1,
            font=("Ubuntu Sans", "9", "italic"),
            command=self._next_search,
        )
        self._button_next.grid(
            row=4,
            column=2,
            sticky="e",
            padx=(0, 5),
        )

        ## Button to replace all matches
        self._button_replace_all = Button(
            self.__replacement_toplevel,
            text="Replace all",
            bg=self._color12,
            activebackground=self._color1,
            fg=self._color1,
            activeforeground=self._color12,
            relief="flat",
            width=15,
            highlightthickness=0,
            highlightcolor=self._color1,
            font=("Ubuntu Sans", "9", "italic"),
            command=lambda: self._replace_all(),
        )
        self._button_replace_all.grid(
            row=4,
            column=2,
            sticky="w",
            padx=(174, 0),
            pady=5,
        )

        ## Button to cancel and close the window
        self._button_cancel = Button(
            self.__replacement_toplevel,
            text="Cancel",
            bg=self._color12,
            activebackground=self._color1,
            fg=self._color1,
            activeforeground=self._color12,
            relief="flat",
            highlightthickness=0,
            highlightcolor=self._color1,
            font=("Ubuntu Sans", "9", "italic"),
            command=self.__replacement_toplevel.destroy,
        )
        self._button_cancel.grid(
            row=5,
            column=2,
            sticky="nswe",
            padx=(18, 5),
        )

        self._search_entry.insert("0", self._savetext_search_entry)

    def _replace(self):
        """
        Replaces the currently highlighted text with the text from the replacement entry.
        If no match is highlighted, displays a warning message.
        """

        if not self._fst_matching_idx:
            self._fst_matching_idx = (
                "1.0"  # Reset to the start if no match is found yet
            )

        else:
            try:
                # Get the range of the next match
                self._fst_matching_idx, self._last_matching_idx = (
                    self._get_select_text().tag_ranges("Next_Previous_Search")
                )

                # Delete the currently matched text
                self._get_select_text().delete(
                    self._fst_matching_idx, self._last_matching_idx
                )

                # Insert the replacement text
                self._get_select_text().insert(
                    self._fst_matching_idx, self._replacement_entry.get()
                )

                # Update the last matching index to match the length of the replacement text
                self._last_matching_idx = (
                    f"{self._fst_matching_idx}+{len(self._replacement_entry.get())}c"
                )

                # Apply a tag to highlight the replaced text
                self._get_select_text().tag_add(
                    "Replace",
                    self._fst_matching_idx,
                    self._last_matching_idx,
                )

                # Set the first matching index to the last, so we continue replacing in the next iteration
                self._fst_matching_idx = self._last_matching_idx

                # Configure the tag to highlight the replaced text with a custom background and foreground color
                self._get_select_text().tag_config(
                    "Replace",
                    background=self._color18,
                    foreground=self._color17,
                )

                # Set the replace flag to indicate that a replacement has occurred
                self._boolreplace.set(True)

            except ValueError:
                print("ValueError")

    def _replace_all(self):
        """
        Replaces all occurrences of the search text with the replacement text in the text widget.
        If no matches are found, displays a warning message.
        If the search entry is empty, removes all applied tags.
        Supports case-sensitive and case-insensitive searches based on the checkbox value.
        """

        # Check if the search entry is not empty
        if self._search_entry.get() != "":

            # Remove all tags from previous searches and replacements
            self._get_select_text().tag_remove("Search", "1.0", END)
            self._get_select_text().tag_remove("Next_Previous_Search", "1.0", END)
            self._get_select_text().tag_remove("Replace", "1.0", END)

            self._fst_matching_idx = "1.0"  # Reset the first matching index
            self._list_index.clear()  # Clear the list of indexes
            self._searchtext = (
                self._search_entry.get()
            )  # Get the search text from the entry

            while True:
                # If the checkbox is checked, perform case-sensitive search, otherwise do case-insensitive search
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

                if not self._fst_matching_idx:
                    self._fst_matching_idx = "1.0"  # Reset if no match is found
                    if self._list_index == []:
                        self._label_warning.config(
                            text="No match found!!!"
                        )  # Show warning if no matches
                    break

                else:
                    # Calculate the last matching index based on the search text length
                    self._last_matching_idx = (
                        f"{self._fst_matching_idx}+{len(self._searchtext)}c"
                    )

                    # Replace the text
                    self._get_select_text().delete(
                        self._fst_matching_idx,
                        self._last_matching_idx,
                    )
                    self._get_select_text().insert(
                        self._fst_matching_idx,
                        self._replacement_entry.get(),
                    )

                    # Update the last matching index after replacement
                    self._last_matching_idx = f"{self._fst_matching_idx}+{len(self._replacement_entry.get())}c"

                    # Apply the "Replace" tag for visual highlighting
                    self._get_select_text().tag_add(
                        "Replace",
                        self._fst_matching_idx,
                        self._last_matching_idx,
                    )

                    # Append the index to the list for tracking replacements
                    self._list_index.append(self._fst_matching_idx)

                    # Configure the tag color for replaced text
                    self._get_select_text().tag_config(
                        "Replace",
                        background=self._color18,
                        foreground=self._color17,
                    )

                    # Update the first matching index to the last one for the next iteration
                    self._fst_matching_idx = self._last_matching_idx
                    self._label_warning.config(text="")  # Clear the warning label

            # Save the current search text for future use
            self._savetext_search_entry = self._searchtext

        # If the search entry is empty, remove tags
        elif self._search_entry.get() == "":
            self._get_select_text().tag_remove("Search", "1.0", END)
            self._get_select_text().tag_remove("Next_Previous_Search", "1.0", END)
            self._get_select_text().tag_remove("Replace", "1.0", END)

    def _bind_event_replace_ctrl_backspace(self, event):
        if self._replacement_entry.select_present() == True:
            self._replacement_entry.delete(
                self._replacement_entry.index(SEL_FIRST),
                self._replacement_entry.index(SEL_LAST),
            )

        else:
            self._replacement_entry.delete("0", END)

        return "break"

    def _add_menureplace(self, event=None):
        self._menu_replace()
        self.__replacement_toplevel.after(
            200, self._search(self.__replacement_toplevel)
        )
        self._search_entry.bind(
            "<Control-BackSpace>", self._bind_event_search_ctrl_backspace
        )
        self._replacement_entry.bind(
            "<Control-BackSpace>", self._bind_event_replace_ctrl_backspace
        )
        self._checkbutton.bind("<FocusIn>", self._bind_event_focus_in)
