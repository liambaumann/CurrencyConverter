from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import *
from PyQt6 import uic, QtGui
from PyQt6.uic.properties import QtCore


class View(QMainWindow):
    def __init__(self, controller):
        """
        init methode des Models
        Hier wird das theme , window title, erste message gesetzt und der ausfuehren button verbunden
        """

        super().__init__()
        #laedt die GUI
        uic.loadUi("ccGUI.ui", self)

        #uic.loadUi("ui_cc.py", self)
        #Setzt den Titel vom Fenster oben
        self.setWindowTitle("Currency Converter")
        #Statusbar message
        self.statusbar.showMessage("Welcome! Please enter an amount, the currency you have, and the currencies you want to convert to")


        #listener connecten
        self.pb_convert.clicked.connect(controller.convert)     #ausfuehren button, Signal und Slot
        #self.pb_refresh.clicked.connect(controller.refresh)
        self.cb_live.clicked.connect(controller.livedata)

        #cb_from füllen
        currencies = ["EUR","USD","AUD","GBP","HRK","NZD","SEK","RUB","PGK","HKD","PLN","BTC"]
        for c in currencies:
            self.cb_from.addItem(c)

        #listWidget befüllen
        for c in currencies:
            self.lw_toCurr.addItem(c)

        print(self.dsb_amount.value())

    def reset(self) -> None:
        pass


    """ Im Sinne von MVC ist es sinnvoll die QT Widgets nicht direkt auszulesen, damit auch andersstrukturierte Views funktionieren:  """

    def getAmountInput(self) -> float:
        """
        :return: Amount in Double Spinbox
        """
        return self.dsb_amount.value()


    def getFromCurr(self) -> str:
        """
        Waehrung
        :return: From currency
        """
        return self.cb_from.currentText()

    def getToCurr(self) -> str:
        """
        Zielwaehrung
        :return: To currencies as array
        """
        temp_toCurr = ""
        for item in self.lw_toCurr.selectedItems():
            temp_toCurr += item.text() + ","
        toCurr = temp_toCurr[:-1]
        return toCurr

    def setResult(self, result) -> None:
        """
        sets the result text in view
        :param result: text that should be set
        :return: None
        """
        self.te_result.setText(result)
        #Result nach unten schieben:
        verScrollBar = self.te_result.verticalScrollBar()
        verScrollBar.setValue(verScrollBar.maximum())