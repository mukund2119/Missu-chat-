from kivy.app import App
from kivy.uix.label import Label

class MissUApp(App):
    def build(self):
        return Label(text="💬 Welcome to MISS U Chat App!", font_size='24sp')

MissUApp().run()