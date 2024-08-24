from kivy.app import App
from Design.Buttons import MyButton
from ButtonsFunctions.Geolocation import get_location as gl
from ButtonsFunctions.GeoLive import geo_live as gt
from ButtonsFunctions.Camera import take_picture as tp


class MyApp(App):
    def build(self):
        pass

    def location(self):
        gl()

    def geo_live(self):
        gt()

    def camera(self):
        tp()


if __name__ == '__main__':
    MyApp().run()
