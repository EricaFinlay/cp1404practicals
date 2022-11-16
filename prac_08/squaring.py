"""
CP1404 2022 Prac 08
Erica Finlay

Square Number
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Lindsay Ward'


class SquareNumberApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number."""

    def build(self):
        """ Build the Kivy app from the kv file."""
        Window.size = (200, 100)
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        """Handle calculation (could be button press or other call) and output result to label widget."""
        try:
            result = float(value) ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            pass


SquareNumberApp().run()
