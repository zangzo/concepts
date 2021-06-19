'''
This mobile app multi timer on kivy was created to help me to solve my working problem at factory where i work as shift supervisor
This simple app has 3 parallel timers, you can choose one each time interval from 1min to 3hourse by simple moving of slider.
The idea was to build simple timer.
'''


from kivy.core.window import Window
Window.size = (340,600)
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton
from kivymd.uix.slider import MDSlider
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.progressbar import MDProgressBar
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
import time


   


class SimpleTimerApp(MDApp):     
    def build(self):  
# BOXES
       self.screen = Screen()
       self.box_1 = MDBoxLayout(orientation="vertical",pos_hint={'center_x':.5, 'center_y':.87},size_hint_x= 0.6,size_hint_y = 0.05)
       self.box_2 = MDBoxLayout(orientation="vertical",pos_hint={'center_x':.5, 'center_y':.57},size_hint_x= 0.6,size_hint_y = 0.05)
       self.box_3 = MDBoxLayout(orientation="vertical",pos_hint={'center_x':.5, 'center_y':.27},size_hint_x= 0.6,size_hint_y = 0.05)
       self.screen.add_widget(self.box_1)
       self.screen.add_widget(self.box_2)
       self.screen.add_widget(self.box_3)    
# TIMERS
       self.timer_1 = MDLabel(text="00:00:00", halign="center",theme_text_color= "Custom",text_color =  (0, 0.5, 0.7, 1),pos_hint={'center_x':.5, 'center_y':.9} )
       self.screen.add_widget(self.timer_1)
       self.timer_2 = MDLabel(text="00:00:00", halign="center",theme_text_color= "Custom",text_color =  (0, 0.5, 0.7, 1),pos_hint={'center_x':.5, 'center_y':.6} )
       self.screen.add_widget(self.timer_2)
       self.timer_3 = MDLabel(text="00:00:00", halign="center",theme_text_color= "Custom",text_color =  (0, 0.5, 0.7, 1),pos_hint={'center_x':.5, 'center_y':.3} )
       self.screen.add_widget(self.timer_3) 
# SLIDERS       
       self.slider_1 = MDSlider(min= 0,max= 10800,value= 0,color=(0,0.5,0.7,1))
       self.slider_1.hint = False
       self.box_1.add_widget(self.slider_1)
       self.slider_1.bind(value = self.value_change_1)
       self.slider_2 = MDSlider(min= 0,max= 10800,value= 0,color=(0,0.5,0.7,1))
       self.slider_2.hint = False
       self.box_2.add_widget(self.slider_2)
       self.slider_2.bind(value = self.value_change_2)
       self.slider_3 = MDSlider(min= 0,max= 10800,value= 0 ,color=(0,0.5,0.7,1))
       self.slider_3.hint = False
       self.box_3.add_widget(self.slider_3)
       self.slider_3.bind(value = self.value_change_3)
# BUTTONS      
       self.start_1 = MDIconButton(icon="play",md_bg_color=(0,0.5,0.7,0.1),pos_hint={'center_x':.4, 'center_y':.8},user_font_size= "32sp",theme_text_color= "Custom",text_color =  (0, 0.5, 0.7, 1),on_release = self.start_1_pressed)
       self.screen.add_widget(self.start_1)
       self.stop_1 = MDIconButton(icon="stop",md_bg_color=(0,0.5,0.7,0.1),pos_hint={'center_x':.6, 'center_y':.8},user_font_size= "32sp",theme_text_color= "Custom",text_color =  (0, 0.5, 0.7, 1),on_release = self.stop_1_pressed)
       self.screen.add_widget(self.stop_1)
       self.start_2 = MDIconButton(icon="play",md_bg_color=(0,0.5,0.7,0.1),pos_hint={'center_x':.4, 'center_y':.5},user_font_size= "32sp",theme_text_color= "Custom",text_color =  (0, 0.5, 0.7, 1),on_release = self.start_2_pressed)
       self.screen.add_widget(self.start_2)
       self.stop_2 = MDIconButton(icon="stop",md_bg_color=(0,0.5,0.7,0.1),pos_hint={'center_x':.6, 'center_y':.5},user_font_size= "32sp",theme_text_color= "Custom",text_color =  (0, 0.5, 0.7, 1),on_release = self.stop_2_pressed)
       self.screen.add_widget(self.stop_2)
       self.start_3 = MDIconButton(icon="play",md_bg_color=(0,0.5,0.7,0.1),pos_hint={'center_x':.4, 'center_y':.2},user_font_size= "32sp",theme_text_color= "Custom",text_color =  (0, 0.5, 0.7, 1),on_release = self.start_3_pressed)
       self.screen.add_widget(self.start_3)
       self.stop_3 = MDIconButton(icon="stop",md_bg_color=(0,0.5,0.7,0.1),pos_hint={'center_x':.6, 'center_y':.2},user_font_size= "32sp",theme_text_color= "Custom",text_color =  (0, 0.5, 0.7, 1),on_release = self.stop_3_pressed)
       self.screen.add_widget(self.stop_3)  
       return self.screen   
   
# VALUE CONVERTERS  
    # Convert seconds (slider's value) to hours/minutes on display
    def value_change_1(self, instance,value):
        converted_value = time.strftime('%H:%M:%S', time.gmtime(int(float(value))))
        self.timer_1.text = str(converted_value)
    def value_change_2(self, instance,value):
        converted_value = time.strftime('%H:%M:%S', time.gmtime(int(float(value))))
        self.timer_2.text = str(converted_value)
    def value_change_3(self, instance,value):
        converted_value = time.strftime('%H:%M:%S', time.gmtime(int(float(value))))
        self.timer_3.text = str(converted_value)
        
#BUTTONS BEHAVIOUR        
    # Button start was pressed
    def start_1_pressed(self,*args):
        if self.slider_1.value == 0:
            return
        if self.start_1.icon == "play":
            self.start_1.icon = "pause"
            self.screen.remove_widget(self.box_1)
            self.bar_1 = MDProgressBar(value= 100,color=(0,0.5,0.7,1),pos_hint={'center_x':.5, 'center_y':.87},size_hint_x= 0.5,size_hint_y = 0.05,type= "determinate",running_duration= self.slider_1.value,running_transition = "linear")
            self.screen.add_widget(self.bar_1)
            self.bar_1.start()
            self.timer_1_interval = Clock.schedule_interval(self.timer_1_change, 1)
            return 
        elif self.start_1.icon == "pause":
            self.start_1.icon = "play"
            self.bar_1.stop()
            self.timer_1_interval.cancel()
            return
    def start_2_pressed(self,*args):
        if self.slider_2.value == 0:
            return
        if self.start_2.icon == "play":
            self.start_2.icon = "pause"
            self.screen.remove_widget(self.box_2)
            self.bar_2 = MDProgressBar(value= 100,color=(0,0.5,0.7,1),pos_hint={'center_x':.5, 'center_y':.57},size_hint_x= 0.5,size_hint_y = 0.05,type= "determinate",running_duration= self.slider_2.value,running_transition = "linear")
            self.screen.add_widget(self.bar_2)
            self.bar_2.start()
            self.timer_2_interval = Clock.schedule_interval(self.timer_2_change, 1)
            return
        elif self.start_2.icon == "pause":
            self.start_2.icon = "play"
            self.bar_2.stop()
            self.timer_2_interval.cancel()
            return
    def start_3_pressed(self,*args):
        if self.slider_3.value == 0:
            return
        if self.start_3.icon == "play":
            self.start_3.icon = "pause"
            self.screen.remove_widget(self.box_3)
            self.bar_3 = MDProgressBar(value= 100,color=(0,0.5,0.7,1),pos_hint={'center_x':.5, 'center_y':.27},size_hint_x= 0.5,size_hint_y = 0.05,type= "determinate",running_duration= self.slider_3.value,running_transition = "linear")
            self.screen.add_widget(self.bar_3)
            self.bar_3.start()
            self.timer_3_interval = Clock.schedule_interval(self.timer_3_change, 1)
            return
        elif self.start_3.icon == "pause":
            self.start_3.icon = "play"
            self.bar_3.stop()
            self.timer_3_interval.cancel()
            return
    # Stop was pressed
    def stop_1_pressed(self,*args):
        if self.slider_1.value == 0:
            return
        self.slider_1.value = 0
        self.start_1.icon = "play"
        self.timer_1_interval.cancel()
        self.screen.add_widget(self.box_1)
        self.screen.remove_widget(self.bar_1)
        return
    def stop_2_pressed(self,*args):
        if self.slider_2.value == 0:
            return
        self.slider_2.value = 0
        self.start_2.icon = "play"
        self.timer_2_interval.cancel()
        self.screen.add_widget(self.box_2)
        self.screen.remove_widget(self.bar_2)
        return
    def stop_3_pressed(self,*args):
        if self.slider_3.value == 0:
            return
        self.slider_3.value = 0
        self.start_3.icon = "play"
        self.timer_3_interval.cancel()
        self.screen.add_widget(self.box_3)
        self.screen.remove_widget(self.bar_3)
        return

# TIMERS ANIMATIONS
    # Animation of timer running
    def timer_1_change(self,*args):
        self.screen.remove_widget(self.timer_1)
        self.slider_1.value -=1
        self.screen.add_widget(self.timer_1)
        if self.slider_1.value == 0:
                self.start_1.icon = "play"
                self.timer_1_interval.cancel()
                self.screen.add_widget(self.box_1)
                self.screen.remove_widget(self.bar_1)
                self.sound = SoundLoader.load('bell.mp3')
                self.sound.play()
        return
    def timer_2_change(self,*args):
        self.screen.remove_widget(self.timer_2)
        self.slider_2.value -=1
        self.screen.add_widget(self.timer_2)
        if self.slider_2.value == 0:
                self.start_2.icon = "play"
                self.timer_2_interval.cancel()
                self.screen.add_widget(self.box_2)
                self.screen.remove_widget(self.bar_2)
                self.sound = SoundLoader.load('bell.mp3')
                self.sound.play()
        return
    def timer_3_change(self,*args):
        self.screen.remove_widget(self.timer_3)
        self.slider_3.value -=1
        self.screen.add_widget(self.timer_3)
        if self.slider_3.value == 0:
                self.start_3.icon = "play"
                self.timer_3_interval.cancel()
                self.screen.add_widget(self.box_3)
                self.screen.remove_widget(self.bar_3)
                self.sound = SoundLoader.load('bell.mp3')
                self.sound.play()
        return


       
       
SimpleTimerApp().run()




