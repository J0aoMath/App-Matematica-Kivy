from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class Main(BoxLayout):
    numero_contas = [12]
    contas = []
    respostas = []
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    def soma(self):
        
        for i in range(0,len(self.numero_contas)):
            conta = 'x+y'
            self.contas.append(conta)
            resposta = 'z'
            self.respostas.append(resposta)
            
    def subtrasao(self):
        pass
    def divisao(self):
        pass
    def multiplikasao(self):
        pass
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




class The_(App):
    def build(self):
        return Main()

The_().run()