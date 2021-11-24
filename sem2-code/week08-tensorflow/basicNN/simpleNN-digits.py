# simple neural network using tensor flow to interpret handwritten digits
# 
# Author: Andrew Beatty

#### Libraries
# My libraries
import mnist_loader
import utils

# Third-party libraries
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt


def run_neural_net():
    training_data, validation_data, test_data = mnist_loader.load_data()
    
    # I used this code to inspect the data
    #print (f"{training_data[0]}, {training_data[1]}")
    #show_image(training_data[0][0], training_data[1][0],0)

    #print (f"{test_data[0]}, {test_data[1]}")
    #utils.show_image(test_data[0][0], test_data[1][0], 0)


    # build the net
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(784,1)),  # input layer (1)
        keras.layers.Dense(128, activation='relu'),  # hidden layer (2)
        keras.layers.Dense(10, activation='softmax')  # output layer (3)
    ])

    model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

    # we pass the data, labels and epochs and watch the magic!
    # I put in an epock of 1 to speed this up
    model.fit(training_data[0], training_data[1], epochs=1)

    validation_loss, validation_acc = model.evaluate(validation_data[0],  validation_data[1], verbose=1)


    print(f'Validation accuracy:{ validation_acc}\nloss: {validation_loss}')

    # make predictions
    predictions = model.predict(test_data[0])

    max = len(test_data)
    num = num = utils.get_number(max)
    while num != -1:
        #image = test_data[num][0]
        image= test_data[0][num]
        label = test_data[1][num]
        guess = np.argmax(predictions[num])
        utils.show_image(image, label, guess)
        num = utils.get_number(max)


if __name__ == '__main__':
    run_neural_net()
