from PIL import Image
import pyautogui as pygui
import cv2
import numpy as np
import RecognizeLocation

entry_dictionary = {0: '攻击', 1: '攻击加成', 2: '暴击', 3: '暴击加成', -1: 'NONE'}
lock_dictionary = {0: '未锁', 1: '上锁'}


def firearms_accessories_filter(image):
    if image.getpixel((1480, 436)) == (239, 239, 239):
        flag_4or3 = 4
    else:
        flag_4or3 = 3
    lock = pic_compare_lock(image.crop((1800, 117, 1830, 147)))
    entry_text = picture_entry_text(flag_4or3, image)
    entry_span = picture_entry_span(flag_4or3, image)
    # print(lock_dictionary[lock])
    # print([entry_dictionary[i] for i in entry_text])
    # print(entry_span)

    image.close()

    if check_accessories(entry_text, entry_span, flag_4or3):
        if lock == 0:
            # keyPress
            pygui.click(1815, 132)
            return 1
        elif lock == 1:
            # it has been locked
            return 0
    else:
        # that's a trash
        return -1


def check_accessories(text, span, n):
    i, t, s = 0, 0, 0
    while i < n:
        if -1 < text[i] < 4:
            t += 1
            if span[i] == 1:
                s += 1
        i += 1
    if t > 2 and t - s <= 1:
        return True
    else:
        return False


def picture_entry_span(flag_4or3, image):
    entry_span = [-1, -1, -1]
    entry_co1 = [(1549, 299), (1549, 344), (1549, 390)]
    if flag_4or3 == 4:
        entry_co1.append((1549, 436))
        entry_span.append(-1)
    i = 0
    for en in entry_co1:
        if image.getpixel(en) == (239, 239, 239):
            entry_span[i] = 1
        i += 1
    return entry_span


def picture_entry_text(flag_4or3, image):
    entry_text = [-1, -1, -1]
    entry_co2 = [(1450, 260, 1550, 295), (1450, 305, 1550, 340), (1450, 350, 1550, 385)]
    if flag_4or3 == 4:
        entry_co2.append((1450, 397, 1550, 432))
        entry_text.append(-1)
    i = 0
    for en in entry_co2:
        entry_text[i] = pic_compare_entry(image.crop(en))
        i += 1
    return entry_text


def pic_compare_entry(im1):
    iat = Image.open('image_png/compare_pictures/entry_attack.png')
    iaa = Image.open('image_png/compare_pictures/entry_attackAdd.png')
    ist = Image.open('image_png/compare_pictures/entry_strike.png')
    isa = Image.open('image_png/compare_pictures/entry_strikeAdd.png')
    li = [ssim(im1, iat), ssim(im1, iaa), ssim(im1, ist), ssim(im1, isa)]
    m = max(li)
    if m <= 0.8:
        return -1
    iat.close()
    iaa.close()
    ist.close()
    isa.close()
    return li.index(m)


def pic_compare_lock(im1):
    iun = Image.open('image_png/compare_pictures/unlock.png')
    ild = Image.open('image_png/compare_pictures/locked.png')
    li = [ssim(im1, iun), ssim(im1, ild)]
    m = max(li)
    iun.close()
    ild.close()
    return li.index(m)


def ssim(image1, image2, window_size=11, K1=0.01, K2=0.03, L=255):

    image1 = np.array(image1.convert("L"))
    image2 = np.array(image2.convert("L"))

    # 计算均值
    mu1 = np.mean(image1)
    mu2 = np.mean(image2)

    # 计算方差
    sigma1 = np.var(image1)
    sigma2 = np.var(image2)

    # 计算协方差
    sigma12 = np.cov(image1.flatten(), image2.flatten())[0, 1]

    # 计算结构相似度
    C1 = (K1 * L) ** 2
    C2 = (K2 * L) ** 2
    ssim_value = (2 * mu1 * mu2 + C1) * (2 * sigma12 + C2) / ((mu1 ** 2 + mu2 ** 2 + C1) * (sigma1 + sigma2 + C2))

    return ssim_value


def compare_pic(name, coords):
    xs, ys = coords
    x1, y1, x2, y2 = RecognizeLocation.Rc.get_coord(name)
    x2 -= x1
    y2 -= y1
    image1 = np.array(pygui.screenshot(region=(x1+xs, y1+ys, x2, y2)))
    image2 = cv2.imread('image_png/compare_pictures/' + name + '.png')

    # 将图像转换为灰度图
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # 使用 ORB 特征检测器
    orb = cv2.ORB_create()

    # 检测关键点和计算描述符
    kp1, des1 = orb.detectAndCompute(gray1, None)
    kp2, des2 = orb.detectAndCompute(gray2, None)

    # 创建暴力匹配器（Brute Force Matcher）
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # 匹配特征点
    matches = bf.match(des1, des2)

    # 按照匹配距离排序
    matches = sorted(matches, key=lambda x: x.distance)

    # 设置匹配条件
    match_count_threshold = 50  # 降低匹配点数量的阈值
    distance_threshold = 40  # 保持相同的距离阈值
    good_match_ratio_threshold = 0.4  # 降低良好匹配点比例阈值

    if len(matches) > 0:
        # 计算匹配的平均距离
        average_distance = sum([match.distance for match in matches]) / len(matches)

        # 计算低于距离阈值的匹配比例
        good_matches = [match for match in matches if match.distance < distance_threshold]
        good_match_ratio = len(good_matches) / len(matches)

        if len(matches) > match_count_threshold and average_distance < distance_threshold and good_match_ratio > good_match_ratio_threshold:
            return True
        else:
            return False
    else:
        return False


def search_pic(name):

    # 1. 读取原始图像和模板图像
    image = np.array(pygui.screenshot(region=(0, 0, 500, 500)))
    template = cv2.imread('image_png/compare_pictures/'+name+'.png')  # 待对比图像（模板）

    # 2. 获取模板图像的尺寸
    w, h = template.shape[1], template.shape[0]

    # 3. 执行模板匹配
    result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

    # 4. 获取匹配位置
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # 5. 通过最大匹配值的位置来确定模板的位置
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    # 6. 在原始图像上绘制矩形框，标记匹配区域
    cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
    """
    # 7. 显示结果
    cv2.imshow('Matched Result', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    
    """

    return max_loc
