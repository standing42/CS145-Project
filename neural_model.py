from sklearn.neural_network import MLPClassifier
import csv
import os

class neural_model():
    def __init__(self):
        self.train_x = [[0.124, 0.876, 0.0, -0.4019],
                        [0.0, 0.682, 0.318, 0.6369]]
        self.train_y = [-1, 1]

    def train(self):
        mlp = MLPClassifier(hidden_layer_sizes=(50, 50), max_iter=100, alpha=1e-4,
                            solver='sgd', random_state=1)

        mlp.fit(self.train_x, self.train_y)
        print("Training set score: %f" % mlp.score(self.train_x, self.train_y))

    def read_one_file(self, file_name):
        table = csv.reader(open(file_name, newline=''), delimiter=',')
        for row in table:
            print(list(row))


if __name__ == '__main__':
    temp = neural_model()
    # temp.train()
    temp.read_one_file("sentiments/2017-11-21-19.csv")





