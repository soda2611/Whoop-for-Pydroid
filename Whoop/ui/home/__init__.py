from ui import *
from ui.home.widget.result_template import *
from ui.home.widget.add_data import add_data
from ui.home.widget.recent import recent, recent_

recent_search=recent_search

class home(MDBoxLayout, TouchBehavior):
    def __init__(self, **kwargs):
        super(home, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [10*scale, 10*scale, 10*scale, 10*scale]
        self.spacing = 20*scale
        Window.bind(on_resize=self.on_window_resize)

        self.md_bg_color=bg
        self.text=""
        self.signal=False
        self.search_thread = None

        theme_font_styles.append('main')
        self.theme_cls.font_styles["main"] = ["main", 16, False, 0.15]
        
        self.alert=MDDialog(
            title="Lỗi trong khi dịch",
            type="alert",
            md_bg_color=boxbg
        )
        
        self.empty_alert=MDDialog(
            title="Không có đầu vào để dịch",
            type="alert",
            md_bg_color=boxbg
        )
        
        self.no_internet_alert=self.alert=MDDialog(
            title="Không có kết nối internet",
            type="alert",
            md_bg_color=boxbg
        )

        self.label = Image(source=settings["banner"], size_hint=(0.9, None), pos_hint={'center_x': 0.5}, height=50*scale)
        
        self.cautionlabel = MDLabel(text="Kết quả có thể sai do bộ dữ liệu chưa qua kiểm tra sàng lọc", font_style="Caption", halign='center', size_hint=(0.75, None), pos_hint={'center_x': 0.5, 'center_y': 0.5}, height=30*scale, theme_text_color="Custom", text_color=primarycolor)

        self.resultlabel = MDLabel(text='', font_style="H6", halign='center', valign='middle', size_hint=(1, None), pos_hint={'center_x': 0.5, 'center_y': 0.5}, height=30)

        self.caplabel = MDLabel(text="Không nhập cả câu vì đây không phải là trình dịch như Google Translate", font_style="Caption", halign="center", size_hint=(0.75, None), pos_hint={'center_x': 0.5, 'center_y': 0.5}, height=30*scale, theme_text_color="Custom", text_color=primarycolor)
        
        self.text_input=MDRelativeLayout(size_hint=(0.75, None), height=30*scale)
        self.text_input.input=MDTextField(icon_left="magnify", icon_left_color_focus=btn, hint_text="Nhập từ cần tìm", line_color_normal=boxbg, line_color_focus=menubg, hint_text_color=[0.75-i for i in primarycolor], hint_text_color_focus=primarycolor, text_color_focus=primarycolor, fill_color_normal=boxbg, mode="round", size_hint=(1, None), pos_hint={'center_x': 0.5}, height=30*scale, multiline=False)        
        self.text_input.button=MDIconButton(icon='translate', theme_icon_color="Custom", icon_color=btn, size_hint=(None, None), pos_hint={"right": 1, "center_y":0.6}, on_press=self.translate)
        self.text_input.add_widget(self.text_input.input)
        self.text_input.add_widget(self.text_input.button)
        
        self.button = MDIconButton(icon='magnify', theme_icon_color="Custom", icon_color=secondarycolor, size_hint=(1, None), pos_hint={"center_x":0.5})
        
        self.homebutton = MDIconButton(icon='home', theme_icon_color="Custom", icon_color=secondarycolor, size_hint=(1, None), pos_hint={"x":0})
        
        self.menubutton = MDIconButton(icon='menu', theme_icon_color="Custom", icon_color=secondarycolor, size_hint=(1, None), pos_hint={"x":1})
        
        self.progress_box=MDBoxLayout(orientation='vertical', size_hint=(0.95,None), height=5*scale, pos_hint={"center_x":0.5})

        self.progress_bar = MDProgressBar(radius=[5,5,5,5], type="indeterminate", pos_hint={"center_x":0.5}, running_duration=0.75, catching_duration=0.5, color=btn, back_color=bg)
        self.progress_box.add_widget(self.progress_bar)

        self.add_widget(self.label)
        self.add_widget(self.cautionlabel)

        self.one_box=MDBoxLayout(size_hint=(0.85, 0.25), pos_hint={'center_x': 0.5, 'center_y': 0.5}, spacing = 20)
        self.add_widget(self.one_box)

        self.noname=MDCard(orientation='vertical',md_bg_color=bg, size_hint=(1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.noname.radius=[i*scale for i in self.noname.radius]
        self.one_box.add_widget(self.noname)

        self.recent=recent(self.create_content_box, self.clear_history, self.noname.radius)

        self.noname.add_widget(self.progress_box)

        self.scrollview = ScrollView(size_hint=(1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        self.result_box=MDBoxLayout(orientation='vertical', size_hint=(1,None), spacing=20, padding=[10*scale, 10*scale, 10*scale, 10*scale])
        self.result_box.bind(minimum_height=self.result_box.setter('height'))

        self.homebox=MDBoxLayout(spacing=20)
        self.scrollview.do_scroll_x=False
        self.homebox.orientation="vertical"
        self.homebox.size_hint_y=None
        self.homebox.bind(minimum_height=self.homebox.setter('height'))
        for i in range(10):
            box__=self.create_content_box(data_[random.choice(word__)])
            home__[i]=box__
            self.homebox.add_widget(box__)
        
        self.noname.add_widget(self.scrollview)
        self.scrollview.add_widget(self.homebox)
        self.refreshbutton=MDFillRoundFlatButton(text="Làm mới",size_hint=(None, None), pos_hint={"center_x":0.5, "center_y":0.5}, md_bg_color=btn, theme_text_color="Custom", text_color=secondarycolor)
        self.refreshbutton.bind(on_press=lambda instance: self.refresh(instance, None))
        self.homebox.add_widget(self.refreshbutton)
        
        self.resultlabel.bind(texture_size=self.resultlabel.setter('text_size'))
        self.resultlabel.bind(texture_size=self.resultlabel.setter('size'))

        self.box = MDBoxLayout(size_hint=(0.9, 0.02), pos_hint={"center_x":0.5})
        self.add_widget(self.box)
        self.box.add_widget(self.text_input)

        self.taskbar=MDCard(md_bg_color=btn, radius=[25,25,25,25], size_hint=(1, None), height=50*scale, pos_hint={"center_x":0.5, "center_y": 0.25})
        self.taskbar.radius=[i*scale for i in self.taskbar.radius]
        self.button.bind(on_press=self.show_input)
        self.homebutton.bind(on_press=self.home)
        self.menubutton.bind(on_press=self.menu_open)
        self.taskbar.add_widget(self.homebutton)
        self.taskbar.add_widget(self.button)
        self.taskbar.add_widget(self.menubutton)
        self.box.add_widget(self.taskbar)

        self.text_input.input.bind(focus=self.hide_input)
        self.text_input.input.bind(text=self.quick_search)
        self.text_input.input.bind(on_text_validate=lambda instance: self.search_button_pressed(instance, self.text_input.input.text))
        self.hide_input(1,False)
        self.add_widget(self.caplabel)

        self.result_template=result_template()
        self.translate_result_template=translate_result_template()

        self.synonyms_box=MDBoxLayout(size_hint_x=None, spacing=20*scale, padding=[10*scale,10*scale,10*scale,10*scale], pos_hint={'center_y': 0.5})
        self.synonyms=ScrollView(do_scroll_y=False, size_hint=(1,None), height=50*scale)
        self.synonyms_box.bind(minimum_width=self.synonyms_box.setter('width'))
        self.synonyms.add_widget(self.synonyms_box)

        self.dialog = recent_(self.create_content_box, self.clear_history, self.noname.radius)
        for i in recent_search:
            self.dialog.recent_scrollview_box.add_widget(self.create_content_box(data_[i]))

        try:
            if int(width)>=900:
                self.noname.size_hint=(0.75, 1)
                self.one_box.add_widget(self.recent)
        except:
            pass

    def show_recent(self, *args):
        self.menu.dismiss()
        self.progress_bar.back_color=bg
        self.progress_bar.color=self.progress_bar.back_color
        self.noname.md_bg_color=bg
        self.scrollview.clear_widgets()
        self.scrollview.add_widget(self.dialog)

    def clear_history(self, instance):
        global recent_search
        recent_search=[]
        self.dialog.recent_scrollview_box.clear_widgets()
        self.recent.recent_scrollview_box.clear_widgets()
        with open("func/data/recent.txt", "w", encoding="utf-8"):
            pass

    def morebutton(self, text):
        morebutton=MDFillRoundFlatButton(text="Xem thêm", pos_hint={"center_y":0.5}, md_bg_color=btn, theme_text_color="Custom", text_color=secondarycolor)
        morebutton.bind(on_press=lambda instance: self.search_button_pressed(instance, text))
        return morebutton

    def create_chips(self, text):
        return MDFillRoundFlatButton(text=text, theme_icon_color='Custom', md_bg_color=btn, theme_text_color="Custom", text_color=secondarycolor, font_name=f"func/setting/fonts/{settings['fonts']}.ttf", font_size=15*scale, on_press=lambda instance: self.search_button_pressed(instance, text))

    def create_content_box(self, text):
        try:
            self.content_box=MDCard(md_bg_color=boxbg, padding=[10*scale,10*scale,10*scale,10*scale], size_hint=(1, None), pos_hint={"center_x":0.5})
            self.content_box.radius=[i*scale for i in self.content_box.radius]
            self.content_box.bind(minimum_height=self.content_box.setter('height'))
            self.content_box.tilte_and_description_box=MDBoxLayout(orientation='vertical', size_hint=(0.8,None))
            self.content_box.tilte_and_description_box.bind(minimum_height=self.content_box.tilte_and_description_box.setter('height'))
            self.content_box.result_head_label=MDLabel(text=text["word"]+" ("+text["type"].lower()+")"+f'\n/{eng_to_ipa.convert(text["word"])}/', font_style="main", font_size=18*scale, size_hint=(0.9,None), pos_hint={"left":0}, theme_text_color="Custom", text_color=primarycolor)
            self.content_box.result_head_label.bind(texture_size=self.content_box.result_head_label.setter('text_size'))
            self.content_box.result_head_label.bind(texture_size=self.content_box.result_head_label.setter('size'))
            self.content_box.result_label=MDLabel(font_size=25*scale, size_hint=(0.9,None), pos_hint={"left":1}, theme_text_color="Custom", text_color=primarycolor)
            if len(text["definition"])>50:
                self.content_box.result_label.text=text["definition"][:50]+"..."
            else:
                self.content_box.result_label.text=text["definition"]
            self.content_box.result_label.bind(texture_size=self.content_box.result_label.setter('text_size'))
            self.content_box.result_label.bind(texture_size=self.content_box.result_label.setter('size'))
            self.content_box.morebutton=MDFillRoundFlatButton(text="Xem thêm", pos_hint={"center_y":0.5}, md_bg_color=btn, theme_text_color="Custom", text_color=secondarycolor)
            self.content_box.tilte_and_description_box.add_widget(self.content_box.result_head_label)
            self.content_box.tilte_and_description_box.add_widget(self.content_box.result_label)
            self.content_box.add_widget(self.content_box.tilte_and_description_box)
            self.content_box.add_widget(self.content_box.morebutton)
            self.content_box.morebutton.bind(on_press=lambda instance: self.search_button_pressed(instance, text["word"]))
        except:
            pass

        return self.content_box
        
    def add_data(self):
        self.menu.dismiss()
        self.progress_bar.back_color=bg
        self.progress_bar.color=self.progress_bar.back_color
        self.noname.md_bg_color=bg
        self.scrollview.clear_widgets()
        self.scrollview.add_widget(add_data())
     
    def refresh(self, instance, dict_):
        self.scrollview.scroll_to(home__[0])
        if dict_==None:
            for i in range(10):
                text=data_[random.choice(word__)]
                home__[i].result_head_label.text=text["word"]+" ("+text["type"].lower()+")"+f'\n/{eng_to_ipa.convert(text["word"])}/'
                if len(text["definition"])>50:
                    home__[i].result_label.text=text["definition"][:50]+"..."
                else:
                    home__[i].result_label.text=text["definition"]
                home__[i].remove_widget(home__[i].morebutton)
                home__[i].morebutton=self.morebutton(text["word"])
                home__[i].add_widget(home__[i].morebutton)
    
    def menu_open(self, instance):
        menu_items = [
            {
                "text": "Cài đặt",
                "text_color": primarycolor,
                "trailing_icon": "cog",
                "theme_trailing_icon_color": "Custom",
                "trailing_icon_color": primarycolor,
                "on_release": lambda x="Setting": self.go_to_page_2(x)
            },
            {
                "text": "Thêm từ vựng",
                "text_color": primarycolor,
                "trailing_icon": "plus-circle",
                "theme_trailing_icon_color": "Custom",
                "trailing_icon_color": primarycolor,
                "on_release": self.add_data
            }
        ]
        if Window.width<900*scale:
            menu_items.insert(2,{"text": "Gần đây",
                                "text_color": primarycolor,
                                "trailing_icon": "history",
                                "theme_trailing_icon_color": "Custom",
                                "trailing_icon_color": primarycolor,
                                "on_release": self.show_recent})
        self.menu=MDDropdownMenu(
            caller=self.menubutton,
            items=menu_items,               
            ver_growth="up",
            md_bg_color=menubg,
            position="top"
        )
        self.menu.open()

    def home(self, instance):
        self.progress_bar.back_color=bg
        self.progress_bar.color=self.progress_bar.back_color
        self.noname.md_bg_color=bg
        self.scrollview.clear_widgets()
        self.scrollview.add_widget(self.homebox)

    def show_input(self, instance):
        self.box.clear_widgets()
        if self.text_input.input.text.split()!=[]: 
            self.scrollview.scroll_y=1
            self.progress_bar.back_color=(boxbg)
            self.noname.md_bg_color=boxbg
            self.scrollview.do_scroll_x, self.scrollview.do_scroll_y=False, True
            self.scrollview.clear_widgets()
            self.scrollview.add_widget(self.result_box)
        self.box.add_widget(self.text_input)
        
    def hide_input(self, instance, value):
        if ((len(self.text_input.input.text)==0) and (not value)) or self.signal:
            self.box.clear_widgets()
            self.box.add_widget(self.taskbar)
        self.signal=False

    def quick_search(self, instance, value):
        if self.search_thread:
            self.search_thread.cancel()
        if self.text_input.input.text!="":
            self.search_thread = threading.Timer(0.5, self.search_button_pressed, args=(instance, self.text_input.input.text))
            self.search_thread.start()
        else:
            self.home(instance)
        self.text=self.text_input.input.text
        
    def translate(self, instance):
        if check_connection():
            try:
                self.translate_result_template.src_text.text=self.text_input.input.text
                self.translate_result_template.dest_text.text=translator.translate(self.text_input.input.text, src='en', dest='vi').text
                self.scrollview.clear_widgets()
                self.scrollview.add_widget(self.translate_result_template)
            except:
            	if len(self.text_input.input.text.replace(" ",""))==0:
            		self.empty_alert.open()
            	else:
            		self.alert.open()
        else:
         	self.no_internet_alert.open()
        self.progress_bar.color=self.progress_bar.back_color
        self.progress_bar.stop()

    def search_button_pressed(self, instance, input_text):
        try:
            self.dialog.dismiss()
        except:
            pass
        threading.Thread(target=self.search, args=(instance, input_text)).start()
        self.progress_bar.color=btn
        self.progress_bar.start()

    def search(self, instance, input_text):
        global result, dict_
        self.scrollview.do_scroll_x, self.scrollview.do_scroll_y=False, True
        self.input_text=input_text
        result=SOD(input_text.replace("\n", " "), boost_performance=settings["boost performance"])
        dict_=result
        
        if len(result)>1 and settings["auto translate"]=="True": Clock.schedule_once(self.translate)
        else: Clock.schedule_once(self.update_UI)

    def update_UI(self, instance):
        global result, recent_search
        self.scrollview.scroll_y=1
        self.progress_bar.back_color=(boxbg)
        self.noname.md_bg_color=boxbg
        self.scrollview.do_scroll_x, self.scrollview.do_scroll_y=False, True
        self.scrollview.clear_widgets()
        self.scrollview.add_widget(self.result_box)
        self.result_box.clear_widgets()
        if result!="Không tìm thấy từ":
            if len(result)==1:
                result=result[0]
                self.result_template.word.text=result["word"].capitalize()+f' ({result["type"].lower()})'
                if result["level"]!="none":
                    self.result_template.cefr_level.text=f"CEFR level: {result['level']}"
                else:
                    self.result_template.cefr_level.text=""
                self.result_template.pronunciation_button.bind(on_release=lambda instance: self.pronounce(instance, result["word"]))
                self.result_template.pronunciation.text=f'/{eng_to_ipa.convert(result["word"])}/'
                self.result_template.definition.text=result["definition"][:1].upper()+result["definition"][1:]
                self.result_template.remove_widget(self.result_template.translation)
                if result["translation"]!="none":
                    self.result_template.translation.text=f'Dịch: {result["translation"]}'
                    self.result_template.add_widget(self.result_template.translation)
                self.result_box.add_widget(self.result_template)
                if result["word"] not in recent_search:
                    self.dialog.recent_scrollview_box.add_widget(self.create_content_box(result), index=0)
                    self.recent.recent_scrollview_box.add_widget(self.create_content_box(result), index=0)
                    recent_search=[result["word"]]+recent_search
            
                self.synonyms_box.clear_widgets()
                head=MDLabel(text="Từ đồng nghĩa", halign="center", font_style="main", size_hint=(1,None), height=25*scale, pos_hint={"center_x":0.5}, theme_text_color="Custom", text_color=primarycolor)
                if result["synonyms"]!='none':
                    self.result_box.add_widget(head)
                    self.result_box.add_widget(self.synonyms)
                    for i in result["synonyms"]:
                        self.synonyms_box.add_widget(self.create_chips(i))
            else:
                self.structure_box=MDBoxLayout(size_hint=(1, None))
                for i in dict_:
                    self.result_box.add_widget(self.create_content_box(i))
                    if i["word"] not in recent_search:
                        self.recent.recent_scrollview_box.add_widget(self.create_content_box(i), index=0)
                        self.dialog.recent_scrollview_box.add_widget(self.create_content_box(i), index=0)
                        recent_search=[i["word"]]+recent_search
                self.result_box.add_widget(self.structure_box)
        else:
            self.resultlabel.text = "".join(result)
            self.result_box.add_widget(self.resultlabel)
        if result!="Không tìm thấy từ":
            if grammar_structure_detector(self.text_input.input.text,"func/data/grammar.txt"):
                self.structure=MDLabel(text="Cấu trúc ngữ pháp đã nhận dạng:\n"+"\n".join(grammar_structure_detector(self.text_input.input.text,"func/data/grammar.txt")), font_style="H6", halign='center', valign='middle', size_hint=(1, None), pos_hint={'center_x': 0.5, 'center_y': 0.5}, theme_text_color="Custom", text_color=primarycolor)
                self.structure.bind(texture_size=self.resultlabel.setter('size'))
                self.structure_box.add_widget(self.structure)

        with open("func/data/recent.txt", "w", encoding="utf-8") as fo:
            for i in recent_search:
                fo.write(f'{i}\n')
        self.progress_bar.color=self.progress_bar.back_color
        self.progress_bar.stop()

    def pronounce(self, instance, text):
        def run():
            pass

        threading.Thread(target=run).start()

    def switch_theme(self, *args):
        self.menu.dismiss()

    def go_to_page_2(self, instance):
        self.menu.dismiss()
        sm.transition.direction = "left"
        sm.current = 'second'

    def on_double_tap(self, instance, *args):
        self.text=self.text_input.input.text
        self.signal=True
        self.hide_input(instance, False)

    def on_window_resize(self, window, width, height):
        is_large_screen = width >= 900*scale
        recent_in_children = self.recent in self.one_box.children

        self.noname.size_hint = (0.75, 1) if is_large_screen else (1, 1)
        if is_large_screen:
            if self.dialog in self.scrollview.children: self.home(None)
            self.one_box.add_widget(self.recent)
        elif recent_in_children:
            self.one_box.remove_widget(self.recent)