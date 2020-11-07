import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel, QHBoxLayout
from PyQt5.QtWidgets import QWidget, QPushButton

class App():
    def __init__(self):
        pass
    def init_qt(self):
        self.inst = QApplication(sys.argv)
    def create_window(self, coords):
        self.window = QWidget()
        self.window.setWindowTitle('PyQt5 App')
        self.window.setGeometry(coords[0], coords[1], coords[2], coords[3])
        self.window.move(60, 15)
        helloMsg = QLabel('<h1>Hello World!</h1>', parent=self.window)

    def set_window_layout(self, layout):
        self.window.setLayout(layout)

def test():
    print("test")

def main():
    app = App()
    app.init_qt()
    app.create_window((100, 100, 1024, 768))
    layout = QHBoxLayout()
    button = QPushButton("test")
    button.clicked.connect(test)
    layout.addWidget(button)
    app.set_window_layout(layout)
    app.window.show()
    sys.exit(app.inst.exec_())

if __name__ == "__main__":
    main()

