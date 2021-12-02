import numpy as np
import random
import time

COLOR_BLACK=-1
COLOR_WHITE=1
COLOR_NONE=0
random.seed(0)
infinity = 1000000
class AI(object):
 #chessboard_size, color, time_out passed from agent
 def __init__(self, chessboard_size, color, time_out):
    self.chessboard_size = chessboard_size
    #You are white or black
    self.color = color
  #the max time you should use, your algorithm's run time must not exceed the time limit.
    self.time_out = time_out
  # You need add your decision into your candidate_list. System will get the end of your candidate_list as your decision .
    self.candidate_list = []


 def go(self, chessboard):
 # Clear candidate_list, must do this step
    self.candidate_list.clear()
    if len( can_go(chessboard, self.color)):
        self.candidate_list = can_go(chessboard, self.color)




def can_go(chessboard, color):
     action_list = []
     for x in range(8):
         for y in range(8):
             if not is_on_board(x, y) or chessboard[x][y] != 0:
                 continue

             turn_over_chess = []
             for x_direction, y_direction in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
                 x_go = x + x_direction
                 y_go = y + y_direction

                 if not is_on_board(x_go, y_go):
                     continue

                 while chessboard[x_go][y_go] == -color:
                     x_go += x_direction
                     y_go += y_direction

                     if not is_on_board(x_go, y_go):
                         break

                     if not is_on_board(x_go, y_go):
                         continue

                     if chessboard[x_go][y_go] == color:
                         while True:
                             x_go -= x_direction
                             y_go -= y_direction
                             if x_go == x and y_go == y:
                                 break

                             turn_over_chess.append([x_go, y_go])

             if len(turn_over_chess) == 0:
                 continue
             else:
                 action_list.append((x, y))
     return action_list

def is_on_board(x, y):
     return x >= 0 and x <= 7 and y >= 0 and y <= 7