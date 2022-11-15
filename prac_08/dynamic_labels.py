"""
CP1404 2022 Prac 08
Erica Finlay

Dynamic Labels

The following sources were consulted in the writing of this program:
    1. Kivy Demos file - dynamic_widgets.py and dynamic_widgets.kv
    2. Question asked on CP1404 Slack channel (12.11.2022) by Kaung Min Aung,
       and answer supplied by Dannielle Jones.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    """DynamicLabelsApp is a Kivy App to display a list of colour names."""
    answer = StringProperty()

    def __init__(self, **kwargs):
        """Initialise list of colours."""
        super().__init__(**kwargs)
        self.colours = ["Red", "Yellow", "Blue", "Green", "Purple", "White", "Orange", "Black", "Brown"]

    def build(self):
        """ Build the Kivy app from the kv file."""
        self.title = "List of Colours"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_list()
        return self.root

    def create_list(self):
        """Display list of colours in widget."""
        for colour in self.colours:
            temp_label = Label(text=colour)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
