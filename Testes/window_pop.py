from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class MainWidget(BoxLayout):
    lb1 = Label(text="Label 1")
    lb2 = Label(text="Label 2")
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.boxlayout2 = BoxLayout2()
        self.add_widget(self.lb1)
        self.add_widget(self.lb2)
        self.add_widget(self.boxlayout2)
                
class BoxLayout2(BoxLayout):
    bt1 = Button(text="Botão 1",size_hint= (1, .5))
    bt2 = Button(text="Botão 2")
    list2 = [bt1,bt2]
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(self.list2[0])
        self.add_widget(self.list2[1])
        
class Opa_(App):
    def build(self):
        return MainWidget()



Opa_().run()