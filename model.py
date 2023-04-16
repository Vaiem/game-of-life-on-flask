import random
import numpy as np

from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField
from wtforms.validators import DataRequired

class SizeForm(FlaskForm):
    weight = IntegerField("weight ", validators=[DataRequired()])
    height = IntegerField("height", validators=[DataRequired()])
    submit = SubmitField("Submit")

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
    


class Game(metaclass = SingletonMeta):
    def __init__(self, size_x= 3, size_y =3):    
        self.y = size_y
        self.x = size_x
        self.countGen = 0
        self.gameMap = None
        #self.gameMap = self.gen_start_map()
        

    def gen_start_map(self):
        game_map = np.zeros((self.y, self.x))
        state = (0,1,-1)
        for i in range(self.y):
            for j in range(self.x):
                game_map[i, j] = random.choice(state)
        self.gameMap = game_map
        

    def gen_next(self):
        self.countGen += 1
        for i in range(self.y):
            for j in range(self.x):
                self.check_live(i,j)
    
    def check_live(self, pos_y, pos_x):
        count_neighbour = 0

        if pos_x + 1 < self.x:
            if self.gameMap[pos_y, pos_x + 1] == 1:
                count_neighbour += 1
            

        if pos_x - 1 >= 0:
            if self.gameMap[pos_y, pos_x - 1] == 1:
                count_neighbour += 1
            
        
        if pos_y + 1 < self.y:
            if self.gameMap[pos_y + 1, pos_x ] == 1:
                count_neighbour += 1
            
        
        if pos_y - 1 >= 0:
            if self.gameMap[pos_y - 1, pos_x ] == 1:
                count_neighbour += 1
        
        if  count_neighbour == 2 or count_neighbour == 3:
            self.gameMap[pos_y, pos_x] = 1
            return
        
        if self.gameMap[pos_y, pos_x] == 1:
            self.gameMap[pos_y, pos_x] = -1
            return
        
        self.gameMap[pos_y, pos_x] = 0
        
