import CoordinateLIst_class as cc
import time


def use_energy_everyday1(done_list, energy, coords):
    """
    :param coords:
    :param done_list: what have done today
    :param energy: how many energy do I have
    :return: dones: what have done
    """
    if done_list[1] < 1:
        print("每日礼包进行中...")
        done_list[1] = cc.list1.call_list(coords)
    else:
        print("每日礼包已经完成")

    if energy >= 80 and done_list[2] < 1:
        print("标准同调进行中...")
        done_list[2] = cc.list2.call_list(coords)
        energy -= 80
    elif energy < 80:
        print("标准同调体力不足")
    else:
        print("标准同调已经完成")

    if energy >= 40 and done_list[3] < 1:
        print("心智勘测进行中...")
        done_list[3] = cc.list3.call_list(coords)
        energy -= 40
    elif energy < 40:
        print("心智勘测体力不足")
    else:
        print("心智勘测已经完成")

    if done_list[5] < 2:
        print("公共区收取进行中...")
        done_list[5] += cc.list5.call_list(coords)
    else:
        print("公共区收取已完成")

    if done_list[4] < 1:
        print("班组任务进行中...")
        done_list[4] = cc.list4.call_list(coords)
    else:
        print("班组任务已经完成")

    return done_list


def clear_accessories():
    y = input("please put in y if you are ready for accessories work:")
    if 'y' == y:
        return True
    return False


def open_url(done, window, coords):
    if done == 0:
        cc.list6.call_list(coords)
        window.minimize()
        window.maximize()
        window.moveTo(10, 10)
        time.sleep(1)
        cc.list7.call_list(coords)
        time.sleep(1)
        return 1
    return done
