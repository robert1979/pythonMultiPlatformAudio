import os
from kivy.core.audio import SoundLoader
from plyer import audio  # Import Plyer for Android
from audio_recorder import AudioRecorder  # Import the AudioRecorder interface

# 3. AndroidRecorder Implementation using Plyer
class AndroidRecorder(AudioRecorder):
    def __init__(self):
        self.recording_path = os.path.join(os.environ['EXTERNAL_STORAGE'], 'recording_android.wav')

    def start_recording(self):
        print("Starting recording on Android")
        audio.start()

    def stop_recording(self):
        print("Stopping recording on Android")
        audio.stop()
        print(f"Recording saved to: {self.recording_path}")

    def play_recording(self):
        print("Playing recording on Android")
        sound = SoundLoader.load(self.recording_path)
        if sound:
            sound.play()
        else:
            print("Error: Unable to play the recording.")
