from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

screen_helper = """
ScreenManager:
    MenuScreen:
    Planetselector:
    Earth:
    
    
<MenuScreen>:
    name: 'menu'
   

<Planetselector>:
    name: 'Planetselector'
    

<Earth>:
    name: 'Earth'
   

"""


class MenuScreen(Screen):
    pass


class Planetselector(Screen):
    pass


class Earth(Screen):
    pass


# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(Planetselector(name='Planetselector'))
sm.add_widget(Earth(name='Earth'))


class Alpha_build(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        self.title = "Planets Dev version"
        return screen


Alpha_build().run()