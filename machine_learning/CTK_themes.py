import customtkinter as ctk


class CustomTheme(ctk.CTk):
    """
    A base singleton class for custom themes.
    Ensures that we can call (CustomTheme inheritor).get_main()
    multiple times and only have it initialised once.
    """
    MAIN = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @classmethod
    def get_main(cls):
        """
        Returns the singleton, creating it if needed.
        """
        if cls.MAIN is None:
            cls.MAIN = cls()
        return cls.MAIN

class DarkMode(CustomTheme):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("dark-blue")

def test():
    root=DarkMode()
    root.title("Dark Mode Example")
    root.geometry("400x300")

    # Add a button to the window
    button = ctk.CTkButton(master=root, text="Click Me")
    button.pack(pady=20)

    root.mainloop()


def main():
    return


if __name__ == "__main__":
    main()
