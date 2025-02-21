import os
import time


def save_log():
    """
    保存登录记录
    :return: bool
    """
    if not os.path.exists('saves/log.txt'):
        return False
    log_directory = 'saves/log.txt'
    with open(log_directory, 'r') as file:
        lines = file.readlines()
        last_line = lines[-1].strip()
        del lines
        count = int(last_line[0])
        count += 1

    with open(log_directory, 'a') as file:
        file.write(str(count) + "times login at {}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        print("save log success")
        return True


def find_game_path():
    if not os.path.exists('saves/gamePath.txt'):
        return False
    with open('saves/gamePath.txt') as file:
        line = file.readline()
        return line.strip()


def save_game_path(exe_path):
    with open('saves/gamePath.txt', 'w') as file:
        file.write(exe_path)


def read_dones():
    """
    每日完成程度
    [0社区签到, 1每日礼包, 2标准同调, 3补给作战, 4班组自律+补给, 5_20小时委托＋金币, 6]
    :return: what program had done today
    """
    with open('saves/done.txt', 'r') as file:
        lines = file.readlines()
        current_time = time.strftime("%Y-%m-%d", time.localtime())
        done_time = lines[0].strip()
        dones = [int(i) for i in lines[1]]
        if current_time != done_time:
            dones = [0 for i in dones]
        return dones


def save_done(dones):
    """
    保存每日完成程度
    :return: None
    """
    with open('saves/done.txt', 'w') as file:
        file.write("{}".format(time.strftime("%Y-%m-%d", time.localtime())))
        file.write("\n")
        for done in dones:
            file.write(str(done))
