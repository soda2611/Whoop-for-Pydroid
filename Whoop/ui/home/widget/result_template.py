from ui import *

class result_template(MDBoxLayout):
    def __init__(self, **kwargs):
        super(result_template, self).__init__(**kwargs)
        self.orientation='vertical'
        self.size_hint_y=None
        self.spacing=20
        self.padding=[10,10,10,10]
        self.bind(minimum_height=self.setter('height'))
        self.word=MDLabel(text="", font_style="main", font_size=20*scale, halign='center', valign='middle', size_hint=(1, None), pos_hint={'center_x': 0.5}, theme_text_color="Custom", text_color=primarycolor)
        self.cefr_level=MDLabel(text="", font_style="Body2", halign='center', size_hint=(1, None), height=20*scale, pos_hint={'center_x': 0.5}, theme_text_color="Custom", text_color=primarycolor)
        self.pronunciation_template=MDBoxLayout(size_hint_y=None, spacing=10, padding=[10,10,10,10], pos_hint={"center_x":0.5})
        self.pronunciation_template.bind(minimum_height=self.pronunciation_template.setter('height'))
        self.pronunciation=MDLabel(text="", font_style="main", font_size=18*scale, halign='center', size_hint=(1, None), pos_hint={'center_x': 0.5}, theme_text_color="Custom", text_color=primarycolor)
        self.pronunciation_button=MDIconButton(icon="volume-high", theme_icon_color="Custom", icon_color=primarycolor, size_hint=(1, None), pos_hint={"center_x":0.5, "center_y": 0.25})
        self.definition=MDLabel(text="", font_style="Body1", halign='center', valign='middle', size_hint=(1, None), pos_hint={'center_x': 0.5}, theme_text_color="Custom", text_color=primarycolor)
        self.translation=MDLabel(text="", font_style="Body1", halign='center', valign='middle', size_hint=(1, None), pos_hint={'center_x': 0.5}, theme_text_color="Custom", text_color=primarycolor)
        self.word.bind(texture_size=self.word.setter('text_size'))
        self.word.bind(texture_size=self.word.setter('size'))
        self.cefr_level.bind(texture_size=self.cefr_level.setter('text_size'))
        self.cefr_level.bind(texture_size=self.cefr_level.setter('size'))
        self.pronunciation.bind(texture_size=self.pronunciation.setter('text_size'))
        self.pronunciation.bind(texture_size=self.pronunciation.setter('size'))
        self.definition.bind(texture_size=self.definition.setter('text_size'))
        self.definition.bind(texture_size=self.definition.setter('size'))
        self.translation.bind(texture_size=self.translation.setter('text_size'))
        self.translation.bind(texture_size=self.translation.setter('size'))      
        self.add_widget(self.word)
        self.add_widget(self.cefr_level)
        self.pronunciation_template.add_widget(self.pronunciation)
        self.pronunciation_template.add_widget(self.pronunciation_button)
        self.add_widget(self.pronunciation_template)
        self.add_widget(self.definition)

class translate_result_template(MDBoxLayout):
    def __init__(self, **kwargs):
        super(translate_result_template, self).__init__(**kwargs)
        self.orientation='vertical'
        self.size_hint_y=None
        self.spacing=20*scale
        self.padding=[10*scale,10*scale,10*scale,10*scale]
        self.bind(minimum_height=self.setter('height'))
        self.src_text=MDLabel(text="", font_style="H6", halign="center", valign='middle', size_hint=(1, None), theme_text_color="Custom", text_color=primarycolor, pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.src=MDLabel(text="Anh", font_style="Body2", halign="center", size_hint=(1, None), theme_text_color="Custom", text_color=primarycolor, pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.dest=MDLabel(text="Việt", font_style="Body2", halign="center", size_hint=(1, None), theme_text_color="Custom", text_color=primarycolor, pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.dest_text=MDLabel(text="", font_style="H6", halign="center", valign='middle', size_hint=(1, None), theme_text_color="Custom", text_color=primarycolor, pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.src_text.bind(texture_size=self.src_text.setter('text_size'))
        self.src_text.bind(texture_size=self.src_text.setter('size'))
        self.dest.bind(texture_size=self.dest.setter('text_size'))
        self.dest.bind(texture_size=self.dest.setter('size'))
        self.dest_text.bind(texture_size=self.dest_text.setter('text_size'))
        self.dest_text.bind(texture_size=self.dest_text.setter('size'))
        self.src.bind(texture_size=self.src.setter('text_size'))
        self.src.bind(texture_size=self.src.setter('size'))      
        self.add_widget(self.src)
        self.add_widget(self.src_text)
        self.add_widget(self.dest)
        self.add_widget(self.dest_text)