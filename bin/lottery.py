#!venv/bin/flask/bin/python
# -*- coding:utf-8 -*-

from flask import Flask
from flask import jsonify
from logbook import Logger, TimedRotatingFileHandler
import os
import sys

BASE_DIR = os.path.abspath(os.path.join(os.getcwd(), ".."))
sys.path.append(BASE_DIR)

from main.double_color_lottery_generator import random_shuangse

app = Flask(__name__)

handler = TimedRotatingFileHandler('../logs/lottery_server.log')
handler.push_application()
my_logger = Logger(name='Lottery Server', level=11)

@app.route('/lottery/api/v1/doublecolor/<int:lottery_nums>', methods=['GET'])
def get_lottery(lottery_nums):
    """
    Parse interface to get numbers then request the lottery funtion to get it and post the res to user.

    """
    my_logger.info('Requests for %s loterries' % lottery_nums)
    try:
        random_shuangses = random_shuangse(lottery_nums)
    except Exception as e:
        my_logger.error(e)
        return jsonify({'status': 'failed', 'lotteries': [], 'msg': '接口返回错误 %s' % e})
    else:
        my_logger.info('Lotteries returned: %s' % random_shuangses)
        return jsonify({'status': 'success', 'lotteries': random_shuangses, 'msg': ''})


