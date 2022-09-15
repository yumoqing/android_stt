from kivyblocks.setconfig import config_set
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from android_stt import RecognizerListenerBase, AndroidNativeSTT

class SttWideget(RecognizerListenerBase, BoxLayout):
	def __init__(self, stt, **kw):
		RecognizerListenerBase.__init__(self, stt)
		BoxLayout.__init__(self, **kw)
		self.orientation = 'vertical'
		self.stt = stt
		self.w_act = Button(text='start', height=60, size_hint_y=None)
		self.w_txt = TextInput(multiline=True)
		self.w_act.bind(on_press=self.toggle_action)
		self.add_widget(w_act)
		self.add_widget(w_txt)
		self.tts.setListener(self)

	def toggle_action(self, *args):
		if self.w_act.text = 'start':
			self.start_recognize()
		else:
			self.stop_recognize()

	def start_recognize(self):
		self.stt.startListening()
		self.w_act.text = 'stop'

	def stop_recognize(self, *args):
		self.stt.stopListening()
		self.w_act.text = 'start'

	def onPartialResults(self, partialResults):
		x = super().onPartialResults(partialResults)
		self.w_txt.text = str(x)

	def onResults(self, results):
		x = super().onResults(results)
		self.w_txt.text = str(x)

class SttApp(App):
	def build(self):
		stt = AndroidNativeSTT()
		w = SttWideget(stt)
		return w

if __name__ == '__main__':
	SttApp().run()

