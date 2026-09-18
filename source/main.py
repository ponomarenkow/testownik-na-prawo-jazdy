from PySide6.QtWidgets import QApplication            
#from PySide6.QtCore import QObject, Signal, Slot 

import elements

app = QApplication()

dialog = elements.QuestionPage()
dialog.showMaximized()
dialog.show_question()

app.exec()