from ui import *

class change_palette(ScrollView):
    def __init__(self, create_palette, **kwargs):
        super(change_palette, self).__init__(**kwargs)
        self.do_scroll_y=False
        self.size_hint=(1, None)
        self.height=300*scale
        self.color_palette_list=MDBoxLayout(size_hint=(None, 1), pos_hint={"center_x": 0.5}, spacing=20*scale, padding=[10*scale, 10*scale, 10*scale, 10*scale])
        self.color_palette_list.bind(minimum_width=self.color_palette_list.setter('width'))
        self.add_widget(self.color_palette_list)
        for i in colors:
            self.color_palette_list.add_widget(create_palette(i))