from tkinter import *
from data.notepad_root import Notepad


class Go_to_menu(Notepad):
    def __init__(self):
        super().__init__()

    def _menu_go_to(self):
        # Create a new top-level window for the "Go to" menu
        self.__go_to_toplevel = Toplevel(padx=20, pady=20, bg=self._color2)
        self.__go_to_toplevel.title("Go to")
        self.__go_to_toplevel.pack_propagate(False)  # Prevent resizing the window
        self.__go_to_toplevel.resizable(0, 0)  # Disable window resizing

        # Set the parent window for the new window
        self.__go_to_toplevel.transient(self._root)
        self.__go_to_toplevel.protocol(
            "WM_DELETE_WINDOW", self.__go_to_toplevel.destroy
        )

        ## Label Line number Config
        Label(
            self.__go_to_toplevel,
            text="Line number",
            bg=self._color2,
            fg=self._color1,
            font=("Ubuntu Sans", "10", "italic"),
        ).grid(row=1, column=1, padx=5, pady=(0, 5), sticky="w")

        ## Entry Line Config
        self.__line_entry = Entry(
            self.__go_to_toplevel,
            bg=self._color12,
            fg=self._color1,
            relief="flat",
            highlightthickness=1,
            highlightbackground=self._color1,
            highlightcolor=self._color1,
            insertbackground=self._color1,
            font=("Ubuntu Sans", "8", "italic"),
        )
        self.__line_entry.grid(
            row=2,
            column=1,
            columnspan=2,
            padx=5,
            pady=(5, 20),
            ipadx=71,
            ipady=1,
            sticky="nswe",
        )
        self.__line_entry.focus()

        ## Button Go to Config
        Button(
            self.__go_to_toplevel,
            text="Go to",
            bg=self._color12,
            activebackground=self._color1,
            fg=self._color1,
            activeforeground=self._color12,
            relief="flat",
            highlightthickness=0,
            highlightcolor=self._color1,
            width=12,
            font=("Ubuntu Sans", "9", "italic"),
            command=self._go_to,
        ).grid(row=3, column=1, sticky="e", padx=5)

        ## Button Cancel config
        Button(
            self.__go_to_toplevel,
            text="Cancel",
            bg=self._color12,
            activebackground=self._color1,
            fg=self._color1,
            activeforeground=self._color12,
            relief="flat",
            highlightthickness=0,
            highlightcolor=self._color1,
            width=12,
            font=("Ubuntu Sans", "9", "italic"),
            command=self.__go_to_toplevel.destroy,
        ).grid(row=3, column=2, sticky="w", padx=5)

    def _go_to(self):
        try:
            # Set the cursor to the specified line number
            self._get_select_text().mark_set(
                "insert",
                float(self.__line_entry.get()),
            )
            self._get_select_text().mark_unset("insert")
            self._get_select_text().focus()
            self._get_select_text().see(float(self.__line_entry.get()))

        except ValueError:
            print("ValueError")

    def _bind_event_go_to_ctrl_backspace(self, event):
        if self.__line_entry.select_present() == True:
            self.__line_entry.delete(
                self.__line_entry.index(SEL_FIRST),
                self.__line_entry.index(SEL_LAST),
            )
        else:
            self.__line_entry.delete("0", END)

        return "break"

    def _bind_event_go_to_return(self, event):
        if self.__line_entry != "":
            self._go_to()

        else:
            print("The entry is empty.")

    def _add_menu_go_to(self, event=None):
        self._menu_go_to()
        self.__line_entry.bind(
            "<Control-BackSpace>", self._bind_event_go_to_ctrl_backspace
        )
        self.__go_to_toplevel.bind("<Return>", self._bind_event_go_to_return)
