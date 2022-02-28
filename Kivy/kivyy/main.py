from imports import *

class MyWidget(FloatLayout):
    def incrementar(self):
        self.ids['lb1'].text = str(int(self.ids['lb1'].text)+1)
    pass

class MyKivyApp(App):
    """ 
    Classe App
    """
    def build(self):
        """
        Construir o aplicativo
        """
        return MyWidget()


if __name__ == "__main__":
    MyKivyApp().run()