from kivy.app import App
from kivy.config import Config
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.textinput import TextInput

Config.set('graphics','width','450')
Config.set('graphics','height','600')

class Main(BoxLayout):
    Opcao_Atual = [0]
    Titulo_Atual = ['']
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        #bt1 = Button(text='R', pos_hint={'x':.9,'y':.1}, size_hint=(.1,.1))
        self.tipo_conta = ['Operações Fundamentais', 'Equação do Primeiro Grau']
        self.Grid_Layout = []
        self.Numero_Contas = [12]
        self.Contas = []
        self.Respostas = []
        self.menu_conta = MenuConta()
        self.tela_inicial = TelaInicial()
        self.add_tela1_inicial()
    def add_tela1_inicial(self):
        self.add_widget(self.tela_inicial)

    def criar_contas():
        pass
    
    
class TelaInicial(AnchorLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def on_press_operacoes_fundamentais(self):
        self.remove_widget(self)
        self.add_widget(Main().menu_conta)
        print('Operações Fundamentais')
        Main.Titulo_Atual = ['Operações Fundamentais']
        Main.Opcao_Atual[0] = 1
    def on_press_equacoes_primeiro_grau(self):
        self.remove_widget(self)
        self.add_widget(Main().menu_conta)
        print('Equações do Primeiro Grau')
        Main.Titulo_Atual = ['Equações do Primeiro Grau']
        Main.Opcao_Atual[0] = 2
        
    def on_press_estatisticas(self):
        print('Estatísticas')
        print(Main().Opcao_Atual[0])
    def on_press_instrucoes(self):
        print('Instruções')
    def on_press_opcoes(self):
        print('Opções')
        
class MenuConta(AnchorLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.tela_inicial = TelaInicial()
        operacoes = MenuOperações()
        self.add_widget(operacoes)
    def on_press_adicao(self):
        print('Adicao')
        print(Main().Opcao_Atual[0])
    def on_press_subtracao(self):
        print('Subtracao')
    def on_press_multiplicacao(self):
        print('Multiplicacao')
    def on_press_divisao(self):
        print('Divisao')
    def on_press_misto(self):
        print('Misto')
    def return_button(self):
        Main.Opcao_Atual[0] = 0
        self.remove_widget(self)
        Main.add_tela1_inicial(self)

class MenuOperações(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.size_hint = (.64,.64)
        self.orientation = 'vertical'
        self.add_widget(Label(text= Main.Titulo_Atual[0], font_size="30dp", color=(.75,0,0)))
        self.add_widget(TextInput(multiline=False,size_hint=(1,.33)))
        self.add_widget(Button(text='Adição',size_hint = (1, .5)))
        self.add_widget(Button(text='Subtração',size_hint = (1, .5)))
        self.add_widget(Button(text='Multiplicação',size_hint = (1, .5)))
        self.add_widget(Button(text='divisão',size_hint = (1, .5)))
        self.add_widget(Button(text='Retornar',size_hint = (1, .33)))
class FormarGrades(BoxLayout):
    Label1_text = ''
    Contas = []
    Grid_Number = 0
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Label1 = Label(text=self.Label1_text)
        self.add_widget(Label1)
    









class RatoDeMatematica(App):
    def build(self):
        return Main()

RatoDeMatematica().run()
