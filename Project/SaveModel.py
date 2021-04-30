"""SaveModel.py: Saves Model in h5 and JSON"""


# Internal Imports
from . import constants

# Function to save model information in h5 and json formats


def saveModelInformation(model):
    model.save("models/{}.h5".format(constants.NAME), save_format='h5')
    model_json = model.to_json()
    with open("savedModelInformation/modelInformation/{}.json".format(constants.NAME), "w") as json_file:
        json_file.write(model_json)
    model.save_weights(
        "savedModelInformation/modelWeights/{}.h5".format(constants.NAME))
