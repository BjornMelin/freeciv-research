import tensorflow as tf
import random
import numpy as np

# Description of our inputs and outputs
"""
government: 0-5
enemies_near: 0 or 1
"""
# input_data_set = int[gold, government, num_cities, tech_level, num_allies, num_enemies, enemies_near]
# output_data_set = int[3]

file = open("TurnData.txt", "r")
if file.mode == "r":
    (input_data_set) = file.read().split("\n")

score_data = []
j = 0
score = open("ScoreData.txt", "r")
if score.mode == "r":
    for j in range(299):
        score_data[j] = score.read().split("\n")
    # score_data = score.read().split('\n')

n_classes = 3
# Play a game of 300 turns
batch_size = 1
num_turns = 300

# Defining 3 hidden layers which our data will be passed through: three layers of five neurons each
hidden1_nodes = 5
hidden2_nodes = 5
hidden3_nodes = 5

x = tf.placeholder("float", [None, 7])
y = tf.placeholder("float")


# Our Neural Network Model
def neural_network(input_data):

    # Each hidden layer is composed of weights applied to the previous input, and a bias added to it.
    hidden_layer_1 = {
        "weights": tf.Variable(tf.random_normal([7, hidden1_nodes])),
        "bias": tf.Variable([1]),
    }

    hidden_layer_2 = {
        "weights": tf.Variable(tf.random_normal([hidden1_nodes, hidden2_nodes])),
        "bias": tf.Variable([1]),
    }

    hidden_layer_3 = {
        "weights": tf.Variable(tf.random_normal([hidden2_nodes, hidden3_nodes])),
        "bias": tf.Variable([1]),
    }

    output_layer = {
        "weights": tf.Variable(tf.random_normal([hidden3_nodes, 3])),
        "bias": tf.Variable(tf.random_normal([3])),
    }

    # Compute the values of each layer by multiplying the previous layer by the weight, add a bias, then feed to next layer
    layer1 = tf.add(
        tf.matmul(input_data, hidden_layer_1["weights"]), hidden_layer_1["bias"]
    )
    layer1 = tf.nn.relu(layer1)

    layer2 = tf.add(
        tf.matmul(layer1, hidden_layer_2["weights"]), hidden_layer_2["bias"]
    )
    layer2 = tf.nn.relu(layer2)

    layer3 = tf.add(
        tf.matmul(layer2, hidden_layer_3["weights"]), hidden_layer_3["bias"]
    )
    layer3 = tf.nn.relu(layer3)

    output = tf.matmul(layer3, output_layer["weights"]) + output_layer["bias"]

    return output


def train_neural_network(x):
    prediction = neural_network(x)
    scoreDifference = 1 / (score_data[i] - score_data[i - 1])
    optimizer = tf.train.AdamOptimizer()

    num_epochs = 1

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        for epoch in range(num_epochs):
            epoch_cost = 0

            i = 0
            while i < num_turns:
                current = int(score_data[i])
                if i == 0:
                    previous = 0
                else:
                    previous = int(score_data[i - 1])
                # scoreDifference = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(1 / (current - previous)))
                # scoreDifference = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=prediction, labels=score_data))

                # The difference between last score and current score is current - previous: if we minimize 1/difference, we incentivize high differences
                scoreDifference = 1 / (current - previous)
                optimizer = tf.train.AdamOptimizer().minimize(scoreDifference)

                start = i
                end = i + batch_size

                batch_x = np.array(input_data_set[start:end])
                batch_y = np.array(score_data[start:end])

                _, c = sess.run(
                    [optimizer, scoreDifference], feed_dict={x: batch_x, y: batch_y}
                )
                epoch_cost += c

                # input_data_set, score_data = input_data_set.train.next_batch(1)

            print("Epoch ", epoch, "completed of ", num_epochs, "loss: ", epoch_cost)


train_neural_network(input_data_set)
