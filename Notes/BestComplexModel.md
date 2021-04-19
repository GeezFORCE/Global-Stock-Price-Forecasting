- ```

    model = tf.keras.Sequential()
    model.add(
    tf.keras.layers.Bidirectional(
        tf.keras.layers.LSTM(
        units=2048 
        input_shape=(XTrain.shape[1], XTrain.shape[2]),
        return_sequences=True
        )
    )
    )
    model.add(
    tf.keras.layers.Bidirectional(
        tf.keras.layers.LSTM(
        units=1024,
        return_sequences=True
        )
    )
    )
    model.add(
    tf.keras.layers.Bidirectional(
        tf.keras.layers.LSTM(
        units=1024
        )
    )
    )
    model.add(tf.keras.layers.Dense(64))
    model.add(tf.keras.layers.Dropout(rate=0.2))
    model.add(tf.keras.layers.Dense(units=32))
    model.add(tf.keras.layers.Dense(units=1))
    model.compile(loss='mean_squared_error', optimizer='adam', metrics=["accuracy"])
  ```