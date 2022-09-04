from time import time
import sys
import time
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from playsound import playsound

app = QApplication(sys.argv)

due = input("Ingresar hora para alarma (formato: hh:mm): ")
message = input("Ingresar motivo de la alarma: ")

try:
    hours, mins = due.split(":")
    due = QTime(int(hours), int(mins))
    if not due.isValid():
        raise ValueError

except ValueError:
    mmessage = "No es una hora valida"

while QTime.currentTime() < due:
    time.sleep(20)

label = QLabel("<font color=red size=72><b>" +message+ "</b>>/<font>")
label.setWindowFlags(Qt.SplashScreen)
label.show()
playsound("alarm.mp3")
QTimer.singleShot(60000, app.quit)
sys.exit(app.exec_())
