# https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
from images2gif import writeGif
from PIL import Image
from PIL import ImageDraw
import random
import copy

LIFE = 1
DEAD = 0


class ConwayLifeGame(object):

    def __init__(self, width, height, life=[]):
        width = width or 0
        height = height or 0
        self.rooms = [[DEAD for y in range(height)] for x in range(width)]
        self.age = 0
        for x, y in life:
            if x in range(self.width) and y in range(self.height):
                self.rooms[x][y] = LIFE

    def print_to_gif(self, ages=20, file_name='ConwayLifeGame'):
        images = []
        squares = {}
        for age in range(ages):
            t_age, rooms, count = self.grow()
            squares[t_age] = rooms
        for age, rooms in squares.items():
            image = Image.new('RGB', (self.width, self.height))
            draw = ImageDraw.Draw(image)
            for y in range(self.height):
                for x in range(self.width):
                    if rooms[x][y]:
                        draw.point((x, y))
            images.append(image)
        writeGif("%s.gif" % file_name, images)
        return squares

    @property
    def count(self):
        return sum([sum(column) for column in self.rooms])

    @property
    def width(self):
        return len(self.rooms)

    @property
    def height(self):
        if self.width:
            return len(self.rooms[0])
        else:
            return 0

    def neighbors(self, width, height):
        neigh_points = [(-1, -1), (0, -1), (1, -1),
                        (-1, 0), (1, 0),
                        (-1, 1), (0, 1), (1, 1), ]
        count = 0
        for px, py in neigh_points:
            x, y = width + px, height + py
            if x in range(self.width) and y in range(self.height):
                if self.rooms[x][y]:
                    count += 1
        return count

    def grow(self, age=1):
        new_rooms = [[0 for y in range(self.height)]
                     for x in range(self.width)]
        for y in range(self.height):
            for x in range(self.width):
                neighs = self.neighbors(x, y)
                if self.rooms[x][y]:
                    if neighs < 2:
                        new_rooms[x][y] = DEAD
                    elif neighs is 2 or neighs is 3:
                        new_rooms[x][y] = LIFE
                    else:
                        new_rooms[x][y] = DEAD
                else:
                    if neighs is 3:
                        new_rooms[x][y] = LIFE
        self.rooms = new_rooms
        self.age += 1
        return self.age, self.rooms, self.count