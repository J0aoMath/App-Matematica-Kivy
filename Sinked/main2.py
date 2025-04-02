from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import *
from kivy.config import Config

Config.set('graphics','width','450')
Config.set('graphics','height', '600')
prop = 0.05
prop2 = 0.075

class Principal(AnchorLayout):
    def __init__(self,**kwargs):
        super(Principal, self).__init__(**kwargs)
        self.bind(size = self.update_rectangles)
        self.menu_inicial = Menu_Inicial()
        self.menu_operacoes = Operacoes_Basicas()
        self.menu_equacoes = Equacoes_2oGrau()
        self.add_menu_inicial()
    def update_rectangles(self, instance, value):
        
        with self.canvas.before:
            Color(1,1,1)
            Rectangle(pos=(0,0),size=(self.width,self.height))
            Color(0,0,0)
            Line(rectangle=(self.width*prop,self.height*prop,self.width*(1-prop*2),self.height*(1-prop*2)), width=2)
            Line(rectangle=(self.width*prop2,self.height*prop2,self.width*(1-prop2*2),self.height*(1-prop2*2)), width=1.025)
    def add_menu_inicial(self):
        self.add_widget(self.menu_inicial)

class Menu_Inicial(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.menu_operacoes = Operacoes_Basicas()
        self.menu_equacoes = Equacoes_2oGrau()
        self.orientation = 'vertical'
        self.bind(size=self.padding_update)
        self.lb1 = Label(text='[color=ff3333]Exercícios de Matemática[/color]', markup=True)
        self.lb2 = Label()
        self.bt1 = Button(text='Operações Basicas', on_press = self.on_press_operacoes)
        self.bt2 = Button(text='Expressões do primeiro grau', on_press = self.on_press_equacoes)
        self.bt3 = Button(text='Estatísticas')
        self.bt4 = Button(text='Opções')
        self.bt5 = Button(text='Instruções')
        self.bts = [self.bt1,self.bt2,self.bt3,self.bt4,self.bt5]
        self.add_widget(self.lb1)
        self.add_widget(self.lb2)
        for c in self.bts:
            self.add_widget(c)
    def on_press_operacoes(self, button):
        print('Operações Básicas')
        self.remove_widget(self)
        
        self.add_widget(Principal().menu_operacoes)
    def on_press_equacoes(self, button):
        print('Equações do primeiro grau')
        self.remove_widget(self)
        self.add_widget(Principal().menu_equacoes)
        
        
    def padding_update(self, instance, value):
        p = 2.33
        x = self.width*prop2*p
        y1 = self.height*prop2*(p*0.8)
        y2 = self.height*prop2*p
        self.padding = x , y1 , x , y2
        self.lb1.font_size = str(self.width*prop2*0.8)+'sp'

class Operacoes_Basicas(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.bind(size=self.padding_update)
        self.lb1 = Label(text='[color=ff3333]Operações Básicas[/color]', markup=True)
        self.lb2 = Label()
        self.bt1 = Button(text='Soma')
        self.bt2 = Button(text='Subtração')
        self.bt3 = Button(text='Multiplicação')
        self.bt4 = Button(text='Divisão')
        self.bt5 = Button(text='Return')
        self.bts = [self.bt1,self.bt2,self.bt3,self.bt4,self.bt5]
        self.add_widget(self.lb1)
        self.add_widget(self.lb2)
        for c in self.bts:
            self.add_widget(c)
    def padding_update(self, instance, value):
        p = 2.33
        x = self.width*prop2*p
        y1 = self.height*prop2*(p*0.8)
        y2 = self.height*prop2*p
        self.padding = x , y1 , x , y2
        self.lb1.font_size = str(self.width*prop2*0.8)+'sp'

class Equacoes_2oGrau(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)




class CanvasApp(App):
    def build(self):
        return Principal()

if __name__ == '__main__':
    CanvasApp().run()