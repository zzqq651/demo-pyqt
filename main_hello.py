import sys

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
)

def main():
    app = QApplication(sys.argv)
    widget = QWidget()

    text_label = QLabel(widget)
    text_label.setText("Hello world!")
    text_label.move(115, 90)

    widget.setWindowTitle("PyQt6 Hello")
    widget.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()