from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from audio_recorder import RecorderFactory  # Import the factory

# 5. The main Kivy app using the factory pattern
class AudioApp(App):
    def build(self):
        # Get the correct recorder instance based on platform
        self.recorder = RecorderFactory.get_recorder()

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.info_label = Label(text="Press Record to start recording", size_hint=(1, 0.2))
        layout.add_widget(self.info_label)

        # Record button
        self.record_button = Button(text="Record", on_press=self.start_recording, size_hint=(1, 0.2))
        layout.add_widget(self.record_button)

        # Stop button
        self.stop_button = Button(text="Stop", on_press=self.stop_recording, size_hint=(1, 0.2))
        layout.add_widget(self.stop_button)

        # Play button
        self.play_button = Button(text="Play", on_press=self.play_recording, size_hint=(1, 0.2))
        layout.add_widget(self.play_button)

        return layout

    def start_recording(self, instance):
        self.recorder.start_recording()
        self.info_label.text = "Recording..."

    def stop_recording(self, instance):
        self.recorder.stop_recording()
        self.info_label.text = "Recording stopped and saved."

    def play_recording(self, instance):
        self.recorder.play_recording()
        self.info_label.text = "Playing recording..."

if __name__ == '__main__':
    AudioApp().run()
