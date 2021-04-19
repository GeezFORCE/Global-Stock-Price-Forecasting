"""ModelDefenition.py: Defines model based on supplied parameters"""


# External Imports
import tensorflow as tf

# Internal Imoprts
from . import constants


# Function to define model based on parameters supplied

def defineModel(XTrain, noOfLSTMUnits=128, noOfDenseUnits=64, noOfBiDirectionalLayers=1,
                noOfDenseLayers=1, dropoutRate=0.01, returnSequences=False):
    model = tf.keras.Sequential()
    model.add(
        tf.keras.layers.Bidirectional(
            tf.keras.layers.LSTM(
                units=noOfLSTMUnits,
                input_shape=(XTrain.shape[1], XTrain.shape[2]),
                return_sequences=returnSequences
            )
        )
    )

    for i in range(noOfBiDirectionalLayers - 1):
        model.add(
            tf.keras.layers.Bidirectional(
                tf.keras.layers.LSTM(
                    units=noOfLSTMUnits,
                    return_sequences=True
                )
            )
        )


    for i in range(noOfDenseLayers - 1):
        model.add(
            tf.keras.layers.Dense(
                units=noOfDenseUnits
            )
        )

    model.add(tf.keras.layers.Dropout(rate=dropoutRate))
    
    model.add(
        tf.keras.layers.Dense(
            units=1
        )
    )

    model.compile(loss=constants.LOSS_FUNCTION,
                  optimizer=tf.keras.optimizers.Adam(learning_rate=constants.LEARNING_RATE),
                  metrics=constants.METRICS
                  )

    return model
