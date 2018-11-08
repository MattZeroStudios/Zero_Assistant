import manager
from PyQt5.QtWidgets import *
from PyQt5.uic import *
import sys

# xManager = manager.Manager()
GoogleAssistant = QApplication(sys.argv)
Window = loadUi('ui/main.ui')
Window.show()
sys.exit(GoogleAssistant.exec_())
