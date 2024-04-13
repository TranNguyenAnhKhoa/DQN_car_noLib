# from math import 
import os, sys
import pygame
import random
import numpy as np
import CarEnv.GameEnv as GameEnv
import matplotlib.pyplot as plt
sys.path.append('CarEnv')
from collections import deque
from dqn import *
from NeuralNetwork.Neuron_Network import *

####################################################################
IN_NET          = "C:/Users/khoah/Desktop/Car_no_lib_main/NeuralNetwork/NET32_32/NET_32"
OUT_NET_MAIN    = "C:/Users/khoah/Desktop/Car_no_lib_main/NeuralNetwork/NET32_32/MAIN_sgd_not_alpha"
OUT_NET_TARGET  = "C:/Users/khoah/Desktop/Car_no_lib_main/NeuralNetwork/NET32_32/TARGET_sgd_not_alpha"
COUNT_STEPS     = "C:/Users/khoah/Desktop/Car_no_lib_main/NeuralNetwork/NET32_32/y_STEPS_sgd_not_alpha.txt"
################################################################################

# ENV PARAMATER
game = GameEnv.RacingEnv()
game.fps = 60

state_size = 19
action_size = 5

# SETUP PARAM PLOT #######################################################################
x_EPISODES = list()
y_STEPS = list()

ddqn_scores = []
eps_history = []
max_steps_history = []
avg_steps_history = []
maxscore = 0

"""_____________________________INIT NETWORK_____________________________________________________
###################################################################################################
neuron_struct = [4, state_size, 24, 24, action_size]
network = initial(neuron_struct, "random")

    IN_NET          = "C:/Users/khoah/Desktop/Car_no_lib_main/NeuralNetwork/NET32_32/NET_32"
    OUT_NET_MAIN    = "C:/Users/khoah/Desktop/Car_no_lib_main/NeuralNetwork/NET32_32/MAIN_sgd_not_alpha"
    OUT_NET_TARGET  = "C:/Users/khoah/Desktop/Car_no_lib_main/NeuralNetwork/NET32_32/TARGET_sgd_not_alpha"
    COUNT_STEPS     = "C:/Users/khoah/Desktop/Car_no_lib_main/NeuralNetwork/NET32_32/y_STEPS_sgd_not_alpha.txt"
###################################################################################################
"""
#___________ PARAMETER DEEP Q LEARNING______________________________
############# CYCLE SYNC NET ##############
count_cycle = np.float32(0)
cycle_sync = np.float32(50)
sync_info = [count_cycle, cycle_sync]

############### MEMORY ####
size_memory = 25000
current_size = np.float32(0)
start_value_to_train = np.float32(256)  # 1000)
is_train = 0
memory = deque(maxlen=size_memory)
memory_info = [size_memory, current_size, start_value_to_train, is_train]

########### SET EPSILON #####
TOTAL_GAMETIME = 100000
EPISODES = 5000
#--------- epsilon information -----------
epsilon = np.float32(1)
epsilon_min = np.float32(0.05)
epsilon_decay = np.float32(0.995)
epsilon_info = [epsilon, epsilon_min, epsilon_decay]

####### SET NET #############
batch_size = 256
""""Changing learning rate"""
# alpha_init = np.float32(0.005) # high
alpha_init = np.float32(0.0005)  # learning rate

################ SET CAL Q VALUE...
gamma = np.float32(0.99)  # độ chiết khấu
thresh_stop = np.float32(5)
#################################################################################
#------------
neuron_struct = [3, state_size, 24, 24, action_size]
network = initial(neuron_struct, "random")

current_net = load_net(IN_NET)
# current_net = load_net("BASE")
target_net = load_net(IN_NET)
#____copy network__________
copy_net(current_net, target_net)

#____________________
##########################################
alpha = np.float32(alpha_init)
reward5 = [np.float32(0), np.float32(0), np.float32(0), np.float32(0), np.float32(0)]

for ep in range(EPISODES):
    # set paramater game
    game.reset()
    done = False
    step = 0
    re_learn = 0
    score = 0
    couter = 0
    state_, reward, done = game.step(0)
    state = np.array(state_)
    gtime = 0  # set game time back to 0
    
    renderFlag = True
    while not done:
        ## HIỂN THỊ LÊN SIMULATION TERMINAL
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
                
        random_value = np.float32(random.random())
        action, ran = get_action(current_net, random_value, epsilon_info, list(state))

        next_state, reward, done = game.step(action)
        next_state = np.array(next_state)
        # next_state_ = []
        #
        # for item in range(len(next_state)):
        #     next_state_ = [[item] for item in next_state]
        # next_state_ = list(zip(*next_state_))
        score += reward
        if reward == 0:
            counter += 1
            if counter > 100:
                done = True
        else:
            counter = 0

        done = np.float32(done)
        
        ## pack ~ [state, action, reward, next_state, done]

        ## SET REWARD
        # if not done or step == env._max_episode_steps - 1:  ## (env._max_episode_steps = 500)
        #     reward = np.float32(reward)
        # else:
        #     reward = np.float32(-100)
        ## LƯU PACK VÀO RELAY MEMORY

        # print(state, type(state[0]))
        # print(next_state, type(next_state[0]))
        # print(reward, type(reward))
        #print('next state ',next_state)
        
        pack = [list(state), action, reward, list(next_state), done]
        store_relay_memory(memory, memory_info, epsilon_info, pack)
        gtime += 1

        if gtime >= TOTAL_GAMETIME:
                done = True

        state = next_state
        step += 1
        if renderFlag:
            game.render(action)

        if done:
            ## LƯU CÁC GIÁ TRỊ ĐỂ BIỂU THỊ TRỰC QUAN
            if (epsilon_info[1] < epsilon_info[0]):
                epsilon_info[0] = epsilon_info[0] * epsilon_info[2]
            x_EPISODES.append(ep + 1)
            y_STEPS.append(step)

            reward5[ep % 5] = np.float32(score)
            avg_reward5 = np.float32(sum(reward5)) / np.float32(5)

            """""""""""""""Changing learning rate"""""""""""""""
            # alpha = np.float32(alpha_init) - (avg_reward5-np.float32(1))*alpha_init/np.float32(200)
            # if alpha < 0.001:
            #     alpha = 0.001
            alpha = alpha_init

            print("Episode: {}/{}, score: {}, ep: {:.4}, alpha: {}".format(ep, EPISODES, score, epsilon_info[0], alpha))
            # if thresh_stop == 5:
            #     save_net(target_net, "my_DQN_sgd")
            #     return
            reinforce_learn_two_net(current_net, target_net, sync_info, memory, memory_info, batch_size, gamma,
                                        alpha, pack)

            # x = input("Wait Key: ")
            # save_net(target_net, "/home/kocodonut/Desktop/KLTN_HDL/NET/NET_NEW_32B_ver6/TARGET_sgd")
            # save_net(current_net, "/home/kocodonut/Desktop/KLTN_HDL/NET/NET_NEW_32B_ver6/MAIN_sgd")

        if (re_learn == 0):
            save_net(target_net, "TARGET_sgd")
            save_net(current_net, "MAIN_sgd")
            # input("Press Enter to continue...")
            re_learn = 0
        else:
            re_learn += 1
    eps_history.append(ep)
    ddqn_scores.append(score)
    max_steps_history.append(score)
    avg_score = np.mean(ddqn_scores[max(0, ep - 100):(ep + 1)])
    if len(max_steps_history) >= 100:
        avg_steps = np.mean(max_steps_history[-100:])
        avg_steps_history.append(avg_steps)
      
    # Vẽ biểu đồ sau mỗi episode
    if ep >= 100 :
        plt.plot(eps_history[100:], avg_steps_history[1:], label='Avg step', linestyle='--')
        plt.plot(eps_history, avg_score, marker='o', linestyle='-')

    if (ep%100==0):
        plt.title("BIỂU ĐỒ REWARD ĐẠT ĐƯỢC TRÊN MỖI 100 EPISODE")
        plt.plot(eps_history, ddqn_scores)
        plt.xlabel('Episode')
        plt.ylabel('Reward')
        plt.legend(['Reward','Avg_step'])
        plt.grid(True)
        plt.pause(0.05)  # Tạo độ trễ ngắn để cập nhật biểu đồ
        plt.savefig('training_step.png')

