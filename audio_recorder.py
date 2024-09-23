import platform as system_platform
from plyer.utils import platform

# 1. The AudioRecorder Interface (abstract methods)
class AudioRecorder:
    def start_recording(self):
        raise NotImplementedError

    def stop_recording(self):
        raise NotImplementedError

    def play_recording(self):
        raise NotImplementedError

# 4. The RecorderFactory that returns the appropriate instance
class RecorderFactory:
    @staticmethod
    def get_recorder():
        if platform == 'android':
            from android_recorder import AndroidRecorder
            return AndroidRecorder()
        elif system_platform.system() == "Darwin":
            from macos_recorder import MacOSRecorder
            return MacOSRecorder()
        else:
            raise NotImplementedError("This platform is not supported")
