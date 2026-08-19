from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class Remoto:
    def __init__(self, marca, cor):
        self.marca = marca
        self.cor = cor
        self.ligado = False
        self.volume = 0
        self.canal = 1

    def Ligado(self):
        self.ligado = True

    def saltar_Canal(self):
        self.canal += 1

    def aumentar_volume(self):
        self.volume += 1

    def Desligar(self):
        self.ligado = False


remoto = Remoto("Tec", "Cinzento")


class MinhaApp(App):
    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=10
        )

        self.info = Label(
            text="Remoto desligado\nCanal: 1\nVolume: 0",
            font_size=25
        )

        for texto, funcao in [
            ("Ligar", self.ligar),
            ("Mudar Canal", self.canal),
            ("Aumentar Volume", self.volume),
            ("Desligar", self.desligar),
        ]:
            botao = Button(text=texto)
            botao.bind(on_press=funcao)
            layout.add_widget(botao)

        layout.add_widget(self.info)
        return layout

    def atualizar(self):
        estado = "ligado" if remoto.ligado else "desligado"
        self.info.text = (
            f"Remoto {estado}\n"
            f"Canal: {remoto.canal}\n"
            f"Volume: {remoto.volume}"
        )

    def ligar(self, instance):
        remoto.Ligado()
        self.atualizar()

    def canal(self, instance):
        remoto.saltar_Canal()
        self.atualizar()

    def volume(self, instance):
        remoto.aumentar_volume()
        self.atualizar()

    def desligar(self, instance):
        remoto.Desligar()
        self.atualizar()


if __name__ == "__main__":
    MinhaApp().run()
