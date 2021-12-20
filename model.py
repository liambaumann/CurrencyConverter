from abc import ABC, abstractmethod
import json
import requests

from result_berechner import result_local
from result_berechner import result_live


class model():
    #init from state
    def __init__(self):
        '''
        init methode
        '''

        self.fromCurr = ""
        self.toCurr = ""
        self.toCurrList = {}
        self.toCurrConverted = {}
        self.result = ""
        self.amount = 0.0

        #Strategie standardmäßig local:
        self.result_berechner = result_local()

    def makeConv(self, fromCurr, toCurr, amount) -> str:
        return self.result_berechner.makeConv(fromCurr, toCurr, amount)

    def getResult(self):
        return self.result_berechner.result

    def toLive(self):
        self.result_berechner = result_live(self.result_berechner.result)

    def toLocal(self):
        self.result_berechner = result_local(self.result_berechner.result)

    def get_model_state(self):
        '''
        gibt die attribute des models zurück als array
        :return:
        '''
        return [self.fromCurr, self.toCurr, self.toCurrList, self.toCurrConverted, self.result, self.amount]

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
        self.view.reset()
