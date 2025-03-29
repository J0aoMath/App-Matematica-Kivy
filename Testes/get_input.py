from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.textinput import re


class Main(BoxLayout):
    Label1 = Label(text='digite seu número:')
    text = ''
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        text_input = FloatInput(multiline = False)
        self.add_widget(self.Label1)
        self.add_widget(text_input)
        def on_enter(instance):
            print(self.text)
        def on_text(instance, value):
            self.text = value
        text_input.bind(text=on_text)
        text_input.bind(on_text_validate=on_enter)

class FloatInput(TextInput):

    pat = re.compile('[^0-9]')
    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        if '.' in self.text:
            s = re.sub(pat, '', substring)
        else:
            s = '.'.join(
                re.sub(pat, '', s)
                for s in substring.split('.', 1)
            )
        return super().insert_text(s, from_undo=from_undo)

class get_input(App):
    def build(self):
        return Main()

get_input().run()