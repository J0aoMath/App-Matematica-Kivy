from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.config import Config
Config.set('graphics','height', '600')
Config.set('graphics','width', '450')

class Main(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        menu_inicial = MenuInicial()
        menu_operacoes = MenuOperacoes()
        menu_equacoes = MenuEquacoes()
        self.add_widget(menu_inicial)
        
        
class MenuInicial(AnchorLayout):
    def bt_operacoes(self):
        print('Operacoes Basicas')
        #self.remove_widget(self)
    def bt_equacoes(self):
        print('Equacoes do Primeiro Grau')
        #self.remove_widget(self)
    def bt_estatisticas(self):
        print('Operacoes Basicas')
        #self.remove_widget(self)
    def bt_opcoes(self):
        print('Equacoes do Primeiro Grau')
        #self.remove_widget(self)
    def bt_instrucoes(self):
        print('Equacoes do Primeiro Grau')
        #self.remove_widget(self)

class DropDown1(DropDown):
    pass

class MenuOperacoes(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        
    
class MenuEquacoes(BoxLayout):
    pass

class Exercicios_Matematica(App):
    pass


Exercicios_Matematica().run()