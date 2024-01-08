# APP BASE

* Toda estrutura do QT começa com um Widget chamado 'QApplication'
- 'QApplication' é o widget da aplicação

# QtWidgets
* São Widgets
* Label -> Caixa fixa de texto -> QLabel('Texto')

# QtGui
* Alguma coisa que acontece com o Widget
* QtFont -> mudança/alteração na fonte

# QtCore
* Qt -> alinhamento -> label.setAlignment(Qt.AlignCenter) 

## Só um único Widget pode aparecer por vez

# Uma janela só pode ter um único Widget 

* A solução é criar um Widget para colocar esses dois Widgets dentro
* Precisamos de um Widget que aceite outros Widgets em sua composição

# Qwidget

* O Qwidget não consegue adicionar outros widgets em sua estrutura. Ele precisa de um widget de Layout!

# Formatos principais de layout 

* QHBoxLayout
* QVBoxLayout
* QGridLayout
* QFormLayout

# Criando Layout

* layout = QVBoxLayout
* Esse é o exemplo de criação de um Layout do tipo Vertical

# Adicionando Widgets no layout

* Primeiro crie o widget e logo depois adicione: 
- botao = QPushButton('Botao')
- layout.addWidget(botao)

# Adicionando o Layout no widget base
* Como foi feito antes tem o Qwidget sendo um widget base. Precisamos colocar o layout nesse widget base: base.setLayout(layout)

# Criando Janela 

* janela = QMainWindow()

# Funcionalidades de Janela

* Como Menus e docks, precisamos de um Widget de Janela
* Para isso utilizamos: 'QMainWindow'

* Para adicionar a Janela, precisamos colocar o Widget central:
- janela.setCentralWidget(base)
- janela.show()

# Menuns e Actions

* Para adicionar itens no menu da janela precisamos pedir seu nome e adicionar ações a elas.
* Essas ações são dadas por outro componente: QtGui.QAction