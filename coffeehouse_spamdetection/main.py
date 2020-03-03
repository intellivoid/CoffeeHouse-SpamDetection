import os
from coffeehouse_dltc.main import DLTC
from coffeehouse_dltc.chmodel.configuration import Configuration

class SpamDetection(object):

    def __int__(self):
        self.dltc = DLTC()

    @staticmethod
    def models_directory():
        return os.path.join(os.path.dirname(__file__), 'model')

    @staticmethod
    def models_trained_directory():
        return  os.path.join(os.path.dirname(__file__), 'model_output')

    def train_model(self):
        configuration = Configuration(self.models_directory())
        configuration.train_model()