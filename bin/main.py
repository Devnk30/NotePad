from tkinter import *
from data.notepad_personalize_menus import Personalize_menu
from data.notepad_shortcut_menu import Shortcut_menu
from data.notepad_help_menu import Help_menus


class Main(Personalize_menu, Shortcut_menu, Help_menus):
    """
    Main class of the Notepad application that inherits from the Personalize,
    Shortcut_menu, and Help_menus classes. These classes manage different aspects of the menu and editor customization.
    """

    def __init__(self):
        super().__init__()

    def _context_menu_config(self):
        """
        Configures context menu options. Includes undo, redo, copy, cut, paste, delete, customize font and color, and select all.
        """

        # Add commands to the context menu with images, labels and keyboard shortcuts
        self._context_menu.config(
            background=self._color3,
            activebackground=self._color1,
            foreground=self._color1,
        )
        self._context_menu.add_command(
            image=self._undo_editionmenu_image,
            label=f"   Undo{40 * " "}Ctrl+Z",
            font=(
                "Ubuntu Sans",
                "10",
                "bold italic",
            ),
            compound="left",
            command=self._custom_event_undo,
        )
        self._context_menu.add_command(
            image=self._redo_editionmenu_image,
            label=f"   Redo{40 * " "}Ctrl+Y",
            font=(
                "Ubuntu Sans",
                "10",
                "bold italic",
            ),
            compound="left",
            command=self._custom_event_redo,
        )
        self._context_menu.add_separator()
        self._context_menu.add_command(
            image=self._copy_editionmenu_image,
            label=f"   Copy{41 * " "}Ctrl+C",
            font=(
                "Ubuntu Sans",
                "10",
                "bold italic",
            ),
            compound="left",
            command=lambda: self._edition_menus("copy"),
        )
        self._context_menu.add_command(
            image=self._cut_editionmenu_image,
            label=f"   Cut{44 * " "}Ctrl+X",
            font=(
                "Ubuntu Sans",
                "10",
                "bold italic",
            ),
            compound="left",
            command=lambda: self._edition_menus("cut"),
        )
        self._context_menu.add_command(
            image=self._paste_editionmenu_image,
            label=f"   Paste{40 * " "}Ctrl+V",
            font=(
                "Ubuntu Sans",
                "10",
                "bold italic",
            ),
            compound="left",
            command=lambda: self._edition_menus("paste"),
        )
        self._context_menu.add_command(
            image=self._delete_editionmenu_image,
            label=f"   Delete{39 * " "}Supr",
            font=(
                "Ubuntu Sans",
                "10",
                "bold italic",
            ),
            compound="left",
            command=lambda: self._edition_menus("delete"),
        )
        self._context_menu.add_separator()
        self._context_menu.add_command(
            image=self._font_personalizemenu_image,
            label=f"   Font...{25 * " "}",
            font=(
                "Ubuntu Sans",
                "10",
                "bold italic",
            ),
            compound="left",
            command=self._add_font_menu,
        )
        self._context_menu.add_command(
            image=self._colorbook_personalizemenu_image,
            label="   Colorbook...",
            font=(
                "Ubuntu Sans",
                "10",
                "bold italic",
            ),
            compound="left",
            command=self._add_colorbook_menu,
        )
        self._context_menu.add_separator()
        self._context_menu.add_command(
            image=self._select_all_editionmenu_image,
            label=f"   Select All{34 * " "}Ctrl+E",
            font=(
                "Ubuntu Sans",
                "10",
                "bold italic",
            ),
            compound="left",
            command=lambda: self._edition_menus("select_all"),
        )

    def _show_context_menu(self, event):
        # Event that shows the context menu at the mouse position when right-clicking.

        self._context_menu.post(event.x_root, event.y_root)

    def _bind_event_ctrl_backspace(self, event):
        # Event q deletes a whole word backward or the selected text when pressing Ctrl+Backspace.

        self.__select_text = self._get_select_text()
        if self.__select_text.tag_ranges(SEL):
            self.__select_text.delete(
                self.__select_text.index(SEL_FIRST), self.__select_text.index(SEL_LAST)
            )

        else:
            self.__select_text.delete("insert-1c wordstart", "insert")

        return "break"

    def _update_state_undobutton(self, event):
        # Updates the state of the undo button (enabled or disabled).

        self._undo_shortcut.config(
            state=NORMAL if self._get_select_text().edit_modified() else DISABLED,
        )

    def _custom_event_paste(self, event):
        # Custom event to paste text and move the view to the cursor position.

        self._get_select_text().event_generate("<<Paste>>")

        self._get_select_text().mark_set("insert", "end-1c")
        self._get_select_text().see("insert")

        return "break"

    def _bind_event_select_all(self, event):
        # Event that selects all text in the text widget when Ctrl+E is pressed.

        self._get_select_text().tag_add(SEL, "1.0", END)
        return "break"

    def _bind_event_remove_tag(self, event):
        # Event that removes all search tags and hides the context menu when pressing Escape.

        self._get_select_text().tag_remove("Search", "1.0", END)
        self._get_select_text().tag_remove("Next_Previous_Search", "1.0", END)
        self._get_select_text().tag_remove("Replace", "1.0", END)
        self._context_menu.unpost()
        return "break"

    def _unpost_context_menu(self, event):
        # Hides the context menu.

        self._context_menu.unpost()

    def _run(self):
        """
        Configure the application, menus, and events, then start the main loop
        """

        self._themes_config_file()
        self._root_config()
        self._notebook_config()
        self._notepad_text_config()
        self._scrollbar_config()
        self._label_lines_config()
        self._add_shortcut_menu()
        self._add_filemenus()
        self._add_editionmenus()
        self._add_personalize_menu()
        self._add_help_menus()
        self._custom_checkbox_config()
        self._context_menu_config()

        # --------------------------- Bind events --------------------------- #
        # Binding events to specific methods for functionality like undo, redo, and paste

        self._get_select_text().bind(
            "<Control-BackSpace>", self._bind_event_ctrl_backspace
        )
        self._root.bind("<Control-n>", self._menu_new)
        self._root.bind("<Control-N>", self._menu_new)
        self._root.bind("<Control-a>", self._menu_openfile)
        self._root.bind("<Control-A>", self._menu_openfile)
        self._root.bind("<Control-g>", lambda save_as: self._menu_save(False))
        self._root.bind("<Control-G>", lambda save_as: self._menu_save(False))
        self._root.bind("<Control-s>", lambda save_as: self._menu_save(True))
        self._root.bind("<Control-S>", lambda save_as: self._menu_save(True))
        self._get_select_text().bind("<Control-v>", self._custom_event_paste)
        self._get_select_text().bind("<Control-V>", self._custom_event_paste)
        self._get_select_text().bind("<Control-z>", self._custom_event_undo)
        self._get_select_text().bind("<Control-Z>", self._custom_event_undo)
        self._get_select_text().bind("<Control-y>", self._custom_event_redo)
        self._get_select_text().bind("<Control-Y>", self._custom_event_redo)
        self._root.bind("<Control-f>", self._add_searchmenu)
        self._root.bind("<Control-F>", self._add_searchmenu)
        self._root.bind("<F1>", self._previous_search)
        self._root.bind("<F2>", self._next_search)
        self._root.bind("<Control-r>", self._add_menureplace)
        self._root.bind("<Control-R>", self._add_menureplace)
        self._root.bind("<Control-t>", self._add_menu_go_to)
        self._root.bind("<Control-T>", self._add_menu_go_to)
        self._get_select_text().bind("<Control-e>", self._bind_event_select_all)
        self._get_select_text().bind("<Control-E>", self._bind_event_select_all)
        self._root.bind("<Button-3>", self._show_context_menu)
        self._root.bind("<Button-1>", self._unpost_context_menu)
        self._menubar.bind("<Button-1>", self._unpost_context_menu)
        self._get_select_text().bind("<Escape>", self._bind_event_remove_tag)
        self._notebook.bind(
            "<<NotebookTabChanged>>",
            self._focustext_on_tab_selected,
        )
        self._notebook.bind("<ButtonPress-1>", self.tab_button_close_press)
        self._notebook.bind("<ButtonRelease-1>", self.tab_button_close_release)
        self._root.protocol("WM_DELETE_WINDOW", self._root.destroy)

        self._show_file_content()
        self._root.after(200, self._show_cursor_idx)
        self._get_select_text().bind("<<Modified>>", self._update_state_undobutton)
        self._root.mainloop()


def main():
    """Main function that creates and starts the Notepad application."""

    if __name__ == "__main__":
        app = Main()
        app._run()


main()
