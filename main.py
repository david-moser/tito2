from kivy.app import App
from kivy.uix.widget import Widget


class Tito(Widget):
    pass


class TitoApp(App):
    def build(self):
        return Tito()


if __name__ == '__main__':
    TitoApp().run()
