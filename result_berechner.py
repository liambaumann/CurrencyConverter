from abc import ABC, abstractmethod
import json
import requests

class result_base(ABC):
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

