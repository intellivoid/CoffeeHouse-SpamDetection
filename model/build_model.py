import os

from coffeehouse_dltc.chmodel.configuration import Configuration

model_directory = os.path.join(os.getcwd(), "spam_ham")
configuration = Configuration(model_directory)
configuration.train_model()