"""KerasTuner.py: Performs hyperparameter tuning"""


# External Imports
from kerastuner.tuners import RandomSearch
import tensorflow as tf

# Internal Imports
from . import constants

# Check whether return sequences needs to be added to situations when multiple dense layers
# are present.

# Function to perform Hyperparameter tuning using custom fields


def HyperparameterTuning(hp, minNoOfLSTMUnits=128, maxNoOfLSTMUnits=256, LSTMUnitSteps=128,
                         minNoOfDenseUnits=1, maxNoOfDenseUnits=64, DenseUnitSteps=32,
                         noOfBiDirectionalLayers=1, noOfDenseLayers=1, minDropoutRate=0.1,
                         maxDropoutRate=0.1, DropoutrateSteps=0.005, learningRate=[1e-2, 1e-3]):

    model = tf.keras.Sequential()

    for i in range(noOfBiDirectionalLayers):
        model.add(
            tf.keras.layers.LSTM(
                units=hp.Int('units',
                             min_value=minNoOfLSTMUnits,
                             max_value=maxNoOfLSTMUnits,
                             step=LSTMUnitSteps
                )
            )
        )

    for i in range(noOfDenseLayers):
        model.add(
            tf.keras.layers.Dense(
                units=hp.Int('units',
                             min_value=minNoOfDenseUnits,
                             max_value=maxNoOfDenseUnits,
                             step=DenseUnitSteps
                             )
            )
        )

        model.add(
            tf.keras.layers.Dropout(
                hp.Float(
                    'dropout',
                    min_value=minDropoutRate,
                    max_value=maxDropoutRate,
                    step=DropoutrateSteps
                )
            )
        )
    model.add(tf.keras.layers.Dense(1))
    model.compile(
        optimizer=tf.keras.optimizers.Adam(hp.Choice('learning_rate', values=learningRate)), 
                                           loss=constants.LOSS_FUNCTION, 
                                           metrics=constants.METRICS
    )
    return model

# Function passed into Keras Tuner and also calls hyperparameter tuner


def buildModel(hp):
    return HyperparameterTuning(hp)

# Keras Tuner Function to search, save, and return best model


def KerasTuner(XTrain, YTrain, XValidation, YValidation):
    tuner = RandomSearch(
        buildModel,
        objective='mse',
        max_trials=30,
        executions_per_trial=10,
        directory='KerasTuner',
        project_name=f'KerasTuner-{constants.NAME}'
    )

    tuner.search_space_summary()

    tuner.search(XTrain,
                 YTrain,
                 epochs=5,
                 validation_data=(XValidation, YValidation)
                 )

    models = tuner.get_best_models(num_models=1)

    tuner.results_summary()

    return models
