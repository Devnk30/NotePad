import os
from tkinter import *
from data.notepad_replace_menu import Replace_menu
from data.notepad_go_to_menu import Go_to_menu


class Edition_menus(Replace_menu, Go_to_menu):
    def __init__(self):
        super().__init__()

        self._copy_editionmenu_image = PhotoImage(
            file=os.path.join(self._xpath_images, "copy_editionmenu.png")
        )
        self._cut_editionmenu_image = PhotoImage(
            file=os.path.join(self._xpath_images, "cut_editionmenu.png")
        )
        self._paste_editionmenu_image = PhotoImage(
            file=os.path.join(self._xpath_images, "paste_editionmenu.png")
        )
        self._delete_editionmenu_image = PhotoImage(
            file=os.path.join(self._xpath_images, "delete_editionmenu.png")
        )
        self._search_editionmenu_image = PhotoImage(
            file=os.path.join(self._xpath_images, "search_editionmenu.png")
        )
        self._nextsearch_editionmenu_image = PhotoImage(
            file=os.path.join(self._xpath_images, "nextsearch_editionmenu.png")
        )
        self._previoussearch_editionmenu_image = PhotoImage(
            file=os.path.join(self._xpath_images, "previoussearch_editionmenu.png")
        )
        self._replace_editionmenu_image = PhotoImage(
            file=os.path.join(self._xpath_images, "replace_editionmenu.png")
        )
        self._go_to_editionmenu_image = PhotoImage(
            file=os.path.join(self._xpath_images, "go_to_editionmenu.png")
        )
        self._select_all_editionmenu_image = PhotoImage(
            file=os.path.join(self._xpath_images, "select_all_editionmenu.png")
        )

    def _add_editionmenus(self):
        # -------------------------- Edition Menus -------------------------- #

        self._menubar.add_cascade(
            label="  Edition  ",
            menu=self._edition_menu,
            font=(
                "Ubuntu Sans",
                "10",
                "bold italic",
            ),
        )
        self._edition_menu.config(
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

        self._edition_menu.add_separator()
        self._edition_menu.add_command(
            image=self._copy_editionmenu_image,
            label=f"   Copy{51 * " "}Ctrl+C",
            compound="left",
            command=lambda: self._edition_menus("copy"),
        )
        self._edition_menu.add_command(
            image=self._cut_editionmenu_image,
            label=f"   Cut{54 * " "}Ctrl+X",
            compound="left",
            command=lambda: self._edition_menus("cut"),
        )
        self._edition_menu.add_command(
            image=self._paste_editionmenu_image,
            label=f"   Paste{50 * " "}Ctrl+V",
            compound="left",
            command=lambda: self._edition_menus("paste"),
        )
        self._edition_menu.add_command(
            image=self._delete_editionmenu_image,
            label=f"   Delete{49 * " "}Supr",
            compound="left",
            command=lambda: self._edition_menus("delete"),
        )
        self._edition_menu.add_separator()
        self._edition_menu.add_command(
            image=self._search_editionmenu_image,
            label=f"   Search...{44 * " "}Ctrl+F",
            compound="left",
            command=self._add_searchmenu,
        )

        self._edition_menu.add_command(
            image=self._nextsearch_editionmenu_image,
            label=f"   Find Next{46 * " "}F3",
            compound="left",
            command=lambda: self._next_search("menu_find_next"),
        )

        self._edition_menu.add_command(
            image=self._previoussearch_editionmenu_image,
            label=f"   Find Previous{38 * " "}F2",
            compound="left",
            command=lambda: self._previous_search("menu_find_previous"),
        )

        self._edition_menu.add_command(
            image=self._replace_editionmenu_image,
            label=f"   Replace...{42 * " "}Ctrl+R",
            compound="left",
            command=self._add_menureplace,
        )

        self._edition_menu.add_command(
            image=self._go_to_editionmenu_image,
            label=f"   Go to line...{38 * " "}Ctrl+T",
            compound="left",
            command=self._add_menu_go_to,
        )

        self._edition_menu.add_separator()
        self._edition_menu.add_command(
            image=self._select_all_editionmenu_image,
            label=f"   Select All{44 * " "}Ctrl+E",
            compound="left",
            command=lambda: self._edition_menus("select_all"),
        )

    def _edition_menus(self, menu):
        self._get_select_text().focus()

        try:
            match menu:

                case "copy":
                    self._get_select_text().event_generate("<<Copy>>")

                case "cut":
                    self._get_select_text().event_generate("<<Cut>>")

                case "paste":
                    self._get_select_text().event_generate("<<Paste>>")
                    self._get_select_text().see(INSERT)

                case "delete":
                    self._get_select_text().delete(
                        self._get_select_text().index(SEL_FIRST),
                        self._get_select_text().index(SEL_LAST),
                    )

                case "select_all":
                    self._get_select_text().tag_add(SEL, "1.0", END)

        except TclError:
            print("TclError")
