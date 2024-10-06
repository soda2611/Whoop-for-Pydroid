from ui import *

class recent(MDCard):
    def __init__(self, create_content_box, clear_history, radius, **kwargs):
        super(recent, self).__init__(**kwargs)
        self.orientation='vertical'
        self.md_bg_color=boxbg
        self.size_hint=(None, 1)
        self.width=250*scale
        self.pos_hint={'center_x': 0.5, 'center_y': 0.5}
        self.padding=[10*scale,10*scale,10*scale,10*scale]
        self.spacing=20*scale
        self.radius=radius
        self.recent_label=MDLabel(text="Gần đây", font_style="H6", halign="center", size_hint=(1,None), height=25*scale, pos_hint={"center_x": 0.5}, theme_text_color="Custom", text_color=primarycolor)
        self.recent_scrollview = ScrollView(size_hint=(1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5}, do_scroll_x=False)
        self.action_box=MDBoxLayout(size_hint=(1, None), height=20*scale, spacing=20, pos_hint={"center_x":0.5})
        self.clear_action=MDFillRoundFlatButton(text="Clear", md_bg_color=btn, pos_hint={"center_x": 0.5}, theme_text_color="Custom", text_color=secondarycolor)
        self.recent_scrollview_box=MDBoxLayout(orientation='vertical', size_hint=(1, None), spacing=20)
        self.recent_scrollview_box.bind(minimum_height=self.recent_scrollview_box.setter('height'))
        self.add_widget(self.recent_label)
        self.add_widget(self.recent_scrollview)
        self.add_widget(self.clear_action)
        self.recent_scrollview.add_widget(self.recent_scrollview_box)
        for i in recent_search:
            self.recent_scrollview_box.add_widget(create_content_box(i))
        self.clear_action.bind(on_release=clear_history)

class recent_(MDCard):
    def __init__(self, create_content_box, clear_history, radius, **kwargs):
        super(recent_, self).__init__(**kwargs)
        self.orientation='vertical'
        self.md_bg_color=boxbg
        self.size_hint=(1, 1)
        self.pos_hint={'center_x': 0.5, 'center_y': 0.5}
        self.padding=[10*scale,10*scale,10*scale,10*scale]
        self.spacing=20*scale
        self.radius=radius
        self.recent_label=MDLabel(text="Gần đây", font_style="H6", halign="center", size_hint=(1,None), height=25*scale, pos_hint={"center_x": 0.5}, theme_text_color="Custom", text_color=primarycolor)
        self.recent_scrollview = ScrollView(size_hint=(1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5}, do_scroll_x=False)
        self.action_box=MDBoxLayout(size_hint=(1, None), height=20*scale, spacing=20, pos_hint={"center_x":0.5})
        self.clear_action=MDFillRoundFlatButton(text="Clear", md_bg_color=btn, pos_hint={"center_x": 0.5}, theme_text_color="Custom", text_color=secondarycolor)
        self.recent_scrollview_box=MDBoxLayout(orientation='vertical', size_hint=(1, None), spacing=20)
        self.recent_scrollview_box.bind(minimum_height=self.recent_scrollview_box.setter('height'))
        self.add_widget(self.recent_label)
        self.add_widget(self.recent_scrollview)
        self.add_widget(self.clear_action)
        self.recent_scrollview.add_widget(self.recent_scrollview_box)
        for i in recent_search:
            self.recent_scrollview_box.add_widget(create_content_box(i))
        self.clear_action.bind(on_release=clear_history)