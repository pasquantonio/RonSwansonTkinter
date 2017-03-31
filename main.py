#!/usr/bin/env python
import Tkinter
import requests


class GUI:
    """
    A simple Tkinter GUI that displays a random Ron Swanson quote from the TV
    show Parks and Recreation. To get the quotes, this hits the ron swanson
    quote API from here: https://github.com/jamesseanwright/ron-swanson-quotes
    """
    def __init__(self):
        """
        Sets up GUI and variables to display quotes
        """
        self.url = "http://ron-swanson-quotes.herokuapp.com/v2/quotes"
        self.root = Tkinter.Tk()
        self.root.title("Ron Swanson Quotes")
        self.text = Tkinter.StringVar()
        self.label = Tkinter.Label(self.root, textvariable=self.text)
        self.text.set(self.request_quote())
        self.label.pack()
        self.button = Tkinter.Button(self.root,
                                     text="Refresh",
                                     command=self.refresh_callback)
        self.button.pack()
        self.root.mainloop()

    def request_quote(self):
        """
        Makes an HTTP request and retrieves one Ron Swonson quote
        """
        response = requests.get(self.url)
        return response.json()[0]

    def refresh_callback(self):
        """
        Invoked when refresh button is pushed
        """
        self.text.set(self.request_quote())
        self.label.pack()


if __name__ == "__main__":
    gui = GUI()
