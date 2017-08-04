import time
import random
from threading import Thread


def random_sequence(count):
    rt_list = list()
    while count > 0:
        num = random.randrange(0, 1000)
        rt_list.append(num)
        count -= 1
    return rt_list


def cancel_range(num_list):

    min_num = min(num_list)

    cleared_list = []
    for num in num_list:
        cleared_list.append(num - min_num)

    return cleared_list


def compress_data(num_list, compressed_max_value):

    num_list = cancel_range(num_list)
    rt_list = []

    max_num = max(num_list)
    ratio = max_num / compressed_max_value

    for num in num_list:
        num = num / ratio
        rt_list.append(num)

    return rt_list, ratio


def depress_data(num_list, ratio):
    rt_list = []
    for num in num_list:
        rt_list.append(int(num * ratio))
    return rt_list


def run(num):
    time.sleep(num)
    sorted_list.append(num)


SLEEP_TIME = 2

fresh_list, final_ratio = compress_data(random_sequence(100), SLEEP_TIME)
sorted_list = []

for out_num in fresh_list:
    tr = Thread(target=run, args=(out_num,))
    tr.start()

time.sleep(SLEEP_TIME + 0.1)
print(depress_data(sorted_list, final_ratio))
