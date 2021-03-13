from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.button import MDRectangleFlatButton

screen_helper = """
ScreenManager:
    MenuScreen:
    Planets:
    Earth:
<MenuScreen>:
    name: 'menu'
    
    
    Carousel:
        direction: 'right'
        pos_hint:{"center_x":0.5,"center_y":0.7}  
        AsyncImage:
            source: 'http://placehold.it/480x270.png&text=slide-1.png'
        AsyncImage:
            source: 'http://placehold.it/480x270.png&text=slide-2.png'
        AsyncImage:
            source: 'http://placehold.it/480x270.png&text=slide-3.png'
        AsyncImage:
            source: 'http://placehold.it/480x270.png&text=slide-4.png'
            
    MDLabel:
        text: "Welcome to Planets, Choose your option: "
        pos_hint:{"center_x":0.8,"center_y":0.3}
        
    MDRectangleFlatButton:
        text: "Planet selection"
        pos_hint:{"center_x":0.5,"center_y":0.2}
        
    MDRectangleFlatButton:
        text: "About us"
        pos_hint:{"center_x":0.5,"center_y":0.1}    
    

<Planets>:
    name: 'Planets'
   
<Earth>:
    name: 'Earth'


"""


class MenuScreen(Screen):
    pass


class Planets(Screen):
    pass


class Earth(Screen):
    pass


# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(Planets(name='Planets'))
sm.add_widget(Earth(name='Earth'))


class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen


DemoApp().run()
