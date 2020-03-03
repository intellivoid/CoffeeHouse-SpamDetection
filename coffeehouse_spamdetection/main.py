import os
from coffeehouse_dltc.main import DLTC

__all__ = ['SpamDetection']


class SpamDetection(object):

    def __int__(self):
        """
        Public Constructor
        """
        self.dltc = DLTC()
        self.dltc.load_model_cluster(self.model_directory())

    @staticmethod
    def model_directory():
        """
        Returns the directory for the built model

        :return: The absolute path for the built model
        """
        return os.path.join(os.path.dirname(__file__), 'spam_ham_build')

    def predict(self, text_input):
        """
        Takes the user input and predicts if the input is either
        spam or ham

        :param text_input:
        :return: Returns dictionary "ham", "spam" prediction values
        """
        return self.dltc.predict_from_text(text_input)
