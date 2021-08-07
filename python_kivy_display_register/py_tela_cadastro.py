from kivy.app import App
from kivy.core.window import Window
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

#INICIA A CLASS DO PROGRAMA
class cadastro(App):
    def build(self):
        # COR DO BACKGROUD
        self.bgdColor = (0.203, 0.194, 0.255, 1)
        Window.clearcolor = self.bgdColor

        #LAYOUT FLOAT
        layout= FloatLayout()

        #CONFIGURAÇÕES DA CAMERA
        self.cameraObject = Camera(play=False)
        self.cameraObject.play = True
        self.cameraObject.resolution = (480, 350)
        self.cameraObject.size_hint = (.4, 1)
        self.cameraObject.pos_hint = {'x': .55, 'y': .10}

        #CONFIGURAÇÕES DO BOTÃO 1
        self.botaoClick1 = Button(text="FOTO")
        self.botaoClick1.size_hint = (.2, .1)
        self.botaoClick1.pos_hint = {'x': .54, 'y': .20}

        #CONFIGURAÇÕES DO BOTÃO 2
        self.botaoClick2 = Button(text="PARAR")
        self.botaoClick2.size_hint = (.2, .1)
        self.botaoClick2.pos_hint = {'x': .76, 'y': .20}

        # CONFIGURAÇÕES DO BOTÃO 3
        self.botaoClick3 = Button(text="CADASTRAR")
        self.botaoClick3.size_hint = (.2, .1)
        self.botaoClick3.pos_hint = {'x': .05, 'y': .20}

        #FUNÇÃO DE CLICK DOS BOTÕES
        self.botaoClick1.bind(on_press=self.botaoclickone)
        self.botaoClick2.bind(on_press=self.botaoclicktwo)
        self.botaoClick3.bind(on_press=self.botaoclicktre)

        #TILULO DO PROGRAMA
        self.title1 = Label(text='SISTEMA DE CADASTRO')
        self.title1.font_size = '60sp'
        self.title1.color = [1, 25, 91, 1]
        self.title1.font_name = 'Roboto-Bold'
        self.title1.size_hint = (.99, .99)
        self.title1.pos_hint = {'x': .0, 'y': .40}


        # CAMPOS DE CADASTRO
        #CAMPO NOME:
        self.caixatexto = (Label(text="NOME:"))
        self.caixatexto.size_hint = (.005, .07)
        self.caixatexto.font_size = 26
        self.caixatexto.pos_hint = {'x': .11, 'y': .72}

        self.username = TextInput(multiline=False)
        self.username.size_hint = (.3, .07)
        self.username.font_size = 26
        self.username.pos_hint = {'x': .20, 'y': .72}

        # CAMPO CPF:
        self.caixatextocpf = (Label(text="CPF:"))
        self.caixatextocpf.size_hint = (.005, .07)
        self.caixatextocpf.font_size = 26
        self.caixatextocpf.pos_hint = {'x': .11, 'y': .60}

        self.cpf = TextInput(multiline=False)
        self.cpf.size_hint = (.3, .07)
        self.cpf.font_size = 26
        self.cpf.pos_hint = {'x': .20, 'y': .60}

        # CAMPO CARGO:
        self.caixatextocargo = (Label(text="CARGO:"))
        self.caixatextocargo.size_hint = (.005, .07)
        self.caixatextocargo.font_size = 26
        self.caixatextocargo.pos_hint = {'x': .11, 'y': .48}

        self.cargo = TextInput(multiline=False)
        self.cargo.size_hint = (.3, .07)
        self.cargo.font_size = 26
        self.cargo.pos_hint = {'x': .20, 'y': .48}

        # CAMPO EMAIL:
        self.caixatextoemail = (Label(text="E-MAIL:"))
        self.caixatextoemail.size_hint = (.005, .07)
        self.caixatextoemail.font_size = 26
        self.caixatextoemail.pos_hint = {'x': .11, 'y': .36}

        self.email = TextInput(multiline=False)
        self.email.size_hint = (.3, .07)
        self.email.font_size = 26
        self.email.pos_hint = {'x': .20, 'y': .36}

        #LAYOUT PARA MOSTRAR OS WIDGET NA TELA
        layout.add_widget(self.title1)
        layout.add_widget(self.cameraObject)
        layout.add_widget(self.botaoClick1)
        layout.add_widget(self.botaoClick2)
        layout.add_widget(self.botaoClick3)
        layout.add_widget(self.username)
        layout.add_widget(self.caixatexto)
        layout.add_widget(self.cpf)
        layout.add_widget(self.caixatextocpf)
        layout.add_widget(self.cargo)
        layout.add_widget(self.caixatextocargo)
        layout.add_widget(self.email)
        layout.add_widget(self.caixatextoemail)

        #RETORNA PARA O WIDGET
        return layout

    #FUNÇÃO DO CLIQUE
    def botaoclickone(self, *args):
        print("VOCE CLICOU NO BOTÃO 1")

    def botaoclicktwo(self, *args):
        print("VOCE CLICOU NO BOTÃO 2")

    def botaoclicktre(self, *args):
        print("CADASTRO EFETUADO")


#INICIA O APP
if __name__ == '__main__':
    cadastro().run()