from query import google_q as query
from speech import ttspeech as say


class Manager:

    def __init__(self):
        self.Ask = query.Query()
        self.Speech = say.Speech()

    def active_listen(self):
        print("Hey Im listening")


class SettingsManager:

    def __init__(self):
        pass


class EGUIManager:
    def __init__(self):
        pass
