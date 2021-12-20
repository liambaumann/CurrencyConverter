from abc import ABC, abstractmethod
import json
import requests

class baseModel(ABC):
    #init from state
    def __init__(self, state = None):
        '''
        init methode
        :param state: alle parameter des alten models als array
        '''
        if(state != None):
            self.fromCurr = state[0]
            self.toCurr = state[1]
            self.toCurrList = state[2]
            self.toCurrConverted = state[3]
            self.result = state[4]
            self.amount = state[5]
        else:
            self.fromCurr = ""
            self.toCurr = ""
            self.toCurrList = {}
            self.toCurrConverted = {}
            self.result = ""
            self.amount = 0.0

    def get_model_state(self):
        '''
        gibt die attribute des models zurück als array
        :return:
        '''
        return [self.fromCurr, self.toCurr, self.toCurrList, self.toCurrConverted, self.result, self.amount]
        #return self.__dict__

    def set_model_state(self, state):
        '''
        setzt die attribute des models
        :param state:
        :return:
        '''
        self.fromCurr = state[0]
        self.toCurr = state[1]
        self.toCurrList = state[2]
        self.toCurrConverted = state[3]
        self.result = state[4]
        self.amount = state[5]

    def reset(self):
        self.fromCurr = ""
        self.toCurr = ""
        self.toCurrList = {}
        self.toCurrConverted = {}
        self.result = ""
        self.amount = 0.0

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

    def reset(self) -> None:
        """
        Alle felder zuruecksetzen
        :return: None
        """
        self.fromCurr = ""
        self.toCurr = ""
        self.toCurrList = {}
        self.toCurrConverted = {}
        self.result = ""
        self.amount = 0.0
        self.loadRates()


class localModel(baseModel):
    def __init__(self, state=None):
        super().__init__(state)
        self.loadRates()

    def loadRates(self):
        '''
        Holt die abgespeicherten Daten in die lokale Variable
        :return:
        '''
        with open('conversion_rates.json') as json_file:
            self.rates = json.load(json_file)
        self.result += "<b>INFO:</b> loaded conversion rates data from local file<br/>"

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

        self.calculate()

class liveModel(baseModel):
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

        self.calculate()

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
