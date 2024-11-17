import os
from tkinter import *
from tkinter.ttk import Separator
from tkinter.ttk import Button as ttk_Button
from data.notepad_edition_menus import Edition_menus
from data.notepad_file_menus import File_menus

"""
Creates and adds a shortcut menu (toolbar) to the Notepad application.
The menu includes buttons for common actions such as creating, opening, saving, undoing, redoing, copying, cutting, pasting, searching, and replacing text.
Each button is represented with an image icon and is associated with a specific command.
The shortcut menu also includes separators between groups of actions for better visual organization.
Additionally, the undo and redo actions are integrated into the edition menu with associated keyboard shortcuts (Ctrl+Z and Ctrl+Y).
"""


class Shortcut_menu(File_menus, Edition_menus):
    def __init__(self):
        super().__init__()

        # Create a frame for the shortcut toolbar
        self._shortcut_bar = Frame(self._root)

        # Load image files for each button (File operations and Edit actions)
        self._new_file_shortcut_image = PhotoImage(
            file=os.path.join(self._xpath_images, "new_file.png"),
        )
        self._open_file_shortcut_image = PhotoImage(
            file=os.path.join(self._xpath_images, "open_file.png"),
        )
        self._save_file_shortcut_image = PhotoImage(
            file=os.path.join(self._xpath_images, "savefile.png"),
        )
        self._undo_shortcut_image = PhotoImage(
            file=os.path.join(self._xpath_images, "undo.png"),
        )
        self._redo_shortcut_image = PhotoImage(
            file=os.path.join(self._xpath_images, "redo.png"),
        )
        self._copy_shortcut_image = PhotoImage(
            file=os.path.join(self._xpath_images, "copy.png"),
        )
        self._cut_shortcut_image = PhotoImage(
            file=os.path.join(self._xpath_images, "cut.png"),
        )
        self._paste_shortcut_image = PhotoImage(
            file=os.path.join(self._xpath_images, "paste.png"),
        )
        self._search_shortcut_image = PhotoImage(
            file=os.path.join(self._xpath_images, "search.png"),
        )
        self._replace_shortcut_image = PhotoImage(
            file=os.path.join(self._xpath_images, "replace.png"),
        )
        self._undo_editionmenu_image = PhotoImage(
            file=os.path.join(self._xpath_images, "undo_editionmenu.png")
        )
        self._redo_editionmenu_image = (
            PhotoImage(  # Create a frame for the shortcut toolbar
                file=os.path.join(self._xpath_images, "redo_editionmenu.png")
            )
        )

    # Method to add the shortcut menu (toolbar) to the interface
    def _add_shortcut_menu(self):

        # Configure the style for separators in the toolbar
        self.style.configure("TSeparator", background="black", borderwidth=5)

        # Set properties for the shortcut bar (toolbar frame)
        self._shortcut_bar.config(
            height=50,
            bg=self._color4,
            relief="flat",
        )

        # Configure style for the shortcut buttons
        self.style.configure(
            "Shortcut.TButton",
            relief="flat",
            background=self._color4,
            highlightthickness=0,
            borderwidth=0,
        )

        # Map button style to change color when active or disabled
        self.style.map(
            "Shortcut.TButton",
            background=[("active", self._color1), ("disabled", self._color4)],
        )

        # Adding buttons to the toolbar
        self._newfile_shortcut = ttk_Button(
            self._shortcut_bar,
            image=self._new_file_shortcut_image,
            cursor="hand2",
            takefocus=False,
            width=34,
            style="Shortcut.TButton",
            command=self._menu_new,
        )
        self._newfile_shortcut.pack(side="left", padx=5, pady=2)

        self._openfile_shortcut = ttk_Button(
            self._shortcut_bar,
            image=self._open_file_shortcut_image,
            cursor="hand2",
            takefocus=False,
            width=34,
            style="Shortcut.TButton",
            command=self._menu_openfile,
        )
        self._openfile_shortcut.pack(side="left", padx=5, pady=2)

        self._savefile_shortcut = ttk_Button(
            self._shortcut_bar,
            image=self._save_file_shortcut_image,
            cursor="hand2",
            takefocus=False,
            width=34,
            style="Shortcut.TButton",
            command=lambda: self._menu_save(False),
        )
        self._savefile_shortcut.pack(side="left", padx=5, pady=2)

        Separator(self._shortcut_bar, orient="vertical").pack(
            side="left", fill="y", padx=5, pady=12
        )

        self._undo_shortcut = ttk_Button(
            self._shortcut_bar,
            image=self._undo_shortcut_image,
            cursor="hand2",
            takefocus=False,
            width=34,
            style="Shortcut.TButton",
            command=self._custom_event_undo,
        )
        self._undo_shortcut.pack(side="left", padx=5, pady=2)

        self._redo_shortcut = ttk_Button(
            self._shortcut_bar,
            image=self._redo_shortcut_image,
            cursor="hand2",
            takefocus=False,
            width=34,
            style="Shortcut.TButton",
            state=DISABLED,
            command=self._custom_event_redo,
        )
        self._redo_shortcut.pack(side="left", padx=5, pady=2)

        # Add a vertical separator between buttons
        Separator(self._shortcut_bar, orient="vertical").pack(
            side="left", fill="y", padx=5, pady=12
        )

        self._copy_shortcut = ttk_Button(
            self._shortcut_bar,
            image=self._copy_shortcut_image,
            cursor="hand2",
            takefocus=False,
            width=34,
            style="Shortcut.TButton",
            command=lambda: self._edition_menus("copy"),
        )
        self._copy_shortcut.pack(side="left", padx=5, pady=2)

        self._cut_shortcut = ttk_Button(
            self._shortcut_bar,
            image=self._cut_shortcut_image,
            cursor="hand2",
            takefocus=False,
            width=34,
            style="Shortcut.TButton",
            command=lambda: self._edition_menus("cut"),
        )
        self._cut_shortcut.pack(side="left", padx=5, pady=2)

        self._paste_shortcut = ttk_Button(
            self._shortcut_bar,
            image=self._paste_shortcut_image,
            cursor="hand2",
            takefocus=False,
            width=34,
            style="Shortcut.TButton",
            command=lambda: self._edition_menus("paste"),
        )
        self._paste_shortcut.pack(side="left", padx=5, pady=2)

        # Add a vertical separator between buttons
        Separator(self._shortcut_bar, orient="vertical").pack(
            side="left", fill="y", padx=5, pady=12
        )

        self._search_shortcut = ttk_Button(
            self._shortcut_bar,
            image=self._search_shortcut_image,
            cursor="hand2",
            takefocus=False,
            width=34,
            style="Shortcut.TButton",
            command=self._add_searchmenu,
        )
        self._search_shortcut.pack(side="left", padx=5, pady=2)

        self._replace_shortcut = ttk_Button(
            self._shortcut_bar,
            image=self._replace_shortcut_image,
            cursor="hand2",
            takefocus=False,
            width=34,
            style="Shortcut.TButton",
            command=self._add_menureplace,
        )
        self._replace_shortcut.pack(side="left", padx=5, pady=2)

        # Place the toolbar in the window using grid layout
        self._shortcut_bar.grid(
            row=0, column=0, columnspan=2, pady=(0, 5), sticky="nwe"
        )

        # Prevent the toolbar from resizing with its content
        self._shortcut_bar.propagate(False)

        # Insert "Undo" command into the edition menu
        self._edition_menu.insert_command(
            0,
            image=self._undo_editionmenu_image,
            label=f"   Undo{50 * " "}Ctrl+Z",  # Label with keyboard shortcut
            compound="left",  # Place image on the left
            command=self._custom_event_undo,  # Link to the undo function
        )

        # Insert "Redo" command into the edition menu
        self._edition_menu.insert_command(
            1,
            image=self._redo_editionmenu_image,
            label=f"   Redo{50 * " "}Ctrl+Y",  # Label with keyboard shortcut
            compound="left",
            command=self._custom_event_redo,  # Link to the redo function
        )

    def _custom_event_undo(self, event=None):
        try:
            # Try to perform the undo
            self._get_select_text().edit_undo()

            # Enable the redo button, since an undo was performed
            self._redo_shortcut.config(state=NORMAL)

        except TclError:
            print("TclError")

        return "break"

    def _custom_event_redo(self, event=None):

        try:
            # Try to perform the redo
            self._get_select_text().edit_redo()
            # Check if there are no more networks available
            self._get_select_text().edit_redo()
            self._get_select_text().edit_undo()  # Restore previous state

        except TclError:
            # Disable the redo button if there are no more redo available
            self._redo_shortcut.config(state=DISABLED)

        return "break"
