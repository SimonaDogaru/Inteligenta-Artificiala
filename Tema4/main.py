import random
import numpy as np
from Neuron import Node


class NN:

    input = []
    hidden = []
    output = []
    b = []
    size_input = 0
    size_hidden = 0
    size_output = 0

    train_data = []
    test_data = []

    max_epochs = 10

    def __init__(self, path_for_data):
        f = open(path_for_data, 'r')
        data_from_file = []
        read_one_line = f.readline()
        while read_one_line != '':
            data_from_file.append(read_one_line.replace('\n', '').split(','))
            read_one_line = f.readline()
        random.shuffle(data_from_file)

        size = len(data_from_file)

        size = 0.80*size
        self.train_data = data_from_file[0:int(size)]
        self.test_data = data_from_file[int(size)+1:]

        self.output = [Node('Setosa', [], []),
                       Node('Versicolour', [], []),
                       Node('Virginica', [], [])]

        self.hidden = [Node('H1', self.output, []),
                       Node('H2', self.output, []),
                       Node('H3', self.output, []),
                       Node('H4', self.output, [])]

        self.input = [Node('sepal_length', self.hidden, []),
                      Node('sepal_width', self.hidden, []),
                      Node('petal_length', self.hidden, []),
                      Node('petal_width', self.hidden, [])]

        self.b=[random.uniform(0, 1)] * 2
        # print(self.b)
        # self.b[0] = float(random.uniform(0, 1))
        # self.b[1] = float(random.uniform(0, 1))

    def print_test_data_train_data(self):
        print('Train data:\n{}'.format(self.train_data))
        print('\nTest data:\n{}'.format(self.test_data))

    def print_parameters(self):
        print('Number of epochs = {}\nInput nodes (size = {})\nHidden nodes (size = {})\nOutput nodes (size = {})\n'.format(
                self.max_epochs, 4, 4, 3))

        # subpunctul 3

        def sigmoid_activation_function(x):
            return 1/(1 + np.exp(-x))


        def sigmoid_derivative(x):
             return sigmoid_activation_function(x)(1-sigmoid_activation_function(x))


        def error_function(target, output):
            sum_error=0
            for index in range(len(target)):
                sum_error=pow((target[index]-output[index]),2)

            return 1/2*sum_error

        #subpunctul 4
        def forwardPropagation(train_data):
            for index in range(len(self.input)):
                self.input[index].name = float(train_data[index])
            net1 = []
            for index in range(len(self.hidden)):
                net1[index] = 0
                for index1 in range(len(self.input)):
                    print(index1)
                    net1[index] += self.input[index1].weights[index] * float(self.input[index1].name[index])
                net1[index] += self.b[0]

            for index in range(len(self.hidden)):
                self.hidden[index].name=sigmoid_activation_function(net1[index])

            net2 = []
            for index in range(len(self.output)):
                net2[index] = 0
                for index1 in range(len(self.hidden)):
                    net2[index] += self.hidden[index1].weights[index] * float(self.hidden[index1].name[index])
                net2[index] += self.b[1]

            max=0
            index_out=0
            for index in range(len(self.output)):
                self.output[index].name=sigmoid_activation_function(net2[index])
                if max< self.output[index].name:
                    max=self.output[index].name
                    index_out=index

            if index_out == 0:
                print('Setosa')
            elif index_out == 1:
                print('Versicolour')
            else:
                print('Virginica')

            # cum fac functia de eroare?  din ce target scad output-ul?  dintr-0 lista de [1,1,1]??


        for data in self.train_data:
            print(forwardPropagation(data))


if __name__ == '__main__':
    RN = NN('iris.data')
    RN.print_test_data_train_data()
    print('\n')
    RN.print_parameters()


    # print('--------------------')
    # print(error_function([1,1,1],[0,0,0]))
