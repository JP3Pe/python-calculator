import sys

from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtWidgets import QApplication

from exit_program import program_exiter


def is_ui_file_openable(ui_file: QFile):
    if not ui_file.open(QIODevice.ReadOnly):
        return False


def ui_importer(ui_file_name: str):
    app = QApplication(sys.argv)
    ui_file = QFile(ui_file_name)

    program_exiter((is_ui_file_openable(ui_file)) == False, lambda file_path, ui_file: print(
        f"Cannot open {file_path}: {ui_file.errorString()}"))

    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()

    program_exiter(window == None, print(loader.errorString()))
    window.show()

    sys.exit(app.exec())
