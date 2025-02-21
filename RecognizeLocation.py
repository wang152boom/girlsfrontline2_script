import cv2
import numpy as np


class RecognizeLocation:
    """
    类还没完全写好，等会再说
    """
    def __init__(self):
        self.coord_to_string = {}
        self.string_to_coord = {}

    def add(self, coord, name):
        self.coord_to_string[coord] = name
        self.string_to_coord[name] = coord

    def get_string(self, coord):
        """通过坐标获取对应的string"""
        return self.coord_to_string.get(coord, None)  # 如果找不到返回None

    def get_coord(self, string):
        """通过string获取对应的坐标"""
        return self.string_to_coord.get(string, None)  # 如果找不到返回None


Rc = RecognizeLocation()
Rc.add((800, 900, 1100, 1000), 'award_check')
Rc.add((900, 925, 1020, 970), 'start')
Rc.add((1500, 50, 1900, 700), 'if_main')
Rc.add((800, 950, 1100, 1020), 'battle_start')
Rc.add((1665, 30, 1715, 60), 'auto_start')
Rc.add((1450, 100, 1750, 190), 'battle_over')
