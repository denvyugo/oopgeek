"""
clsses for printing of points
"""
from random import randint
import turtle
from time import sleep

COLORS = ['red', 'black', 'blue', 'green']

DIRECTION = {
    'RIGHT': (1, 0),
    'LEFT': (-1, 0),
    'UP': (0, 1),
    'DOWN': (0, -1)
}


class Point:
    radius = 5

    def __init__(self, x=0, y=0, color='red'):
        self.x = x
        self.y = y
        self.color = color

    def setpoint(self):
        turtle.up()
        turtle.setposition(self.x, self.y)
        turtle.dot(self.radius, self.color)

    def clear(self):
        turtle.setposition(self.x, self.y)
        turtle.dot(self.radius, turtle.Screen().bgcolor())


class Figure:

    def draw(self):
        for p in self.points:
            p.setpoint()


class HorizontalLine(Figure):

    def __init__(self, startx, starty, length, color):
        self.startx = startx
        self.starty = starty
        self.length =length
        self.color = color
        self.points = []

        for i in range(self.length):
            p = Point(self.startx + i, self.starty, self.color)
            self.points.append(p)


class VerticallLine(Figure):

    def __init__(self, startx, starty, length, color):
        self.startx = startx
        self.starty = starty
        self.length = length
        self.color = color
        self.points = []

        for i in range(self.length):
            p = Point(self.startx, self.starty + i, self.color)
            self.points.append(p)


class Snake(Figure):

    def __init__(self, tail, length, direction):
        self.length = length
        self.tail = tail
        self.direction = direction
        self.points = []

        curx = tail.x
        cury = tail.y
        color = tail.color
        direct = DIRECTION[direction]

        for i in range(length):
            curx += direct[0]
            cury += direct[1]
            p = Point(curx, cury, 'green')
            self.points.append(p)

    def move(self):
        tail = self.points.pop(0)
        direct = DIRECTION[self.direction]
        tail.clear()
        tail = self.points[0]
        tail.setpoint()
        cur_head = self.points[self.length - 2]
        curx = cur_head.x + direct[0]
        cury = cur_head.y + direct[1]
        color = cur_head.color
        head = Point(curx , cury , color)
        self.points.append(head)
        head.setpoint()


if __name__ == '__main__':
    window = turtle.Screen()
    turtle.ht()
    p = Point(10, 20, 'red')
    p.setpoint()

    hr = HorizontalLine(100, 100, 20, 'blue')
    hr.draw()

    vr = VerticallLine(110, 90, 20, 'red')
    vr.draw()

    pnt = Point(50, 50, 'green')
    sk = Snake(pnt, 10, 'DOWN')
    sk.draw()
    for _ in range(20):
        # sleep(1)
        sk.move()
    while True:
        window.update()
