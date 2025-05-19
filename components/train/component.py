import tensorflow as tf
import pandas as pd
import os

def train_model(input_dir, output_dir):
    X = pd.read_csv(os.path.join(input_dir, "X.csv"))
    y = pd.read_csv(os.path.join(input_dir, "y.csv"))

    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy', tf.keras.metrics.AUC()])
    model.fit(X, y, epochs=5, batch_size=2048, validation_split=0.2)

    model.save(os.path.join(output_dir, "model"))
