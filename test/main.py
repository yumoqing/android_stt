import time
from kivyblocks.setconfig import config_set
from kivy.app import App
from kivy.utils import platform
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
if platform=='android':
	from android_stt import RecognizerListenerBase, AndroidNativeSTT
else:
	class RecognizerListenerBase(object):
		pass
	class AndroidNativeSTT:
		pass

from version import __version__

class SttWideget(RecognizerListenerBase, BoxLayout):
	def __init__(self, **kw):
		RecognizerListenerBase.__init__(self)
		BoxLayout.__init__(self, **kw)
		self.orientation = 'vertical'
		self.w_act = Button(text='start', height=60, size_hint_y=None)
		self.w_txt = TextInput(multiline=True)
		self.w_act.bind(on_press=self.toggle_action)
		self.add_widget(self.w_act)
		self.add_widget(self.w_txt)
		self.stt = None
		if platform == 'android':
			self.stt = AndroidNativeSTT()
			time.sleep(1)
			self.stt.setListener(self)
		print(f'Speech To Text test version={__version__}')

	def toggle_action(self, *args):
		if self.w_act.text == 'start':
			self.start_recognize()
		else:
			self.stop_recognize()

	def start_recognize(self):
		self.w_act.text = 'stop'
		if self.stt:
			self.stt.startListening()

	def stop_recognize(self, *args):
		self.w_act.text = 'start'
		if self.stt:
			self.stt.stopListening()

	def onPartialResults(self, partialResults):
		x = super().onPartialResults(partialResults)
		self.w_txt.text = str(x)

	def onResults(self, results):
		x = super().onResults(results)
		self.w_txt.text = str(x)

class SttApp(App):
	def build(self):
		w = SttWideget()
		return w

if __name__ == '__main__':
	SttApp().run()

