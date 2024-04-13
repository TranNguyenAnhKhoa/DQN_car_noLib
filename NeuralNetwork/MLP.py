from lib2to3.pytree import convert
import sys
import numpy as np
import random
from math import exp

from numpy.lib.function_base import gradient
"""
## NETWORK:     chứa các trọng số của mạng
## INPUTS:      input của mạng
## OUTPUTS:     output của các node trong mạng
## EXPECTED:    giá trị đầu ra mong muốn
## ERRORS:      các giá trị sai số giữa đầu ra và dự đoán ở đầu ra các node trong mạng
## DELTA:       độ sai lệch so với kết quả mong muốn
"""
##-----------------------------------------------------------------------------------------------------------------------------##
##-------------------------------PHẦN KHỞI TẠO---------------------------------------------------------------------------------##
##-----------------------------------------------------------------------------------------------------------------------------##
"""
################## KHỞI TẠO MẠNG VỚI 
## neuron_struct: cấu trúc - số lớp: số nút tại mỗi lớp
## Example :  neuron_struct = [3,4,8,1], mạng có 3 lớp, lớp đầu vào 4 input, 
                                                    # 1 hiden layer 8 node ,
                                                    # lướp đầu ra dự đoán 1 node
## [NUMBER_LAYER, NUMBER_NODE_LAYER_1, NUMBER_NODE_LAYER_2,... NUMBER_NODE_LAYER_N]
"""

class ANN:

## command: lệnh để khởi tạo
    def __init__(self, neuron_struct = [1,1], command = "random"):
        self.network = []
        previous = neuron_struct[1]
        for i in range (neuron_struct[0]-1):
            current = neuron_struct[i+2]
            if (command=="random"):
                layer = [[random.uniform(-1,1) for i in range(previous+1)] for i in range(current)]
            elif (command=="one"):
                layer = [[1 for i in range(previous+1)] for i in range(current)]
            else: # Create array zeros
                layer = [[0 for i in range(previous+1)] for i in range(current)]
            previous = current
            self.network.append(layer)

##-----------------------------------------------------------------------------------------------------------------------------##
##-------------------------------PHẦN TÍNH FORWARD-----------------------------------------------------------------------------##
##-----------------------------------------------------------------------------------------------------------------------------##

################## HÀM KÍCH HOẠT - SIGMOID
    def sigmoid(self, activation):
        return 1.0 / (1.0 + exp(-activation))

################## HÀM KÍCH HOẠT - RELU
    def relu (self, value_node):
        return max(0, value_node)

################## HÀM KÍCH HOẠT - RELU
    def leakyRelu (self, value_node):
        if (value_node<0):
            return 0.1*value_node
        return 0.2*value_node

################## TÍNH OUTPUTS CỦA NODE
    def forward_calculation_node (self, weights, inputs, select_activate):
        # TÍNH OUTPUTS NODE
        value_node = weights[-1]
        for i in range(len(inputs)):
            value_node += weights[i]*inputs[i]
            if not (value_node<np.finfo(np.double).max):
                print("OUT_VALUE")
                print(weights[i], inputs[i])
                print(weights)
                weights.save_net(weights, "ERROR_NET")
                sys.exit()
        # TÍNH OUTPUT KHI QUA ACTIVE
        if (select_activate=="sigmoid"):
            return self.sigmoid(value_node)
        if (select_activate=="leakyRelu"):
            return self.leakyRelu(value_node)
        elif(select_activate=="relu"):
            return self.relu(value_node)
        elif("linear"):
            return value_node

################## TÍNH FORWARD
    def forward (self, inputs):
        outputs = [inputs]
        out_layer = inputs
        
        for layer in self.network[:-1]: ## TRỪ RA LAST LAYER
            next_layer = []
            
            for node in layer:
                # value_node = self.forward_calculation_node (node, out_layer, "relu")
                value_node = self.forward_calculation_node (node, out_layer, "leakyRelu")
                next_layer.append(value_node)
            
            outputs.append(next_layer)
            out_layer = next_layer
        
        next_layer = []
        for node in self.network[-1]: ## LAST LAYER, dùng LINEAR -> ko xài activate
            value_node = self.forward_calculation_node (node, out_layer, "linear")
            next_layer.append(value_node)
            
        outputs.append(next_layer)
        out_layer = next_layer
        return outputs

##-----------------------------------------------------------------------------------------------------------------------------##
##-------------------------------PHẦN TÍNH BACKWARD----------------------------------------------------------------------------##
##-----------------------------------------------------------------------------------------------------------------------------##

################## NGUYÊN HÀM CỦA SIGMOID
    def back_sigmoid(self, value_node):
        return value_node * (1.0 - value_node)

################## NGUYÊN HÀM CỦA RELU
    def back_relu (self, value_node):
        back_value = 0
        if (value_node>0):
            back_value = 1
        return back_value

################## NGUYÊN HÀM CỦA RELU
    def back_leakyRelu (self, value_node):
        back_value = 0.1
        if (value_node>0):
            back_value = 0.2
        return back_value

################## BACK-ACTIVE 
    def deactivate (self, value_node, select_back_active):
        if (select_back_active=="sigmoid"):
            return self.back_sigmoid(value_node)
        if (select_back_active=="leakyRelu"):
            return self.back_leakyRelu(value_node)
        elif(select_back_active=="relu"):
            return self.back_relu(value_node)
        elif(select_back_active=="linear"):
            return 1

################## TÍNH ERROR - BACKWARD
    def backward (self, outputs, expected):
        Err = [[0 for y in range(len(outputs[x]))] for x in range(len(outputs))] ## LẤY SIZE CỦA NEURON
        # E   = [[0 for y in range(len(outputs[x]))] for x in range(len(outputs))]

        for i in reversed(range(len(outputs))):
            layer = outputs[i]
            errors = list()

            if i == len(outputs)-1: 
                for j in range(len(layer)):
                    ## GRADIENT CỦA LOSS FUNCTION (Y-Out) hay (Predict-Expected)
                    errors.append((expected[j]-layer[j]))
            ## NOT LAST LAYER
            else: 
                for j in range(len(layer)):
                    error = 0.0
                    for pos_weight in range(len(self.network[i+1])):
                        error += self.network[i+1][pos_weight][j] * Err[i+1][pos_weight]
                        ## TÍNH TỔNG TRÊN TẤT CẢ CÁC WEIGHT TRỞ NGƯỢC
                    errors.append(error)
            # print("ERROR", errors)
            # CALCULATION Err
            for j in range(len(layer)):
                ## LINEAR CHO LAST LAYER
                if i != len(outputs)-1: 
                    # print("NONE", deactivate(layer[j], "relu"))
                    Err[i][j] = errors[j]*self.deactivate(layer[j], "leakyRelu")
                    # Err[i][j] = errors[j]*self.deactivate(layer[j], "relu") # VOI SIGMOID THI TRONG HAM SU DUNG LA LAYER[j]
                    # E[i][j]   = errors[j]
                else:
                ## RELU CHO CÁC LAYER CÒN LẠI
                    # print("LAST", layer[j], deactivate(layer[j], "linear"))
                    Err[i][j] = errors[j]*self.deactivate(layer[j], "linear")
                    # E[i][j]   = errors[j]
            # print("ERROR-R", Err)
        return Err

################## TÍNH DELTA - BACKWARD
### DÙNG CLIP ĐỂ NORMALIZE CHO GRADIENT TRÁNH BỊ EXPLODING GRADIENT (overflow-underflow: giá trị weight đạt inf hoặc ~0)
    def clip_gradient(self, gradient_delta, min_g, max_g):
        # print("------------------------GD",gradient_delta)
        for i in range(len(gradient_delta)):
            if (gradient_delta[i]>max_g):
                gradient_delta[i] = max_g
            if (gradient_delta[i]<min_g):
                gradient_delta[i] = min_g
        return 

    def cal_delta(self, outputs, error):
        delta = [[[0 for z in range(len(self.network[x][y]))] for y in range(len(self.network[x]))] for x in range(len(self.network))]

        for _ in range(len(self.network)):        
            for j in range(len(error[_])):            
                for i in range(len(outputs[_])):                         
                    delta[_][j][i] = outputs[_][i]*error[_][j]
                delta[_][j][-1] = error[_][j]
        return delta

##-----------------------------------------------------------------------------------------------------------------------------##
##-------------------------------CẬP NHẬT MẠNG---------------------------------------------------------------------------------##
##-----------------------------------------------------------------------------------------------------------------------------##

################## CỘNG MẠNG DELTA
    def add(self, delta_base, delta_add, command):
        if (command=="None"):
            return delta_base
        else:
            for i in range(len(delta_base)):
                for j in range(len(delta_base[i])):
                    for k in range(len(delta_base[i][j])):
                        delta_base[i][j][k] += delta_add[i][j][k]
        return delta_base

################## CHIA MẠNG DELTA
    def div(self, delta, batch_size):
        for i in range(len(delta)):
            for j in range(len(delta[i])): 
                for k in range(len(delta[i][j])):
                    delta[i][j][k] = delta[i][j][k]/batch_size
        return delta

################## HÀM CẬP NHẬT MẠNG
    def update_weights(self, delta, learning_rate):
        for i in range(len(self.network)):
            for j in range(len(self.network[i])):
                for k in range(len(self.network[i][j])):
                    self.network[i][j][k] = self.network[i][j][k]*(1-0.01) + learning_rate*delta[i][j][k]
        return self.network

################## TÍNH THEO GRADIENT DESCENT BÌNH THƯỜNG
    def fit(self, X_sample, Y_sample, learning_rate):
        ## CLIPPING

        outputs = self.forward(X_sample)

        errors = self.backward(outputs[1:], Y_sample)

        delta = self.cal_delta(outputs, errors)

        self = self.update_weights(delta, learning_rate)

        return outputs, errors, delta
################## TÍNH THEO MINI-BATCH GRADIENT DESCENT 
    def fit_minibatch(self, X_train, Y_train, batch_size, learning_rate, clipping):
        
        command = "None"
        for count in range(batch_size):
            ## CLIPPING
            min_g = clipping[count][0]
            max_g = clipping[count][1]

            outputs = self.forward(X_train[count])

            errors = self.backward(outputs[1:], Y_train[count])

            delta = self.cal_delta(outputs, errors, min_g, max_g)

            if (command=="None"):
                sum_delta = delta
                command = "Continue"
            else:
                sum_delta = self.add(sum_delta, delta, command)


        sum_delta = self.div(sum_delta, batch_size)

        network = self.update_weights(sum_delta, learning_rate)


##-----------------------------------------------------------------------------------------------------------------------------##
##-------------------------------THEO DÕI MẠNG---------------------------------------------------------------------------------##
##-----------------------------------------------------------------------------------------------------------------------------##

################## XEM TRỌNG SỐ TRONG MẠNG
    def display_weights(self, name):
        for i in range(len(self.network)):
            print("-",name,"- Layer", i+1, ":", "size(", len(self.network[i][0])-1,",", len(self.network[i]),")")
            for neuron in self.network[i]:
                print(np.array(neuron))

    def predict(self, inputs):
        return self.forward(inputs)[-1]

    def save_net(self, file_name):
        text_file = open(file_name, "w+")

        number_layer_weights_network = str(len(self.network))
        text_file.write(number_layer_weights_network + "\n")

        for i in range(len(self.network)):
            text_layer = open(file_name + "_layer_" + str(i+1), "w+")

            number_next_layer_nodes = str(len(self.network[i]))
            number_this_layer_nodes = str(len(self.network[i][0]))
            text_file.write((number_next_layer_nodes) + " " + (number_this_layer_nodes) + "\n")

            for j in range(len(self.network[i])):
                for weights in self.network[i][j]:
                    text_layer.write(str(weights)+"\n")
            
            text_layer.close()

        text_file.close()

    def load_net(self, file_name):
        self.network = []

        text_file = open(file_name, "r")

        number_layer_weights_network = int(text_file.readline())

        for i in range(number_layer_weights_network):
            info = text_file.readline().split()
            number_next_layer_nodes = int(info[0])
            number_this_layer_nodes = int(info[1])

            layer = []

            text_layer = open(file_name + "_layer_" + str(i+1), "r")

            for a in range(number_next_layer_nodes):
                node = []
                for b in range(number_this_layer_nodes):
                    node += [float(text_layer.readline())]
                layer += [node]
            self.network += [layer]
        
        return self

    def copy_net(self, base_net):
        for i in range(len(base_net.network)):
            for j in range(len(base_net.network[i])):
                for k in range(len(base_net.network[i][j])):
                    self.network[i][j][k] = base_net.network[i][j][k]

    def clean_net(self):
        for i in range(len(self.network)):
            for j in range(len(self.network[i])):
                for k in range(len(self.network[i][j])):
                    self.network[i][j][k] = 0

    def compare_net(self, net_one):
        return net_one == self.network

    def soft_update(self, main_net):
        for i in range(len(self.network)):
            for j in range(len(self.network[i])):
                for k in range(len(self.network[i][j])):
                    self.network[i][j][k] = self.network[i][j][k]*0.5 + main_net.network[i][j][k]*0.5

    
#base = ANN([3,4,8,1], "random")
#copy = ANN([3,4,8,1], "zero")

#base.display_weights("BASE")
#copy.display_weights("COPY_OLD")
# base.copy_net(copy)
# copy.display_weights("COPY_NEW")
# base.clean_net()
# base.display_weights("CLEAN-BASE")

# copy.display_weights("COPY_NEW2")


# network = ANN([3,4,8,1], "random")

# print(network.save_net("NET-TEST1"))

# network.display_weights("OLD")

# test_load = ANN()
# test_load = test_load.load_net("NET-TEST1")

# test_load.display_weights("NEW")



# ################### TEST
# network = ANN([4,4,10,10,1], "random")
# # network = [
# # [
# # [-0.8757,  -1.0642,  -0.2612,  0.0125, 0],
# # [-0.4838,  1.6035 , 0.4434  , -3.0292, 0],
# # [-0.7120,  1.2347 , 0.3919  , -0.4570, 0],
# # [-1.1742,  -0.2296,  -1.2507,  1.2424, 0],
# # [-0.1922,  -1.5062,  -0.9480, -1.0667, 0],
# # [-0.2741,  -0.4446,  -0.7411,  0.9337, 0],
# # [1.5301 , -0.1559 , -0.5078 ,  0.3503, 0],
# # [-0.2490,  0.2761 , -0.3206 , -0.0290, 0],
# # ],
# # [
# # [0.0983, 0.0414, -0.7342, -0.0308, 0.2323, 0.4264, -0.3728, -0.2365, 0],
# # [0.0983, 0.0414, -0.7342, -0.0308, 0.2323, 0.4264, -0.3728, -0.2365, 0]
# # ]
# # ]
# ## [weights, bias]


# inputs = [
#         [0, 0, 0, 0],
#         [0, 0, 0, 1],
#         [0, 0, 1, 0],
#         [0, 0, 1, 1],
#         [0, 1, 0, 0],
#         [0, 1, 0, 1],
#         [0, 1, 1, 0],
#         [0, 1, 1, 1],
#         [1, 0, 0, 0],
#         [1, 0, 0, 1],
#         [1, 0, 1, 0],
#         [1, 0, 1, 1],
#         [1, 1, 0, 0],
#         [1, 1, 0, 1],
#         [1, 1, 1, 0],
#         [1, 1, 1, 1],
#         ] 

# # expected = [
# #         [1,0],
# #         [0,1],
# #         [0,1],
# #         [1,0],
# #         [0,1],
# #         [1,0],
# #         [1,0],
# #         [0,1],
# #         [0,1],
# #         [1,0],
# #         [1,0],
# #         [0,1],
# #         [1,0],
# #         [0,1],
# #         [0,1],
# #         [1,0],
# #         ]

# expected = [
#         [0],
#         [1],
#         [2],
#         [3],
#         [4],
#         [5],
#         [6],
#         [7],
#         [8],
#         [9],
#         [10],
#         [11],
#         [12],
#         [13],
#         [14],
#         [15],
#         ]

# network.display_weights("OLD")

# # # x = 11

# # # print("P",predict(network, inputs[x]))
# # # print("o",forward(network, inputs[x]))
# # # print("e",backward(network, forward(network, inputs[x])[1:], expected[x]))
# # # fit_minibatch(network, [inputs[x]], [expected[x]], 1, 1)
# # # print("o(new)",forward(network, inputs[x]))



# for a in range(30000):
#     temp_mem = list(zip(inputs[1:15], expected[1:15]))
#     random.shuffle(temp_mem)
    
#     X, Y = zip(*temp_mem[0:10])
#     clipping = []
#     for i in Y:
#         clipping.append([-1, Y[0][0]])
    
#     network.fit_minibatch(X[0:9], Y[0:9], 9, 0.00025, clipping)

# for x in range(16):
#     print("\n", inputs[x], "PREDICT        :", network.predict(inputs[x]))

# network.display_weights("NEW")

# print("p(new)", network.predict(inputs[x]))


