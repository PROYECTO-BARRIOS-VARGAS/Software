from PyQt5 import QtCore, QtGui, QtWidgets


class SeleccionColorDialog(object):
    def setupUi(self, SeleccionColorDialog):
        SeleccionColorDialog.setObjectName("SeleccionColorDialog")
        SeleccionColorDialog.resize(800, 700)
        self.btn_seleccionar_color = QtWidgets.QPushButton(SeleccionColorDialog)
        self.btn_seleccionar_color.setGeometry(QtCore.QRect(20, 130, 151, 31))
        self.btn_seleccionar_color.setObjectName("btn_seleccionar_color")
        self.frm_color_seleccionado = QtWidgets.QFrame(SeleccionColorDialog)
        self.frm_color_seleccionado.setGeometry(QtCore.QRect(200, 100, 120, 80))
        self.frm_color_seleccionado.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_color_seleccionado.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_color_seleccionado.setObjectName("frm_color_seleccionado")
        self.lbl_color_seleccionado = QtWidgets.QLabel(SeleccionColorDialog)
        self.lbl_color_seleccionado.setGeometry(QtCore.QRect(16, 220, 400, 16))
        self.lbl_color_seleccionado.setText("")
        self.lbl_color_seleccionado.setObjectName("lbl_color_seleccionado")

        self.retranslateUi(SeleccionColorDialog)
        QtCore.QMetaObject.connectSlotsByName(SeleccionColorDialog)

    def retranslateUi(self, SeleccionColorDialog):
        _translate = QtCore.QCoreApplication.translate
        SeleccionColorDialog.setWindowTitle(_translate("SeleccionColorDialog", "Seleccion de color"))
        self.btn_seleccionar_color.setText(_translate("SeleccionColorDialog", "Seleccionar Color..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SeleccionColorDialog = QtWidgets.QDialog()
    ui = SeleccionColorDialog()
    ui.setupUi(SeleccionColorDialog)
    SeleccionColorDialog.show()
    sys.exit(app.exec_())
