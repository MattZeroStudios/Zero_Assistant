import manager
from PyQt5.QtWidgets import *
from PyQt5.uic import *
import sys
GoogleAssistant = QApplication(sys.argv)
Window = loadUi('ui/main.ui')
# manager = manager.Manager()
Window.show()
sys.exit(GoogleAssistant.exec_())
