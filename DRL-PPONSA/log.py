# 训练日志函数
# -*- coding: utf-8 -*-
"""
@File     : log.py
@Date     : 2022-10-15
@Author   : Terry_Li   -- 你我皆为过客，逝者亦是归人。
IDE       : PyCharm
@Mail     : terry.ljq.dev@foxmail.com
"""
import logging
import time
import os
from pathlib import Path


class NyLog:
    """
    日志记录
    mylog = Mylog()
    logger = mylog.logger
    logger.info()
    logger.warning()
    """

    def __init__(self, path: Path, file_save=False, console_print=True, name=None):
        """
        log
        :param path: 运行日志的当前文件Path(__file__)
        :param file_save: 是否存储日志
        :param console_print: 是否打印到终端
        """
        self.formatter = logging.Formatter(
            f"{name}: %(message)s")  # 打印日期格式logging.getLogger()
        self.logger = logging.getLogger(name=__name__)  # 创建日志对象，获得logger
        # self.set_log_level()
        self.log_path = Path.joinpath(path.parent, 'Logs')
        if name is None:
            self.log_file = os.path.join(self.log_path,
                                         path.stem + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()))
        else:
            self.log_file = os.path.join(self.log_path, path.stem + name)
            # self.mk_log_dir()

        # log_path = os.path.join(os.getcwd(), 'Logs')

        if file_save:
            self.file_handler()

        if console_print:
            self.console_handler()

    def set_log_level(self, level=logging.DEBUG):
        """
        设置日志等级
        :param level: 日志的等级
        :return:
        """
        self.logger.setLevel(level)

    def mk_log_dir(self):
        try:
            # os.mkdir(log_path)
            Path.mkdir(self.log_path)
        except FileExistsError:
            for child in self.log_path.iterdir():
                if child.stat().st_size == 0:
                    Path.unlink(child)

    def file_handler(self):
        """
        创建一个handler，用于写入日志文件
        :return:
        """
        fh = logging.FileHandler(self.log_file + '.log',
                                 mode='w', encoding='utf-8')
        fh.setLevel(logging.INFO)  # 打印信息
        fh.setFormatter(self.formatter)  # 打印时间信息
        self.logger.addHandler(fh)  # 给handler添加formatter

    def console_handler(self):
        """
        创建一个handler，用于输出到控制台
        :return:
        """
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)  # 给handler添加formatter

    def pd_to_csv(self, dataframe):
        dataframe.to_csv(self.log_file + '.csv')
        self.logger.info("csv saved")
