from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
from random import randint

app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Генератор") 
main_window.resize(1000, 500)

instruction_label = QLabel("Натисніть щоб обрати переможця!")

random_number = QLabel("?")

generate_button = QPushButton("Згенерувати")

def generate():
    random_number.setText(str(randint(1, 100)))


generate_button.clicked.connect(generate )

main_layout = QVBoxLayout()
main_layout.addWidget(instruction_label)
main_layout.addWidget(random_number)
main_layout.addWidget(generate_button)

main_window.setLayout(main_layout)
main_window.show()
app.exec()