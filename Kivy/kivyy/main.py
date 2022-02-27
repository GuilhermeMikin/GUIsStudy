from imports import *

# GUI = Builder.load_file("tela.kv")
class MyWidget(GridLayout):
    def incrementar(self):
        self.ids['lb1'].text = str(int(self.ids['lb1'].text)+1)

class MeuAplcativo(App):
    """ 
    Classe App
    """
    def build(self):
        """
        Construir o aplicativo
        """
        
        return MyWidget()


if __name__ == "__main__":
    MeuAplcativo().run()