import tkinter as tk

class App(tk.Frame):
    """Aplicação GUI simples com uma caixa de entrada de texto e um retorno de chamada com tecla Enter."""

    def __init__(self, master):
        """
        Initialize the application.

        :param master: The Tkinter master widget.
        """
        super().__init__(master)
        self.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("this is a variable")
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.contents

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrythingy.bind('<Key-Return>',
                             self.print_contents)

    def print_contents(self, event):
        """
        Print the current content of the entry widget when the user hits return.

        :param event: The event that triggered this callback.
        """
        print("Hi. The current entry content is:",
              self.contents.get())

    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get())

root = tk.Tk()
myapp = App(root)
myapp.mainloop()
