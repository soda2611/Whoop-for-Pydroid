from ui import *

class change_fonts(ScrollView):
    def __init__(self, create_preview, **kwargs):
        super(change_fonts, self).__init__(**kwargs)
        self.do_scroll_y=False
        self.size_hint=(1, None)
        self.height=50*scale
        self.font_list=MDBoxLayout(size_hint=(None, 1), pos_hint={"center_x": 0.5}, spacing=20*scale, padding=[10*scale, 10*scale, 10*scale, 10*scale])
        self.font_list.height=self.font_list.height*scale
        self.font_list.bind(minimum_width=self.font_list.setter('width'))
        self.add_widget(self.font_list)
        for i in fonts_name:
            self.font_list.add_widget(create_preview(i))