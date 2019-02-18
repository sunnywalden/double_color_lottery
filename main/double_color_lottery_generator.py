#venv/bin/python
# -*- coding:utf-8 -*-

from random import randint
from random import choice
from logbook import Logger, TimedRotatingFileHandler
import os
import sys

# BASE_DIR = os.path.abspath(os.path.join(os.getcwd(), ".."))
# sys.path.append(BASE_DIR)

handler = TimedRotatingFileHandler('../logs/lottery_generator.log')
handler.push_application()
logger = Logger(name='Lottery Generator', level='info')


def random_int_generator(num_list):
    #num = randint(m, n + 1)
    num = choice(num_list)
    yield num


def shuangseqiu_lottery_generator():
    """
    Double color lottery generator.

    """

    blue_nums = [i for i in range(1, 34)]
    red_nums = [i for i in range(1, 17)]

    nums = []
    randint_generator = random_int_generator
    i = 1
    while i < 7:
        num = next(randint_generator(blue_nums))
        # print(num)
        nums.append(num)
        blue_nums.remove(num)
        # print(blue_nums)
        i += 1
    last_num = next(randint_generator(red_nums))
    green_nums = sorted(nums)
    green_nums.append(last_num)

    shuangseqiu_lottery = green_nums

    yield shuangseqiu_lottery


def random_shuangse(n):
    """
    Get few random double color lotteries using choice function.

    """
    lotteries = []
    i = 1

    while i < n + 1:
        shuangse_lottery = shuangseqiu_lottery_generator

        lottery = next(shuangse_lottery())
        # print(lottery)
        lotteries.append(lottery)
        i += 1
    return lotteries


if __name__ == '__main__':
        lottery_num = int(input('请输入需要随机的双色球彩票数：'))
        shuangse_lotteries = random_shuangse(lottery_num)
        print('随机生成的彩票投注信息如下：')
        for shuangse_lottery in shuangse_lotteries:
            print(shuangse_lottery)









