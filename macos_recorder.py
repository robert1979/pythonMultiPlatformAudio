import os
import soundfile as sf
import numpy as np
import sounddevice as sd  # Import sounddevice for macOS
from kivy.core.audio import SoundLoader
from audio_recorder import AudioRecorder  # Import the AudioRecorder interface

# 2. MacOSRecorder Implementation using sounddevice
class MacOSRecorder(AudioRecorder):
    def __init__(self):
        self.recording_path = os.path.join(os.getcwd(), 'recording_macos.wav')
        self.samplerate = 44100
        self.channels = 2
        self.recording = []
        self.stream = None

    def callback(self, indata, frames, time, status):
        """Callback function for sounddevice to capture audio data."""
        self.recording.append(indata.copy())

    def start_recording(self):
        print("Starting recording on macOS")
        self.recording = []  # Clear previous recording
        self.stream = sd.InputStream(samplerate=self.samplerate, channels=self.channels, callback=self.callback)
        self.stream.start()

    def stop_recording(self):
        print("Stopping recording on macOS")
        self.stream.stop()
        self.stream.close()
        # Convert list of recorded chunks into a single NumPy array
        recording_np = np.concatenate(self.recording, axis=0)
        # Save the recorded data as a WAV file
        sf.write(self.recording_path, recording_np, self.samplerate)
        print(f"Recording saved to: {self.recording_path}")

    def play_recording(self):
        print("Playing recording on macOS")
        sound = SoundLoader.load(self.recording_path)
        if sound:
            sound.play()
        else:
            print("Error: Unable to play the recording.")
