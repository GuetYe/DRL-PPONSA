# -*- coding: utf-8 -*-
"""
@File     : utils.py
@Date     : 2022-10-08
@Author   : Terry_Li     --长歌当哭为君仗剑弑天下。
IDE       : PyCharm
@Mail     : terry.ljq.dev@foxmail.com
"""

import numpy as np
from matplotlib import pyplot as plt


class OrnsteinUhlenbeckActionNoise:

    def __init__(self, action_dim, mu=0, theta=0.15, sigma=0.2):
        self.action_dim = action_dim
        self.mu = mu
        self.theta = theta
        self.sigma = sigma
        self.X = np.ones(self.action_dim) * self.mu

    def reset(self):
        self.X = np.ones(self.action_dim) * self.mu

    def sample(self):
        dx = self.theta * (self.mu - self.X)
        dx = dx + self.sigma * np.random.randn(len(self.X))
        self.X = self.X + dx
        return self.X


if __name__ == "__main__":
    ou = OrnsteinUhlenbeckActionNoise(1)
    states = []
    for i in range(1000):
        states.append(ou.sample())
    plt.plot(states)
    plt.show()
