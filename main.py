import sys
import pyautogui as pygui
import Picture_information_extraction as Pie
import time
import subprocess
import pygetwindow as gw
import txtOs as txt
import auto_energy_spent as Aes
import CoordinateLIst_class
from PIL import Image


def screen_crop():
    im = Image.open('image_png/test.png')
    im = im.crop((9, 1, 200, 37))
    # 3500:43
    # 1980:
    im.save('image_png/test1.png')
    im.close()


def open_gf2(_auto, game_path):
    """
    启动程序
    :return: bool
    """
    # 检查是否有指定窗口
    width, height = pygui.size()
    print("程序启动\n屏幕大小:", width, height)
    open_window = True
    for title in gw.getAllTitles():
        if title == '少女前线2：追放':
            print("游戏已经启动：")
            open_window = False
    if open_window:
        # 启动exe程序
        try:
            subprocess.Popen(game_path)
        except Exception as e:
            print(e)
            game_path = input("游戏启动过程出错，请重新输入游戏启动路径")
            txt.save_game_path(exe_path)
        # 等待程序启动
        time.sleep(4)

    window = gw.getWindowsWithTitle('少女前线2：追放')[0]

    window.minimize()
    window.maximize()
    window.moveTo(0, 0)
    window.resize(1920, 1080)
    time.sleep(1)
    print("游戏界面大小：", end=" ")
    print(window.width, window.height)
    if window.width - 1920 > 100 and window.height - 1080 > 100:
        input("游戏界面大小与1920*1080相差过大，请将游戏窗口调整为1920*1080大小窗口后运行此程序\n输入任何字符或者关闭此窗口以退出:")

    xi, yi = Pie.search_pic('title')
    coords = (xi, yi + 30)

    print(width, height)
    if width - 1920 < 100 and height - 1080 < 100:
        coords = (0, 0)

    for i in range(60):
        if Pie.compare_pic('if_main', coords):
            print("游戏开始")
            return [True, window, coords]

        if Pie.compare_pic('start', coords):
            _auto.call(950, 950, coords, 1)  # 点击开始
        _auto.call(950, 950, coords, 1)

    print("游戏加载时间过长")
    return [False, window, coords]


def lock_acc():
    # this is to lock good weapon accessories
    count = 0
    count2 = 0
    count3 = 0
    while True:
        x, y = pygui.position()
        if x == 1919:
            print("鼠标X坐标达到1919，退出循环")
            break
        im = pygui.screenshot()
        c = Pie.firearms_accessories_filter(im)
        if c == 1:
            count += 1
            count2 += 1
        elif c == 0:
            count2 += 1
        elif c == -1:
            count3 += 1
        time.sleep(0.1)
        pygui.click(1880, 515)  # go to next
        time.sleep(0.1)
    print("配件清理助手本次上锁", end="")
    print(count, end="")
    print("个配件")
    print("配件清理助手本次发现", end="")
    print(count2, end="")
    print("个好配件")
    print("配件清理助手本次发现", end="")
    print(count3, end="")
    print("个垃圾配件")
    print("配件清理助手完成任务！Ciallo～(∠・ω< )⌒★")


def find_energy():
    """
    [Point(x=230, y=1010), Point(x=310, y=1037)]
    :return:
    """
    pygui.click()


if __name__ == '__main__':
    try:
        pygui.PAUSE = 1
        # screen_crop()
        # print(txt.read_dones())
        auto = CoordinateLIst_class.CoordinateList()

        exe_path = txt.find_game_path()
        if not exe_path:
            print("未找到saves/gamePath.txt文件，退出")
            sys.exit(0)
        if exe_path == 'None':
            exe_path = input("请输入游戏启动路径")
            txt.save_game_path(exe_path)
        if exe_path == '':
            exe_path = input("请输入游戏启动路径")
            txt.save_game_path(exe_path)
        print(exe_path)
        flag, win, coords = open_gf2(auto, exe_path)

        if flag:
            # this is for clean energy everyday
            dones = txt.read_dones()
            dones[0] = Aes.open_url(dones[0], win, coords)

            dones = Aes.use_energy_everyday1(dones, 120, coords)
            txt.save_done(dones)
            txt.save_log()

        input("输入任何字符或者关闭此窗口以退出:")
    except Exception as ex:
        input("程序运行出错，错误信息如下：" + str(ex) + "\n输入任何字符或者关闭此窗口以退出:")

    """
    auto = CoordinateLIst_class.CoordinateList()
    flag, win = open_gf2(auto)
    if flag:
        # this is for clean energy everyday
        dones = txt.read_dones()
        dones[0] = Aes.open_url(dones[0])
        dones = Aes.use_energy_everyday1(dones, 195)
        txt.save_done(dones)
        txt.save_log()
    """

    """
    input("wait for an input when you are ready for lock_acc()")
    lock_acc(absolute_path)  # this is to lock good weapon accessories        
    """

    """
    # this is for clean energy everyday
    done = txt.read_done()
    done = Aes.use_energy_everyday1(done, 195)
    txt.save_done(done)
    txt.save_log()
    """
    # guiprint.main_gui()

    """
    image = Image.open('image_png/girlsFrontline2/pic2.png')
    draw = ImageDraw.Draw(image)
    draw.point((1549, 299), fill='black')
    draw.point((1549, 344), fill='black')
    draw.point((1549, 390), fill='black')
    draw.point((1480, 436), fill='red')
    print(image)
    image.save('image_png/girlsFrontline2/pic1-1.png')
    image.close()
    """

    # paused_function()
    # keyboard.wait()

    # pygui.alert(text="press", title="a test", button="ok")
    """
    E:\girlsfight2_game\GF2Exilium\GF2 Game\GF2_Exilium.exe  
    D:\compile\pyautoGUI_scripe
    pyinstaller --onefile --add-data "image_png;image_png" --add-data "saves;saves" main.py
    """
