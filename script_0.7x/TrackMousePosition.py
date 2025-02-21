import pyautogui as pygui
import time
import pygetwindow as gw


def track_mouse_position():
    """
    辅助函数，打印鼠标位置，确定坐标
    :return:
    """
    while True:
        # 获取鼠标的当前位置
        x, y = pygui.position()
        # 打印当前鼠标坐标
        print(f"鼠标坐标: ({x}, {y})")
        # 如果 X 坐标为 1919，退出循环

        if x == 1919:
            print("鼠标X坐标达到1919，退出循环")
            break
        # 为了避免过快打印，可以加点延时
        time.sleep(0.1)


scripts = gw.getWindowsWithTitle('gf2_script')
if scripts:
    script = scripts[0]
    script.resizeTo(400, 200)
    script.moveTo(500, 400)
else:
    print("没有使用.bat文件启动")
track_mouse_position()
