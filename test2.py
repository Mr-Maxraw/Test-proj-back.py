from random import randint
class SearchPoint():
    def __init__(self, w, h):
        self.__x = randint(0, w)
        self.__y = randint(0, h)
    def where_is_point(self, x, y):
        pos_x = pos_y = ''
        if x > self.__x:
            pos_x = 'L'
        elif x < self.__x:
            pos_x = 'R'
        if y > self.__y:
            pos_y = 'D'
        elif y < self.__y:
            pos_y = 'U'
        return pos_x+pos_y
w = int(input())
h = int(input())
x = int(input())
y = int(input())
SP = SearchPoint(w, h)
xf = False
yf = False
lx = 0
rx = w
dy = 0
uy = h
while (not xf or not yf) :
    x = round((lx + rx) / 2)
    y = round((dy + uy) / 2)
    print(x , y)
    check = SP.where_is_point(x, y)
    for ch in check :
        if ch == 'R' :
            lx = x
        if ch == 'L' :
            rx = x
        if ch == 'U' :
            dy = y
        if ch == 'D' :
            uy = y
    if (not ('R' in check)) and (not ('L' in check)) : 
        xf = True
    if (not ('U' in check)) and (not ('D' in check)) : 
        yf = True