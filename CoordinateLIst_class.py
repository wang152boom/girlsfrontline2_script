import pyautogui
import time
import Picture_information_extraction as Pie


class CoordinateList:
    def __init__(self):
        self.Clist = []

    def add(self, x=-1, y=-1, ti=0.2, sign='empty',):
        if sign == 'empty':
            self.Clist.append([x, y, ti])
        else:
            self.Clist.append([sign, ti])

    def call_list(self, coords):
        for co in self.Clist:

            if isinstance(co[0], str):

                if co[0] == 'award_check':
                    self._award_check(coords)

                elif co[0] == 'auto_use':
                    self.auto_use(co[1], coords)

                elif co[0] == 'back_main':
                    self.call(143, 54, coords, 1)

                elif co[0] == 'back_upper':
                    self.call(50, 50, coords, 1)

            else:
                self.call(co[0], co[1], coords, co[2])
                time.sleep(co[2])
        return 1

    @staticmethod
    def call(x, y, coords, tick=0.2):
        xs, ys = coords
        # pyautogui.moveTo(x, y)
        pyautogui.click(xs + x, ys + y)
        time.sleep(tick)

    @staticmethod
    def auto_use(times, coords):
        CoordinateList.call(1500, 1000,coords, 0.5)

        for i in range(times-1):
            CoordinateList.call(1225, 575, coords)
        CoordinateList.call(1170, 770, coords)

        for i in range(10):
            if Pie.compare_pic('award_check', coords):
                time.sleep(1)
                CoordinateList.call(950, 950, coords)  # 每日签到
                break
            time.sleep(1)

        time.sleep(0.2)

    @staticmethod
    def auto_battle(coords):
        for i in range(10):
            if Pie.compare_pic('battle_start', coords):
                time.sleep(1)
                CoordinateList.call(980, 980, coords)  # 作战开始
            time.sleep(1)
        for i in range(10):
            if Pie.compare_pic('auto_start', coords):
                time.sleep(1)
                CoordinateList.call(1687, 40, coords)  # 自律
            time.sleep(1)
        for i in range(600):
            if Pie.compare_pic('battle_over', coords):
                time.sleep(1)
                CoordinateList.call(980, 980, 2)
                CoordinateList.call(980, 980, 1)
            time.sleep(1)

    @staticmethod
    def _award_check(coords):
        for i in range(10):
            if Pie.compare_pic('award_check', coords):
                time.sleep(1)
                CoordinateList.call(950, 950, coords)  # 每日签到
                break
            time.sleep(1)


list1 = CoordinateList()  # 每日礼包
list2 = CoordinateList()  # 标准同调
list3 = CoordinateList()  # 心智勘测
list4 = CoordinateList()  # 班组作战
list5 = CoordinateList()  # 公共区
list6 = CoordinateList()  # 社区签到
list7 = CoordinateList()  # 社区签到邮件收取
list_test = CoordinateList()  # 测试版本

list1.add(1800, 665)  # 商城
list1.add(130, 385)  # 品质甄选
list1.add(1254, 141)  # 品质甄选
list1.add(464, 305)  # 常驻礼包
list1.add(1180, 766)  # 每日免费礼包
list1.add(sign='award_check')  # 点击任意位置确定
list1.add(sign='back_main')

list2.add(1721, 146)  # 战役推进
list2.add(1540, 50)  # 补给作战
list2.add(1670, 550)  # 标准同调
list2.add(sign='auto_use', ti=4)  # 自律开始
list2.add(sign='back_main')

list3.add(1721, 146)  # 战役推进
list3.add(1750, 50)  # 模拟作战
list3.add(200, 550)  # 心智勘测
list3.add(1200, 700)  # 第五关
list3.add(sign='auto_use', ti=1)  # 自律开始
list3.add(50, 50)  # 返回
list3.add(1880, 520)  # 下一页
list3.add(500, 500)  # 第六关
list3.add(sign='auto_use', ti=1)  # 自律开始
list3.add(sign='back_main')

list4.add(1492, 970, 1)  # 班组
list4.add(1315, 976)  # 补给
list4.add(1672, 986)  # 领取全部
list4.add(sign='award_check')  # 点击任意位置确定
list4.add(50, 50)  # 返回
list4.add(1431, 970)  # 每日要务
list4.add(1443, 845, 6)  # 开始作战
list4.add(980, 980, 6)  # 作战开始
list4.add(1687, 40)  # 自律

list5.add(1780, 464, 0.4)  # 公共区
list5.add(225, 365, 0.4)  # 调度室
list5.add(1700, 880, 1)  # 一键领取
list5.add(1253, 876, 3)  # 再次派遣
list5.add(1400, 1000, 0.4)  # 调度收益
list5.add(157, 248, 0.4)  # 资源生产
list5.add(1400, 950)  # 收取
list5.add(sign='award_check')  # 点击任意位置确定
list5.add(sign='back_main')

list6.add(110, 849, 1)
list6.add(1136, 250, 4)
list6.add(1460, 334, 1)  # 签到
list6.add(960, 830)  # 关闭

list7.add(1390, 255, 1)  # 打开邮件
list7.add(420, 1010)   # 领取全部
list7.add(sign='award_check')  # 点击任意位置确定
list7.add(sign='back_main')
