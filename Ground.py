from pico2d import *

import random
import json
import os
import title_state


class Ground:
    Image_init = None
    PIXEL_PER_METER = (10.0 / 0.08)                  #10 pixel 30 cm
    RUN_SPEED_KMPH = 10.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        self.first_x = 400
        self.first_y = 400
        self.second_x = 1200
        self.second_y = 400
        self.speed = 10
        self.distance = 0
        self.frame = 0
        if Ground.Image_init == None:
            self.ground_first = load_image('Image\\First_ground.png')
            self.ground_second = load_image('Image\\First_ground.png')


    def update(self, frame_time):

        if Ground.RUN_SPEED_PPS * frame_time > 13:
            self.distance = 12
        else:
            self.distance = Ground.RUN_SPEED_PPS * frame_time

        self.first_x -= self.distance
        self.second_x -= self.distance

        if self.first_x <= 400:
            self.second_x = self.first_x + 800

        if self.second_x <= 400:
            self.first_x = self.second_x + 800


    def draw(self):
        self.ground_first.draw(self.first_x, self.first_y)
        self.ground_second.draw(self.second_x, self.second_y)
