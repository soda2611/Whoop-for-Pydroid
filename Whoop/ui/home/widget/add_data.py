from ui import *

list_=[]

class add_data(MDBoxLayout):
    def __init__(self, **kwargs):
        super(add_data, self).__init__(**kwargs)
        self.orientation='vertical'
        self.size_hint_y=None
        self.spacing=20
        self.padding=[10,10,10,10]
        self.bind(minimum_height=self.setter('height'))
        
        self.container=MDTextField(hint_text="Type here", line_color_normal=boxbg, line_color_focus=menubg, hint_text_color=[0.75-i for i in primarycolor], hint_text_color_focus=primarycolor, text_color_focus=primarycolor, fill_color_normal=boxbg, mode="round", size_hint=(1, None), pos_hint={'center_x': 0.5}, height=30*scale, multiline=False)
        
        self.add__=MDDialog(
            title=f"Add synonym",
            type="custom",
            content_cls=self.container,
            buttons=[
                MDFillRoundFlatButton(
                    text="Apply",
                    md_bg_color=btn,
                    theme_text_color="Custom",
                    text_color=secondarycolor
                ),
                MDFillRoundFlatButton(
                    text="Cancel",
                    md_bg_color=btn,
                    theme_text_color="Custom",
                    text_color=secondarycolor
                )],
            md_bg_color=boxbg
        )
        self.add__.buttons[0].bind(on_release=self.add_)
        self.add__.buttons[1].bind(on_release=self.add__.dismiss)
        
        self.label=MDLabel(text="Add data", font_style="H6", valign='middle', size_hint=(1, None), pos_hint={'center_x': 0.5}, theme_text_color="Custom", text_color=primarycolor, halign='center')
        self.word=MDTextField(hint_text="Word", hint_text_color=[0.75-i for i in primarycolor], hint_text_color_focus=primarycolor, text_color_focus=primarycolor, fill_color_normal=boxbg, size_hint=(1, None), pos_hint={'center_x': 0.5}, height=30*scale, multiline=False)
        self.type=MDTextField(hint_text="Type", hint_text_color=[0.75-i for i in primarycolor], hint_text_color_focus=primarycolor, text_color_focus=primarycolor, fill_color_normal=boxbg, size_hint=(1, None), pos_hint={'center_x': 0.5}, height=30*scale, multiline=False)
        self.cefr_level=MDTextField(hint_text="CEFR level", hint_text_color=[0.75-i for i in primarycolor], hint_text_color_focus=primarycolor, text_color_focus=primarycolor, fill_color_normal=boxbg, size_hint=(1, None), pos_hint={'center_x': 0.5}, height=30*scale, multiline=False)
        self.definition=MDTextField(hint_text="Definition", hint_text_color=[0.75-i for i in primarycolor], hint_text_color_focus=primarycolor, text_color_focus=primarycolor, fill_color_normal=boxbg, size_hint=(1, None), pos_hint={'center_x': 0.5}, height=30*scale, multiline=False)
        self.add_synonyms=add_synonyms()
        self.add=MDFillRoundFlatIconButton(text="Add synonym", icon="plus-circle", theme_icon_color='Custom', md_bg_color=btn, theme_text_color="Custom", icon_color=secondarycolor,  text_color=secondarycolor, on_press=self.add__.open)
        self.add_synonyms.synonyms_list.add_widget(self.add)
        
        self.admin_code=MDTextField(hint_text="Administrator code", hint_text_color=[0.75-i for i in primarycolor], hint_text_color_focus=primarycolor, text_color_focus=primarycolor, fill_color_normal=boxbg, size_hint=(1, None), pos_hint={'center_x': 0.5}, height=30*scale, multiline=False)
        self.button=MDFillRoundFlatButton(text="Apply",size_hint=(None, None), pos_hint={"center_x":0.5, "center_y":0.5}, md_bg_color=btn, theme_text_color="Custom", text_color=secondarycolor, on_press=self.add_data)
        
        self.add_widget(self.label)
        self.add_widget(self.word)
        self.add_widget(self.type)
        self.add_widget(self.cefr_level)
        self.add_widget(self.definition)
        self.add_widget(self.add_synonyms)
        self.add_widget(self.admin_code)
        self.add_widget(self.button)
        
    def add_(self, instance):
        while "  " in self.container.text:
            self.container.text=self.container.text.replace("  "," ")
        self.container.text=self.container.text.strip()
        if self.container.text not in list_ and self.container.text!="":
            list_.append(self.container.text)
            self.add_synonyms.synonyms_list.add_widget(self.create_chips(self.container.text, on_press=self.remove))
          
        self.container.text=""
        self.add__.dismiss()
        
    def remove(self, instance):
        print(instance)
        list_.remove(instance.text)
        self.add_synonyms.synonyms_list.remove_widget(instance)
        
    def add_data(self, instance):
    	global list_
    	if self.word.text and self.type.text and self.definition.text and self.cefr_level.text:
    	    if self.admin_code.text==admin_code:
                with open("func/data/tu_dien_nguon.txt", "a", encoding="utf-8") as f:
                    f.write(f"{self.word.text} % {self.type.text} % {self.definition.text} % none % none % {self.cefr_level.text}\n")
                upload_file("Whoop/func/data/tu_dien_nguon.txt", "func/data/tu_dien_nguon.txt")
    	    else:
                with open("func/data/unverified.txt", "a", encoding="utf-8") as f:
                    f.write(f"{self.word.text} % {self.type.text} % {self.definition.text}% none % {', '.join(list_)} % {self.cefr_level.text}\n")
    		
    	    self.word.text=self.type.text=self.definition.text=self.cefr_level.text=""
    	    self.add_synonyms.synonyms_list.clear_widgets()
    	    self.add_synonyms.synonyms_list.add_widget(self.add)
    	    list_=[]
    	    
    def create_chips(self, text, on_press):
        return MDFillRoundFlatButton(text=text, theme_icon_color='Custom', md_bg_color=btn, theme_text_color="Custom", text_color=secondarycolor, on_press=on_press)
        
class add_synonyms(ScrollView):
    def __init__(self, **kwargs):
        super(add_synonyms, self).__init__(**kwargs)
        self.do_scroll_y=False
        self.size_hint=(1, None)
        self.height=50*scale
        self.synonyms_list=MDBoxLayout(size_hint=(None, 1), pos_hint={"center_x": 0.5}, spacing=20*scale, padding=[10*scale, 10*scale, 10*scale, 10*scale])
        self.synonyms_list.height=self.synonyms_list.height*scale
        self.synonyms_list.bind(minimum_width=self.synonyms_list.setter('width'))
        self.add_widget(self.synonyms_list)