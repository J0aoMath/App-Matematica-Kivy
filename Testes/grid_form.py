from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class Main(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        grid_contas = GridContas()
        self.add_widget(grid_contas)
    
    
class GridContas(BoxLayout):
    Layout1 = GridLayout(cols = 3,rows = 2, orientation='lr-tb')
    Layout2 = GridLayout(cols = 3,rows = 2, orientation='lr-tb')
    Layout3 = GridLayout(cols = 3,rows = 2, orientation='lr-tb')
    Grid_Layouts = [Layout1, Layout2, Layout3]
    Text_Inputs = []
    equacoes = []
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        for i in range(0,len(self.Grid_Layouts)):
            for b in range(0,3):
                box_layout = BoxLayout(orientation = 'vertical')
                el_label = Label(text='Olá, Mundo! ' + str(i))
                text_input = TextInput(multiline=False)
                self.Text_Inputs.append(text_input)
                box_layout.add_widget(el_label)
                box_layout.add_widget(text_input)
                self.Grid_Layouts[i].add_widget(box_layout)
            self.add_widget(self.Grid_Layouts[i])
        print(self.Text_Inputs)






class The(App):
    def build(self):
        return Main()

The().run()