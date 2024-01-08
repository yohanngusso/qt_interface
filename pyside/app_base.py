from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
    )
# Criando algum widget para ser usado
app = QApplication()

# Criando um Widget base 
base = QWidget()

# Criando Layout 
layout = QVBoxLayout()


# Mudando a fonte
font = QFont()
font.setPixelSize(90)

# Adicionando o primeiro Widget
label = QLabel('Deixa o like')
label.setFont(font)
label.setAlignment(Qt.AlignCenter)
layout.addWidget(label)


# Adicionando botão
botao = QPushButton('Botao')
b1 = QPushButton('B1')
b2 = QPushButton('B2')
botao.setFont(font)
layout.addWidget(botao)
layout.addWidget(b1)
layout.addWidget(b2)

# Adicionando o Layout 
base.setLayout(layout)
base.show()


app.exec()