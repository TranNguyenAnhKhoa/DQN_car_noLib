from numpy import save
import os 
from keras import metrics, optimizers
from keras.models import Model, load_model
from keras.layers import Input, Dense
from keras.optimizers import Adam, RMSprop, SGD


def OurModel(input_shape, size_hidden, action_space):
    X_input = Input(input_shape)

    X = Dense(size_hidden[0], activation='relu', kernel_initializer='he_uniform')(X_input)

    X = Dense(size_hidden[1], activation='relu', kernel_initializer='he_uniform')(X)

    # X = Dense(32, activation='relu', kernel_initializer='he_uniform')(X)

    X = Dense(action_space, activation='linear', kernel_initializer='he_uniform')(X)

    model = Model(inputs=X_input, outputs=X, name='RacingCar')
    model.compile(loss='mse', optimizer=SGD(lr=1), metrics=["accuracy"])
## RMSprop(lr=0.00025, rho=0.95, epsilon=0.01)
    model.summary()
    return model

def save_random_keras(net, name = "NET_32"):
    num_layer = int(len(net)/2)

    dir = os.path.dirname(__file__)
    net_info = open(dir + "/" + name, "w+")
    print(dir)
    net_info.write(str(num_layer) + "\n")

    for i in range(num_layer):
        net_info.write(str(len(net[i*2][0])) + " " + str(len(net[i*2])+1) + "\n")
        
        layer = open(dir + "/" + name + "_layer_" + str(i+1), "w+")
        for num_node in range(len(net[i*2][0])):
        
            for num_value in range(len(net[i*2])):
                layer.write(str(net[i*2][num_value][num_node]) + "\n")
        
            layer.write(str(net[i*2+1][num_node]) + "\n")
        
        layer.close()
    return 

''' SET SIZE HIDDEN LAYER'''
size_hidden = [32,32]

X = OurModel(19, size_hidden, 5)
save_random_keras(X.get_weights(), "NET_32")

# print(X.predict([[1,2,3,4]]))
# for _ in range(10):
#     X.fit([[1,2,3,4]], [[8,8]])
#     print(X.predict([[1,2,3,4]]))
