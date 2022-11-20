from ui_loader import ui_importer


def button_clicked(self, button_value: str):
    print(button_value)


if __name__ == "__main__":
    ui_file_name = "calculator-window.ui"

    ui_importer(ui_file_name)
