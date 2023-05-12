# -*- coding: utf-8 -*-
"""
@File     : dataSet.py
@Date     : 2022-10-18
@Author   : Terry_Li  --ye。
IDE       : PyCharm
@Mail     : terry.ljq.dev@foxmail.com
"""
# 是否使用GPU进行加速
import torch


def gpu():
    """
    GPU加速指令
    :return:
    """
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')  # 检查是否可用GPU进行加速
    return device
