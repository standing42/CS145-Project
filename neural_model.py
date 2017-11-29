from sklearn.neural_network import MLPClassifier
import csv
import os
import numpy

class neural_model():
    def __init__(self):
        self.train_x = []
        self.train_y = []

    def train(self):
        mlp = MLPClassifier(hidden_layer_sizes=(50, 50), max_iter=100, alpha=1e-4,
                            solver='sgd', random_state=1)

        mlp.fit(self.train_x, self.train_y)
        print("Training set score: %f" % mlp.score(self.train_x, self.train_y))

    def read_one_input_file(self, file_name):
        table = csv.reader(open(file_name, newline=''), delimiter=',')
        for row in table:
            float_row = [float(i) for i in row]
            # print(float_row)
            self.train_x.append(float_row)

        self.train_x = numpy.matrix(self.train_x)
        print(self.train_x.shape)

    def read_one_truth_file(self, file_name):
        table = csv.reader(open(file_name, newline=''), delimiter=',')
        for row in table:

            if row == ['1'] or row == ['-1'] or row ==['0']:
                int_row = [int(i) for i in row]
                # print(int_row)
                self.train_y.append(int_row)
            else:
                print(row[0][-1])
                self.train_y.append([int(row[0][-1])])
        self.train_y = numpy.matrix(self.train_y)
        # self.train_y = self.train_y.T
        print(self.train_y.shape)


if __name__ == '__main__':
    temp = neural_model()
    # temp.train()
    temp.read_one_input_file("input/2017-11-21.csv")
    temp.read_one_truth_file("truth/2017-11-21.csv")
    temp.train()





