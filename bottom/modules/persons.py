from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import MDList, TwoLineAvatarListItem, ImageLeftWidget
import json
import os

person_list = [{"name": "UwU", "state": "CZE"},
               {"name": "OwO", "state": "RUS"},
               {"name": "OmO", "state": "USA"}]

class MyItem(TwoLineAvatarListItem):
    def __init__(self, nazev, popisek, img,  *args, **kwargs):
        super(MyItem, self).__init__(*args)
        self.text = nazev
        self.secondary_text = popisek
        self._no_ripple_effect = True
        self.image = ImageLeftWidget(source=img)
        self.add_widget(self.image)


    def on_press(self):
        print(self.text)
        self.image.source = "images/fiadi.png"
    def on_touch_down(self, touch):
        print(touch)
        self.image.source = "images/green.png"
    def on_touch_up(self, touch):
        print(touch)
        self.image.source = "images/blue.png"

class Persons(BoxLayout):
    def __init__(self, *args, **kwargs):
        super(Persons, self).__init__(orientation="horizontal") #předek
        scrollview = ScrollView()
        list = MDList()
        #self.add_widget(MDLabel(text="Pokus"))
        dir_path = os.path.dirname(os.path.realpath(__file__))
        '''
        for i in person_list:
            list.add_widget(MyItem(name=i['name'], state=i['state']))
        '''
        with open(dir_path + '/' + 'botky.json') as json_file:
            data = json.load(json_file)
            for udaj in data["botky"]:
                list.add_widget(MyItem(nazev=udaj['nazev'], popisek=udaj['popisek'], img=udaj['img']))
        scrollview.add_widget(list)
        self.add_widget(scrollview)