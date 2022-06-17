from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_string("""
<ExampleApp>:
    orientation: "vertical"
    Button:
        text: ""
        on_press: gif.anim_delay = 0.10
        on_press: gif._coreimage.anim_reset(True)

        Image:
            id: gif
            source: 'img_src/tdas.zip'
            center: self.parent.center
            size: 500, 500
            allow_stretch: True
            anim_loop: 30
""")

class Tdas(App, BoxLayout):
    def build(self):
        return self

if __name__ == "__main__":
    Tdas().run()
