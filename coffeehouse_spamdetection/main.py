import os
from coffeehouse_dltc.main import DLTC
from coffeehouse_dltc.chmodel.configuration import Configuration

class SpamDetection(object):

    def __int__(self):
        self.models_directory = os.path.join(os.path.dirname(__file__), 'model')
        self.models_trained_directory = os.path.join(os.path.dirname(__file__), 'model_output')
        self.dltc = DLTC()

    def train_model(self):
        configuration = Configuration(self.models_directory)
        configuration.train_model()