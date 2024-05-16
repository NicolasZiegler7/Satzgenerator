from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QWidget, QPushButton, QGridLayout, QLCDNumber, QLabel, QTextBrowser


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        self.pos = 0
        self.linebreak = False

        subjektLabel = QLabel("Subjekt")

        self.subjektButton1 = QPushButton("Michell")
        self.subjektButton1.pressed.connect(self.ausgabe_in_browser)
        self.subjektButton2 = QPushButton("Das Auto")
        self.subjektButton2.pressed.connect(self.ausgabe_in_browser)
        self.subjektButton3 = QPushButton("Der Gärtner")
        self.subjektButton3.pressed.connect(self.ausgabe_in_browser)
        self.subjektButton4 = QPushButton("Meine Wenigkeit")
        self.subjektButton4.pressed.connect(self.ausgabe_in_browser)

        prätikatLabel = QLabel("Prädikat")

        self.prädikatButton1 = QPushButton("spielt")
        self.prädikatButton1.pressed.connect(self.ausgabe_in_browser)
        self.prädikatButton2 = QPushButton("fährt")
        self.prädikatButton2.pressed.connect(self.ausgabe_in_browser)
        self.prädikatButton3 = QPushButton("lacht")
        self.prädikatButton3.pressed.connect(self.ausgabe_in_browser)
        self.prädikatButton4 = QPushButton("singt")
        self.prädikatButton4.pressed.connect(self.ausgabe_in_browser)

        objektLabel = QLabel("Objekt")

        self.objektButton1 = QPushButton("Back Jack")
        self.objektButton1.pressed.connect(self.ausgabe_in_browser)
        self.objektButton2 = QPushButton("zur Schule")
        self.objektButton2.pressed.connect(self.ausgabe_in_browser)
        self.objektButton3 = QPushButton("über dich")
        self.objektButton3.pressed.connect(self.ausgabe_in_browser)
        self.objektButton4 = QPushButton("im Garten")
        self.objektButton4.pressed.connect(self.ausgabe_in_browser)

        ausgabeLabel = QLabel("Ausgabe")

        self.browserFenster = QTextBrowser()

        grid_layout = QGridLayout()

        grid_layout.addWidget(subjektLabel, 0, 0)

        grid_layout.addWidget(self.subjektButton1, 1, 0)
        grid_layout.addWidget(self.subjektButton2, 1, 1)
        grid_layout.addWidget(self.subjektButton3, 1, 2)
        grid_layout.addWidget(self.subjektButton4, 1, 3)

        grid_layout.addWidget(prätikatLabel, 2, 0)

        grid_layout.addWidget(self.prädikatButton1, 3, 0)
        grid_layout.addWidget(self.prädikatButton2, 3, 1)
        grid_layout.addWidget(self.prädikatButton3, 3, 2)
        grid_layout.addWidget(self.prädikatButton4, 3, 3)

        grid_layout.addWidget(objektLabel, 4, 0)

        grid_layout.addWidget(self.objektButton1, 5, 0)
        grid_layout.addWidget(self.objektButton2, 5, 1)
        grid_layout.addWidget(self.objektButton3, 5, 2)
        grid_layout.addWidget(self.objektButton4, 5, 3)

        grid_layout.addWidget(ausgabeLabel, 6, 0)

        grid_layout.addWidget(self.browserFenster, 7, 0, 1, 4)

        self.setLayout(grid_layout)

    @pyqtSlot()
    def ausgabe_in_browser(self):

        current_text = self.browserFenster.toPlainText()

        if self.pos == 0 and self.sender() == self.subjektButton1 or self.pos == 0 and self.sender() == self.subjektButton2 or self.pos == 0 and self.sender() == self.subjektButton3 or self.pos == 0 and self.sender() == self.subjektButton4:

            if self.linebreak:

                current_text += self.sender().text() + " "

                self.browserFenster.setText(current_text)

                self.pos += 1


            else:

                current_text += self.sender().text() + " "

                self.browserFenster.setText(current_text)

                self.pos += 1

        if self.pos == 1 and self.sender() == self.prädikatButton1 or self.pos == 1 and self.sender() == self.prädikatButton2 or self.pos == 1 and self.sender() == self.prädikatButton3 or self.pos == 1 and self.sender() == self.prädikatButton4:
            current_text += self.sender().text() + " "

            self.browserFenster.setText(current_text)

            self.pos += 1

        if self.pos == 2 and self.sender() == self.objektButton1 or self.pos == 2 and self.sender() == self.objektButton2 or self.pos == 2 and self.sender() == self.objektButton3 or self.pos == 2 and self.sender() == self.objektButton4:

            current_text += self.sender().text() + " " + "\n"

            self.browserFenster.setText(current_text)

            self.pos = 0

            self.linebreak = True

        else:
            pass
