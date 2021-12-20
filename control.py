import sys
from PyQt6.QtWidgets import QApplication
import model
import view
import requests
import json



class Controller:
    def __init__(self):
        self.model = model.localModel()
        self.view = view.View(self)
        self.refresh_view()

    def reset(self) -> None:
        self.model.reset()
        self.view.reset()

    def refresh(self) -> None:
        '''
        refreshes conversion rates via API
        lädt im Model über Request neue Daten ins Model und ins json file
        :return: None
        '''
        self.model.makeReq()
        self.model.saveRates()
        self.refresh_view()

    def livedata(self) -> None:
        '''
        Setzt die Livedata auf die aktuelle View einstellung
        :return:
        '''
        if(self.view.cb_live.isChecked()):
            self.model = model.liveModel(self.model.get_model_state())
        else:
            self.model = model.localModel(self.model.get_model_state())
        #INFO Ausgabe aktualisieren
        self.refresh_view()

    def refresh_view(self):
        self.view.setResult(self.model.result)

    def convert(self) -> None:
        """
        Hier wird der Controller ausgefuehrt
        :return: None
        """
        # spinbox wert von view holen
        from_amount = self.view.getAmountInput()
        print(from_amount)
        self.model.amount = from_amount

        from_curr = self.view.getFromCurr()
        print(from_curr)
        self.model.fromCurr = from_curr

        to_curr = self.view.getToCurr()
        print(to_curr)
        self.model.toCurr = to_curr

        #make conversion
        result = self.model.makeConv(from_curr, to_curr, from_amount)
        self.view.setResult(result)
        self.refresh_view()


if __name__ == '__main__':
    print("main?")
    app = QApplication([])
    c = Controller()
    c.view.show()
    sys.exit(app.exec())
