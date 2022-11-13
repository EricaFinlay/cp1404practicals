"""
CP1404 2022 Prac 08
Erica Finlay
Miles to Kilometres Converter

The solutions branch in GitHub was consulted for the writing of this program:
https://github.com/CP1404/Practicals/tree/solutions/prac_08
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

__author__ = 'Erica Finlay'

MILES_TO_KILOMETRES_CONVERSION = 1.60934


class DistanceConverter(App):
    """Provide conversion of miles to kilometres."""
    output_number = StringProperty()

    def build(self):
        """Create kivy app using kivy file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, text):
        """Handle calculation of data."""
        miles = self.convert_to_number(text)
        self.update_result(miles)

    def handle_editing(self, text, edit):
        """Handle editing of number"""
        miles = self.convert_to_number(text) + edit
        self.root.ids.input_number.text = str(miles)

    def update_result(self, miles):
        """Re-calculate output number."""
        self.output_number = str(miles * MILES_TO_KILOMETRES_CONVERSION)

    def convert_to_number(self, text):
        """Convert text to float and provide error checking."""
        try:
            return float(text)
        except ValueError:
            return 0.0


DistanceConverter().run()
