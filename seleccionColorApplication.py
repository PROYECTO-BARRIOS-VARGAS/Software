import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QDialog
from PyQt5.QtGui import QColor
from seleccionColorDialog import SeleccionColorDialog


class seleccionColorApplication(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = SeleccionColorDialog()
        self.ui.setupUi(self)
        color = QColor(100, 52, 4)
        self.ui.frm_color_seleccionado.setStyleSheet('QWidget {background-color: %s }' % color.name())
        self.ui.btn_seleccionar_color.clicked.connect(self.seleccionar_color)
        self.show()

    def seleccionar_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.ui.frm_color_seleccionado.setStyleSheet('QWidget {background-color: %s }' %color.name())
            self.ui.lbl_color_seleccionado.setText('Se selecciono el color con codigo hexadecimal: {}'.format(str(color.name())))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = seleccionColorApplication()
    ventana.show()
    sys.exit(app.exec_())

