from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934

class MilesConverterApp(App):
    result = StringProperty()

    def build(self):
        self.title = "Miles to Kilometres Converter"
        self.result = "0.0"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self):
        self.update_result()

    def handle_increment(self, value):
        try:
            current = float(self.root.ids.input_miles.text)
        except ValueError:
            current = 0.0
        current += value
        self.root.ids.input_miles.text = str(current)
        self.update_result()

    def update_result(self):
        try:
            miles = float(self.root.ids.input_miles.text)
            km = miles * MILES_TO_KM
            self.result = str(km)
        except ValueError:
            self.result = "0.0"