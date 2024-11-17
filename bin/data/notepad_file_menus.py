import os
from tkinter import *
from tkinter import filedialog
from data.notepad_root import Notepad


class File_menus(Notepad):
    def __init__(self):
        super().__init__()

        self._newfile_editionmenu_image = PhotoImage(
            file=os.path.join(self._xpath_images, "newfile_editionmenu.png")
        )
        self._openfile_editionmenu_image = PhotoImage(
            file=os.path.join(self._xpath_images, "openfile_editionmenu.png")
        )
        self._savefile_editionmenu_image = PhotoImage(
            file=os.path.join(self._xpath_images, "savefile_editionmenu.png")
        )
        self._savefile_as_editionmenu_image = PhotoImage(
            file=os.path.join(self._xpath_images, "savefile_as_editionmenu.png")
        )

    def _add_filemenus(self):

        # --------------------------- File Menus ---------------------------- #
        self._menubar.add_cascade(
            label="  File  ",
            menu=self._file_menu,
            font=(
                "Ubuntu Sans",
                "10",
                "bold italic",
            ),
        )
        self._file_menu.config(
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
        self._file_menu.add_command(
            image=self._newfile_editionmenu_image,
            label=f"   New{50 * " "}Ctrl+N",
            compound="left",
            command=self._menu_new,
        )
        self._file_menu.add_command(
            image=self._openfile_editionmenu_image,
            label=f"   Open File...{36 * " "}Ctrl+A",
            compound="left",
            command=self._menu_openfile,
        )
        self._file_menu.add_command(
            image=self._savefile_editionmenu_image,
            label=f"   Save{49 * " "}Ctrl+G",
            compound="left",
            command=lambda: self._menu_save(False),
        )
        self._file_menu.add_command(
            image=self._savefile_as_editionmenu_image,
            label=f"   Save As...{40 * " "}Ctrl+S",
            compound="left",
            command=lambda: self._menu_save(True),
        )
        self._file_menu.add_separator()
        self._file_menu.add_command(
            label="Exit",
            command=self._root.destroy,
        )

    def _menu_new(self, event=None):
        self._notebook.add(self._notepad_text_config(), text="New File*")
        self._file_path_list.append(os.path.join(os.getcwd(), "New File*"))

        self._notebook.select(self._notebook.winfo_children()[-1])
        self._get_select_text().focus()

    def _menu_openfile(self, event=None):
        try:

            self.__text = filedialog.askopenfilename(
                title="Open",
                defaultextension="*.txt",
                filetypes=(
                    ("All files", "*.*"),
                    ("Text files", "*.txt"),
                ),
            )

            self._filename = os.path.basename(self.__text)
            self._title_filename = os.path.splitext(self._filename)[0]
            self._file_path_list.append(self.__text)

            with open(self.__text, "r", encoding="utf-8") as f:
                self._notebook.add(
                    self._notepad_text_config(), text=self._title_filename
                )

                # accessing the notebook's children list to select the last tab created using the len function.
                self._notebook.select(self._notebook.winfo_children()[-1])

                self._notebook.winfo_children()[-1].focus()
                self._notebook.winfo_children()[-1].insert("1.0", f.read())
                self._root.title(self.__text)

        except TypeError:
            print("type error")

        except FileNotFoundError:
            print("file not found")

    def _menu_save(self, save_as, event=None):

        self.__file_path = self._file_path_list[
            self._notebook.index(self._notebook.select())
        ]

        self._filename = os.path.basename(self.__file_path)

        if self._filename == "New File*" or save_as == True:

            try:
                self.__text = filedialog.asksaveasfilename(
                    title="Save",
                    initialfile=self._filename,
                    defaultextension="*.txt",
                    filetypes=(("txt files", "*.txt"),),
                )

                with open(self.__text, "w", encoding="utf8") as f:
                    f.write(self._get_select_text().get("1.0", END))

                    self._filename = os.path.basename(self.__text)
                    self._title_filename = os.path.splitext(self._filename)[0]
                    self.__index_file = self._file_path_list.index(self.__file_path)
                    self._file_path_list.pop(self.__index_file)
                    self._file_path_list.insert(self.__index_file, self.__text)

                    self._notebook.tab(
                        self._notebook.winfo_children()[
                            self._notebook.index(self._notebook.select())
                        ],
                        text=self._title_filename,
                    )
                    self._root.title(self.__text)

            except TypeError:
                print("Type Error")

            except FileNotFoundError:
                print("FileNotFoundError")

        else:
            with open(self.__file_path, "w", encoding="utf8") as f:
                f.write(self._get_select_text().get("1.0", END))
