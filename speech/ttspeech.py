import pyttsx3


class Speech:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.load_configurations()

# Setters and Getters

    def set_speed(self, rate):
        self.engine.setProperty("rate", rate)

    def set_voice(self):
        pass

    def set_volume(self, volume):
        self.engine.setProperty("volume", volume)

    def get_speed(self):
        __speed = self.engine.getProperty("speed")
        return __speed

    def get_voice(self):
        __voice = self.engine.getProperty("voice")
        return __voice

    def get_volume(self):
        __volume = self.engine.getProperty("volume")
        return __volume

# End of getters and setters and utility based methods begin.

    def load_configurations(self):
        pass

    def say(self, msg):
        s_msg = str(msg)
        self.engine.say(s_msg)
        self.engine.runAndWait()

    def stop(self):
        pass
