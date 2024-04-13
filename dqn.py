import random
import numpy as np
from NeuralNetwork.Neuron_Network import *

"""_summary_
epsilon_info = [epsilon, epsilon_min, epsilon_decay]
memory_info = [size_memory, current_size, start_value_to_train, is_train]
"""
def store_relay_memory(memory, memory_info, epsilon_info, pack):
    size_memory = memory_info[0]
    current_size = memory_info[1]
    start_value_to_train = memory_info[2]
    # is_train = memory_info[3]

    # epsilon = epsilon_info[0]
    # epsilon_min = epsilon_info[1]
    # epsilon_decay = epsilon_info[2]

    memory.append(pack)
    if (current_size != size_memory - 1):
        memory_info[1] = (current_size + 1) % size_memory

    if (current_size >= start_value_to_train - 1):
        memory_info[3] = 1

    ## EPSILON DECAY
    if (epsilon_info[1]<epsilon_info[0]):
        epsilon_info[0] -= epsilon_info[2]
    #     epsilon_info[0] = epsilon_info[0]*epsilon_info[2]

    return memory

####------------------ SELECT ACTION
def get_action(network, random_value, epsilon_info, state):
    value_all_action = predict(network, state)

    ran = 1

    epsilon = epsilon_info[0]
    if (random_value < epsilon):
        act = random.randrange(len(value_all_action))
        # print("RANDOM", act)
        # return act #random.randrange(len(value_all_action))
    else:
        act = value_all_action.index(max(value_all_action))
        ran = 0
        # print("CHOOSE", act)
        # return act #value_all_action.index(max(value_all_action))
    return act, ran

def reinforce_learn_two_net(current_net, target_net, sync_info, memory, memory_info, batch_size, gamma, alpha, last_pack):

    # size_memory = memory_info[0]
    current_size = memory_info[1]
    # start_value_to_train = memory_info[2]    
    is_train = memory_info[3]

    count_cycle = sync_info[0]
    cycle_sync = sync_info[1]

    if (is_train==0):
        return
    # print("TRAIN")
    
    ## TẠO MINI_BATCH
    mini_batch = random.sample(memory, batch_size)

    """Addition""""""""""""""""""""last pack"""""""""""""""
    mini_batch[0] = last_pack
    ################################################



    # mini_batch = []
    # for i in range(batch_size):
    #     mini_batch.append(memory[i])

    # memory_info[1] = current_size-batch_size

    memory_info[1] = current_size-batch_size
    ## mini_bach ~ [state, action, reward, next_state, done]

    state_current = []
    Q_current = []
    Q_next    = []
    Q_target  = []
    
    clipping = []
    ## NƠI SỬ DỤNG MẠNG NƠ RON

    # count_done = 0
    # update = ""
    for i in range(batch_size):
        state_current.append(mini_batch[i][0])
        # print(mini_batch[i][0])
        Q_current.append (predict(current_net, mini_batch[i][0]))
        # print(type(Q_current[0][0]))
        Q_next.append (predict(target_net, mini_batch[i][3]))
        # print(type(Q_next[0][0]))

        Q_target.append (predict(current_net, mini_batch[i][0]))
        # print(type(Q_target[0][0]))

        # print(i, "Q(old)   :", Q_value[i])
        # print("Q_next   :", Q_value_next[i])
        ## TÍNH Q-VALUE
        if mini_batch[i][4]:

            # count_done += 1
            # if (mini_batch[i][2]==-100):
            #     update += "-"
            # else:
            #     update += "+"
            if (mini_batch[i][2]<0):
                Q_target[i][mini_batch[i][1]] = np.float32(mini_batch[i][2])
            else:
                Q_target[i][mini_batch[i][1]] = np.float32(mini_batch[i][2]) + np.float32(gamma)*np.float32(max(Q_next[i]))

        else:
            # update += "O"
            Q_target[i][mini_batch[i][1]] = np.float32(mini_batch[i][2]) + np.float32(gamma)*np.float32(max(Q_next[i]))
        clipping.append([-1000, Q_target[i][mini_batch[i][1]]])
    
    
    # print(update, count_done)

    ## MINI BATCH FIT HERE
    # fit_minibatch(current_net, state_current, Q_target, batch_size, alpha)
    for i in range(batch_size):
        fit(current_net, state_current[i], Q_target[i], alpha)#, clipping[i])

    # fit_minibatch(current_net, state_current, Q_target, batch_size, alpha, clipping)

    # count = 0
    # for i in update:
    #     if(i=="-"):
    #         print("Q:", Q_current[count], "T", Q_target[count], "N:", predict(current_net, state_current[count]))
    #     count += 1
    # P = []
    # for i in range(len(Q_current)):
    #     P.append(predict(current_net, state_current[i]))
    #     print(i, "R:", mini_batch[i][2], "Q(old)   :", Q_current[i], "Q_next   :", Q_next[i], "Q(target)    :", Q_target[i],"Q(new)   :", P[i])
    
    # print("COUNT_CYCLE", sync_info[0])
    if (count_cycle==cycle_sync-1):
        # print("COMPARE(B): ", compare_net(current_net, target_net))
        soft_update(current_net, target_net)
        print("TARGET-COPY...")
        # print("COMPARE(A): ", compare_net(current_net, target_net))
        # print("COPIED!!!")
    
    sync_info[0] = (sync_info[0]+1)%sync_info[1]
    return
 