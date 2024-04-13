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
## command: lệnh để khởi tạo
def initial(neuron_struct, command):
    network = []
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
        network.append(layer)

    return network

##-----------------------------------------------------------------------------------------------------------------------------##
##-------------------------------PHẦN TÍNH FORWARD-----------------------------------------------------------------------------##
##-----------------------------------------------------------------------------------------------------------------------------##

################## HÀM KÍCH HOẠT - SIGMOID
def sigmoid(activation):
	return np.float32(1.0) / (np.float32(1.0) + exp(-activation))

################## HÀM KÍCH HOẠT - RELU
def relu (value_node):
    return max(np.float32(0), value_node)

################## HÀM KÍCH HOẠT - LEAKY RELU -> C = 0.1
def leakyRelu (value_node):
    if (value_node<0):
        return np.float32(0.1)*value_node
    return np.float32(0.2)*value_node

################## TÍNH OUTPUTS CỦA NODE
def forward_calculation_node (weights, inputs, select_activate):
    # TÍNH OUTPUTS NODE
    value_node = weights[-1]
    # print(len(inputs))
    for i in range(len(inputs)):
        value_node += weights[i]*np.float32(inputs[i])
        # print("+", weights[i]*np.float32(inputs[i]))
        ## CHECK VALUE NODE FOR FIXED POINT
        if (value_node>2**9):
            print("OVER_FLOW_HIGH", value_node)
        elif (value_node>-2**-24 and value_node<2**-24 and value_node!=0):
            print("OVER_FLOW_LOW", value_node)
            
        ## CEHCK OVER FLOW NaN
        if not (value_node<np.finfo(np.double).max):
            print("OUT_VALUE")
            print(weights[i], inputs[i])
            print(weights)
            save_net(weights, "ERROR_NET")
            sys.exit()
    # print("Value Node: ", value_node)
        ## END CHECK
    # TÍNH OUTPUT KHI QUA ACTIVE
    if (select_activate=="sigmoid"):
        return value_node, sigmoid(value_node)
    elif(select_activate=="relu"):
        return value_node, relu(value_node)
    elif(select_activate=="leakyRelu"):
        return value_node, leakyRelu(value_node)
    elif(select_activate=="linear"):
        return value_node, value_node

################## TÍNH FORWARD
def forward (network, inputs):
    outputs = [[np.float32(i) for i in inputs]]
    out_layer = inputs
    
    for layer in network[:-1]: ## TRỪ RA LAST LAYER
        next_layer = []
        
        for node in layer:
            # _, value_node = forward_calculation_node (node, out_layer, "relu")
            _, value_node = forward_calculation_node (node, out_layer, "leakyRelu")
            # _, value_node = forward_calculation_node (node, out_layer, "sigmoid")
            next_layer.append(value_node)
        
        outputs.append(next_layer)
        out_layer = next_layer
    
    next_layer = []
    for node in network[-1]: ## LAST LAYER, dùng LINEAR -> ko xài activate
        _, value_node = forward_calculation_node (node, out_layer, "linear")
        next_layer.append(value_node)
        
    outputs.append(next_layer)
    out_layer = next_layer
    return outputs

##-----------------------------------------------------------------------------------------------------------------------------##
##-------------------------------PHẦN TÍNH BACKWARD----------------------------------------------------------------------------##
##-----------------------------------------------------------------------------------------------------------------------------##

################## NGUYÊN HÀM CỦA SIGMOID
def back_sigmoid(value_node):
	return value_node * (np.float32(1.0) - value_node)

################## NGUYÊN HÀM CỦA RELU
def back_relu (value_node):
    back_value = 0
    if (value_node>0):
        back_value = 1
    return np.float32(back_value)
################## NGUYÊN HÀM CỦA LEAKY_RELU -> C = 0.1
def back_leakyRelu (value_node):
    back_value = 0.1
    if (value_node>0):
        back_value = 0.2
    return np.float32(back_value)

################## BACK-ACTIVE 
def deactivate (value_node, select_back_active):
    if (select_back_active=="sigmoid"):
        return back_sigmoid(value_node)
    elif(select_back_active=="relu"):
        return back_relu(value_node)
    elif(select_back_active=="leakyRelu"):
        return back_leakyRelu(value_node)
    elif(select_back_active=="linear"):
        return np.float32(1)

################## TÍNH ERROR - BACKWARD
def backward (network, outputs, expected):
    Err = [[np.float32(0) for y in range(len(outputs[x]))] for x in range(len(outputs))] ## LẤY SIZE CỦA NEURON
    # E   = [[0 for y in range(len(outputs[x]))] for x in range(len(outputs))]

    for i in reversed(range(len(outputs))):
        layer = outputs[i]
        errors = list()

        if i == len(outputs)-1: 
            for j in range(len(layer)):
                ## GRADIENT CỦA LOSS FUNCTION (Y-Out) hay (Predict-Expected)
                errors.append((np.float32(expected[j])-layer[j]))
        ## NOT LAST LAYER
        else: 
            for j in range(len(layer)):
                error = np.float32(0.0)
                for pos_weight in range(len(network[i+1])):
                    error += network[i+1][pos_weight][j] * Err[i+1][pos_weight]
                    ## TÍNH TỔNG TRÊN TẤT CẢ CÁC WEIGHT TRỞ NGƯỢC
                errors.append(error)
        # print("ERROR", errors)
        # CALCULATION Err
        for j in range(len(layer)):
            ## LINEAR CHO LAST LAYER
            if i != len(outputs)-1: 
                # print("NONE", deactivate(layer[j], "relu"))
                # Err[i][j] = errors[j]*deactivate(layer[j], "relu")
                Err[i][j] = errors[j]*deactivate(layer[j], "leakyRelu")
                # Err[i][j] = errors[j]*deactivate(layer[j], "sigmoid")
                # E[i][j]   = errors[j]
            else:
            ## RELU CHO CÁC LAYER CÒN LẠI
                # print("LAST", layer[j], deactivate(layer[j], "linear"))
                Err[i][j] = errors[j]*deactivate(layer[j], "linear")
                # E[i][j]   = errors[j]
        # print("ERROR-R", Err)
    return Err

################## TÍNH DELTA - BACKWARD
### DÙNG CLIP ĐỂ NORMALIZE CHO GRADIENT TRÁNH BỊ EXPLODING GRADIENT (overflow-underflow: giá trị weight đạt inf hoặc ~0)
def clip_gradient(gradient_delta, min_g, max_g):
    # print("------------------------GD",gradient_delta)
    for i in range(len(gradient_delta)):
        if (gradient_delta[i] > max_g):
            gradient_delta[i] = max_g
        if (gradient_delta[i] < min_g):
            gradient_delta[i] = min_g
    return 

def cal_delta(network, outputs, error):#, min_g, max_g):
    delta = [[[np.float32(0) for z in range(len(network[x][y]))] for y in range(len(network[x]))] for x in range(len(network))]

    for _ in range(len(network)):        
        for j in range(len(error[_])):            
            for i in range(len(outputs[_])):                         
                delta[_][j][i] = outputs[_][i]*error[_][j]
            delta[_][j][-1] = error[_][j]
            # ## CLIPPING
            # clip_gradient(delta[_][j], min_g, max_g)

    return delta

##-----------------------------------------------------------------------------------------------------------------------------##
##-------------------------------CẬP NHẬT MẠNG---------------------------------------------------------------------------------##
##-----------------------------------------------------------------------------------------------------------------------------##

################## CỘNG MẠNG DELTA
def add(delta_base, delta_add, command):
    if (command=="None"):
        return delta_base
    else:
        for i in range(len(delta_base)):
            for j in range(len(delta_base[i])):
                for k in range(len(delta_base[i][j])):
                    delta_base[i][j][k] += delta_add[i][j][k]
    return delta_base

################## CHIA MẠNG DELTA
def div(delta, batch_size):
    for i in range(len(delta)):
        for j in range(len(delta[i])): 
            for k in range(len(delta[i][j])):
                delta[i][j][k] = delta[i][j][k]/batch_size
    return delta

################## HÀM CẬP NHẬT MẠNG
def update_weights(network, delta, learning_rate):
    for i in range(len(network)):
        for j in range(len(network[i])):
            for k in range(len(network[i][j])):
                network[i][j][k] = network[i][j][k] + learning_rate*delta[i][j][k] # 2**(-6)
    return network

################## TÍNH THEO GRADIENT DESCENT BÌNH THƯỜNG
def fit(network, X_sample, Y_sample, learning_rate):#, clipping):
    # ## CLIPPING
    # min_g = clipping[0]
    # max_g = clipping[1]

    outputs = forward(network, X_sample)

    errors = backward(network, outputs[1:], Y_sample)

    delta = cal_delta(network, outputs, errors)#, min_g, max_g)

    network = update_weights(network, delta, learning_rate)

    return outputs, errors, delta
    # spectral_normal(network)

################## TÍNH THEO MINI-BATCH GRADIENT DESCENT 
def fit_minibatch(network, X_train, Y_train, batch_size, learning_rate):
    
    command = "None"
    for count in range(batch_size):
        # ## CLIPPING
        # min_g = clipping[count][0]
        # max_g = clipping[count][1]

        outputs = forward(network, X_train[count])

        errors = backward(network, outputs[1:], Y_train[count])

        delta = cal_delta(network, outputs, errors)#, min_g, max_g)

        if (command=="None"):
            sum_delta = delta
            command = "Continue"
        else:
            sum_delta = add(sum_delta, delta, command)


    sum_delta = div(sum_delta, batch_size)

    network = update_weights(network, sum_delta, learning_rate)


##-----------------------------------------------------------------------------------------------------------------------------##
##-------------------------------THEO DÕI MẠNG---------------------------------------------------------------------------------##
##-----------------------------------------------------------------------------------------------------------------------------##

################## XEM TRỌNG SỐ TRONG MẠNG
def display_weights(network, name):
    for i in range(len(network)):
        print("-",name,"- Layer", i+1, ":", "size(", len(network[i][0])-1,",", len(network[i]),")")
        for neuron in network[i]:
            print(np.array(neuron))

def predict(network, inputs):
    return forward(network, inputs)[-1]

def save_net(network, file_name):
    text_file = open(file_name, "w+")

    number_layer_weights_network = str(len(network))
    text_file.write(number_layer_weights_network + "\n")

    for i in range(len(network)):
        text_layer = open(file_name + "_layer_" + str(i+1), "w+")

        number_next_layer_nodes = str(len(network[i]))
        number_this_layer_nodes = str(len(network[i][0]))
        text_file.write((number_next_layer_nodes) + " " + (number_this_layer_nodes) + "\n")

        for j in range(len(network[i])):
            for weights in network[i][j]:
                text_layer.write(str(weights)+"\n")
        
        text_layer.close()

    text_file.close()

def load_net(file_name):
    network = []

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
                node += [np.float32(text_layer.readline())]
            layer += [node]
        network += [layer]
    
    return network

def copy_net(base_net, cop_net):
    for i in range(len(base_net)):
        for j in range(len(base_net[i])):
            for k in range(len(base_net[i][j])):
                cop_net[i][j][k] = base_net[i][j][k]

def clean_net(net):
    for i in range(len(net)):
        for j in range(len(net[i])):
            for k in range(len(net[i][j])):
                net[i][j][k] = 0

def compare_net(net_one, net_two):
    return net_one == net_two

################## OPTIMIZE NETWORK

def soft_update(base_net, cop_net):
    for i in range(len(base_net)):
        for j in range(len(base_net[i])):
            for k in range(len(base_net[i][j])):
                cop_net[i][j][k] = cop_net[i][j][k]*np.float32(0.5) + base_net[i][j][k]*np.float32(0.5)

# def spectral_normal(net):
#     M = net[0][0][0]
#     for i in range(len(net)-1):
#         for j in range(len(net[i])):
#             for k in range(len(net[i][j])):
#                 M = max(M, net[i][j][k])

#     for i in range(len(net)-1):
#         for j in range(len(net[i])):
#             for k in range(len(net[i][j])):
#                 net[i][j][k] = net[i][j][k]/M
#     return 
