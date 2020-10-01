import os
import sys
from PyQt5.QtWidgets import *

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from window import SimulatorWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    wnd = SimulatorWindow()
    wnd.show()
    sys.exit(app.exec_())
