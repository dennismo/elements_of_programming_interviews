# 4.11

class Rect:
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

def line_intersect(x1, x2, x3, x4):
    left = max(x1, x3)
    right = min(x2, x4)
    if left < right:
        return (left, right)
    else: 
        return None

def rect_intersect(rect1, rect2):
    x_intersect = line_intersect(rect1.x1, rect1.x2, rect2.x1, rect2.x2)
    y_intersect = line_intersect(rect1.y1, rect1.y2, rect2.y1, rect2.y2)
    if x_intersect is not None and y_intersect is not None:
        return Rect(x_intersect[0], x_intersect[1], y_intersect[0], y_intersect[1])
