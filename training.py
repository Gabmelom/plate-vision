import sys
import numpy as np
from tensorflow.keras.layers import Dense, Flatten, Input
from tensorflow.keras.models import Model
from tensorflow.keras.applications import InceptionResNetV2


# This file is used to train the model on the SCS Openstack server with a better GPU than mine
# The model is saved as object_detection.h5
# The model is trained on a subset of the data (5000 images) due to the computational cost of training on the full dataset
# Data is split 80-20 for training and testing

 
def train_model(X_train, X_test, y_train, y_test):
    inception_resnet = InceptionResNetV2(weights="imagenet",include_top=False, input_tensor=Input(shape=(224,224,3)))

    head_model = inception_resnet.output
    head_model = Flatten()(head_model)
    head_model = Dense(500,activation="relu")(head_model)
    head_model = Dense(250,activation="relu")(head_model)
    head_model = Dense(4,activation='sigmoid')(head_model)

    model = Model(inputs=inception_resnet.input, outputs=head_model)

    model.compile(loss="mean_squared_error", optimizer="adam")
    print("Model compiled")
    print(model.summary())
    model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=200, batch_size=16)
    model.save("plate_detection.h5")
    print("Model trained and saved")


if __name__ == "__main__":
    # Load data
    loaded = np.load("data.npz")
    X_train = loaded["X_train"]
    X_test = loaded["X_test"]
    y_train = loaded["y_train"]
    y_test = loaded["y_test"]
    
    print("Data loaded:")
    print("X_train shape:", X_train.shape)
    print("X_test shape:", X_test.shape)
    print("y_train shape:", y_train.shape)
    print("y_test shape:", y_test.shape)

    # Train model
    train_model(X_train, X_test, y_train, y_test)
