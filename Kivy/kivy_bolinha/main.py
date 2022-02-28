from imports import *

class MyWidget(BoxLayout):
    pass

class MyKivyApp(App):
    """ 
    Classe App
    """
    def build(self):
        """
        Método para construir o aplicativo
        """
        return MyWidget()


if __name__ == "__main__":
    Window.size = (800,600)
    Window.fullscreen = False
    MyKivyApp().run()