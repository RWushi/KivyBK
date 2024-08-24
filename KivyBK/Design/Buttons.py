from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.graphics import Line


class MyButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(mouse_pos=self.on_mouse_pos)

    def on_mouse_pos(self, *args):
        self.update_border(1.1 if self.collide_point(*args[1]) else 1.0)

    def update_border(self, scale_factor):
        for instruction in self.canvas.before.children:
            if isinstance(instruction, Line):
                instruction.rectangle = (
                    self.x - (self.width * (scale_factor - 1) / 2),
                    self.y - (self.height * (scale_factor - 1) / 2),
                    self.width * scale_factor,
                    self.height * scale_factor
                )
