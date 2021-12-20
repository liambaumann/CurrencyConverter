from abc import ABC, abstractmethod
import json
import requests

class result_base(ABC):
    def __init__(self, result = ""):
        self.result = result
        self.fromCurr = ""
        self.toCurr = ""
        self.toCurrList = {}
        self.amount = 0.0
        self.rates = {}

    @abstractmethod
    def makeConv(self, fromCurr, toCurr, amount) -> str:
        """
        Macht eine Umrechnung im Model
        :param fromCurr:
        :param toCurr:
        :param amount:
        :return: str fuer ergebnis
        """
        pass

    def calculate(self):
        # erste zeile:
        self.result += f"{round(self.amount, 2)} {self.fromCurr} equal:<br/>"

        # ergebnis zeilen:
        if (self.fromCurr.upper() == "EUR"):  # Wenn ausgangswährung EUro ist die Conversion einfacher
            for currency in self.toCurrList:
                rate = self.rates['rates'][currency]
                self.result += "   - " + str(round(self.amount * rate, 2)) + f" {currency} (rate: {rate})<br/>"
        else:  # Bei einer anderen Währung muss auch ein neuer Kurs errechnet werden
            for currency in self.toCurrList:
                # Die zwei Währungen holen:
                rateTo = self.rates['rates'][currency]
                rateFrom = self.rates['rates'][self.fromCurr]
                rate = rateTo / rateFrom  # Neuer Kurs Muss berechnet werden
                self.result += "   - " + str(round(self.amount * rate, 2)) + f" {currency} (rate: {rate})<br/>"
        self.result += "<br/>"

        return self.result

class result_local(result_base):
    def __init__(self, result = ""):
        super().__init__(result)
        self.loadRates()
    def makeConv(self, fromCurr, toCurr, amount) -> str:
        '''
        macht eine locale Conversion
        :param fromCurr: anfangswährung
        :param toCurr: zielwährung
        :param amount: betrag
        :return: result string
        '''
        self.fromCurr = fromCurr
        self.toCurr = toCurr
        self.toCurrList = toCurr.split(',')
        self.amount = amount
        return self.calculate()

    def loadRates(self):
        '''
        Holt die abgespeicherten Daten in die lokale Variable
        :return:
        '''
        with open('conversion_rates.json') as json_file:
            self.rates = json.load(json_file)
        self.result += "<b>INFO:</b> loaded conversion rates data from local file<br/>"

class result_live(result_base):
    def makeConv(self, fromCurr, toCurr, amount) -> str:
        '''
        macht eine locale Conversion
        :param fromCurr: anfangswährung
        :param toCurr: zielwährung
        :param amount: betrag
        :return: result string
        '''
        self.fromCurr = fromCurr
        self.toCurr = toCurr
        self.toCurrList = toCurr.split(',')
        self.amount = amount

        #aktuelle daten holen
        self.makeReq()
        self.saveRates()

        return self.calculate()

    def makeReq(self):
        '''
        macht ein Request an die API und speichert in lokale Variable self.req
        :return:
        '''
        self.rates = requests.get("http://api.exchangeratesapi.io/v1/latest",
                                  params={"access_key": "1c075de943a2b42973dda2f58e5df5ad"}).json()
        self.result += "<b>INFO:</b> made request to conversion rates API<br/>"

    def saveRates(self):
        '''
        Speichert die daten aus der Variable in ein Lokales Json file
        :return:
        '''
        #json file speichern
        with open('conversion_rates.json', 'w') as outfile:
            json.dump(self.rates, outfile)
        self.result += "<b>INFO:</b> saved conversion rates data on device<br/>"

