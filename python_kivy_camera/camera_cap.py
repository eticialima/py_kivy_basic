import cv2
from kivy.app import App
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

# DIRETORIO DO HAAR
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


class ChamaCamera(App):
    def build(self):
        self.img1 = Image(source='logoCL.jpg')  # cria uma imagem onde depois iremos inserir a imagem da camera
        layout = BoxLayout(orientation='vertical')  # aqui criamos um layout  vertical
        layout.add_widget(self.img1)

        self.capture = cv2.VideoCapture(0)  # criamos um objeto de capture de vídeo. Associamos à primeira camera

        Clock.schedule_interval(self.atualizaImagem,
                                1.0 / 30.0)  # criamos um clock para atualizar a imagem a cada 1/320 de segundo
        return layout

    def atualizaImagem(self, dt):
        ret, frame = self.capture.read()  # captura uma imagem da camera
        buf1 = cv2.flip(frame, 0)  # inverte para não ficar de cabeça para baixo
        buf = buf1.tostring()  # converte em textura
        texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        self.img1.texture = texture1  # apresenta a imagem


# INICIA O APP
if __name__ == '__main__':
    ChamaCamera().run()
