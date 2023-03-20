import sys

from PySide6.QtWidgets import QApplication
from control.main_controller import MainController

import tempfile

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # creating a temp folder called tempdir
    with tempfile.TemporaryDirectory() as tempdir:
        controller = MainController(tempdir)
        controller.show()
        app.exec()
