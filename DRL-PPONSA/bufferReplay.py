# -*- coding: utf-8 -*-
"""
@File     :bufferReplay.py
@Date     : 2022-10-06
@Author   : Terry_Li     --这个世界，从来都要求你去独当一面。
IDE       : PyCharm
@Mail     : terry.ljq.dev@foxmail.com
"""
import random
from collections import deque

import numpy as np


class ReplayBuffer(object):
    """
    经验回放函数
    """

    def __init__(self, capacity):
        self.buffer = deque(maxlen=capacity)

    def push(self, state, action, reward, next_state, done):
        state = np.expand_dims(state, 0)
        next_state = np.expand_dims(next_state, 0)

        self.buffer.append((state, action, reward, next_state, done))

    def sample(self, batch_size):
        state, action, reward, next_state, done = zip(*random.sample(self.buffer, batch_size))
        return np.concatenate(state), action, reward, np.concatenate(next_state), done

    def __len__(self):
        return len(self.buffer)

# =======================================#
#             Buffer Memory             #
# =======================================#
#
# class RolloutBuffer:
#     def __int__(self):
#         self.actions = []
#         self.states = []
#         self.logprobs = []
#         self.rewards = []
#         self.is_terminals = []
#
#     def clear(self):
#         del self.actions[:]
#         del self.states[:]
#         del self.logprobs[:]
#         del self.rewards[:]
#         del self.is_terminals[:]


# if __name__ == "__main__":
#     memory_buffer = MemoryBuffer()
#     # rollout_buffer = RolloutBuffer()
