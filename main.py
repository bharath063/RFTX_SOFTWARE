from rftx_gui import RFTXMainWindow

import sys
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = RFTXMainWindow()
    window.show_splash()
    window.show()
    sys.exit(app.exec_())
