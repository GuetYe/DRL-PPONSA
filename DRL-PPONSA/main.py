# -*- coding: utf-8 -*-
"""
@File     : train.py
@Date     : 2022-10-13
@Author   : Terry_Li     --古有曳影之剑，腾空而舒，克伐四方，历史我的源代码。
IDE       : PyCharm
@Mail     : terry.ljq.dev@foxmail.com
"""
import torch

import utils
from train_model import *
from utils import *
from env import UnicastEnv
from collections import namedtuple

# 打印环境的状态空间和动作空间
print('State Dimensions :', config.STATE_NUM)
print('Action Dimensions :', config.ACTION_NUM)

render = True
seed = 1
torch.manual_seed(seed)
Transition = namedtuple('Transition', ['state', 'action', 'a_log_prob', 'reward', 'next_state'])


def main():
    agent = PPO()
    episode_reward = []
    episode = []
    step_num = []
    picture_path, experimental_data_path = utils.create_picture_path()
    for i_epoch in range(1000):
        env = UnicastEnv(config.dataset.graph)
        for index, pkl_path in enumerate(config.dataset.pickle_file_path_yield()):
            env.read_pickle_and_modify(pkl_path)  # 将pkl_graph的值覆盖graph
            for src, dst in config.START_END:
                state = env.reset(src, dst)  # 获取当前的状态信息
                state = utils.combine_state(state)
                reward_temp = 0
                while True:
                    action, action_prob = agent.select_action(state)
                    action_node = utils.index_to_node(action)  # 将动作转成节点
                    # print("agent_index----->", agent_index)
                    next_state, reward, done, info = env.step(action_node, state)
                    trans = Transition(state, action, action_prob, reward, next_state)
                    agent.store_transition(trans)
                    reward_temp += reward

                    if done:
                        if len(agent.buffer) >= agent.batch_size: agent.update(i_epoch)
                        agent.writer.add_scalar('liveTime/livestep', i_epoch, global_step=i_epoch)
                        break
                    state = next_state
                step_num.append(info.get("step_num"))
                episode_reward.append(reward_temp)
                episode.append(i_epoch)
                print(index)
                print(info)
                print(reward_temp)
                print("\n")
    utils.save_experimental_data(episode, experimental_data_path, "episode")
    utils.save_experimental_data(episode_reward, experimental_data_path, "episode_reward")
    utils.save_experimental_data(step_num, experimental_data_path, "step_num")
    utils.plot_episode_data(picture_path, episode, episode_reward, "episode", "episode_reward", "episode_reward")
    utils.plot_episode_data(picture_path, episode, step_num, "episode", "step_num", "step_num")


if __name__ == '__main__':
    main()
    print("training over")
